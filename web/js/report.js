// Turns model outputs and measurements into plain-language findings.

export const TASK_LABELS = {
  modic: "Modic change (bone marrow signal next to the disc)",
  up_endplate: "Upper endplate irregularity",
  low_endplate: "Lower endplate irregularity",
  spondylolisthesis: "Vertebral slip (spondylolisthesis)",
  herniation: "Disc herniation",
  narrowing: "Disc space narrowing",
  bulging: "Disc bulging",
};
const TASKS = Object.keys(TASK_LABELS);
const LUMBAR = ["L5/S1", "L4/L5", "L3/L4", "L2/L3", "L1/L2"];

const softmax = (a) => { const m = Math.max(...a); const e = a.map((x) => Math.exp(x - m)); const s = e.reduce((x, y) => x + y, 0); return e.map((x) => x / s); };
const sigmoid = (x) => 1 / (1 + Math.exp(-x));

export function decodeGrades(logits, n) {
  const k = 5 + TASKS.length;
  const out = [];
  for (let i = 0; i < n; i++) {
    const row = Array.from(logits.slice(i * k, (i + 1) * k));
    const pf = softmax(row.slice(0, 5));
    const bin = Object.fromEntries(TASKS.map((t, j) => [t, sigmoid(row[5 + j])]));
    out.push({ pfirrmann: pf, expected: pf.reduce((s, p, g) => s + p * (g + 1), 0), binary: bin });
  }
  return out;
}

function z(value, ref) {
  if (!ref || !Number.isFinite(value)) return NaN;
  return (value - ref.median) / ref.robust_sd;
}

export function deviation(zv, lowIsBad = true) {
  if (!Number.isFinite(zv)) return { tag: "n/a", level: 0 };
  const bad = lowIsBad ? -zv : Math.abs(zv);
  if (bad >= 2.5) return { tag: "well outside reference", level: 3 };
  if (bad >= 2) return { tag: "outside reference", level: 2 };
  if (bad >= 1.5) return { tag: "borderline", level: 1 };
  return { tag: "within reference", level: 0 };
}

export function buildReport({ meas, grades, gradeMetrics, norms, seq }) {
  const thr = gradeMetrics?.tasks ?? {};
  const levels = [];
  meas.discs.forEach((d, i) => {
    if (!LUMBAR.includes(d.name)) return;
    const ref = norms?.levels?.[d.name] ?? {};
    const glob = norms?.global ?? {};
    const zs = {
      dhi: z(d.dhi, ref.dhi || glob.dhi),
      canal_ratio: z(d.canal_ratio, ref.canal_ratio || glob.canal_ratio),
      slip_pct: z(d.slip_pct, ref.slip_pct || glob.slip_pct),
    };
    const measures = [
      { key: "dhi", label: "Disc height (relative to vertebral body height)", value: d.dhi, z: zs.dhi,
        dev: deviation(zs.dhi, true), fmt: (v) => v.toFixed(2) },
      { key: "canal_ratio", label: "Spinal canal depth at the disc (relative to vertebral depth)", value: d.canal_ratio,
        z: zs.canal_ratio, dev: deviation(zs.canal_ratio, true), fmt: (v) => v.toFixed(2) },
      { key: "slip_pct", label: "Forward slip of the vertebra above (% of vertebral depth)", value: d.slip_pct,
        z: zs.slip_pct, dev: deviation(zs.slip_pct, false), fmt: (v) => `${v.toFixed(1)}%` },
    ];
    const findings = [];
    const g = grades?.[i];
    if (g && seq === "T2") {
      for (const t of TASKS) {
        const p = g.binary[t], th = thr[t];
        if (!th || th.auc === null || th.auc < 0.65) continue;   // do not report findings the model cannot separate
        const status = p >= th.t_hi ? "likely" : p <= th.t_lo ? "unlikely" : "uncertain";
        if (status !== "unlikely") findings.push({ task: t, label: TASK_LABELS[t], p, status, auc: th.auc });
      }
    }
    let pfirrmann = null;
    if (g && seq === "T2") {
      const top = g.pfirrmann.indexOf(Math.max(...g.pfirrmann));
      pfirrmann = { grade: top + 1, p: g.pfirrmann[top], expected: g.expected,
        text: top + 1 <= 2 ? "no meaningful degeneration" : top + 1 === 3 ? "moderate degeneration" : "advanced degeneration" };
    }
    const score = findings.filter((f) => f.status === "likely").length * 2 +
      findings.filter((f) => f.status === "uncertain").length + measures.reduce((s, m) => s + m.dev.level, 0) +
      (pfirrmann && pfirrmann.grade >= 4 ? 2 : 0);
    levels.push({ name: d.name, disc: d, findings, measures, pfirrmann, score });
  });

  const vertebrae = meas.vertebrae.filter((v) => v.name !== "?" && v.name !== "S1").map((v) => {
    const ref = norms?.global?.wedge_upper;
    const zv = z(v.wedge, ref);
    const loss = Number.isFinite(v.wedge) ? Math.max(0, 1 - v.wedge) : NaN;
    // Genant semiquantitative bands on anterior height loss: 20-25% mild, 25-40% moderate, >40% severe
    const genant = !Number.isFinite(loss) ? null : loss >= 0.4 ? "severe" : loss >= 0.25 ? "moderate" : loss >= 0.2 ? "mild" : null;
    return { name: v.name, wedge: v.wedge, z: zv, dev: deviation(zv, true), genant };
  });

  const lordRef = norms?.global?.lordosis_deg;
  const lordosis = { value: meas.lordosis_deg, z: z(meas.lordosis_deg, lordRef),
    dev: deviation(z(meas.lordosis_deg, lordRef), false) };

  const notable = levels.filter((l) => l.score >= 2).sort((a, b) => b.score - a.score);
  return { levels, vertebrae, lordosis, notable };
}
