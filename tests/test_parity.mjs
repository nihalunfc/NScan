// node tests/test_parity.mjs <dump.json> : JS morphometry must match Python.
import { readFileSync } from "node:fs";
import { measure, discCrop } from "../web/js/measure.js";
const cases = JSON.parse(readFileSync(process.argv[2], "utf8"));
let worst = 0, fails = 0;
const cmp = (a, b, what) => {
  if (a === null && Number.isNaN(b)) return;
  const d = Math.abs(a - b) / Math.max(1e-6, Math.abs(a));
  worst = Math.max(worst, d);
  if (d > 1e-6) { fails++; console.log("mismatch", what, a, b); }
};
for (const [k, c] of cases.entries()) {
  const m = measure(Uint8Array.from(c.cls), 256);
  if (m.n_discs !== c.m.n_discs || m.n_vertebrae !== c.m.n_vertebrae) { fails++; console.log("count mismatch", k); continue; }
  c.m.discs.forEach((d, i) => {
    for (const f of ["dhi", "slip_pct", "canal_ratio", "length", "thickness"]) cmp(d[f], m.discs[i][f], `${k}:${d.name}:${f}`);
    if (d.name !== m.discs[i].name) { fails++; console.log("name", d.name, m.discs[i].name); }
  });
  c.m.vertebrae.forEach((v, i) => cmp(v.wedge, m.vertebrae[i].wedge, `${k}:${v.name}:wedge`));
  cmp(c.m.lordosis_deg, m.lordosis_deg, `${k}:lordosis`);
  const crop = discCrop(Float32Array.from(c.img), 256, m.discs[1]);
  let cw = 0; c.crop.forEach((x, i) => { cw = Math.max(cw, Math.abs(x - crop[i])); });
  if (cw > 2e-3) { fails++; console.log("crop diff", k, cw); }
}
console.log(fails ? `FAIL (${fails})` : "parity ok", "worst rel diff", worst.toExponential(2));
process.exit(fails ? 1 : 0);
