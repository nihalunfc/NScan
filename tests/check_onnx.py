"""Validate exported models and metadata before they are published."""
import json, pathlib, sys
import numpy as np
import onnxruntime as ort

out = pathlib.Path(sys.argv[1])
seg = ort.InferenceSession(str(out / "spine_seg.onnx"))
y = seg.run(None, {"image": np.random.rand(1, 1, 256, 256).astype(np.float32)})[0]
assert y.shape == (1, 4, 256, 256) and np.isfinite(y).all(), y.shape
g = ort.InferenceSession(str(out / "disc_grade.onnx"))
z = g.run(None, {"crops": np.random.rand(3, 1, 64, 64).astype(np.float32)})[0]
assert z.shape == (3, 12) and np.isfinite(z).all(), z.shape
for f in out.glob("*.json"):
    json.loads(f.read_text(), parse_constant=lambda c: (_ for _ in ()).throw(ValueError(f"{f.name}: {c}")))
print("onnx and json ok:", sorted(p.name for p in out.iterdir()))
