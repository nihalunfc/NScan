"""Train the per-disc grader (Pfirrmann + 7 binary findings) on SPIDER T2 midline crops.

python train_grade.py --cache data/cache --out ../web/models --minutes 25
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import time

import numpy as np
import torch
import torch.nn.functional as F

from common import to_json, BINARY_TASKS, CROP, N_PFIRRMANN
from models import DiscGrader
from splits import is_val


def auc(y, p):
    y, p = np.asarray(y), np.asarray(p)
    pos, neg = p[y == 1], p[y == 0]
    if not len(pos) or not len(neg):
        return float("nan")
    r = np.argsort(np.argsort(np.concatenate([pos, neg]))) + 1
    return float((r[: len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def thresholds(y, p, ppv=0.7, npv=0.9):
    """Two cut-offs: call positive at/above t_hi, negative at/below t_lo, otherwise indeterminate."""
    y, p = np.asarray(y), np.asarray(p)
    cand = np.unique(np.round(p, 3))
    best_j, youden = 0.5, -1
    t_hi, t_lo = None, None
    for t in cand:
        pred = p >= t
        tp, fp = (pred & (y == 1)).sum(), (pred & (y == 0)).sum()
        fn, tn = (~pred & (y == 1)).sum(), (~pred & (y == 0)).sum()
        j = tp / max(tp + fn, 1) + tn / max(tn + fp, 1) - 1
        if j > youden:
            youden, best_j = j, float(t)
        if t_hi is None and tp + fp >= 5 and tp / (tp + fp) >= ppv:
            t_hi = float(t)
        neg = p <= t
        if neg.sum() >= 5 and ((y[neg] == 0).mean() >= npv):
            t_lo = float(t)
    # No cut-off reaches the target PPV (rare findings): never call "likely", only uncertain/unlikely.
    if t_hi is None:
        t_hi = 1.01
    if t_lo is None:
        t_lo = -0.01
    if t_hi < t_lo:  # the bands overlap, so a single cut-off separates likely from unlikely
        t_lo = t_hi = best_j
    return {"t_lo": t_lo, "t_hi": t_hi, "youden": best_j}


def jitter(x):
    b = x.shape[0]
    ang = (torch.rand(b) * 2 - 1) * math.radians(10)
    s = torch.empty(b).uniform_(0.9, 1.12)
    t = (torch.rand(b, 2) * 2 - 1) * 0.08
    th = torch.stack([torch.stack([torch.cos(ang) / s, -torch.sin(ang) / s, t[:, 0]], 1),
                      torch.stack([torch.sin(ang) / s, torch.cos(ang) / s, t[:, 1]], 1)], 1)
    x = F.grid_sample(x, F.affine_grid(th, x.shape, align_corners=False), align_corners=False)
    g = torch.exp(torch.empty(b, 1, 1, 1).uniform_(-0.4, 0.4))
    x = x.clamp(0, 1) ** g * torch.empty(b, 1, 1, 1).uniform_(0.8, 1.2)
    return x + torch.randn_like(x) * 0.03


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="data/cache")
    ap.add_argument("--out", default="../web/models")
    ap.add_argument("--minutes", type=float, default=25)
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    z = np.load(pathlib.Path(args.cache) / "discs.npz", allow_pickle=True)
    keep = np.array([str(s).startswith("t2") for s in z["seq"]])
    X = torch.from_numpy(z["crop"][keep]).float()[:, None] / 255
    pf = z["pfirrmann"][keep].astype(float)
    B = z["binary"][keep].astype(float)
    va = np.array([is_val(p) for p in z["patient"][keep]])
    tr = ~va
    print(f"T2 disc crops: train {tr.sum()} val {va.sum()}")
    yp = torch.from_numpy(np.nan_to_num(pf - 1, nan=-100)).long()            # classes 0..4, -100 ignored
    yb = torch.from_numpy(np.nan_to_num(B, nan=0)).float()
    mb = torch.from_numpy(~np.isnan(B)).float()
    prev = (yb[tr] * mb[tr]).sum(0) / mb[tr].sum(0).clamp_min(1)
    pos_w = ((1 - prev) / prev.clamp_min(1e-3)).clamp(1, 20)
    print("prevalence", dict(zip(BINARY_TASKS, prev.numpy().round(3).tolist())))

    model = DiscGrader()
    opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-3)
    idx = np.nonzero(tr)[0]
    rng = np.random.default_rng(0)
    t0, ep, budget = time.time(), 0, args.minutes * 60
    while time.time() - t0 < budget:
        model.train()
        rng.shuffle(idx)
        frac = min((time.time() - t0) / budget, 1)
        for g in opt.param_groups:
            g["lr"] = 1e-3 * (0.02 + 0.98 * 0.5 * (1 + math.cos(math.pi * frac)))
        ls = []
        for i in range(0, len(idx), 64):
            j = idx[i:i + 64]
            o = model(jitter(X[j].clone()))
            lp = F.cross_entropy(o[:, :N_PFIRRMANN], yp[j], ignore_index=-100, label_smoothing=0.05)
            lb = (F.binary_cross_entropy_with_logits(o[:, N_PFIRRMANN:], yb[j], pos_weight=pos_w, reduction="none")
                  * mb[j]).sum() / mb[j].sum().clamp_min(1)
            loss = lp + lb
            opt.zero_grad()
            loss.backward()
            opt.step()
            ls.append(float(loss))
        ep += 1
        if ep % 5 == 0:
            print(f"epoch {ep} loss {np.mean(ls):.4f} t={(time.time() - t0) / 60:.1f}m", flush=True)

    model.eval()
    with torch.no_grad():
        o = model(X[va])
    probs_p = o[:, :N_PFIRRMANN].softmax(1).numpy()
    probs_b = torch.sigmoid(o[:, N_PFIRRMANN:]).numpy()
    gt_p = pf[va]
    ok = ~np.isnan(gt_p)
    pred_p = probs_p.argmax(1) + 1
    report = {"n_val_discs": int(va.sum()), "n_train_discs": int(tr.sum()), "epochs": ep,
              "pfirrmann_acc": float((pred_p[ok] == gt_p[ok]).mean()) if ok.any() else None,
              "pfirrmann_acc_within1": float((np.abs(pred_p[ok] - gt_p[ok]) <= 1).mean()) if ok.any() else None,
              "tasks": {}}
    for k, name in enumerate(BINARY_TASKS):
        m = ~np.isnan(B[va][:, k])
        y = B[va][m, k]
        report["tasks"][name] = {"auc": auc(y, probs_b[m, k]), "prevalence": float(y.mean()) if len(y) else None,
                                 "n": int(m.sum()), **thresholds(y, probs_b[m, k])}
    print(json.dumps(report, indent=1))
    (out / "grade_metrics.json").write_text(to_json(report))
    torch.onnx.export(model, torch.zeros(1, 1, CROP, CROP), out / "disc_grade.onnx", input_names=["crops"],
                      output_names=["logits"], dynamic_axes={"crops": {0: "n"}, "logits": {0: "n"}},
                      opset_version=17, dynamo=False)
    print("exported", out / "disc_grade.onnx")


if __name__ == "__main__":
    main()
