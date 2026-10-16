// Deciding whether a result is conclusive. Thresholds come from models/quality.json,
// which training calibrates on held-out SPIDER scans (train/train_seg.py).

const SIZE = 256;

export function lapVar(x, size = SIZE) {
  let s = 0, s2 = 0, n = 0;
  for (let i = 1; i < size - 1; i++) {
    for (let j = 1; j < size - 1; j++) {
      const k = i * size + j;
      const v = x[k - size] + x[k + size] + x[k - 1] + x[k + 1] - 4 * x[k];
      s += v; s2 += v * v; n++;
    }
  }
  const m = s / n;
  return s2 / n - m * m;
}

// p, pf: Float32Array [4 * SIZE * SIZE] softmax probabilities (class-major) for the image and its flip.
export function modelFeatures(p, pf, size = SIZE) {
  const n = size * size;
  let inter = 0, sa = 0, sb = 0, same = 0, union = 0, entSum = 0, fg = 0;
  const lab = new Uint8Array(n);
  const log4 = Math.log(4);
  for (let i = 0; i < n; i++) {
    let a = 0, b = 0, m = 0, ba = -1, bb = -1, bm = -1, ent = 0;
    for (let c = 0; c < 4; c++) {
      const x = p[c * n + i], y = pf[c * n + i], z = (x + y) / 2;
      if (x > ba) { ba = x; a = c; }
      if (y > bb) { bb = y; b = c; }
      if (z > bm) { bm = z; m = c; }
      ent -= z * Math.log(Math.max(z, 1e-8));
    }
    lab[i] = m;
    const fa = a > 0, fb = b > 0;
    if (fa) sa++;
    if (fb) sb++;
    if (fa && fb) inter++;
    if (fa || fb) { union++; if (a === b) same++; }
    if (m > 0) { fg++; entSum += ent / log4; }
  }
  return {
    labels: lab,
    tta_dice: sa + sb ? (2 * inter) / (sa + sb) : 0,
    tta_label_agree: union ? same / union : 0,
    fg_entropy: fg ? entSum / fg : 1,
    fg_frac: fg / n,
  };
}

// T2-weighted images show CSF (canal) brighter than vertebral bone marrow; T1 the reverse.
export function guessSequence(x, labels) {
  let canal = 0, nc = 0, vert = 0, nv = 0;
  for (let i = 0; i < labels.length; i++) {
    if (labels[i] === 3) { canal += x[i]; nc++; } else if (labels[i] === 1) { vert += x[i]; nv++; }
  }
  if (nc < 30 || nv < 100) return { seq: "unknown", ratio: NaN };
  const ratio = canal / nc / Math.max(vert / nv, 1e-3);
  return { seq: ratio > 1.15 ? "T2" : ratio < 0.85 ? "T1" : "unknown", ratio };
}

// Collects every reason the reading should not be trusted, each with advice for a better scan.
export function assess({ raw, feats, lap, meas, thr, modality, seq }) {
  const issues = [];
  const add = (level, title, advice) => issues.push({ level, title, advice });
  const short = Math.min(raw.width, raw.height);
  if (modality !== "mri") {
    add("block", "This modality is not supported yet",
      "Phase one reads sagittal lumbar MRI only. CT and X-ray models are planned; for now, upload a sagittal MRI slice.");
  }
  if (short < 160) {
    add("block", `The image is very small (${raw.width}×${raw.height} px)`,
      "Upload the original slice, or a screenshot at full screen resolution (at least 256 px on the short side).");
  }
  if (raw.colourfulness > 0.08) {
    add("warn", "The image contains a lot of colour",
      "Upload the plain greyscale scan without coloured annotations or overlays.");
  }
  if (raw.range !== undefined && raw.bitDepth === 8 && raw.range < 40) {
    add("block", "The image has very low contrast",
      "Avoid photos of a screen in bright light; export the slice directly from the viewer or the DICOM file.");
  }
  if (thr && lap < thr.min_lap_var) {
    add("block", "The image looks blurred",
      "Use a sharper image: export the slice rather than photographing it, and avoid zoomed-in screenshots.");
  }
  if (thr && feats.fg_frac < thr.min_fg_frac) {
    add("block", "No spine anatomy was recognised",
      "Make sure the image is a sagittal (side view) MRI slice of the lower back, through the middle of the spinal canal.");
  } else if (meas.n_discs < (thr?.min_discs ?? 3) || meas.n_vertebrae < 3) {
    add("block", `Only ${meas.n_discs} disc(s) and ${meas.n_vertebrae} vertebra(e) could be identified`,
      "Upload a mid-sagittal slice that shows at least L3 down to the sacrum, without cropping.");
  }
  if (thr && feats.fg_frac >= thr.min_fg_frac) {
    if (feats.tta_dice < thr.min_tta_dice || feats.tta_label_agree < thr.min_tta_label_agree) {
      add("block", "The model's outline of the anatomy is unstable",
        "This usually means an unusual view, heavy artefact or surgical hardware. A standard sagittal T2-weighted slice through the canal works best.");
    } else if (feats.fg_entropy > thr.max_fg_entropy) {
      add("warn", "The model is less certain than usual about the anatomy outline",
        "Results are shown, but a cleaner mid-sagittal slice would give a more reliable reading.");
    }
  }
  if (seq.seq !== "T2" && modality === "mri") {
    add("warn", seq.seq === "T1" ? "This looks like a T1-weighted image" : "The MRI sequence could not be identified",
      "Disc degeneration (Pfirrmann) and most findings are graded on T2-weighted images. Add a sagittal T2 slice for those findings.");
  }
  const blocked = issues.some((i) => i.level === "block");
  return { conclusive: !blocked, issues };
}
