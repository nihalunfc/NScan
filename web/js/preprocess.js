// Image loading and preprocessing. Mirrors train/common.py (normalize, letterbox).

export const SIZE = 256;

// Returns { width, height, data: Float32Array (grey values), bitDepth, source }.
export async function loadImageFile(file) {
  const head = new Uint8Array(await file.slice(0, 132).arrayBuffer());
  const isDicom = /\.dcm$/i.test(file.name) ||
    (head.length >= 132 && String.fromCharCode(...head.slice(128, 132)) === "DICM");
  if (isDicom) return loadDicom(await file.arrayBuffer());
  const bmp = await createImageBitmap(file);
  return fromBitmap(bmp, file.name);
}

export async function loadImageUrl(url) {
  const blob = await (await fetch(url)).blob();
  return fromBitmap(await createImageBitmap(blob), url);
}

function fromBitmap(bmp, name) {
  const c = document.createElement("canvas");
  c.width = bmp.width; c.height = bmp.height;
  const ctx = c.getContext("2d", { willReadFrequently: true });
  ctx.drawImage(bmp, 0, 0);
  const px = ctx.getImageData(0, 0, c.width, c.height).data;
  const data = new Float32Array(c.width * c.height);
  let colour = 0;
  for (let i = 0, j = 0; i < data.length; i++, j += 4) {
    data[i] = 0.299 * px[j] + 0.587 * px[j + 1] + 0.114 * px[j + 2];
    colour += Math.abs(px[j] - px[j + 1]) + Math.abs(px[j + 1] - px[j + 2]);
  }
  return { width: c.width, height: c.height, data, bitDepth: 8, source: name,
    colourfulness: colour / data.length / 255 };
}

function loadDicom(buf) {
  /* global dicomParser */
  const ds = dicomParser.parseDicom(new Uint8Array(buf));
  const rows = ds.uint16("x00280010"), cols = ds.uint16("x00280011");
  const bits = ds.uint16("x00280100") || 16;
  const signed = ds.uint16("x00280103") === 1;
  const ts = ds.string("x00020010") || "";
  const el = ds.elements.x7fe00010;
  if (!el || !rows || !cols) throw new Error("This DICOM file has no readable image.");
  if (/^1\.2\.840\.10008\.1\.2\.4|^1\.2\.840\.10008\.1\.2\.5/.test(ts)) {
    throw new Error("This DICOM file is compressed. Please export the slice as PNG, or as an uncompressed DICOM.");
  }
  if ((ds.uint16("x00280002") || 1) !== 1) throw new Error("Colour DICOM files are not supported; please export a greyscale slice.");
  const n = rows * cols;
  const off = ds.byteArray.byteOffset + el.dataOffset;
  let raw;
  if (bits <= 8) raw = new Uint8Array(ds.byteArray.buffer, off, n);
  else raw = signed ? new Int16Array(ds.byteArray.buffer.slice(off, off + 2 * n)) : new Uint16Array(ds.byteArray.buffer.slice(off, off + 2 * n));
  const slope = parseFloat(ds.string("x00281053") || "1"), icpt = parseFloat(ds.string("x00281052") || "0");
  const data = new Float32Array(n);
  for (let i = 0; i < n; i++) data[i] = raw[i] * slope + icpt;
  const modality = ds.string("x00080060") || "";
  const desc = [ds.string("x0008103e"), ds.string("x00180024")].filter(Boolean).join(" ");
  const ps = (ds.string("x00280030") || "").split("\\").map(parseFloat);
  return { width: cols, height: rows, data, bitDepth: bits, source: "dicom", colourfulness: 0,
    dicom: { modality, description: desc, pixelSpacing: ps.length === 2 ? ps : null } };
}

export function percentile(data, p) {
  // sampled for speed on large images; exact enough for normalisation
  const step = Math.max(1, Math.floor(data.length / 200000));
  const s = [];
  for (let i = 0; i < data.length; i += step) s.push(data[i]);
  s.sort((a, b) => a - b);
  const x = (p / 100) * (s.length - 1);
  const lo = Math.floor(x), hi = Math.min(lo + 1, s.length - 1);
  return s[lo] + (s[hi] - s[lo]) * (x - lo);
}

export function normalize(img) {
  const lo = percentile(img.data, 0.5), hi = percentile(img.data, 99.5);
  const out = new Float32Array(img.data.length);
  const span = hi - lo;
  if (span < 1e-6) return { ...img, data: out, range: 0 };
  for (let i = 0; i < out.length; i++) out[i] = Math.min(1, Math.max(0, (img.data[i] - lo) / span));
  return { ...img, data: out, range: span };
}

// Pad to a centred square with zeros, then bilinear-resize to SIZE (grid_mode, edge clamp),
// as scipy.ndimage.zoom(order=1, mode="nearest", grid_mode=True) does in training.
export function letterbox(img, size = SIZE) {
  const { width: w, height: h, data } = img;
  const s = Math.max(w, h);
  const y0 = Math.floor((s - h) / 2), x0 = Math.floor((s - w) / 2);
  const at = (r, c) => {
    r = Math.min(s - 1, Math.max(0, r)); c = Math.min(s - 1, Math.max(0, c));
    const rr = r - y0, cc = c - x0;
    return rr < 0 || cc < 0 || rr >= h || cc >= w ? 0 : data[rr * w + cc];
  };
  const out = new Float32Array(size * size);
  const k = s / size;
  for (let i = 0; i < size; i++) {
    const r = (i + 0.5) * k - 0.5, r0 = Math.floor(r), fr = r - r0;
    for (let j = 0; j < size; j++) {
      const c = (j + 0.5) * k - 0.5, c0 = Math.floor(c), fc = c - c0;
      out[i * size + j] = (1 - fr) * ((1 - fc) * at(r0, c0) + fc * at(r0, c0 + 1)) +
        fr * ((1 - fc) * at(r0 + 1, c0) + fc * at(r0 + 1, c0 + 1));
    }
  }
  return out;
}

export function flipH(x, size = SIZE) {
  const out = new Float32Array(x.length);
  for (let i = 0; i < size; i++) for (let j = 0; j < size; j++) out[i * size + j] = x[i * size + size - 1 - j];
  return out;
}
