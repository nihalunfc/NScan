"""Reference ranges for the "deviation from normal anatomy" readout.

Reference set: discs in SPIDER training patients that radiologists graded as
unremarkable (Pfirrmann <= 2 and no Modic change, endplate defect,
spondylolisthesis, herniation, narrowing or bulging). Measured with the same
code the browser runs (measure.py / measure.js) on the reference masks.

Caveat recorded in the output: SPIDER patients have low back pain, so this is a
"radiologically unremarkable level" reference, not a healthy-population norm,
and it is not stratified by age or sex (SPIDER does not release them per scan).

python build_norms.py --cache data/cache --out ../web/models
"""
from __future__ import annotations

import argparse
import json
import pathlib

import numpy as np

from common import to_json
from splits import is_val
from train_grade import auc

FEATURES = ["dhi", "canal_ratio", "slip_pct", "wedge_upper"]
LUMBAR = ["L5/S1", "L4/L5", "L3/L4", "L2/L3", "L1/L2"]


def stats(x):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if len(x) < 8:
        return None
    # robust centre/scale so a few segmentation glitches do not inflate the SD
    med = float(np.median(x))
    mad = float(np.median(np.abs(x - med)) * 1.4826)
    return {"n": int(len(x)), "mean": float(x.mean()), "sd": float(x.std(ddof=1)), "median": med,
            "robust_sd": mad if mad > 0 else float(x.std(ddof=1)),
            "p2_5": float(np.percentile(x, 2.5)), "p97_5": float(np.percentile(x, 97.5))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="data/cache")
    ap.add_argument("--out", default="../web/models")
    args = ap.parse_args()
    z = np.load(pathlib.Path(args.cache) / "discs.npz", allow_pickle=True)
    pf, B = z["pfirrmann"].astype(float), z["binary"].astype(float)
    normal = (pf <= 2) & np.all(B == 0, axis=1)
    val = np.array([is_val(p) for p in z["patient"]])
    ref = normal & ~val
    levels = z["level"].astype(str)
    out = {"reference": "SPIDER training patients, discs graded radiologically unremarkable",
           "caveat": "Back-pain cohort; not age/sex stratified; 2D midline sagittal measurements.",
           "n_reference_discs": int(ref.sum()), "levels": {}, "global": {}}
    for lv in LUMBAR:
        m = ref & (levels == lv)
        out["levels"][lv] = {f: stats(z[f][m]) for f in FEATURES}
    for f in FEATURES:
        out["global"][f] = stats(z[f][ref])
    # lordosis: one value per series (it repeats on every disc row)
    seen, lord = set(), []
    for p, s, l in zip(z["patient"], z["seq"], z["lordosis_deg"]):
        if (p, s) not in seen and not is_val(p):
            seen.add((p, s))
            lord.append(l)
    out["global"]["lordosis_deg"] = stats(lord)

    # does the deviation score separate graded findings on held-out patients?
    def zscore(f, i):
        s = out["levels"].get(levels[i], {}).get(f) or out["global"][f]
        return (z[f][i] - s["median"]) / s["robust_sd"] if s else np.nan
    check = {}
    for f, task, sign in [("dhi", 5, -1), ("canal_ratio", 4, -1), ("slip_pct", 3, 1)]:
        idx = np.nonzero(val & ~np.isnan(B[:, task]))[0]
        zs = np.array([sign * zscore(f, i) for i in idx])
        ok = np.isfinite(zs)
        check[f"{f}_vs_{['modic','up_endplate','low_endplate','spondylolisthesis','herniation','narrowing','bulging'][task]}_auc"] = \
            auc(B[idx[ok], task], zs[ok]) if ok.sum() > 10 else None
    out["validation_on_heldout"] = check
    print(json.dumps(out, indent=1))
    (pathlib.Path(args.out) / "norms.json").write_text(to_json(out))


if __name__ == "__main__":
    main()
