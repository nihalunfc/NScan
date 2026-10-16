import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "train"))
import numpy as np
from common import inst_to_class
from measure import measure
from synthetic import phantom


def test_recovers_geometry():
    rng = np.random.default_rng(0)
    errs = []
    for i in range(10):
        img, inst, truth = phantom(rng)
        m = measure(inst_to_class(inst))
        assert m["n_discs"] == 5 and m["n_vertebrae"] == 6
        dhi = [d["dhi"] for d in m["discs"]]
        errs += [abs(a - b) / b for a, b in zip(dhi, truth["dhi"])]
        assert all(d["canal_ratio"] > 0.2 for d in m["discs"])
        assert m["vertebrae"][0]["name"] == "S1"
    assert np.median(errs) < 0.12, np.median(errs)


def test_detects_pathology():
    rng = np.random.default_rng(1)
    _, inst, _ = phantom(rng, disc_scale={1: 0.4}, slip={3: 0.2}, wedge={2: 0.6})
    m = measure(inst_to_class(inst))
    d = {x["name"]: x for x in m["discs"]}
    assert d["L4/L5"]["dhi"] < 0.6 * d["L3/L4"]["dhi"]
    assert d["L3/L4"]["slip_pct"] > 10, d["L3/L4"]["slip_pct"]   # vertebra 3 (L3) slips anterior over L4
    v = {x["name"]: x for x in m["vertebrae"]}
    assert v["L4"]["wedge"] < 0.8, v["L4"]["wedge"]


if __name__ == "__main__":
    test_recovers_geometry(); test_detects_pathology(); print("ok")
