"""Shared constants and preprocessing.

Everything here has a twin in web/js/ so that training and in-browser inference
see identical inputs. Keep the two in sync.
"""
from __future__ import annotations

import numpy as np
from scipy import ndimage

SIZE = 256          # segmentation input (pixels, square)
CROP = 64           # disc crop for the grading model
CLASSES = ["background", "vertebra", "disc", "canal"]

# Instance encoding used in the cached dataset (fits in uint8):
#   1..25   vertebrae (SPIDER labels 1..25)
#   100     spinal canal
#   101..125 intervertebral discs (SPIDER labels 201..225)
CANAL = 100
DISC_OFFSET = 100

# Per-disc targets of the grading model, in output order after the 5 Pfirrmann logits.
BINARY_TASKS = [
    "modic",              # any Modic change (type 1-3)
    "up_endplate",        # upper endplate defect
    "low_endplate",       # lower endplate defect
    "spondylolisthesis",
    "herniation",
    "narrowing",
    "bulging",
]
N_PFIRRMANN = 5


def inst_to_class(inst: np.ndarray) -> np.ndarray:
    """Map the uint8 instance encoding to semantic classes 0..3."""
    cls = np.zeros(inst.shape, np.uint8)
    cls[(inst >= 1) & (inst <= 25)] = 1
    cls[(inst > DISC_OFFSET) & (inst <= DISC_OFFSET + 25)] = 2
    cls[inst == CANAL] = 3
    return cls


def normalize(img: np.ndarray) -> np.ndarray:
    """Robust min-max to [0, 1] using the 0.5/99.5 percentiles."""
    img = img.astype(np.float32)
    lo, hi = np.percentile(img, [0.5, 99.5])
    if hi - lo < 1e-6:
        return np.zeros_like(img)
    return np.clip((img - lo) / (hi - lo), 0, 1)


def letterbox(img: np.ndarray, size: int = SIZE, order: int = 1) -> np.ndarray:
    """Pad to a centred square with zeros, then resize to size x size.

    order=1 for images (bilinear), order=0 for label maps (nearest).
    Mirrors letterbox() in web/js/preprocess.js.
    """
    h, w = img.shape
    s = max(h, w)
    out = np.zeros((s, s), img.dtype)
    y0, x0 = (s - h) // 2, (s - w) // 2
    out[y0:y0 + h, x0:x0 + w] = img
    if s == size:
        return out
    return ndimage.zoom(out, size / s, order=order, mode="nearest", grid_mode=True)[:size, :size]


def resample_isotropic(img: np.ndarray, spacing_rc: tuple[float, float], order: int = 1) -> np.ndarray:
    """Resample a 2D slice so rows and columns share the finer spacing."""
    sr, sc = spacing_rc
    t = min(sr, sc)
    if abs(sr - sc) / t < 0.02:
        return img
    return ndimage.zoom(img, (sr / t, sc / t), order=order, mode="nearest", grid_mode=True)


def to_json(obj) -> str:
    """json.dumps that writes NaN/inf as null (browsers reject bare NaN)."""
    import json
    import math

    def clean(o):
        if isinstance(o, float):
            return o if math.isfinite(o) else None
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [clean(v) for v in o]
        if hasattr(o, "item"):
            return clean(o.item())
        return o
    return json.dumps(clean(obj), indent=1, allow_nan=False)
