# N Scanning

Research project: AI that reads spine scans, reports what stands out at each level, measures how far the anatomy deviates from a reference, and asks for a better scan when the image is not good enough to read. Phase one is the spine, starting with lumbar MRI; CT and X-ray come next, then other body parts.

> **Research software, not a medical device.** It has not been clinically validated and must not be used for diagnosis or treatment decisions.

**Live prototype:** https://nihalunfc.github.io/n-scanning/ (runs entirely in the browser; images are never uploaded)

## What is here

| Path | What it is |
|---|---|
| `web/` | The GitHub Pages app: ONNX Runtime Web inference, morphometry, quality gate, readout |
| `train/` | Data preparation (SPIDER), training of the browser models, reference ranges, ONNX export |
| `research/nspine/` | Reference implementation of the large NSpine architecture (runnable skeleton) |
| `docs/ARCHITECTURE.md` | The research architecture and how the prototype maps onto it |
| `docs/PAPER.md` | Paper plan: claims, experiments, baselines, metrics |
| `docs/research/` | Literature review (`reference.md`, `references.bib`), dataset catalogue, state-of-the-art synthesis |
| `tests/` | Unit tests, Python/JavaScript measurement parity, ONNX checks |

## How the prototype works

1. **Outline:** a 2M-parameter residual U-Net segments vertebrae, discs and the spinal canal on a sagittal slice. It runs on the image and on its mirror image.
2. **Measure:** disc height index, canal depth, slip and vertebral wedge ratio, all scale-free. The same code exists in `train/measure.py` and `web/js/measure.js`, and a test keeps the two identical.
3. **Compare:** robust z-scores against discs graded radiologically unremarkable in the training patients.
4. **Grade:** a disc-crop CNN predicts the Pfirrmann grade and seven SPIDER findings on T2 images. Each finding is called likely, uncertain or unlikely, using two cut-offs fixed on held-out patients.
5. **Decide:** size, colour, contrast and sharpness checks, plus anatomy found, mirror-run agreement and entropy. The thresholds are calibrated on held-out scans. If any check fails, the app shows no findings and explains what scan to get.

## Training (GitHub Actions, CPU)

Run **Actions → Train models → Run workflow**. The workflow:

1. downloads SPIDER from Zenodo;
2. trains both models on a free 4-core runner, which takes about 4 hours;
3. builds reference ranges and example images;
4. publishes everything to the `models-latest` release and redeploys the site.

The site itself deploys with **Deploy site** on every push to `web/`.

To run it locally:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r train/requirements.txt
cd train
python prepare_spider.py            # downloads SPIDER (several GB)
python train_seg.py --minutes 200 --out out
python train_grade.py --minutes 20 --out out
python build_norms.py --out out
```

Tests: `python -m pytest tests`. Parity: `python tests/parity_dump.py /tmp/p.json && node tests/test_parity.mjs /tmp/p.json`.

## Data and credit

Phase-one models are trained on **SPIDER**: van der Graaf JW et al., *Lumbar spine segmentation in MR images: a dataset and a public benchmark*, Scientific Data 11:264 (2024), doi:10.1038/s41597-024-03090-w. The data is licensed CC BY 4.0. Example images on the site are derived from SPIDER.

## Licence

Code: MIT. Trained weights inherit the terms of their training data (SPIDER: CC BY 4.0).
