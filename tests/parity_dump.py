"""Dump phantom masks with Python measurements for the JS parity test."""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "train"))
import numpy as np
from common import inst_to_class, to_json
from measure import measure, disc_crop
from synthetic import phantom

rng = np.random.default_rng(7)
cases = []
for i in range(8):
    img, inst, _ = phantom(rng, disc_scale={i % 5: 0.5}, slip={(i + 1) % 6: 0.15})
    cls = inst_to_class(inst)
    m = measure(cls)
    crop = disc_crop(img, m["discs"][1]["centroid"], m["discs"][1]["u"], m["discs"][1]["v"], m["discs"][1]["length"])
    cases.append({"cls": cls.flatten().tolist(), "img": np.round(img, 4).flatten().tolist(), "m": m,
                  "crop": crop.flatten().tolist()})
pathlib.Path(sys.argv[1]).write_text(to_json(cases))
