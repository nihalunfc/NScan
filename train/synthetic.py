"""Synthetic sagittal lumbar phantoms.

Used for unit tests, for a pipeline smoke test without real data, and as a
sanity check that the morphometry recovers known geometry. Not training data
for the real model.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import ndimage

from common import CANAL, DISC_OFFSET


def _poly(shape, corners):
    """Rasterise a convex quadrilateral given as 4 (row, col) corners."""
    rr, cc = np.mgrid[0:shape[0], 0:shape[1]]
    inside = np.ones(shape, bool)
    n = len(corners)
    for i in range(n):
        (r0, c0), (r1, c1) = corners[i], corners[(i + 1) % n]
        inside &= (cc - c0) * (r1 - r0) - (rr - r0) * (c1 - c0) <= 0
    return inside


def phantom(rng: np.random.Generator, size: int = 256, n_vert: int = 6,
            disc_scale: dict | None = None, slip: dict | None = None, wedge: dict | None = None):
    """Return (image float32 [0,1], inst uint8, truth dict).

    disc_scale: {disc_index_from_bottom: factor} to narrow a disc.
    slip: {vertebra_index_from_bottom: fraction_of_depth} anterior shift.
    wedge: {vertebra_index_from_bottom: anterior/posterior height ratio}.
    """
    disc_scale, slip, wedge = disc_scale or {}, slip or {}, wedge or {}
    inst = np.zeros((size, size), np.uint8)
    depth = rng.uniform(0.11, 0.13) * size
    vh = rng.uniform(0.75, 0.85) * depth
    dh = rng.uniform(0.28, 0.36) * vh
    tilt0 = math.radians(rng.uniform(-8, 8))
    curve = math.radians(rng.uniform(4, 9))     # per-level change of tilt (lordosis)
    r = size * 0.92
    c0 = size * rng.uniform(0.42, 0.5)
    truth = {"dhi": [], "wedge": [], "slip": []}
    for k in range(n_vert):
        a = tilt0 + curve * (k - n_vert / 2)
        u = np.array([math.sin(a), math.cos(a)])          # posterior (row, col)
        v = np.array([-math.cos(a), math.sin(a)])         # superior
        if v[0] > 0:
            v = -v
        shift = slip.get(k, 0.0) * depth
        center = np.array([r - vh / 2, c0 - shift])
        w = wedge.get(k, 1.0)
        ha, hp = vh * w, vh
        corners = [center - u * depth / 2 + v * ha / 2, center + u * depth / 2 + v * hp / 2,
                   center + u * depth / 2 - v * hp / 2, center - u * depth / 2 - v * ha / 2]
        # clockwise order in (row, col) for _poly
        m = _poly(inst.shape, [tuple(p) for p in corners]) | _poly(inst.shape, [tuple(p) for p in corners[::-1]])
        inst[m] = k + 1
        truth["wedge"].append(ha / hp)
        truth["slip"].append(slip.get(k, 0.0))
        if k == n_vert - 1:
            break
        top = r - vh - 1
        h = dh * disc_scale.get(k, 1.0)
        dcen = np.array([top - h / 2, c0 - shift])
        dc = [dcen - u * depth * 0.47 + v * h / 2, dcen + u * depth * 0.47 + v * h / 2,
              dcen + u * depth * 0.47 - v * h / 2, dcen - u * depth * 0.47 - v * h / 2]
        m = _poly(inst.shape, [tuple(p) for p in dc]) | _poly(inst.shape, [tuple(p) for p in dc[::-1]])
        inst[m & (inst == 0)] = DISC_OFFSET + k + 1
        truth["dhi"].append(h / vh)
        r = top - h - 1
    # canal: band posterior to the column
    rows = np.arange(size)
    occupied = np.nonzero(inst.any(1))[0]
    for row in rows[occupied.min():occupied.max()]:
        cols = np.nonzero(inst[row])[0]
        if len(cols):
            back = cols.max() + 2
            inst[row, back:back + int(depth * 0.35)] = np.where(inst[row, back:back + int(depth * 0.35)] == 0,
                                                                CANAL, inst[row, back:back + int(depth * 0.35)])
    img = 0.25 + 0.08 * ndimage.gaussian_filter(rng.standard_normal((size, size)), 6) * 5
    img[(inst >= 1) & (inst <= 25)] = 0.45
    img[inst > DISC_OFFSET] = 0.75
    img[inst == CANAL] = 0.95
    img = ndimage.gaussian_filter(img, 1.0) + rng.normal(0, 0.03, img.shape)
    return np.clip(img, 0, 1).astype(np.float32), inst, truth


def negative(rng: np.random.Generator, size: int = 256) -> np.ndarray:
    """A non-spine image: smooth blobs, gradients or noise."""
    kind = rng.integers(3)
    if kind == 0:
        img = ndimage.gaussian_filter(rng.standard_normal((size, size)), rng.uniform(2, 20))
    elif kind == 1:
        yy, xx = np.mgrid[0:size, 0:size] / size
        img = rng.uniform(-1, 1) * yy + rng.uniform(-1, 1) * xx + 0.2 * rng.standard_normal((size, size))
    else:
        img = rng.random((size, size)) ** rng.uniform(0.5, 3)
    img = img - img.min()
    return (img / (img.max() + 1e-6)).astype(np.float32)
