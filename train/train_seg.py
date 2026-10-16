"""Train the sagittal segmentation model, calibrate the quality gate, export ONNX.

python train_seg.py --cache data/cache --out ../web/models --minutes 90
"""
from __future__ import annotations

import argparse
import json
import pathlib
import time

import numpy as np
import torch
import torch.nn.functional as F

from augment import augment
from common import to_json, SIZE, inst_to_class
from measure import measure
from models import UNet
from splits import is_val
from synthetic import negative, phantom

torch.set_num_threads(max(1, torch.get_num_threads()))


def split_patients(patients):
    u = np.unique(patients).tolist()
    return {p for p in u if not is_val(p)}, {p for p in u if is_val(p)}


def load(cache: pathlib.Path, synthetic: int):
    if synthetic:
        rng = np.random.default_rng(0)
        imgs, insts, pats, kinds, offs = [], [], [], [], []
        for i in range(synthetic):
            im, ins, _ = phantom(rng)
            imgs.append((im * 255).astype(np.uint8)); insts.append(ins); pats.append(i); kinds.append("sag"); offs.append(0)
        return dict(image=np.array(imgs), inst=np.array(insts), patient=np.array(pats),
                    kind=np.array(kinds), offset=np.array(offs), seq=np.array(["t2"] * synthetic))
    z = np.load(cache / "slices.npz")
    return {k: z[k] for k in z.files}


def dice_loss(logits, target, eps=1.0):
    p = logits.softmax(1)[:, 1:]
    t = F.one_hot(target, logits.shape[1]).permute(0, 3, 1, 2)[:, 1:].float()
    inter = (p * t).sum((0, 2, 3))
    return 1 - ((2 * inter + eps) / (p.sum((0, 2, 3)) + t.sum((0, 2, 3)) + eps)).mean()


def dice_per_class(pred, target, n=4):
    out = []
    for c in range(1, n):
        a, b = pred == c, target == c
        s = a.sum() + b.sum()
        out.append(float(2 * (a & b).sum() / s) if s else float("nan"))
    return out


@torch.no_grad()
def predict(model, x):
    """Probabilities with flip test-time augmentation. Returns (p, p_flip)."""
    p = model(x).softmax(1)
    pf = model(x.flip(-1)).softmax(1).flip(-1)
    return p, pf


def lap_var(x):
    """Variance of the 4-neighbour Laplacian on the [0,1] input (sharpness); see quality.js."""
    k = torch.tensor([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=x.dtype)[None, None]
    return F.conv2d(x, k).flatten(1).var(1, unbiased=False)


def quality_features(p, pf):
    """Per-image features used by the quality gate (mirrored in web/js/quality.js)."""
    pm = (p + pf) / 2
    lab, lab_f = p.argmax(1), pf.argmax(1)
    fg = (pm.argmax(1) > 0)
    agree = []
    ent = -(pm * pm.clamp_min(1e-8).log()).sum(1) / np.log(pm.shape[1])
    feats = []
    for i in range(p.shape[0]):
        a, b = lab[i] > 0, lab_f[i] > 0
        s = int(a.sum() + b.sum())
        tta = float(2 * (a & b).sum() / s) if s else 0.0
        # class-wise agreement is stricter than foreground agreement
        same = float(((lab[i] == lab_f[i]) & (a | b)).sum() / max(int((a | b).sum()), 1))
        f = fg[i]
        feats.append({"tta_dice": tta, "tta_label_agree": same,
                      "fg_entropy": float(ent[i][f].mean()) if f.any() else 1.0,
                      "fg_frac": float(f.float().mean())})
    return feats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="data/cache")
    ap.add_argument("--out", default="../web/models")
    ap.add_argument("--minutes", type=float, default=90)
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--base", type=int, default=16)
    ap.add_argument("--synthetic", type=int, default=0, help="smoke test on N phantoms instead of SPIDER")
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.cache).mkdir(parents=True, exist_ok=True)
    D = load(pathlib.Path(args.cache), args.synthetic)
    tr_p, va_p = split_patients(D["patient"])
    tr = np.array([p in tr_p for p in D["patient"]])
    va = ~tr
    X = torch.from_numpy(D["image"]).float()[:, None] / 255
    Y = torch.from_numpy(inst_to_class(D["inst"])).long()
    print(f"train {tr.sum()} val {va.sum()} slices; patients {len(tr_p)}/{len(va_p)}", flush=True)

    model = UNet(base=args.base).to(memory_format=torch.channels_last)  # ~2x faster on CPU
    print("params", sum(p.numel() for p in model.parameters()))
    opt = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=1e-4)
    tr_idx = np.nonzero(tr)[0]
    steps_per_epoch = max(1, len(tr_idx) // args.batch)
    rng = np.random.default_rng(0)
    t0, step, epoch, budget = time.time(), 0, 0, args.minutes * 60
    est_total = None
    while time.time() - t0 < budget:
        model.train()
        rng.shuffle(tr_idx)
        losses = []
        for b in range(steps_per_epoch):
            idx = tr_idx[b * args.batch:(b + 1) * args.batch]
            x, y = X[idx].clone(), Y[idx].clone()
            # extra synthetic negatives: the model should find nothing in non-spine images
            k = max(1, args.batch // 8)
            neg = torch.from_numpy(np.stack([negative(rng) for _ in range(k)]))[:, None]
            x, y = torch.cat([x, neg]), torch.cat([y, torch.zeros(k, SIZE, SIZE, dtype=torch.long)])
            x, y = augment(x, y)
            if est_total is None:
                est_total = budget  # cosine schedule over the time budget
            frac = min((time.time() - t0) / est_total, 1.0)
            for g in opt.param_groups:
                g["lr"] = 2e-3 * (0.02 + 0.98 * 0.5 * (1 + np.cos(np.pi * frac)))
            logits = model(x.contiguous(memory_format=torch.channels_last))
            loss = F.cross_entropy(logits, y) + dice_loss(logits, y)
            opt.zero_grad()
            loss.backward()
            opt.step()
            losses.append(loss.item())
            step += 1
            if time.time() - t0 > budget:
                break
        epoch += 1
        print(f"epoch {epoch} step {step} loss {np.mean(losses):.4f} lr {opt.param_groups[0]['lr']:.2e} "
              f"t={(time.time() - t0) / 60:.1f}m", flush=True)

    # ---- evaluation on held-out patients
    model.eval()
    sag = va & (D["kind"] == "sag")
    neg = va & (D["kind"] != "sag")
    dices, feats_pos, feats_neg, plaus = [], [], [], []
    for name, mask, store in [("pos", sag, feats_pos), ("neg", neg, feats_neg)]:
        ids = np.nonzero(mask)[0]
        for i in range(0, len(ids), 32):
            j = ids[i:i + 32]
            p, pf = predict(model, X[j])
            fs = quality_features(p, pf)
            for f, lv in zip(fs, lap_var(X[j]).tolist()):
                f["lap_var"] = lv
            store += fs
            pred = ((p + pf) / 2).argmax(1).numpy()
            for a, b, jj in zip(pred, Y[j].numpy(), j):
                if name == "pos":
                    if D["offset"][jj] == 0:
                        dices.append(dice_per_class(a, b))
                    m = measure(a)
                    plaus.append(m["n_discs"])
    # synthetic negatives too
    xs = torch.from_numpy(np.stack([negative(rng) for _ in range(64)]))[:, None]
    p, pf = predict(model, xs)
    fs = quality_features(p, pf)
    for f, lv in zip(fs, lap_var(xs).tolist()):
        f["lap_var"] = lv
    feats_neg += fs

    dices = np.array(dices)
    metrics = {"val_patients": len(va_p), "val_mid_slices": len(dices),
               "dice_vertebra": float(np.nanmean(dices[:, 0])) if len(dices) else None,
               "dice_disc": float(np.nanmean(dices[:, 1])) if len(dices) else None,
               "dice_canal": float(np.nanmean(dices[:, 2])) if len(dices) else None,
               "epochs": epoch, "steps": step, "minutes": (time.time() - t0) / 60,
               "params": sum(p.numel() for p in model.parameters()), "synthetic_smoke_test": bool(args.synthetic)}
    print(json.dumps(metrics, indent=1))

    def pct(fs, key, q):
        return float(np.percentile([f[key] for f in fs], q)) if fs else None
    quality = {
        # thresholds at the 1st / 99th percentile of held-out real sagittal scans, so about 1-3%
        # of readable scans are wrongly sent back; abnormal anatomy must not count as "unreadable"
        "min_tta_dice": pct(feats_pos, "tta_dice", 1),
        "min_tta_label_agree": pct(feats_pos, "tta_label_agree", 1),
        "max_fg_entropy": pct(feats_pos, "fg_entropy", 99),
        "min_fg_frac": pct(feats_pos, "fg_frac", 2),
        "min_discs": 3,
        "min_lap_var": (pct(feats_pos, "lap_var", 1) or 0) * 0.5,
        "pos_summary": {k: [pct(feats_pos, k, q) for q in (5, 50, 95)] for k in ["tta_dice", "tta_label_agree", "fg_entropy", "fg_frac", "lap_var"]},
        "neg_summary": {k: [pct(feats_neg, k, q) for q in (5, 50, 95)] for k in ["tta_dice", "tta_label_agree", "fg_entropy", "fg_frac", "lap_var"]},
        "pos_discs_found": [int(np.percentile(plaus, q)) for q in (5, 50, 95)] if plaus else None,
    }
    # how many held-out negatives each rule would wrongly pass
    def passes(f):
        return (f["tta_dice"] >= quality["min_tta_dice"] and f["tta_label_agree"] >= quality["min_tta_label_agree"]
                and f["fg_frac"] >= quality["min_fg_frac"] and f["lap_var"] >= quality["min_lap_var"])
    quality["neg_pass_rate"] = float(np.mean([passes(f) for f in feats_neg])) if feats_neg else None
    quality["pos_pass_rate"] = float(np.mean([passes(f) for f in feats_pos])) if feats_pos else None
    print(json.dumps(quality, indent=1))

    (out / "seg_metrics.json").write_text(to_json(metrics))
    (out / "quality.json").write_text(to_json(quality))
    torch.save(model.state_dict(), pathlib.Path(args.cache) / "seg.pt")
    model = model.to(memory_format=torch.contiguous_format)
    torch.onnx.export(model, torch.zeros(1, 1, SIZE, SIZE), out / "spine_seg.onnx", input_names=["image"],
                      output_names=["logits"], opset_version=17, dynamo=False)
    print("exported", out / "spine_seg.onnx")


if __name__ == "__main__":
    main()
