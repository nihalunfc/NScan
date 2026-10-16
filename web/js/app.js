/* global ort */
import { SIZE, loadImageFile, loadImageUrl, normalize, letterbox, flipH } from "./preprocess.js";
import { measure, discCrop } from "./measure.js";
import { lapVar, modelFeatures, guessSequence, assess } from "./quality.js";
import { decodeGrades, buildReport, TASK_LABELS } from "./report.js";

const $ = (s) => document.querySelector(s);
const state = { modality: "mri", seg: null, grade: null, meta: {}, last: null };

ort.env.wasm.wasmPaths = new URL("vendor/ort/", location.href).href;
ort.env.wasm.numThreads = 1; // GitHub Pages cannot enable cross-origin isolation

async function loadJSON(url) {
  try { const r = await fetch(url, { cache: "no-cache" }); return r.ok ? await r.json() : null; } catch { return null; }
}

async function init() {
  const [quality, seg, grade, norms, build] = await Promise.all(
    ["quality", "seg_metrics", "grade_metrics", "norms", "build"].map((n) => loadJSON(`models/${n}.json`)));
  state.meta = { quality, seg, grade, norms, build };
  try {
    state.seg = await ort.InferenceSession.create("models/spine_seg.onnx", { executionProviders: ["wasm"] });
  } catch (e) {
    console.error("model load failed", e);
    $("#model-status").textContent = "The model has not been published yet. Training runs on GitHub Actions; check back soon.";
    $("#model-status").classList.add("warn");
    return;
  }
  try { state.grade = await ort.InferenceSession.create("models/disc_grade.onnx", { executionProviders: ["wasm"] }); } catch { state.grade = null; }
  $("#model-status").textContent = "Model loaded. Your image is analysed in this browser and never uploaded.";
  $("#model-status").classList.add("ok");
  renderModelCard();
  document.body.classList.add("ready");
}

async function run(raw) {
  $("#results").hidden = false;
  $("#verdict").className = "card verdict busy";
  $("#verdict").innerHTML = "<h2>Analysing…</h2>";
  await new Promise((r) => setTimeout(r, 20));
  const t0 = performance.now();
  const norm = normalize(raw);
  raw.range = norm.range;
  const x = letterbox(norm);
  const thr = state.meta.quality;
  const [p, pf] = await segment(x);
  const feats = modelFeatures(p, pf);
  const lap = lapVar(x);
  const meas = measure(feats.labels, SIZE);
  const seq = guessSequence(x, feats.labels);
  const verdict = assess({ raw, feats, lap, meas, thr, modality: state.modality, seq });
  let grades = null;
  if (state.grade && meas.discs.length) {
    const crops = new Float32Array(meas.discs.length * 64 * 64);
    meas.discs.forEach((d, i) => crops.set(discCrop(x, SIZE, d), i * 64 * 64));
    const out = await state.grade.run({ crops: new ort.Tensor("float32", crops, [meas.discs.length, 1, 64, 64]) });
    grades = decodeGrades(out.logits.data, meas.discs.length);
  }
  const report = buildReport({ meas, grades, gradeMetrics: state.meta.grade, norms: state.meta.norms, seq: seq.seq });
  state.last = { x, labels: feats.labels, meas, report, verdict, feats, seq, lap, ms: performance.now() - t0, source: raw.source };
  window.__last = state.last; // for debugging and automated tests
  draw();
  renderVerdict();
  renderReport();
}

async function segment(x) {
  const n = SIZE * SIZE;
  const soft = (logits) => {
    const p = new Float32Array(4 * n);
    for (let i = 0; i < n; i++) {
      let m = -Infinity;
      for (let c = 0; c < 4; c++) m = Math.max(m, logits[c * n + i]);
      let s = 0;
      for (let c = 0; c < 4; c++) { const e = Math.exp(logits[c * n + i] - m); p[c * n + i] = e; s += e; }
      for (let c = 0; c < 4; c++) p[c * n + i] /= s;
    }
    return p;
  };
  const a = await state.seg.run({ image: new ort.Tensor("float32", x, [1, 1, SIZE, SIZE]) });
  const b = await state.seg.run({ image: new ort.Tensor("float32", flipH(x), [1, 1, SIZE, SIZE]) });
  const p = soft(a.logits.data);
  const pfRaw = soft(b.logits.data);
  const pf = new Float32Array(4 * n);
  for (let c = 0; c < 4; c++) pf.set(flipH(pfRaw.subarray(c * n, (c + 1) * n)), c * n);
  return [p, pf];
}

const COLORS = { 1: [217, 119, 87], 2: [95, 168, 211], 3: [140, 200, 120] };

function draw() {
  const { x, labels, meas, report } = state.last;
  const cv = $("#view"), ctx = cv.getContext("2d");
  const img = ctx.createImageData(SIZE, SIZE);
  const overlay = $("#show-overlay").checked;
  const flagged = new Set(report.notable.map((l) => l.name));
  for (let i = 0; i < SIZE * SIZE; i++) {
    const g = x[i] * 255;
    let r = g, gg = g, b = g;
    if (overlay && labels[i]) {
      const c = COLORS[labels[i]];
      r = 0.6 * g + 0.4 * c[0]; gg = 0.6 * g + 0.4 * c[1]; b = 0.6 * g + 0.4 * c[2];
    }
    img.data.set([r, gg, b, 255], i * 4);
  }
  const off = new OffscreenCanvas(SIZE, SIZE);
  off.getContext("2d").putImageData(img, 0, 0);
  ctx.imageSmoothingEnabled = true;
  ctx.drawImage(off, 0, 0, cv.width, cv.height);
  if (!overlay) return;
  const k = cv.width / SIZE;
  ctx.font = `600 ${Math.round(11 * k / 2)}px system-ui, sans-serif`;
  ctx.textBaseline = "middle";
  for (const d of meas.discs) {
    const [r, c] = d.centroid;
    const tx = c * k - d.u[1] * d.length * 0.75 * k, ty = r * k - d.u[0] * d.length * 0.75 * k;
    const bad = flagged.has(d.name);
    ctx.fillStyle = bad ? "#f2b84b" : "rgba(255,255,255,.9)";
    ctx.textAlign = "right";
    ctx.fillText(d.name, tx, ty);
  }
  for (const v of meas.vertebrae) {
    if (v.name === "?") continue;
    ctx.fillStyle = "rgba(255,255,255,.75)";
    ctx.textAlign = "center";
    ctx.fillText(v.name, v.centroid[1] * k, v.centroid[0] * k);
  }
}

function renderVerdict() {
  const { verdict, report, seq } = state.last;
  const el = $("#verdict");
  const issues = verdict.issues.map((i) =>
    `<li class="${i.level}"><strong>${i.title}.</strong> ${i.advice}</li>`).join("");
  if (!verdict.conclusive) {
    el.className = "card verdict inconclusive";
    el.innerHTML = `<h2>Inconclusive: please get a better scan</h2>
      <p>The image could not be read reliably, so no findings are shown. Here is what to change:</p><ul class="issues">${issues}</ul>`;
    $("#report").hidden = true;
    return;
  }
  const n = report.notable;
  el.className = "card verdict " + (n.length ? "findings" : "clear");
  const summary = n.length
    ? `Possible changes at ${n.map((l) => `<strong>${l.name}</strong>`).join(", ")}. Details for every level are below.`
    : "No level stands out from the reference range or the model's findings. Details for every level are below.";
  el.innerHTML = `<h2>${n.length ? "Readout ready: some levels stand out" : "Readout ready: nothing stands out"}</h2>
    <p>${summary}</p>
    <p class="muted">Sequence detected: ${seq.seq === "unknown" ? "not identified" : seq.seq + "-weighted"}.
    Degenerative changes are common in people without back pain and become more common with age, so a finding here is not necessarily the cause of symptoms.</p>
    ${issues ? `<ul class="issues">${issues}</ul>` : ""}`;
  $("#report").hidden = false;
}

const fmtP = (p) => `${Math.round(p * 100)}%`;
const devClass = (d) => ["ok", "mild", "warn", "bad"][d.level] ?? "";

function renderReport() {
  const { report } = state.last;
  const rows = report.levels.map((l) => {
    const findings = l.findings.length
      ? l.findings.map((f) => `<li class="${f.status}"><span>${f.label}</span><em>${f.status} (${fmtP(f.p)})</em></li>`).join("")
      : `<li class="none">${state.last.seq.seq === "T2" && state.grade ? "No findings flagged" : "Findings need a T2-weighted image"}</li>`;
    const pf = l.pfirrmann
      ? `<p class="pf">Disc degeneration (Pfirrmann): grade <strong>${l.pfirrmann.grade}</strong> of 5, ${l.pfirrmann.text} <span class="muted">(${fmtP(l.pfirrmann.p)} confidence)</span></p>` : "";
    const meas = l.measures.map((m) => `<tr><td>${m.label}</td><td>${Number.isFinite(m.value) ? m.fmt(m.value) : "–"}</td>
      <td class="${devClass(m.dev)}">${Number.isFinite(m.z) ? `z = ${m.z.toFixed(1)}, ` : ""}${m.dev.tag}</td></tr>`).join("");
    return `<details class="level" ${l.score >= 2 ? "open" : ""}><summary><span class="lv">${l.name}</span>
      <span class="badge ${l.score >= 4 ? "bad" : l.score >= 2 ? "warn" : "ok"}">${l.score >= 4 ? "notable" : l.score >= 2 ? "possible change" : "unremarkable"}</span></summary>
      ${pf}<ul class="findings">${findings}</ul><table>${meas}</table></details>`;
  }).join("");
  const verts = report.vertebrae.map((v) => `<tr><td>${v.name}</td><td>${Number.isFinite(v.wedge) ? v.wedge.toFixed(2) : "–"}</td>
    <td class="${v.genant ? "warn" : devClass(v.dev)}">${v.genant ? `anterior height loss in the ${v.genant} range (Genant)` : v.dev.tag}</td></tr>`).join("");
  const L = report.lordosis;
  $("#report").innerHTML = `<div class="card"><h3>Disc levels</h3>${rows || "<p>No lumbar levels identified.</p>"}</div>
    <div class="card"><h3>Vertebral bodies</h3><p class="muted">Ratio of front to back height. Wedge-shaped vertebrae can indicate a compression deformity.</p>
    <table><tr><th>Level</th><th>Front/back height</th><th>Compared with reference</th></tr>${verts}</table>
    <p>Lumbar curve (angle between the lowest and highest lumbar discs): ${Number.isFinite(L.value) ? `${L.value.toFixed(0)}°, ${L.dev.tag}` : "not measurable on this image"}.</p></div>
    <div class="card small"><p class="muted">Analysed in ${Math.round(state.last.ms)} ms on this device. Level names assume the lowest disc is L5/S1; transitional vertebrae are not detected yet.</p>
    <button id="download">Download readout (JSON)</button></div>`;
  $("#download").onclick = downloadReport;
}

function downloadReport() {
  const { meas, report, verdict, feats, seq, source } = state.last;
  const out = { software: "N Scanning research prototype (not a medical device)", build: state.meta.build, source,
    verdict, sequence: seq, quality: { tta_dice: feats.tta_dice, tta_label_agree: feats.tta_label_agree, fg_entropy: feats.fg_entropy },
    measurements: meas, report: { ...report, levels: report.levels.map(({ disc, ...r }) => r) } };
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([JSON.stringify(out, null, 1)], { type: "application/json" }));
  a.download = "n-scanning-readout.json";
  a.click();
}

function renderModelCard() {
  const { seg, grade, norms, build } = state.meta;
  const pct = (v) => (v === null || v === undefined ? "–" : `${(v * 100).toFixed(1)}%`);
  const f2 = (v) => (v === null || v === undefined ? "–" : v.toFixed(2));
  const tasks = grade ? Object.entries(grade.tasks).map(([k, t]) => `<tr><td>${TASK_LABELS[k]}</td><td>${f2(t.auc)}</td><td>${pct(t.prevalence)}</td><td>${t.n}</td></tr>`).join("") : "";
  $("#model-card").innerHTML = `
    <p>Held-out test patients: ${seg?.val_patients ?? "–"}. ${seg?.synthetic_smoke_test ? "<strong>These numbers come from a synthetic smoke test, not real scans.</strong>" : ""}</p>
    <table><tr><th>Segmentation (Dice, mid-sagittal slice)</th><th></th></tr>
      <tr><td>Vertebrae</td><td>${f2(seg?.dice_vertebra)}</td></tr><tr><td>Discs</td><td>${f2(seg?.dice_disc)}</td></tr><tr><td>Spinal canal</td><td>${f2(seg?.dice_canal)}</td></tr></table>
    ${grade ? `<table><tr><th>Finding (T2, per disc)</th><th>AUC</th><th>Prevalence</th><th>n</th></tr>${tasks}
      <tr><td>Pfirrmann grade, exact / within one grade</td><td colspan="3">${pct(grade.pfirrmann_acc)} / ${pct(grade.pfirrmann_acc_within1)}</td></tr></table>
      <p class="muted">Findings with AUC below 0.65 are hidden in the readout. For comparison, radiologists agree with each other only moderately on several of these grades.</p>` : ""}
    <p class="muted">Reference ranges: ${norms ? `${norms.n_reference_discs} discs graded unremarkable in the training patients. ${norms.caveat}` : "not available"}.
    ${build ? `Model build ${build.commit?.slice(0, 7) ?? ""} on ${build.date ?? ""}.` : ""}</p>`;
}

// ---------- wiring
document.querySelectorAll("[name=modality]").forEach((r) => r.addEventListener("change", (e) => {
  state.modality = e.target.value;
  $("#modality-note").hidden = state.modality === "mri";
}));
$("#file").addEventListener("change", (e) => e.target.files[0] && handle(() => loadImageFile(e.target.files[0])));
const dz = $("#drop");
dz.addEventListener("dragover", (e) => { e.preventDefault(); dz.classList.add("over"); });
dz.addEventListener("dragleave", () => dz.classList.remove("over"));
dz.addEventListener("drop", (e) => {
  e.preventDefault(); dz.classList.remove("over");
  if (e.dataTransfer.files[0]) handle(() => loadImageFile(e.dataTransfer.files[0]));
});
document.querySelectorAll("[data-sample]").forEach((b) => b.addEventListener("click", () => handle(() => loadImageUrl(b.dataset.sample))));
$("#show-overlay").addEventListener("change", () => state.last && draw());
$("#consent").addEventListener("change", (e) => document.body.classList.toggle("consented", e.target.checked));

async function handle(loader) {
  if (!$("#consent").checked) { $("#consent-box").classList.add("shake"); setTimeout(() => $("#consent-box").classList.remove("shake"), 500); return; }
  if (!state.seg) return;
  try {
    const raw = await loader();
    await run(raw);
    $("#results").scrollIntoView({ behavior: "smooth", block: "start" });
  } catch (err) {
    $("#results").hidden = false;
    $("#verdict").className = "card verdict inconclusive";
    $("#verdict").innerHTML = `<h2>Could not read this file</h2><p>${err.message}</p>`;
    $("#report").hidden = true;
  }
}

init();
