# NSpine: research architecture

This is the model we train once large GPUs are connected. The browser prototype in `web/` is a deliberately small, distilled slice of it (one 2D MRI slice, two small CNNs). Citations point to entries in `research/reference.md` by first author and year; DOIs and arXiv ids are there.

## 1. What the system must do

For any spine image (MRI, CT or X-ray), per vertebral level:

1. **Decide if the input is readable** and, if not, say what scan to get (re-scan), separately from "the image is fine but the model is unsure" (inconclusive).
2. **Find and name the anatomy**: vertebrae C1 to S1 (with transitional variants), discs, canal, cord, foramina, facets, endplates.
3. **Report findings** with calibrated probabilities: disc degeneration (Pfirrmann), herniation type (Fardon 2014 nomenclature), canal, subarticular and foraminal stenosis (RSNA 2024 three-level scale), Modic type, endplate defects, spondylolisthesis (Meyerding), vertebral fracture (Genant), alignment (Cobb, lordosis, PI/PT/SS).
4. **Quantify deviation from normal anatomy** as centiles and z-scores adjusted for age, sex, level and scanner.
5. **Write a level-grounded report** in which every sentence traces to a structured output.

## 2. Design choices the literature supports

| Choice | Evidence (see reference.md) |
|---|---|
| CNN U-Net backbone (residual encoder or MedNeXt), not a pure transformer, for dense tasks | nnU-Net Revisited (Isensee 2024): ResEnc-L and MedNeXt beat SwinUNETR and Mamba variants under a fair benchmark |
| Localise the level first, then classify 2.5D/3D crops per level and fuse slices and series with a sequence model | RSNA 2024 lumbar and RSNA 2022 cervical winners (Lee 2024; LumbarDISC write-ups); SpineNetV2 (Windsor 2022) |
| Self-supervised pretraining on all unlabeled volumes before supervised training | nnFoundation (2026, +1.9 Dice over nnU-Net), SuPreM, VoCo |
| Contrast and sequence independence via domain randomisation | TotalSegmentator MRI (sequence-independent), SynthSeg |
| Ensembles plus test-time augmentation for uncertainty; pairwise Dice between members as the failure score | Zenk 2025 failure-detection benchmark; Mehrtash 2020 (entropy predicts Dice, r 0.77 to 0.92) |
| Risk-controlled abstention rather than raw confidence cut-offs | Conformal risk control / Learn-then-Test (Angelopoulos); Kompa 2021 on declining to answer |
| Normative z-scores from morphometry, adjusted for age and sex | Marquand 2016 normative modelling; brain charts (Bethlehem 2022); none exist for the spine |
| Measure first, then write the report from structured outputs | Beyond Fluency (2026): general VLMs are near chance per level; SpineAgent (2026) uses task heads feeding a report agent |

## 3. Architecture

```
            ┌──────────────────────────── input study (one or more series) ───────────────────────────┐
            │  MRI sagittal T1/T2/STIR, axial T2 · CT (any kernel) · X-ray AP/lateral                 │
            └──────────────────────────────────────────────┬──────────────────────────────────────────┘
                                                           ▼
 A. Gate         modality / view / sequence classifier · image-quality head · OOD score ──► RE-SCAN advice
                                                           ▼
 B. Backbone     modality-conditioned ResEnc U-Net (3D for CT/MRI, 2D twin for X-ray), SSL-pretrained
                 dense outputs: vertebra instances + level id, discs, canal, cord, foramina, endplates
                                                           ▼
 C. Level tokens per vertebra/disc: multi-scale feature pooling + curved-planar 2.5D crops in the local
                 spine frame (u = antero-posterior, v = cranio-caudal) from every available series
                                                           ▼
 D. Level transformer   self-attention along the spine (C1…S1) + cross-attention across series/modalities
                 heads: grading · fracture · landmarks → alignment parameters
                                                           ▼
 E. Normative module    morphometrics → GAMLSS / hierarchical Bayesian z-scores (age, sex, level, site)
                        + learned anomaly score (feature-reconstruction autoencoder on level tokens)
                                                           ▼
 F. Abstention          5-fold ensemble × TTA → per-finding risk-controlled thresholds
                        outputs per finding: likely · unlikely · INCONCLUSIVE
                                                           ▼
 G. Report              deterministic level-by-level template; optional LLM paraphrase constrained to facts
                                                           ▼
 H. Distillation        per-modality 2D/2.5D students, FP16/INT8, ONNX Runtime Web + WebGPU
```

### A. Gate (re-scan vs readable)

- A small 2D classifier on three orthogonal thumbnails predicts modality, body region, view/plane and MRI sequence. It rejects images that are out of scope before any finding is produced.
- An image-quality head regresses artefact, noise, blur and coverage scores. Training labels come from synthetic degradation of good scans (motion ghosting, k-space undersampling, noise, low resolution, metal streaks) with known severity, plus MRIQC-style metrics.
- An OOD score uses the Mahalanobis distance in backbone feature space (Gonzalez 2021) and the energy score.
- Output: a re-scan message naming the missing or poor element, for example "add a sagittal T2" (Modic needs T1 and T2, Modic 1988), "slice does not include the canal", or "motion artefact".

### B. Backbone

- **Network:** nnU-Net ResEnc-L (or MedNeXt-L) with a 2D twin for radiographs. The two share the decoder design and the deep-supervision heads.
- **Modality conditioning:** FiLM layers take a learned embedding of (modality, sequence, plane), so one set of weights serves CT and MRI.
- **Pretraining:** masked image modelling on every unlabeled volume we can use (Tier 1 and 2 data, plus TotalSegmentator CT/MRI images). This follows nnFoundation and SuPreM.
- **Supervised training:** multi-dataset training with a partial-label (marginal plus exclusion) loss, because each dataset labels different structures. Pseudo-labels come from SPINEPS and TotalSegmentator where the licences allow it.
- **Level identification:** a vertebra-centroid heatmap plus a 1D level classifier along the detected spine curve (as in Payer's SpatialConfiguration-Net). It has an explicit "transitional" class, trained on VerSe's labelled variants.

### C/D. Level tokens and level transformer

- For each vertebra and disc, crop 2.5D stacks (for example 5 × 96 × 96 in the local spine frame) from every series, and add ROI-pooled backbone features.
- **Token contents:** a level-position embedding (C1…S1), a series/modality embedding and a missing-series mask, so a study with only T2 still works.
- **Model:** 6 to 8 transformer layers, with self-attention along the spine (adjacent-level context matters for slip and alignment) and cross-attention across series.
- **Grading heads:** ordinal (CORAL) for Pfirrmann, stenosis and Genant; multi-label for herniation and Modic.
- **Landmark head:** vertebral corners, from which alignment is computed analytically rather than regressed.

### E. Normative module

- **Morphometry from instances:** vertebral body heights (anterior, middle, posterior), disc height index, canal cross-section, foraminal height, slip, segmental and global lordosis and kyphosis, and spinopelvic parameters.
- **Reference cohort:** levels graded unremarkable, plus healthy-volunteer sets (spine-generic for cervical). Population cohorts such as NAKO and UK Biobank can be added if access is granted.
- **Model:** GAMLSS or hierarchical Bayesian regression with covariates age, sex, level and site. Outputs are centiles and z-scores; the check is that about 4.6% of reference levels have |z| > 2.
- **Learned anomaly score:** an autoencoder trained to reconstruct level tokens of unremarkable levels; its reconstruction error captures shape changes that the hand-made measurements miss.
- **Age context:** degenerative findings are common in people without pain (Brinjikji 2015), so the report always gives age-matched prevalence context.

### F. Abstention

- **Uncertainty sources:** a 5-fold ensemble, and flips and small affine transforms at test time.
- **Per-finding thresholds:** Learn-then-Test conformal risk control on a calibration split from different sites. This bounds the false-finding rate among reported findings and the false-reassurance rate among reported negatives.
- **Inconclusive:** anything between the two thresholds.
- **Two outputs:** aleatoric (input-driven) uncertainty feeds re-scan advice, and epistemic/OOD uncertainty feeds "inconclusive, needs a radiologist".

### G. Report

- A template generator writes one paragraph per level from the structured outputs, with each statement tagged by its source head and probability.
- An optional small LLM may rephrase the text, but it is checked against the structured facts, and a mismatch drops the paraphrase.
- Metrics: per-level clinical-efficacy F1 and level-localisation accuracy. BLEU and BERTScore are secondary only.

### H. Distillation to the browser

- **Students:** a 2D sagittal MRI student (today's prototype), a 2D X-ray student, and a 2.5D CT student working on reformatted mid-sagittal slabs.
- **Deployment:** INT8 or FP16 ONNX, run with ONNX Runtime Web on WebGPU with a WASM fallback.
- **Reporting:** the accuracy, calibration and abstention change after quantisation is reported, not just latency.

## 4. Data plan

| Stage | Data (licence) |
|---|---|
| SSL pretraining | TotalSegmentator CT v3 (CC BY 4.0) and MRI (CC BY-NC-SA), VerSe (CC BY-SA), CTSpine1K (CC BY-NC-SA), SPIDER (CC BY 4.0), NHANES II X-rays; RSNA 2022/2024 images (non-commercial, competition rules) |
| Segmentation and levels | VerSe, CTSpine1K, TotalSegmentator, SPIDER, BUU-LSPINE (X-ray corners) |
| Grading | SPIDER (Pfirrmann, Modic, endplates, herniation, bulging, narrowing, slip), RSNA LumbarDISC (stenosis, 2,697 patients, 8 sites), VerSe'19 (Genant), RSNA 2022 (cervical fracture) |
| Normative | unremarkable levels across the above; spine-generic (healthy, cervical) |
| External test | leave-one-site-out on LumbarDISC; SPIDER hidden test via grand-challenge |

Licensing: non-commercial datasets (CC BY-NC-SA, RSNA rules) restrict any model trained on them to non-commercial use. We keep a "commercially clean" model variant trained on CC BY / CC BY-SA data only, so the choice stays open. Details are in `research/datasets.md`.

## 5. Compute estimate (to be refined)

These are rough planning numbers, not measurements.

- **SSL pretraining:** ResEnc-L on about 10k volumes at 1.5 mm takes on the order of a few days on 8 × H100-class GPUs.
- **Supervised segmentation and level identification:** 5 folds of about 1 day each on 1 to 2 GPUs per fold.
- **Level transformer and heads:** hours per fold on a single GPU, because the level tokens are precomputed.
- **Normative fitting, calibration and distillation:** CPU or single GPU, hours.

## 6. Phase-one prototype vs this design

| Component | Prototype (live now) | NSpine |
|---|---|---|
| Input | one 2D sagittal lumbar MRI slice (PNG/JPEG/DICOM) | full studies, MRI/CT/X-ray |
| Gate | rules plus thresholds calibrated on held-out SPIDER (size, colour, contrast, sharpness, anatomy found, flip-TTA agreement, entropy) | learned IQA, modality and OOD heads |
| Segmentation | 2M-parameter residual 2D U-Net, 4 classes | SSL-pretrained ResEnc-L, about 20 classes plus level ids |
| Findings | 64 × 64 disc crop CNN, 8 SPIDER gradings | level transformer, all gradings, multi-series |
| Normal anatomy | robust z-scores vs unremarkable SPIDER discs, by level | GAMLSS centiles by age, sex, level and site |
| Abstention | two cut-offs per finding fixed on held-out patients (PPV ≥ 0.7, NPV ≥ 0.9) | conformal risk control per site |
