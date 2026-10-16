"""Download SPIDER (lumbar spine MRI, CC BY 4.0) and cache 2D sagittal training data.

SPIDER: van der Graaf et al., "Lumbar spine segmentation in MR images: a dataset
and a public benchmark", Scientific Data 2024. Zenodo record 10159290.

Outputs (in --out):
  slices.npz   image uint8 (N,256,256), inst uint8 (N,256,256), patient, seq, slice_offset, kind
  discs.npz    per-disc crops from mid-sagittal T2 slices with radiological gradings
  manifest.json  counts and the label values found, for the record
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import shutil
import urllib.request
import zipfile

import numpy as np
import pandas as pd
import SimpleITK as sitk

from common import to_json, BINARY_TASKS, CANAL, DISC_OFFSET, SIZE, CROP, inst_to_class, letterbox, normalize, resample_isotropic
from measure import disc_crop, measure

ZENODO = "https://zenodo.org/api/records/{}"


def zenodo_meta(record: str) -> dict:
    """Record metadata; the literature cites two ids for SPIDER (10159290, 10159224), so try both."""
    errors = []
    for rid in dict.fromkeys([record, "10159290", "10159224"]):
        try:
            meta = json.load(urllib.request.urlopen(ZENODO.format(rid)))
            if any(f["key"].endswith(".zip") for f in meta.get("files", [])):
                print("using Zenodo record", rid, "-", meta.get("metadata", {}).get("title"))
                return meta
            errors.append(f"{rid}: no zip files")
        except Exception as e:  # noqa: BLE001 - report every attempt
            errors.append(f"{rid}: {e}")
    raise RuntimeError("SPIDER not found on Zenodo: " + "; ".join(errors))


def download(record: str, dest: pathlib.Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    meta = zenodo_meta(record)
    for f in meta["files"]:
        key, url, size = f["key"], f["links"]["self"], f["size"]
        target = dest / key
        print(f"  {key}  {size / 1e6:.0f} MB", flush=True)
        if target.exists() and target.stat().st_size == size:
            continue
        with urllib.request.urlopen(url) as r, open(target, "wb") as w:
            shutil.copyfileobj(r, w, 1 << 22)
        if key.endswith(".zip"):
            with zipfile.ZipFile(target) as z:
                z.extractall(dest)


def remap(mask: np.ndarray) -> np.ndarray:
    """SPIDER labels -> uint8 instance encoding (see common.py)."""
    out = np.zeros(mask.shape, np.uint8)
    v = (mask >= 1) & (mask <= 25)
    out[v] = mask[v]
    out[mask == 100] = CANAL
    d = (mask >= 201) & (mask <= 225)
    out[d] = (mask[d] - 200 + DISC_OFFSET)
    return out


def sagittal(img: sitk.Image) -> tuple[np.ndarray, tuple[float, float, float]]:
    """Return array [L, S, P] with superior first row flipped to the top, and spacing (L, S, P)."""
    img = sitk.DICOMOrient(img, "LPS")
    a = sitk.GetArrayFromImage(img)          # (S, P, L): axes z=S, y=P, x=L
    sx, sy, sz = img.GetSpacing()
    a = np.transpose(a, (2, 0, 1))[:, ::-1, :]  # (L, S, P), superior at row 0
    return np.ascontiguousarray(a), (sx, sz, sy)


def prep_slice(img2d, mask2d, spacing_rc):
    im = resample_isotropic(normalize(img2d), spacing_rc, order=1)
    im = letterbox(im, SIZE, order=1)
    if mask2d is None:
        return (im * 255).astype(np.uint8), None
    mk = resample_isotropic(mask2d, spacing_rc, order=0)
    mk = letterbox(mk, SIZE, order=0)
    return (im * 255).astype(np.uint8), mk


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", default="10159290")
    ap.add_argument("--raw", default="data/raw")
    ap.add_argument("--out", default="data/cache")
    ap.add_argument("--half-width", type=int, default=3, help="sagittal slices each side of the midline")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--no-download", action="store_true")
    args = ap.parse_args()
    raw, out = pathlib.Path(args.raw), pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if not args.no_download:
        print("Downloading SPIDER from Zenodo", args.record)
        download(args.record, raw)

    images = sorted(p for p in raw.rglob("*.mha") if "image" in str(p.parent).lower())
    masks = {p.name: p for p in raw.rglob("*.mha") if "mask" in str(p.parent).lower()}
    print(f"found {len(images)} images, {len(masks)} masks")
    grad_csv = next(iter(sorted(raw.rglob("*grading*.csv"))), None)
    grades = pd.read_csv(grad_csv) if grad_csv else None
    if grades is not None:
        print("gradings columns:", list(grades.columns))
        print(grades.head(3).to_string())

    S = {k: [] for k in ["image", "inst", "patient", "seq", "offset", "kind"]}
    discs = {k: [] for k in ["crop", "patient", "level", "pfirrmann", "binary", "seq",
                             "dhi", "slip_pct", "canal_ratio", "wedge_upper", "lordosis_deg"]}
    labels_seen: set[int] = set()
    if args.limit:
        images = images[: args.limit]
    for n, ip in enumerate(images):
        m = re.match(r"(\d+)_(.+)\.mha", ip.name)
        if not m or ip.name not in masks:
            continue
        patient, seq = int(m.group(1)), m.group(2).lower()
        img, sp = sagittal(sitk.ReadImage(str(ip)))
        msk, _ = sagittal(sitk.ReadImage(str(masks[ip.name])))
        if img.shape != msk.shape:
            print("shape mismatch", ip.name, img.shape, msk.shape)
            continue
        labels_seen |= set(np.unique(msk).tolist())
        inst = remap(msk)
        canal_area = (inst == CANAL).sum((1, 2))
        if canal_area.max() == 0:
            continue
        mid = int(np.argmax(canal_area))
        for off in range(-args.half_width, args.half_width + 1):
            k = mid + off
            if 0 <= k < img.shape[0] and canal_area[k] > 0.25 * canal_area[mid]:
                im, mk = prep_slice(img[k], inst[k], (sp[1], sp[2]))
                for key, val in zip(S, [im, mk, patient, seq, off, "sag"]):
                    S[key].append(val)
        # negatives: one axial and one coronal reformat, labelled background
        for kind, plane, spc in [("axial", img[:, img.shape[1] // 2, :].T, (sp[2], sp[0])),
                                 ("coronal", img[:, :, img.shape[2] // 2].T, (sp[1], sp[0]))]:
            im, _ = prep_slice(plane, None, spc)
            for key, val in zip(S, [im, np.zeros((SIZE, SIZE), np.uint8), patient, seq, 0, kind]):
                S[key].append(val)

        # disc crops, gradings and reference morphometry from the midline slice
        # (the grader trains on T2 only, since Pfirrmann is a T2 grade; norms use every sequence)
        if grades is not None:
            im, mk = prep_slice(img[mid], inst[mid], (sp[1], sp[2]))
            meas = measure(inst_to_class(mk))
            g = grades[grades.iloc[:, 0] == patient]
            for d in meas["discs"]:
                rr, cc = np.round(d["centroid"]).astype(int)
                ids = mk[max(rr - 1, 0):rr + 2, max(cc - 1, 0):cc + 2]
                ids = ids[ids > DISC_OFFSET]
                if not len(ids):
                    continue
                ivd = int(np.bincount(ids).argmax()) - DISC_OFFSET
                row = g[g.iloc[:, 1] == ivd]
                if not len(row):
                    continue
                row = row.iloc[0]
                pf = _col(row, "pfirr")
                bins = [_col(row, k) for k in ["modic", "up endplate", "low endplate", "spondylolisthesis",
                                               "herniation", "narrowing", "bulging"]]
                bins = [np.nan if b != b else float(b > 0) for b in bins]
                discs["crop"].append((disc_crop(im / 255.0, d["centroid"], d["u"], d["v"], d["length"], CROP) * 255).astype(np.uint8))
                discs["patient"].append(patient)
                discs["level"].append(d["name"])
                discs["pfirrmann"].append(pf)
                discs["binary"].append(bins)
                discs["seq"].append(seq)
                up = meas["vertebrae"][d["upper"]] if d["upper"] is not None else None
                for key, val in [("dhi", d["dhi"]), ("slip_pct", d["slip_pct"]), ("canal_ratio", d["canal_ratio"]),
                                 ("wedge_upper", up["wedge"] if up else np.nan), ("lordosis_deg", meas["lordosis_deg"])]:
                    discs[key].append(val)
        if n % 25 == 0:
            print(f"{n}/{len(images)} {ip.name} slices={len(S['image'])} discs={len(discs['crop'])}", flush=True)

    np.savez_compressed(out / "slices.npz", **{k: np.array(v) for k, v in S.items()})
    if discs["crop"]:
        np.savez_compressed(out / "discs.npz", **{k: np.array(v) for k, v in discs.items()})
    manifest = {"n_slices": len(S["image"]), "n_disc_crops": len(discs["crop"]),
                "patients": len(set(S["patient"])), "labels_seen": sorted(labels_seen),
                "binary_tasks": BINARY_TASKS}
    (out / "manifest.json").write_text(to_json(manifest))
    print(json.dumps(manifest))


def _col(row, needle):
    for c in row.index:
        if needle in c.lower():
            v = row[c]
            try:
                return float(v)
            except (TypeError, ValueError):
                return np.nan
    return np.nan


if __name__ == "__main__":
    main()
