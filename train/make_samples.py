"""Export example images for the web page from held-out SPIDER patients (CC BY 4.0).

python make_samples.py --cache data/cache --out ../web/samples
"""
from __future__ import annotations

import argparse
import pathlib

import numpy as np
from PIL import Image, ImageFilter

from splits import is_val


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="data/cache")
    ap.add_argument("--out", default="../web/samples")
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    z = np.load(pathlib.Path(args.cache) / "slices.npz")
    val = np.array([is_val(p) for p in z["patient"]])
    mid = val & (z["kind"] == "sag") & (z["offset"] == 0)
    seq = z["seq"].astype(str)
    picks = {}
    for want in ["t2", "t1"]:
        idx = np.nonzero(mid & (seq == want))[0]
        if len(idx):
            # the slice with the most labelled discs makes the clearest example
            n_discs = [len(np.unique(z["inst"][i][z["inst"][i] > 100])) for i in idx]
            picks[want] = idx[int(np.argmax(n_discs))]
    for want, i in picks.items():
        Image.fromarray(z["image"][i]).resize((512, 512), Image.BICUBIC).save(out / f"sample_{want}.png")
    if "t2" in picks:
        bad = Image.fromarray(z["image"][picks["t2"]]).resize((120, 120), Image.BILINEAR)
        bad = bad.filter(ImageFilter.GaussianBlur(2.5)).resize((360, 360), Image.BILINEAR)
        bad.save(out / "sample_bad.png")
    (out / "ATTRIBUTION.txt").write_text(
        "Derived from the SPIDER lumbar spine MRI dataset (van der Graaf et al., Scientific Data 2024,\n"
        "doi:10.1038/s41597-024-03090-w), licensed CC BY 4.0. Resized; sample_bad.png was deliberately degraded.\n")
    print("samples:", sorted(p.name for p in out.iterdir()))


if __name__ == "__main__":
    main()
