// Morphometry from a sagittal class map (0 bg, 1 vertebra, 2 disc, 3 canal).
// Port of train/measure.py; tests/test_parity.mjs checks both give the same numbers.
// Points are [row, col]. Per disc: u = long axis pointing posterior, v = perpendicular pointing up.

export const DISC_NAMES = ["L5/S1", "L4/L5", "L3/L4", "L2/L3", "L1/L2", "T12/L1", "T11/T12",
  "T10/T11", "T9/T10", "T8/T9", "T7/T8", "T6/T7"];
export const VERT_NAMES = ["S1", "L5", "L4", "L3", "L2", "L1", "T12", "T11", "T10", "T9", "T8", "T7", "T6"];
const MIN_PX = { 1: 40, 2: 15, 3: 15 };

export function q(arr, p) {
  const s = Float64Array.from(arr).sort();
  return s[Math.floor((p / 100) * (s.length - 1) + 0.5)];
}

const dot = (a, b) => a[0] * b[0] + a[1] * b[1];
const sub = (a, b) => [a[0] - b[0], a[1] - b[1]];
const norm = (a) => { const n = Math.hypot(a[0], a[1]); return [a[0] / n, a[1] / n]; };

function mean(pts) {
  let r = 0, c = 0;
  for (const p of pts) { r += p[0]; c += p[1]; }
  return [r / pts.length, c / pts.length];
}

export function components(cls, size, label, minPx) {
  const seen = new Uint8Array(size * size);
  const out = [];
  const stack = new Int32Array(size * size);
  for (let i = 0; i < size * size; i++) {
    if (cls[i] !== label || seen[i]) continue;
    let top = 0; stack[top++] = i; seen[i] = 1;
    const pts = [];
    while (top) {
      const j = stack[--top];
      const r = (j / size) | 0, c = j - r * size;
      pts.push([r, c]);
      if (r > 0 && cls[j - size] === label && !seen[j - size]) { seen[j - size] = 1; stack[top++] = j - size; }
      if (r < size - 1 && cls[j + size] === label && !seen[j + size]) { seen[j + size] = 1; stack[top++] = j + size; }
      if (c > 0 && cls[j - 1] === label && !seen[j - 1]) { seen[j - 1] = 1; stack[top++] = j - 1; }
      if (c < size - 1 && cls[j + 1] === label && !seen[j + 1]) { seen[j + 1] = 1; stack[top++] = j + 1; }
    }
    if (pts.length >= minPx) out.push(pts);
  }
  return out;
}

export function majorAxis(pts) {
  const c = mean(pts);
  let a = 0, b = 0, e = 0;
  for (const p of pts) {
    const dr = p[0] - c[0], dc = p[1] - c[1];
    a += dr * dr; b += dr * dc; e += dc * dc;
  }
  a /= pts.length; b /= pts.length; e /= pts.length;
  const tr = a + e, det = a * e - b * b;
  const lam = tr / 2 + Math.sqrt(Math.max(tr * tr / 4 - det, 0));
  let vec;
  if (Math.abs(b) > 1e-9) vec = [lam - e, b];
  else vec = a >= e ? [1, 0] : [0, 1];
  return [c, norm(vec)];
}

function orient(u, c, canal, reach) {
  let sign = 0;
  if (canal && canal.length) {
    let r = 0, cc = 0, n = 0;
    for (const p of canal) {
      if (Math.hypot(p[0] - c[0], p[1] - c[1]) < reach) { r += p[0]; cc += p[1]; n++; }
    }
    if (n) sign = dot([r / n - c[0], cc / n - c[1]], u);
  }
  if (sign === 0) sign = u[1];
  if (sign < 0) u = [-u[0], -u[1]];
  let v = [-u[1], u[0]];
  if (v[0] > 0) v = [-v[0], -v[1]];
  return [u, v];
}

function project(pts, c, u) {
  const out = new Float64Array(pts.length);
  for (let i = 0; i < pts.length; i++) out[i] = (pts[i][0] - c[0]) * u[0] + (pts[i][1] - c[1]) * u[1];
  return out;
}

export function measure(cls, size) {
  const verts = components(cls, size, 1, MIN_PX[1]);
  const discs = components(cls, size, 2, MIN_PX[2]);
  const canal = [];
  for (let i = 0; i < size * size; i++) if (cls[i] === 3) canal.push([(i / size) | 0, i % size]);
  const canalPts = canal.length ? canal : null;

  const D = discs.map((pts) => {
    let [c, u] = majorAxis(pts);
    const pu0 = project(pts, c, u);
    const length = q(pu0, 98) - q(pu0, 2) + 1;
    let v;
    [u, v] = orient(u, c, canalPts, 1.5 * length);
    return { pts, c, u, v, length, thickness: pts.length / length, upper: null, lower: null };
  });
  D.sort((x, y) => y.c[0] - x.c[0]);

  const V = verts.map((pts) => ({ pts, c: mean(pts) })).sort((x, y) => y.c[0] - x.c[0]);
  for (const d of D) {
    const best = { upper: 1e9, lower: 1e9 };
    V.forEach((vt, j) => {
      const rel = sub(vt.c, d.c);
      const along = dot(rel, d.u), up = dot(rel, d.v);
      if (Math.abs(along) > d.length) return;
      const side = up > 0 ? "upper" : "lower";
      const dist = Math.hypot(along, up);
      if (dist < best[side]) { best[side] = dist; d[side] = j; }
    });
  }

  V.forEach((vt, j) => {
    const us = D.filter((d) => d.upper === j || d.lower === j).map((d) => d.u);
    let u;
    if (us.length) {
      u = norm([us.reduce((s, x) => s + x[0], 0) / us.length, us.reduce((s, x) => s + x[1], 0) / us.length]);
    } else {
      u = majorAxis(vt.pts)[1];
      u = orient(u, vt.c, canalPts, 80)[0];
      if (Math.abs(u[0]) > Math.abs(u[1])) u = orient([-u[1], u[0]], vt.c, canalPts, 80)[0];
    }
    let v = [-u[1], u[0]];
    if (v[0] > 0) v = [-v[0], -v[1]];
    const pu = project(vt.pts, vt.c, u), pv = project(vt.pts, vt.c, v);
    const lo = q(pu, 2), hi = q(pu, 98), depth = hi - lo + 1;
    const ant = [], post = [];
    for (let i = 0; i < pu.length; i++) {
      if (pu[i] <= lo + 0.25 * depth) ant.push(pv[i]);
      if (pu[i] >= hi - 0.25 * depth) post.push(pv[i]);
    }
    const antH = ant.length > 2 ? q(ant, 95) - q(ant, 5) + 1 : NaN;
    const postH = post.length > 2 ? q(post, 95) - q(post, 5) + 1 : NaN;
    Object.assign(vt, { u, depth, height: vt.pts.length / depth, antH, postH,
      wedge: postH > 0 ? antH / postH : NaN });
  });

  const discsOut = D.map((d, k) => {
    const up = d.upper !== null ? V[d.upper] : null;
    const lo = d.lower !== null ? V[d.lower] : null;
    const hs = [up, lo].filter(Boolean).map((x) => x.height);
    const ref = lo || up;
    const dhi = hs.length ? d.thickness / (hs.reduce((a, b) => a + b, 0) / hs.length) : NaN;
    let slip = NaN;
    if (up && lo) slip = (100 * dot(sub(lo.c, up.c), d.u)) / lo.depth;
    let canalRatio = NaN;
    if (canalPts && ref) {
      const pu = [], half = Math.max(d.thickness, 4) / 2;
      for (const p of canalPts) {
        const rel = sub(p, d.c);
        const a = dot(rel, d.u), b = dot(rel, d.v);
        if (Math.abs(b) <= half && a > 0 && a < 1.5 * d.length) pu.push(a);
      }
      if (pu.length >= 3) canalRatio = (q(pu, 98) - q(pu, 2) + 1) / ref.depth;
    }
    return { name: k < DISC_NAMES.length ? DISC_NAMES[k] : `disc${k}`, centroid: d.c, u: d.u, v: d.v,
      length: d.length, thickness: d.thickness, dhi, slip_pct: slip, canal_ratio: canalRatio,
      upper: d.upper, lower: d.lower };
  });

  const vnames = {};
  D.forEach((d, k) => {
    if (d.upper !== null && k + 1 < VERT_NAMES.length) vnames[d.upper] = VERT_NAMES[k + 1];
    if (k === 0 && d.lower !== null) vnames[d.lower] = VERT_NAMES[0];
  });
  const vertsOut = V.map((vt, j) => ({ name: vnames[j] ?? "?", centroid: vt.c, depth: vt.depth,
    height: vt.height, ant_h: vt.antH, post_h: vt.postH, wedge: vt.wedge }));

  let lordosis = NaN;
  const lumbar = discsOut.slice(0, 5);
  if (lumbar.length >= 4) {
    lordosis = (Math.acos(Math.min(1, Math.abs(dot(lumbar[0].u, lumbar[lumbar.length - 1].u)))) * 180) / Math.PI;
  }
  return { discs: discsOut, vertebrae: vertsOut, lordosis_deg: lordosis,
    n_discs: D.length, n_vertebrae: V.length, canal_px: canal.length };
}

// Rotated square crop centred on a disc (anterior left, superior up), bilinear,
// matching measure.disc_crop / scipy map_coordinates(order=1, cval=0).
export function discCrop(img, size, disc, out = 64) {
  const side = 2.2 * disc.length;
  const [c, u, v] = [disc.centroid, disc.u, disc.v];
  const res = new Float32Array(out * out);
  for (let i = 0; i < out; i++) {
    const ti = (i + 0.5) / out - 0.5;
    for (let j = 0; j < out; j++) {
      const tj = (j + 0.5) / out - 0.5;
      const r = c[0] + side * (tj * u[0] - ti * v[0]);
      const cc = c[1] + side * (tj * u[1] - ti * v[1]);
      res[i * out + j] = bilinear(img, size, r, cc);
    }
  }
  return res;
}

function bilinear(img, size, r, c) {
  const r0 = Math.floor(r), c0 = Math.floor(c);
  const fr = r - r0, fc = c - c0;
  const at = (rr, cc) => (rr < 0 || cc < 0 || rr >= size || cc >= size ? 0 : img[rr * size + cc]);
  return (1 - fr) * ((1 - fc) * at(r0, c0) + fc * at(r0, c0 + 1)) + fr * ((1 - fc) * at(r0 + 1, c0) + fc * at(r0 + 1, c0 + 1));
}
