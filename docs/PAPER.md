# Paper plan

Target: arXiv (eess.IV, cross-list cs.CV), then a journal or MICCAI-style venue. The paper follows CLAIM 2024 (Tejani 2024) and TRIPOD+AI; metric choices follow Metrics Reloaded (Maier-Hein 2024). References are in `research/reference.md` and `research/references.bib`.

## Paper 1 (phase one, achievable on open data)

**Working title:** *Know when to re-scan: calibrated abstention and normative deviation scores for lumbar spine MRI, running entirely in the browser*

**Claim in one sentence:** A lumbar MRI pipeline that pairs per-level findings with normal-anatomy z-scores and a calibrated "re-scan / inconclusive" decision. It reduces confident errors at a fixed coverage compared with confidence-only baselines, and it runs on-device.

**Contributions**
1. **Abstention split by cause.** A two-way decision that separates re-scan (input quality, wrong view, missing sequence) from inconclusive (model uncertainty). Evaluated with risk–coverage curves (AURC, risk at 80/90/95% coverage). We found no published spine model that does this (gap 2 in `literature_synthesis.md`).
2. **Normative deviation scores for the lumbar spine.** Robust z-scores for disc height index, canal depth, slip and vertebral wedge ratio against radiologically unremarkable levels. We validate that the z-scores separate graded pathology on held-out patients: the AUROC of the DHI z-score for disc narrowing, of the canal z-score for herniation, and of the slip z-score for spondylolisthesis. The browser pipeline already computes these.
3. **An open, reproducible, on-device system.** Training runs on free CI hardware from a public dataset, and inference runs in a web page with no upload. We report the accuracy and calibration change after quantisation.

**Experiments**

| # | Question | Data | Baselines | Metrics |
|---|---|---|---|---|
| E1 | Segmentation quality | SPIDER held-out patients; SPIDER hidden test via grand-challenge | nnU-Net 2D/3D, SPINEPS, TotalSegmentator MRI | Dice, NSD @ 1 mm, HD95 |
| E2 | Per-disc findings | SPIDER gradings | SpineNetV2 (where licence permits), a 2.5D RSNA-style crop model | AUROC, balanced accuracy, linear κ, ±1-grade accuracy (Pfirrmann) |
| E3 | Normative z-scores | SPIDER | raw measurements without normalisation | AUROC vs graded findings; fraction with \|z\|>2 among unremarkable levels (target ≈ 4.6%) |
| E4 | Abstention | SPIDER + synthetic degradations (blur, low-res, motion, wrong plane, wrong sequence) + non-spine images | max-softmax, entropy, MC dropout, deep ensemble, TTA | AURC, selective risk at fixed coverage, re-scan precision/recall per degradation type |
| E5 | Generalisation | RSNA LumbarDISC (8 sites) for canal and stenosis-related measures | same | per-site AUROC, per-site coverage and risk |
| E6 | On-device | browsers on laptop and phone | PyTorch FP32 | latency, model MB, metric deltas after FP16/INT8 |

**Figures**
1. Pipeline overview.
2. Example readouts: a conclusive one, a re-scan case and an inconclusive case.
3. Risk–coverage curves.
4. Z-score distributions for unremarkable vs graded levels.
5. Per-site coverage.

**Known limitations to state:** a single 2D slice; a back-pain cohort as the reference; no age or sex adjustment yet (SPIDER does not release them per scan); level naming assumes L5/S1 at the bottom; findings labels come from one reader in SPIDER.

## Paper 2 (after GPUs): the NSpine architecture

**Working title:** *NSpine: one model for spine CT, MRI and radiographs, with level-grounded reports, normative centiles and risk-controlled abstention*

It extends paper 1 with the full architecture in `ARCHITECTURE.md`. The comparisons are against per-task nnU-Net and the RSNA-winner pipelines, with leave-one-site-out testing and subgroup reporting (Seyyed-Kalantari 2021 showed under-diagnosis bias for "normal" outputs).

## Reproducibility checklist
- Code, configs and training logs are public, and models are published as release assets with a build id shown on the site.
- Patient-level splits are deterministic (`train/splits.py`), and the held-out patients are never used for thresholds or norms.
- The model card on the site shows held-out metrics from the same run that produced the deployed weights.
- Dataset licences are listed per model variant (commercially clean vs non-commercial).

## Timeline
1. **Now:** prototype live; first SPIDER training run; collect E1–E3 numbers.
2. **Next:** E4 degradation suite and baselines; RSNA LumbarDISC for E5 (needs Kaggle rule acceptance).
3. **Then:** write paper 1; start SSL pretraining for NSpine when GPUs are connected.
