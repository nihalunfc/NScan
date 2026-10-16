"""Morphometry from a sagittal class map (0 bg, 1 vertebra, 2 disc, 3 canal).

This is the reference implementation of web/js/measure.js. Both must give the
same numbers for the same mask (tests/test_parity.mjs checks this), so the
algorithms deliberately use only simple operations: 4-connected components,
2x2 PCA, sorted-index quantiles.

Geometry convention, per disc:
  u = unit vector along the disc's long (antero-posterior) axis, pointing posterior
  v = unit vector perpendicular to u, pointing superior (up in the image)
"""
from __future__ import annotations

import math

import numpy as np
from scipy import ndimage

MIN_PX = {1: 40, 2: 15, 3: 15}
DISC_NAMES = ["L5/S1", "L4/L5", "L3/L4", "L2/L3", "L1/L2", "T12/L1", "T11/T12",
              "T10/T11", "T9/T10", "T8/T9", "T7/T8", "T6/T7"]
VERT_NAMES = ["S1", "L5", "L4", "L3", "L2", "L1", "T12", "T11", "T10", "T9", "T8", "T7", "T6"]


def q(a: np.ndarray, p: float) -> float:
    """Quantile by sorted index (no interpolation); mirrors q() in measure.js."""
    s = np.sort(a)
    return float(s[int(math.floor(p / 100 * (len(s) - 1) + 0.5))])


def components(mask: np.ndarray, min_px: int) -> list[np.ndarray]:
    lab, n = ndimage.label(mask, structure=[[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    out = []
    for i in range(1, n + 1):
        rr, cc = np.nonzero(lab == i)
        if len(rr) >= min_px:
            out.append(np.stack([rr, cc], 1).astype(np.float64))
    return out


def major_axis(pts: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    c = pts.mean(0)
    d = pts - c
    a, b, e = (d[:, 0] ** 2).mean(), (d[:, 0] * d[:, 1]).mean(), (d[:, 1] ** 2).mean()
    # largest eigenvector of [[a, b], [b, e]] in closed form
    tr, det = a + e, a * e - b * b
    lam = tr / 2 + math.sqrt(max(tr * tr / 4 - det, 0))
    if abs(b) > 1e-9:
        vec = np.array([lam - e, b])
    else:
        vec = np.array([1.0, 0.0]) if a >= e else np.array([0.0, 1.0])
    return c, vec / np.linalg.norm(vec)


def orient(u: np.ndarray, c: np.ndarray, canal_pts: np.ndarray | None, reach: float):
    """Flip u to point posterior (towards the canal); build v pointing up."""
    sign = 0.0
    if canal_pts is not None and len(canal_pts):
        near = canal_pts[np.hypot(*(canal_pts - c).T) < reach]
        if len(near):
            sign = float((near.mean(0) - c) @ u)
    if sign == 0.0:
        sign = u[1]  # fall back: posterior is to the right of the image
    if sign < 0:
        u = -u
    v = np.array([-u[1], u[0]])
    if v[0] > 0:  # rows grow downwards; superior means negative row
        v = -v
    return u, v


def measure(cls: np.ndarray) -> dict:
    verts = components(cls == 1, MIN_PX[1])
    discs = components(cls == 2, MIN_PX[2])
    canal = np.argwhere(cls == 3).astype(np.float64)
    canal = canal if len(canal) else None

    D = []
    for pts in discs:
        c, u = major_axis(pts)
        pu0 = (pts - c) @ u
        length = q(pu0, 98) - q(pu0, 2) + 1
        u, v = orient(u, c, canal, 1.5 * length)
        D.append({"pts": pts, "c": c, "u": u, "v": v, "length": length,
                  "thickness": len(pts) / length})
    D.sort(key=lambda d: -d["c"][0])  # bottom of the image first

    V = sorted(({"pts": p, "c": p.mean(0)} for p in verts), key=lambda x: -x["c"][0])
    for d in D:
        d["upper"] = d["lower"] = None
        best = {"upper": 1e9, "lower": 1e9}
        for j, vt in enumerate(V):
            rel = vt["c"] - d["c"]
            along, up = rel @ d["u"], rel @ d["v"]
            if abs(along) > d["length"]:
                continue
            side = "upper" if up > 0 else "lower"
            dist = math.hypot(along, up)
            if dist < best[side]:
                best[side], d[side] = dist, j

    for j, vt in enumerate(V):
        us = [d["u"] for d in D if d["upper"] == j or d["lower"] == j]
        if us:
            u = np.mean(us, 0)
            u /= np.linalg.norm(u)
        else:
            _, u = major_axis(vt["pts"])
            u, _ = orient(u, vt["c"], canal, 80)
            if abs(u[0]) > abs(u[1]):  # want the more horizontal axis as AP
                u, _ = orient(np.array([-u[1], u[0]]), vt["c"], canal, 80)
        v = np.array([-u[1], u[0]])
        if v[0] > 0:
            v = -v
        rel = vt["pts"] - vt["c"]
        pu, pv = rel @ u, rel @ v
        lo, hi = q(pu, 2), q(pu, 98)
        depth = hi - lo + 1
        ant, post = pv[pu <= lo + 0.25 * depth], pv[pu >= hi - 0.25 * depth]
        ant_h = q(ant, 95) - q(ant, 5) + 1 if len(ant) > 2 else float("nan")
        post_h = q(post, 95) - q(post, 5) + 1 if len(post) > 2 else float("nan")
        vt.update(u=u, depth=depth, height=len(vt["pts"]) / depth, ant_h=ant_h, post_h=post_h,
                  wedge=ant_h / post_h if post_h == post_h and post_h > 0 else float("nan"))

    discs_out = []
    for k, d in enumerate(D):
        up = V[d["upper"]] if d["upper"] is not None else None
        lo = V[d["lower"]] if d["lower"] is not None else None
        hs = [x["height"] for x in (up, lo) if x is not None]
        ref = lo or up
        dhi = d["thickness"] / float(np.mean(hs)) if hs else float("nan")
        slip = float("nan")
        if up is not None and lo is not None:
            slip = 100 * float((lo["c"] - up["c"]) @ d["u"]) / lo["depth"]  # + = upper slips anterior
        canal_ratio = float("nan")
        if canal is not None and ref is not None:
            rel = canal - d["c"]
            pu, pv = rel @ d["u"], rel @ d["v"]
            band = (np.abs(pv) <= max(d["thickness"], 4) / 2) & (pu > 0) & (pu < 1.5 * d["length"])
            if band.sum() >= 3:
                canal_ratio = (q(pu[band], 98) - q(pu[band], 2) + 1) / ref["depth"]
        discs_out.append({
            "name": DISC_NAMES[k] if k < len(DISC_NAMES) else f"disc{k}",
            "centroid": d["c"].tolist(), "u": d["u"].tolist(), "v": d["v"].tolist(),
            "length": d["length"], "thickness": d["thickness"], "dhi": dhi,
            "slip_pct": slip, "canal_ratio": canal_ratio,
            "upper": d["upper"], "lower": d["lower"],
        })

    # name vertebrae from the disc they sit above
    vnames = {}
    for k, d in enumerate(D):
        if d["upper"] is not None and k + 1 < len(VERT_NAMES):
            vnames[d["upper"]] = VERT_NAMES[k + 1]
        if k == 0 and d["lower"] is not None:
            vnames[d["lower"]] = VERT_NAMES[0]
    verts_out = [{"name": vnames.get(j, "?"), "centroid": vt["c"].tolist(), "depth": vt["depth"],
                  "height": vt["height"], "ant_h": vt["ant_h"], "post_h": vt["post_h"],
                  "wedge": vt["wedge"]} for j, vt in enumerate(V)]

    lordosis = float("nan")
    lumbar = [d for d in discs_out[:5]]
    if len(lumbar) >= 4:
        a, b = np.array(lumbar[0]["u"]), np.array(lumbar[-1]["u"])
        lordosis = math.degrees(math.acos(min(1.0, abs(float(a @ b)))))
    return {"discs": discs_out, "vertebrae": verts_out, "lordosis_deg": lordosis,
            "n_discs": len(D), "n_vertebrae": len(V), "canal_px": 0 if canal is None else len(canal)}


def disc_crop(img: np.ndarray, centroid, u, v, length: float, size: int = 64) -> np.ndarray:
    """Rotated square crop centred on a disc, anterior left, superior up.

    Side = 2.2 x disc length. Bilinear sampling; mirrors discCrop() in measure.js.
    """
    side = 2.2 * length
    c, u, v = np.asarray(centroid, float), np.asarray(u, float), np.asarray(v, float)
    t = (np.arange(size) + 0.5) / size - 0.5
    jj, ii = np.meshgrid(t, t)              # jj along u (left->right), ii along -v (top->bottom)
    rr = c[0] + side * (jj * u[0] - ii * v[0])
    cc = c[1] + side * (jj * u[1] - ii * v[1])
    return ndimage.map_coordinates(img.astype(np.float32), [rr, cc], order=1, mode="constant", cval=0.0)
