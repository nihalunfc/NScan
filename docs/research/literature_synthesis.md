# Literature survey: AI for spine / vertebrae analysis (MRI, CT, X-ray)

Compiled 2026-10-16 for the n-scanning project (target: arXiv paper). Scope covers 2021-2026, with an emphasis on 2022-2026.

**How this was verified.** Every entry marked **[V]** was checked this session against its arXiv abstract or HTML, a publisher or PubMed page, the challenge or organiser page, a Hugging Face model card, or the repository's LICENSE file (fetched from raw.githubusercontent.com). Entries marked **[M]** are well-known papers cited from memory. Their bibliographic details are standard but were **not re-fetched**, so check them before final citation. Entries marked **[U]** are only partially verified, and the field in question is flagged inline. Code licenses come from the repository's LICENSE file. A weights license is stated only where a model card says it.

Limits of this session:
- The web-search budget ran out before every item could be checked. The open items are listed at the end of the document.
- The Kaggle writeup pages render without their body text. RSNA 2024 solution details therefore come from secondary summaries, which are cited.

---

## 1. Segmentation and labelling of vertebrae, discs and the spinal canal

| # | Work | Venue / ID | Key result | Code / weights / license |
|---|---|---|---|---|
| 1.1 | **nnU-Net Revisited: A Call for Rigorous Validation in 3D Medical Image Segmentation**. Isensee, Wald, Ulrich, Baumgartner, Roy, Maier-Hein, Jaeger, 2024 **[V]** | MICCAI 2024 (papers.miccai.org lists it as Paper 2847); arXiv:2404.09556 | Under rigorous validation, CNN U-Nets win. MedNeXt-L (k5) is best on BTCV, LiTS, BraTS and AMOS (AMOS DSC 89.73). nnU-Net ResEnc-XL is best on KiTS (88.67) and within 0.05 of the best on AMOS. SwinUNETR, SwinUNETRv2, nnFormer and CoTr trail the CNNs. U-Mamba's gain disappears against a "No-Mamba" ablation. The paper releases the ResEnc M, L and XL presets (about 9, 23 and 37 GB VRAM) and recommends ACDC, AMOS and KiTS as benchmarks, not BTCV or BraTS. | github.com/MIC-DKFZ/nnUNet, **Apache-2.0** |
| 1.2 | **nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation**. Isensee et al., 2021 **[M]** | Nature Methods 18:203-211 | The default strong baseline for 3D segmentation. | Apache-2.0 (same repository) |
| 1.3 | **MedNeXt: Transformer-driven Scaling of ConvNets for Medical Image Segmentation**. Roy, Koehler, Ulrich, Baumgartner, Petersen, Isensee, Jaeger, Maier-Hein, 2023 **[V]** (venue [U]: commonly cited as MICCAI 2023) | arXiv:2303.09975 | A fully ConvNeXt 3D encoder-decoder with UpKern large-kernel initialisation and compound scaling. Reports SOTA on 4 CT and MRI tasks. | github.com/MIC-DKFZ/MedNeXt, **Apache-2.0** |
| 1.4 | **STU-Net: Scalable and Transferable Medical Image Segmentation Models Empowered by Large-Scale Supervised Pre-training**. Huang, Wang, Deng, Ye, Su, Sun, He, Gu, Gu, Zhang, Qiao, 2023 **[V]** | arXiv:2304.06716 | nnU-Net-style models from 14M to 1.4B parameters, pre-trained on TotalSegmentator. Transfers to 14 downstream datasets. In 1.1, TotalSegmentator pre-training improves STU-Net-L on 4 of 6 datasets. | github.com/Ziyan-Huang/STU-Net (moved to uni-medical/STU-Net); license **not found** [U] |
| 1.5 | **Swin UNETR: Swin Transformers for Semantic Segmentation of Brain Tumors in MRI Images**. Hatamizadeh et al., 2022 **[M]** | BrainLes / MICCAI 2021 workshop; arXiv:2201.01266 | A transformer baseline. It trails CNNs in the rigorous benchmark 1.1. | MONAI, Apache-2.0 [M] |
| 1.6 | **TotalSegmentator: robust segmentation of 104 anatomical structures in CT images**. Wasserthal et al., 2023 **[V]** | Radiology: AI, DOI 10.1148/ryai.230024; arXiv:2208.05868 | 1,204 CTs, 104 structures (59 of them bones, including individual vertebrae), Dice 0.943. | github.com/wasserth/TotalSegmentator, code **Apache-2.0**. Some sub-task weights need a separate (non-commercial) license [M, check]. |
| 1.7 | **TotalSegmentator MRI: Robust Sequence-independent Segmentation of Multiple Anatomic Structures in MRI**. Akinci D'Antonoli, ..., Wasserthal, 2025 **[V]** | Radiology, DOI 10.1148/radiol.241613; arXiv:2405.19492 | 80 structures and sequence-independent. Dice 0.839 internal. Beats AMOS and MRSegmentator (0.862 vs 0.759; 0.838 vs 0.560). | Same repository, Apache-2.0 |
| 1.8 | **Lumbar spine segmentation in MR images: a dataset and a public benchmark (SPIDER)**. van der Graaf, van Hooff, Buckens, Rutten, van Susante, Kroeze, de Kleuver, van Ginneken, Lessmann, 2024 **[V]** | Scientific Data, DOI 10.1038/s41597-024-03090-w; arXiv:2306.12217 | 447 sagittal T1/T2 series from 218 low-back-pain patients at 4 hospitals. Labels cover vertebrae, IVDs and the spinal canal. The hidden test set has 97 series. The authors' baseline matches nnU-Net. The challenge at spider.grand-challenge.org runs continuously (ranked by mean relative rank). It was reused as UNICORN Task 11 (mean Dice). | Data on Zenodo 10159224. A baseline nnU-Net algorithm runs on Grand Challenge. |
| 1.9 | **SPINEPS: Automatic whole spine segmentation of T2-weighted MR images using a two-phase approach to multi-class semantic and instance segmentation**. Möller, Graf, ..., Rueckert, Kirschke, 2024/25 **[V]** | European Radiology, DOI 10.1007/s00330-024-11155-y; arXiv:2402.16368 | 14 classes, including 10 vertebral substructures, IVD, cord, canal and sacrum. On SPIDER, instance vertebra Dice is 0.929 vs 0.907 for the baseline. On NAKO, Dice is vertebrae 0.920, IVD 0.967 and canal 0.958. | github.com/Hendrik-code/spineps, **Apache-2.0**; installs from PyPI as `spineps` |
| 1.10 | **VerSe: A Vertebrae labelling and segmentation benchmark for multi-detector CT images**. Sekuboyina et al. (VerSe'19/'20), 2021 **[V]** for '19 numbers, [M] for venue | Medical Image Analysis 2021 [M: DOI 10.1016/j.media.2021.102166]; arXiv:2001.09193 | 160 CTs in VerSe'19 (374 across '19 and '20 [M]). The best algorithm reached a 95% identification rate and 90% Dice. The winners were the Payer et al. / Graz coarse-to-fine heatmap-localisation-then-segmentation pipeline [M]. | Data: github.com/anjany/verse [M] |
| 1.11 | **SAM-Med3D**. Wang et al., 2023/24 **[V]** | arXiv:2310.15161 | A promptable 3D SAM trained on SA-Med3D-140K (22K volumes, 143K masks). Works from a few 3D point prompts. | github.com/uni-medical/SAM-Med3D, **Apache-2.0** |
| 1.12 | **MedSAM2: Segment Anything in 3D Medical Images and Videos**. Ma, Yang, Kim, Chen, Baharoon, Fallahpour, Asakereh, Lyu, Wang, 2025 **[V]** | arXiv:2504.03600 | Fine-tuned from SAM2 on more than 455K 3D image-mask pairs and 76K video frames. Cuts annotation cost by more than 85% in human-in-the-loop use. | github.com/bowang-lab/MedSAM2, **Apache-2.0** (SAM2 itself is Apache-2.0) |

**Takeaway.** For segmentation, use nnU-Net ResEnc-L or MedNeXt as the backbone and baseline. Do not claim gains from transformers or Mamba without the rigorous protocol of 1.1. Instance labelling of vertebrae comes from SPINEPS and TotalSegmentator, with VerSe for CT and SPIDER for MRI. Promptable models are best positioned as annotation tools, not as the main segmenter.

---

## 2. Degenerative grading from MRI

| # | Work | Venue / ID | Key result | Code / license |
|---|---|---|---|---|
| 2.1 | **RSNA 2024 Lumbar Spine Degenerative Classification AI Challenge** (Kaggle) **[V]** | rsna.org news, Nov 2024 | 1,874 teams (an RSNA record). The task is to grade spinal canal, subarticular and foraminal stenosis (normal/mild, moderate, severe) at L1-L2 to L5-S1. Winners: 1 Avengers, 2 IanPan-Kevin-Yuji-Bartley, 3 SonySpine s & tkmn & Moyashii. The metric is a sample-weighted log loss with severe up-weighted, plus an "any severe" term [M, standard Kaggle definition]. | Winning code is on Kaggle |
| 2.2 | **Architectures of the top RSNA 2024 solutions** **[U]** (secondary sources: zenn.dev/mkj summary; appendix of arXiv:2512.12887) | none | **1st:** localise, then classify. A 3D ConvNeXt picks the slice and a 2D ConvNeXt regresses disc coordinates. Multi-view 2.5D crops then pass through a ConvNeXt-S or EfficientNetV2-S encoder, a BiLSTM and attention-MIL across slices and views. **2nd:** an ensemble of three pipelines: YOLOX disc detection with a ConvNeXt classifier; slice-identification CNN-transformer, keypoints and 2D CNN classifiers with attention or MIL (MaxViT, CoAtNet, NFNet, CSN-R101); and a sagittal-only encoder with LSTM and attention pooling, pseudo-labels and 9x TTA. Severe-class logits were scaled by 1.25. **3rd:** a CenterNet-style detector (EffNet-B6/B4 with FPN), then a 2D encoder with attention, plus label fixing and pseudo-labels. | Kaggle writeups (body not machine-readable this session) |
| 2.3 | **The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset**. Richards, Flanders, Colak, Prevedello, Ball, Kitamura, Mongan, ..., Talbott, 2026 **[V]** | Radiology: AI 8(2), DOI 10.1148/ryai.250480; arXiv:2506.09162 | 2,697 patients and 8,593 series from 8 sites in 6 countries. Sequences are Sag T1, Sag T2 and Ax T2. 1.5T 63.6% and 3T 34.1%. The 4-point scale was collapsed to 3 points. Canal grades are 85.4% normal/mild, 8.8% moderate and 5.9% severe. | Free for non-commercial use (Kaggle, RSNA MIRA) |
| 2.4 | **SpineNetV2: Automated Detection, Labelling and Radiological Grading of Clinical MR Scans**. Windsor, Jamaludin, Kadir, Zisserman, 2022 **[V]** | arXiv:2205.01683 (tech report) | Grades Pfirrmann, narrowing, canal stenosis (4 classes), endplate defects, marrow (Modic-like) changes, foraminal stenosis, spondylolisthesis and herniation. Balanced accuracy is about 71% for Pfirrmann. Vertebra identification rate is 96.5-98.4%. Runs in about 3 s on GPU and 25 s on CPU. | No weights in the paper (demo on request). An open-source release is reported in the 2.5 validation [U]. |
| 2.5 | **External Validation of SpineNet ... Using the Northern Finland Birth Cohort 1966**. 2023 **[U]**: details could not be fetched (PMC captcha) | PMC9990601 | External validation of SpineNet for Pfirrmann and Modic grading. | none |
| 2.6 | **Deep Learning Model for Automated Detection and Classification of Central Canal, Lateral Recess, and Neural Foraminal Stenosis at Lumbar Spine MRI**. Hallinan et al., 2021 **[V]** (first author [M]) | Radiology 300(1):130-138, DOI 10.1148/radiol.2021204289 | 446 studies plus 100 external. Dichotomous Gwet κ: canal 0.96, recess 0.92, foramina 0.89, comparable to subspecialists. External κ 0.95-0.96. | none |
| 2.7 | **Lumbar spine MRI annotation with intervertebral disc height and Pfirrmann grade predictions**. Natalia, Sudirman, Ruslim, Al Kafri, 2024 **[V]** | PLoS ONE, DOI 10.1371/journal.pone.0302067 | Pfirrmann and disc height on the 515-patient Mendeley lumbar MRI dataset. | Data: data.mendeley.com/datasets/k57fr854j2; radiologist notes at s6bgczr8s2 |
| 2.8 | **Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification (AnyMC3D)**. Liu, Georgescu, ..., Grbic (Siemens Healthineers), 2025 **[V]** | arXiv:2512.12887 | A frozen 2D foundation model with LoRA and query-based slice-attention pooling beats 3D architectures on 3D classification. This supports the 2.5D designs of the RSNA winners. | No code released |

**Takeaway.** Every top RSNA solution follows the same pattern. First localise the level (by slice index and keypoint, or by a detector). Then extract per-level, per-view 2.5D crops, encode them with a 2D ImageNet-pretrained CNN (ConvNeXt or EfficientNetV2), fuse across slices and views with a BiLSTM or attention-MIL, ensemble, and recalibrate the severe class. This is the baseline to beat on LumbarDISC.

---

## 3. Fracture detection and grading

| # | Work | Venue / ID | Key result | Code |
|---|---|---|---|---|
| 3.1 | **Performance of the Winning Algorithms of the RSNA 2022 Cervical Spine Fracture Detection Challenge**. Lee, Flanders, Richards, Kitamura, Colak, Lin, Ball, Talbott, Prevedello, 2024 **[V]** | Radiology: AI 6(1):e230256 | 3,112 CTs from 12 sites, with a test set of 1,093 scans and 847 fractures. The top 3 used segmentation, then a 2D CNN, then an RNN. First place scored a weighted log loss of 0.2047. Top-8 patient-level means: AUC 0.96, sensitivity 88%, specificity 94%. Performance was weakest at C4. | Kaggle |
| 3.2 | **RSNA 2022 1st place architecture** **[U]**, summarised in the appendix of arXiv:2512.12887 | none | 2.5D CNN-RNN at vertebra level. EffNetV2-S or ConvNeXt slice encoder with an LSTM across slices. Vertebrae are located by segmentation first. | Kaggle |
| 3.3 | **Semantic Latent Space Regression of Diffusion Autoencoders for Vertebral Fracture Grading**. Keicher, Atad, ..., Kirschke, Navab, 2023 **[V]** (venue [U]) | arXiv:2303.12031 | Genant grading by distance to a hyperplane in diffusion-autoencoder latent space, plus counterfactual visualisation. Detection AUC 0.96 vs 0.98 for supervised DenseNet. Grading macro-F1 0.56 vs 0.65, so it lags supervised methods. | none |
| 3.4 | **Faint Features Tell: Automatic Vertebrae Fracture Screening Assisted by Contrastive Learning**. Wei, Cong, Zhang, Peng, Chen, Li, 2022 **[V]** (venue [U]) | arXiv:2208.10698 | SupCon on Genant grades. On VerSe, AUC 0.93 and macro-F1 0.72 over all grades. Without G1, AUC 0.99. Grade 1 (mild) remains the hard case. | none |
| 3.5 | **VerSe** (see 1.10). Genant fracture grades are included for some vertebrae [M]. | none | The standard public CT source for fracture grading. | none |

**Takeaway.** Detection is close to saturated on curated CT (AUC about 0.96). The open problems are Genant grade 1, mild deformities, and doing this from radiographs and MRI. A further open problem is reporting **vertebral height-loss ratios** (a quantitative Genant measure) that come from segmentation and not from a classifier.

---

## 4. X-ray: landmarks, Cobb angle, spondylolisthesis, VinDr-SpineXR

| # | Work | Venue / ID | Key result | Code |
|---|---|---|---|---|
| 4.1 | **Evaluation and comparison of accurate automated spinal curvature estimation algorithms with spinal anterior-posterior X-Ray images: The AASCE2019 challenge**. Wang, Xie, ..., Shuo Li, 2021 **[V]** | Medical Image Analysis 72:102115, DOI 10.1016/j.media.2021.102115 | Covers 8 of 12 teams. The best SMAPE was 21.71% on the challenge test set. | Data: AASCE (SpineWeb) |
| 4.2 | **CurvNet: Latent Contour Representation and Iterative Data Engine for Curvature Angle Estimation**. Shao, Yuan, Ma, Zhu, 2024 **[V]** (venue [U], Elsevier-format) | arXiv:2411.12604 | SMAPE 5.05% on AASCE2019 (prior best in their table is 7.91%). Releases Spinal-AI2024 (20K synthetic images). | github.com/Ernestchenchen/CurvNet, **Apache-2.0** (MMOCR-derived) |
| 4.3 | **A Landmark-aware Network for Automated Cobb Angle Estimation Using X-ray Images (LaNet)**. Yang, Wang, Meng, 2024 **[V]** | arXiv:2405.19645 | SMAPE on AASCE is 4.51% on validation and 8.99% on test. Note that splits differ between papers, so SMAPE values are not directly comparable. | none |
| 4.4 | **VinDr-SpineXR: A deep learning framework for spinal lesions detection and classification from radiographs**. Nguyen, Pham, Nguyen, Nguyen, Huynh, Dao, Vu, 2021 **[V]** (venue [U]: commonly cited as MICCAI 2021) | arXiv:2106.12930 | 10,468 images from 5,000 studies; test set 2,078 images from 1,000 studies. 13 classes, 7 of them localised. Image-level AUROC 88.61%; lesion mAP@0.5 33.56%. | PhysioNet (credentialed access) |
| 4.5 | **Deep learning system assisted detection and localization of lumbar spondylolisthesis**. Zhang, Lin, Wang, et al., 2023 **[V]** | Frontiers in Bioeng. Biotech., DOI 10.3389/fbioe.2023.1194009 | 1,596 lateral radiographs from 3 hospitals. Faster R-CNN AP 0.966 and F1 0.935, beating surgeons on sensitivity. Uses boxes, not keypoints, so slip percentage and Meyerding grade are not computed. | Data not public |
| 4.6 | **SpineFM: Leveraging Foundation Models for Automatic Spine X-ray Segmentation**. Simons et al., 2024 **[V]** (author list [U]) | ISBI 2025; arXiv:2411.00326 | Sequential vertebra inference with Medical-SAM-Adapter on two public cervical and lumbar X-ray sets. Identifies 97.8% and 99.6% of vertebrae, with Dice 0.942 and 0.921. | none |
| 4.7 | **BUU-LSPINE** (lumbar AP/LA X-ray corner landmarks, Thailand) **[U]**: not verified this session (search budget exhausted) | none | A candidate public dataset for spondylolisthesis keypoints. | none |

**Takeaway.** The SOTA formulation is to segment or keypoint each vertebra and then compute the angle from geometry. CurvNet and LaNet are the baselines on AASCE (SMAPE). For spondylolisthesis, a geometric slip percentage from vertebral-corner keypoints is more interpretable than box detection, and no public keypoint-based Meyerding baseline was found.

---

## 5. Foundation models usable as backbones (2025-2026)

| # | Model | Paper / ID | Modalities and architecture | Weights and license |
|---|---|---|---|---|
| 5.1 | **MedImageInsight**. Codella et al. (Microsoft), 2024 **[V]** | arXiv:2410.06542 | X-ray, CT, MRI, ultrasound, derm, OCT, fundus, path and mammography. An image-text embedding model. SOTA on CT 3D retrieval and on CXR, derm and OCT classification. | Official release is through Azure. A third-party mirror (lion-ai/MedImageInsights) is tagged MIT; the official terms are **unverified [U]**. |
| 5.2 | **BiomedCLIP**. Zhang et al. (Microsoft), 2023 **[V]** | arXiv:2303.00915 (NEJM AI 2025 [M]) | PubMedBERT plus ViT-B/16, trained on PMC-15M figure-caption pairs. | **MIT**, but the model card says "deployed use ... commercial or otherwise is out of scope". |
| 5.3 | **RAD-DINO**. Pérez-García et al. (Microsoft), 2025 **[V]** | Nature Machine Intelligence, DOI 10.1038/s42256-024-00965-w; arXiv:2401.10815 | A DINOv2 ViT-B (86.6M parameters) trained on 882K **chest** X-rays. | **MIT** (HF model card) |
| 5.4 | **CT-FM: Vision Foundation Models for Computed Tomography**. Pai, Hadzic, Bontempi, Bressem, Kann, Fedorov, Mak, Aerts, 2025 **[V]** | arXiv:2501.09001 | 3D SegResEncoder (77M), contrastive pre-training on 148K CTs from IDC. Covers whole-body and tumour segmentation, triage and retrieval. | github.com/project-lighter/CT-FM **MIT** (code); weights on HF project-lighter ("permissive"; exact license [U]) |
| 5.5 | **Merlin: A Vision Language Foundation Model for 3D CT**. Blankemeier, ..., Chaudhari, 2024/2026 **[V]** | Nature 2026, DOI 10.1038/s41586-026-10181-8; arXiv:2406.06512 | 3D CT with EHR codes and reports. Trained on 15,331 CTs and externally tested on 44K. | github.com/StanfordMIMI/Merlin **MIT** (code); HF stanfordmimi/Merlin (weights license [U]) |
| 5.6 | **MRI-CORE: A Foundation Model for MRI**. Dong, Chen, Gu, Konz, Chen, Li, Mazurowski, 2025 **[V]** | arXiv:2506.12186 | A ViT-B initialised from SAM and trained with DINOv2 on 116,806 MRI volumes (6M slices, 18 body regions; brain, face and neck excluded). Beats SAM and nnU-Net in few-shot segmentation. Spine in pretraining is not explicit. | github.com/mazurowski-lab/mri_foundation, **Apache-2.0** (README) |
| 5.7 | **Curia: A Multi-Modal Foundation Model for Radiology**. Dancette, Khlaut, ..., Hérent (Raidium), 2025 **[V]** | arXiv:2509.06830 | A DINOv2-tagged ViT-B (86M) trained on 150K CT and MRI exams (130 TB). Validated on 19 external tasks. | HF raidium/curia: **Research-only RAIL-M, gated**. Not usable commercially. |
| 5.8 | **MedSigLIP / MedGemma**. Google, 2025 **[V]** | arXiv:2507.05201 | SigLIP-400M image and text towers, 448 px, trained on CXR, derm, ophthalmology, pathology and CT/MRI slices. MedGemma 4B and 27B are the VLMs. | **Health AI Developer Foundations terms**, gated |
| 5.9 | **MedDINOv3**. Li, Wu, Lai, Hu, Yang, 2025 **[V]** | arXiv:2509.02379 | DINOv3 ViT-B with continued pretraining on CT-3M (3.87M axial slices). With multi-scale token aggregation it beats nnU-Net on AMOS (+2.6 DSC) and BTCV (+5.5) and is on par for tumours. | github.com/ricklisz/MedDINOv3 **Apache-2.0** (code). Base DINOv3 weights fall under the **DINOv3 License** (custom, not OSI) **[V]** |
| 5.10 | **SAM2 / SAM-based**: MedSAM2 (1.12), SAM-Med3D (1.11), Efficient MedSAMs (9.3) | none | Promptable segmentation | SAM2 **Apache-2.0** |
| 5.11 | **XR-0: Multi Anatomy X-Ray Foundation Model**. Singla et al., 2025 **[V]** | arXiv:2509.12146 | SSL on 1.15M private multi-anatomy X-rays across 20 tasks. | No weights mentioned |
| 5.12 | **STU-Net / TotalSegmentator-pretrained nnU-Nets** (1.4) | none | Supervised 3D pretraining | See 1.4 |

**Takeaway.**
- For a **commercially clean** stack, use SAM2, MedSAM2, MRI-CORE, nnU-Net, MedNeXt, SPINEPS or MedDINOv3 code (all Apache-2.0), or RAD-DINO and CT-FM code (MIT).
- Avoid or isolate the restricted models: Curia (RAIL-M research-only), MedSigLIP/MedGemma (HAI-DEF terms), the DINOv3 weights (custom license) and BiomedCLIP (out-of-scope for deployment).
- No released foundation model covers **spine across CT, MRI and X-ray** with one encoder.

---

## 6. Normative modelling and anomaly detection ("deviation from normal anatomy")

| # | Work | Venue / ID | Key result | Code |
|---|---|---|---|---|
| 6.1 | **Brain charts for the human lifespan**. Bethlehem et al., 2022 **[M]** | Nature 604:525-533 | Centile and z-score normative charts from more than 100K scans using GAMLSS. This is the methodological template for spine normative scores. | brainchart.io [M] |
| 6.2 | **Normative modelling in neuroimaging** (tutorial/review), 2025 **[U]** (authors not fetched) | arXiv:2509.07237 | Reviews normative modelling (HBR, GAMLSS, PCNtoolkit) and deviation z-scores. | PCNtoolkit [M] |
| 6.3 | **VIBESegmentator: Full body MRI segmentation for the NAKO and UK Biobank**. Graf, Platzek, ..., Kirschke, 2025 **[V]** | European Radiology, DOI 10.1007/s00330-025-12035-9; arXiv:2406.00125 | 71 classes, including vertebral bodies, posterior elements, IVDs, cord and canal, on NAKO and UKBB VIBE. This makes **population-scale spine morphometry** possible. | github.com/robert-graf/TotalVibeSegmentator **Apache-2.0** |
| 6.4 | **Detecting Unforeseen Data Properties with Diffusion Autoencoder Embeddings using Spine MRI data**. Graf, Hunecke, ..., Kirschke, 2024 **[V]** | MICCAI 2024 iMIMIC workshop; arXiv:2410.10220 | Diffusion-autoencoder embeddings of 11,186 NAKO spine T2 scans expose site, positioning (+43 mm shift) and sex-label outliers. Directly relevant to OOD and quality checks. | none |
| 6.5 | **MedIAnomaly: A comparative study of anomaly detection in medical images**. Cai, Zhang, Chen, Cheng, 2025 **[V]** | Medical Image Analysis 2025; arXiv:2404.04518 | Benchmarks 30 methods. No paradigm wins everywhere. Feature reconstruction (FAE, ReContrast) is best for image-level detection. A denoising-AE U-Net is best for pixel-level detection. ImageNet features help. | github (MedIAnomaly) [U] |
| 6.6 | **AI-based CT assessment of 3117 vertebrae reveals significant sex-specific vertebral height differences**. 2025 **[U]** (fetch failed; title from search result) | Scientific Reports 2025, s41598-025-05091-0 | AI-derived vertebral-height reference data, a starting point for normative vertebral z-scores. | none |
| 6.7 | Statistical shape models of the spine, e.g. *A Statistical Model of Spine Shape and Material for Population-Oriented Biomechanical Simulation* (IEEE, 2021) **[U]** (details not fetched) | IEEE Xplore 9618930 | Shows that population spine SSMs exist. None found for automatic clinical deviation scoring. | none |

**Takeaway.** Normative z-scores (GAMLSS or hierarchical Bayesian, conditioned on age, sex and height) are mature in neuroimaging but **essentially absent for the spine**. Segmentation tools that make population-scale spine morphometry feasible exist (SPINEPS and VIBESegmentator on NAKO, TotalSegmentator on CT). For spine, generative anomaly detection has only been used for fracture grading (3.3) and for data-bias discovery (6.4).

---

## 7. Image quality, uncertainty and selective prediction ("inconclusive, re-scan")

| # | Work | Venue / ID | Key result | Code |
|---|---|---|---|---|
| 7.1 | **Understanding Silent Failures in Medical Image Classification**. Bungert, Kobelke, Jaeger, 2023 **[V]** | MICCAI 2023; arXiv:2307.14729 | Across 4 biomedical tasks under distribution shift, **no** confidence-scoring function reliably prevents silent failures. Introduces SF-Visuals. | github.com/IML-DKFZ/sf-visuals |
| 7.2 | **ValUES: A Framework for Systematic Validation of Uncertainty Estimation in Semantic Segmentation**. Kahl, Lüth, Zenk, Maier-Hein, Jaeger, 2024 **[V]** | ICLR 2024 (oral); arXiv:2401.08501 | Ensembles are the most robust. TTA is a cheap alternative. Separating aleatoric from epistemic uncertainty does not transfer to real data. **Aggregating** pixel uncertainty to an image score is a neglected but crucial step. | github.com/IML-DKFZ/values **Apache-2.0** |
| 7.3 | **Pitfalls of Conformal Predictions for Medical Image Classification**. Mehrtens, Bucher, Brinker, 2025 **[V]** | arXiv:2506.18162 | Coverage is only marginal, so subgroups and rare classes are under-covered. Coverage breaks under shift. Taking singleton sets is **not** valid selective classification. Prediction sets carry little information for 2-3 classes, which matters for 3-class stenosis grading. | none |
| 7.4 | **Learn then Test: Calibrating Predictive Algorithms to Achieve Risk Control**. Angelopoulos, Bates, Candès, Jordan, Lei, 2021 **[V]** | arXiv:2110.01052 | Finite-sample risk control for any model through multiple testing. The correct tool for an **abstention threshold with a guaranteed error rate** on accepted cases. | none |
| 7.5 | **A Gentle Introduction to Conformal Prediction and Distribution-Free UQ**. Angelopoulos & Bates **[V: exists]** | arXiv:2107.07511 | Standard reference | none |
| 7.6 | **Low-dose CT perceptual image quality assessment (LDCTIQAC 2023)**. Lee, Wagner, ..., Choi, 2025 **[V]** | Medical Image Analysis 99:103343, DOI 10.1016/j.media.2024.103343 | 1,000 CT images with radiologist quality scores. No-reference IQA can beat PSNR and SSIM at matching radiologists. | Data on Zenodo |
| 7.7 | **A Deep Learning-Based Approach to Reduce Rescan and Recall Rates in Clinical MRI Examinations** (AJNR) **[U]** (authors and year not fetched) | AJNR | Gives a brain-MRI series a usability probability with indication-specific thresholds. Rescan rates vs technologists depend on indication (MS higher, stroke lower). | none |
| 7.8 | Classic UQ baselines: MC dropout (Gal & Ghahramani, ICML 2016) **[M]**, deep ensembles (Lakshminarayanan et al., NeurIPS 2017) **[M]**, MRIQC (Esteban et al., PLoS ONE 2017) **[M]** | none | none | none |

**Takeaway.** The defensible recipe has five parts:
- **Ensembles and TTA** for uncertainty.
- An explicit **aggregation** step from pixels to levels to the study.
- **Separate** gates: input quality or OOD ("re-scan") versus model uncertainty ("inconclusive, refer to a human").
- Abstention thresholds calibrated with **Learn-then-Test or conformal risk control**, reported per site, not marginally.
- Evaluation with risk-coverage curves and AURC, as in the DKFZ failure-detection line of work.

No spine-specific IQA or "re-scan" model was found.

---

## 8. Report generation and vision-language for spine

| # | Work | Venue / ID | Key result | Code / data |
|---|---|---|---|---|
| 8.1 | **SpineBench: A Clinically Salient, Level-Aware Benchmark Powered by the SpineMed-450k Corpus**. Zhao, Dong, Zhang, ..., Shan, 2025/26 **[V]** | ICLR 2026; arXiv:2510.03160 | 450K instruction instances (X-ray, CT and MRI) covering level identification, pathology and surgical planning. General LVLMs are weak at level-specific reasoning, and fine-tuning helps. | Availability [U] |
| 8.2 | **SpineBench: Benchmarking Multimodal LLMs for Spinal Pathology Analysis**. Zhang, Li, Li, Cui, Xia, Yan, Zhang, Zhuang, 2025 **[V]** (a *different* paper with the same name) | arXiv:2510.12267 | 64,878 multiple-choice QA pairs over 40,263 images and 11 diseases. All 12 MLLMs tested perform poorly. | none |
| 8.3 | **Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine MRI Report Generation**. Palau, Vogt, Laslo, Li, Konukoglu, Monzon, Jutzeler (ETH), 2026 **[V]** | arXiv:2608.07117 | Uses LSMRI (515 patients with reports), SPIDER (template reports) and LumbarDISC. MedGemma-27B is best zero-shot, but **per-level detection is near chance** (balanced accuracy 50-57%). BLEU and BERTScore penalise paraphrase more than negation errors. Anomaly heatmaps are used to guide generation. | Code [U] |
| 8.4 | **GateSPINE: Gated Cross-View Fusion for Lumbar Spine MRI Report Generation**. Nguyen Van et al., 2026 **[V]** | arXiv:2609.40091 | Sag T1+T2 fusion with gated sagittal/axial cross-view fusion. Highest clinical-efficacy F1 on 3 datasets. | none |
| 8.5 | **Auto-Rad: End-to-End Report Generation from Lumbar Spine MRI Using Vision-Language Model**. Yeasin, Moinuddin, Havugimana, Wang, Park, 2024 **[V]** | J. Clin. Med. 13(23):7092 | GIT-base on 515-patient axial composites. METEOR 0.37, but diagnostic completeness is only 24.7%. | none |
| 8.6 | **Lumbar Spine MRI Dataset with radiologist notes** (Sudirman et al., Mendeley) **[V: exists]** | data.mendeley.com k57fr854j2 / s6bgczr8s2 | The only public spine MRI dataset with free-text reports (515 patients). | Mendeley license [U] |

**Takeaway.** End-to-end spine report generation fails on clinical correctness, especially level-specific findings. The credible design is **structured findings first**: per-level grades and measurements from task heads, then a templated or LLM verbaliser. Evaluate it with clinical-efficacy F1 per level, not with BLEU.

---

## 9. Browser and edge deployment

| # | Work | Venue / ID | Key result | Code / license |
|---|---|---|---|---|
| 9.1 | **ONNX Runtime Web with WebGPU** (ORT 1.17), Microsoft, Feb 2024 **[V]** | opensource.microsoft.com blog, 2024-02-29 | WebGPU vs WASM speedup: SAM encoder about 19x, decoder about 3.8x (RTX 3060 laptop). | onnxruntime, MIT [M] |
| 9.2 | **Transformers.js v3: WebGPU support**, Hugging Face, Oct 22, 2024 **[V]** | HF blog | WebGPU backend ("up to 100x faster than WASM", no benchmarks given). `dtype` options fp32, fp16, q8 and q4. | Apache-2.0 [M] |
| 9.3 | **Efficient MedSAMs: Segment Anything in Medical Images on Laptop** (CVPR 2024 challenge). Ma, Li, Kim, ..., Wang, 2024 **[V]** | arXiv:2412.16085 | CPU-only. The winner MedficientSAM (EfficientViT-L1 distilled from MedSAM, OpenVINO, embedding caching) takes about 1-2 s per 2D image. 3D takes 10-70 s or more per case. | github.com/bowang-lab/MedSAM (LiteMedSAM branch); codabench 1847 |
| 9.4 | **Efficient Quantization-Aware Training on SAM in Medical Images and Its Deployment**. Lu, Fu, Zhang, Zhang, 2024 **[V]** | arXiv:2412.11186 | INT8 QAT exported to ONNX (QCDQ) for OpenVINO. Multi-box runtime falls from 14.7 s to 4.2 s with a DSC change of -0.36. | none |
| 9.5 | **Brainchop: Next Generation Web-Based Neuroimaging Application**. Masoud, Reddy, Hu, Plis, 2023 **[V]** | arXiv:2310.16162 (prior JOSS 2023) | In-browser 3D brain MRI segmentation (TF.js with WebGL, MeshNet), about 8-40 s per volume. MeshNet is far smaller than a U-Net (0.89 MB vs 288 MB). The closest prior work to a browser spine tool. | github.com/neuroneural/brainchop **MIT** |
| 9.6 | **Characterizing browser-based medical imaging AI with serverless edge computing: towards addressing clinical data security constraints** **[U]** (title only; page fetch failed, probably SPIE 2023) | ResearchGate 369938707 | Prior work on browser medical AI for data security. | none |

**Takeaway.** In-browser 3D segmentation is shown for **brain only** (Brainchop, with WebGL and TF.js). No published work runs spine MRI, CT or X-ray models in the browser with **ORT-Web or WebGPU**. Nor does any report quantised accuracy deltas together with calibrated abstention on-device.

---

## 10. Baselines and metrics per task

| Task | Public dataset(s) | Strongest baselines to compare against | Primary metrics |
|---|---|---|---|
| Vertebra/IVD/canal segmentation (MRI) | SPIDER (Zenodo 10159224); NAKO (restricted) | nnU-Net ResEnc-L, MedNeXt-L, SPINEPS, TotalSegmentator MRI; STU-Net-L (pretrained) | Dice, NSD at 1-2 mm, HD95; SPIDER mean-relative-rank |
| Vertebra labelling and segmentation (CT) | VerSe'19/'20; TotalSegmentator CT data | TotalSegmentator, nnU-Net ResEnc, VerSe winners (Payer et al. [M]) | Identification rate (≤20 mm [M]), localisation error (mm), Dice, HD |
| Promptable / few-shot segmentation | SPIDER, VerSe | MedSAM2, SAM-Med3D, MRI-CORE few-shot | Dice vs number of prompts or shots; annotation time |
| Lumbar stenosis grading (MRI) | RSNA LumbarDISC | RSNA 2024 1st/2nd/3rd place pipelines; SpineNetV2 (canal) | Competition weighted log loss (severe up-weighted with an any-severe term [M]); per-condition AUROC; quadratic-weighted κ vs readers; ECE |
| Pfirrmann / Modic / disc grading | Mendeley 515 (Pfirrmann labels from 2.7); Genodisc (restricted) | SpineNet(V2) | Balanced accuracy, linear/quadratic κ, ±1-grade accuracy |
| Cervical fracture (CT) | RSNA 2022 CSFD | RSNA 2022 winners (2.5D CNN-RNN) | Weighted log loss (patient and vertebra), AUC, sensitivity, specificity |
| Osteoporotic fracture Genant grading | VerSe (Genant subset) | SupCon (3.4), DAE regression (3.3), 3D SE-ResNet50 [U] | AUC (G0 vs G1+ and G0 vs G2+), macro-F1 over grades, κ; height-loss % MAE |
| Cobb angle (AP X-ray) | AASCE2019 (609 images); Spinal-AI2024 | CurvNet (SMAPE 5.05%), LaNet (8.99% test) | SMAPE, MAE (degrees), circular MAE; landmark MRE (px or mm) |
| Spinal lesion detection (X-ray) | VinDr-SpineXR | VinDr baseline (AUROC 88.61, mAP@0.5 33.56) | Image AUROC, mAP@0.5, FROC |
| Spondylolisthesis (lateral X-ray) | BUU-LSPINE [U]; private | Faster R-CNN (4.5) | Slip-% MAE, Meyerding κ, AP |
| Uncertainty / abstention | Any of the above under site shift | Deep ensembles, TTA, MC dropout, MSP/energy OOD, conformal (LAC/APS/RAPS), Learn-then-Test | AURC, risk at fixed coverage, selective accuracy, ECE, coverage per site and subgroup, OOD AUROC |
| Image quality / re-scan | LDCTIQAC (CT); MRIQC-style | MRIQC [M], LDCTIQAC top methods | SRCC/PLCC vs radiologist score; rescan precision and recall |
| Normative deviation | NAKO / UKBB (restricted); VerSe and SPIDER for pathology | GAMLSS / HBR z-scores; SSM Mahalanobis; DAE / FAE anomaly | AUROC of z-score for pathology; z-score calibration (fraction with \|z\|>2 in healthy ≈ 4.6%) |
| Report generation | LSMRI (Mendeley 515), SPIDER templates, SpineMed-450k | MedGemma-4B/27B, MAIRA-2, VILA-M3, GateSPINE | Clinical-efficacy F1 per level, level-localisation accuracy, RadGraph-F1 [M]; BLEU/BERTScore only as secondary |
| Browser / edge | none | Brainchop; MedficientSAM / LiteMedSAM | Latency per volume (CPU, WebGPU), model MB, accuracy delta after INT8/FP16 |

---

## 11. Research gaps a new paper could credibly claim

1. **A single model for spine across CT, MRI and X-ray.** All verified SOTA systems are single-modality: SPINEPS and SPIDER for MRI, VerSe and TotalSegmentator for CT, AASCE and VinDr for X-ray. The general foundation models either do not cover X-ray and 3D together, or carry restrictive licenses (Curia, MedSigLIP). TotalSegmentator MRI shows that sequence independence is possible. A model with a shared vertebra-level token space across modalities and tasks (segmentation, grading, fracture, alignment) has no direct prior work. 1.1 and 2.8 show that the evaluation must be rigorous, so compare it against per-task nnU-Net and RSNA-winner baselines.
2. **Calibrated abstention with guarantees for spine, separating "re-scan" from "inconclusive".**
   - No spine IQA model or rescan model was found.
   - Spine work reports point accuracy without risk-coverage analysis.
   - 7.1 and 7.3 show that naive confidence and conformal sets fail under shift and for 3-class grading.
   - A paper could gate studies with an IQA/OOD head (diffusion-AE or feature-reconstruction embeddings, as in 6.4 and 6.5). It could then apply Learn-then-Test risk control per site, using LumbarDISC's 8 sites as natural shifts, and report AURC and per-site coverage.
3. **Normative spine z-scores.** Normative modelling is standard in neuroimaging (6.1, 6.2), but there are no published **age- and sex-conditioned centiles for vertebral height, disc height and canal area**. Tools now exist to derive them automatically (SPINEPS, VIBESegmentator, TotalSegmentator). Deviation scores give a label-free "abnormal anatomy" signal and an interpretable report line ("L4-L5 disc height z = -2.7"). The signal can be checked against Genant and Pfirrmann labels.
4. **Structured, level-grounded report generation.** 8.3 shows that LVLMs are near chance on per-level detection. Grounding report text in per-level heads, normative z-scores and abstention flags would be new. It should be evaluated with per-level clinical-efficacy F1.
5. **On-device / in-browser spine analysis.** Only brain-MRI browser tools (WebGL) and CPU-laptop SAM exist. A WebGPU/ORT-Web spine pipeline would be a smaller but solid systems contribution, provided it reports accuracy, calibration and abstention after quantisation.
6. **Smaller gaps.**
   - Genant grade 1 (mild) fractures from MRI or X-ray.
   - Meyerding grading from keypoints on public data.
   - Applying the RSNA-winner 2.5D design to Pfirrmann and Modic grading.

---

## 12. References (IDs as verified above)

- Isensee F. et al. nnU-Net Revisited. MICCAI 2024. arXiv:2404.09556.
- Isensee F. et al. nnU-Net. Nature Methods 2021. [M]
- Roy S. et al. MedNeXt. arXiv:2303.09975.
- Huang Z. et al. STU-Net. arXiv:2304.06716.
- Hatamizadeh A. et al. Swin UNETR. arXiv:2201.01266. [M]
- Wasserthal J. et al. TotalSegmentator. Radiol AI 2023. DOI 10.1148/ryai.230024. arXiv:2208.05868.
- Akinci D'Antonoli T. et al. TotalSegmentator MRI. Radiology 2025. DOI 10.1148/radiol.241613. arXiv:2405.19492.
- van der Graaf J.W. et al. SPIDER. Sci Data 2024. DOI 10.1038/s41597-024-03090-w. arXiv:2306.12217.
- Möller H. et al. SPINEPS. Eur Radiol. DOI 10.1007/s00330-024-11155-y. arXiv:2402.16368.
- Sekuboyina A. et al. VerSe. Med Image Anal 2021. arXiv:2001.09193.
- Wang H. et al. SAM-Med3D. arXiv:2310.15161.
- Ma J. et al. MedSAM2. arXiv:2504.03600.
- RSNA. 2024 Lumbar Spine Degenerative Classification AI Challenge winners. rsna.org/news/2024/november/2024-ai-challenge-winners.
- Richards T.J. et al. LumbarDISC. Radiol AI 2026;8(2). DOI 10.1148/ryai.250480. arXiv:2506.09162.
- Windsor R., Jamaludin A., Kadir T., Zisserman A. SpineNetV2. arXiv:2205.01683.
- Hallinan J.T.P.D. et al. [first author M] Radiology 2021;300(1):130-138. DOI 10.1148/radiol.2021204289.
- Natalia F. et al. PLoS ONE 2024. DOI 10.1371/journal.pone.0302067.
- Liu H. et al. AnyMC3D. arXiv:2512.12887.
- Lee G.R. et al. RSNA 2022 CSFD winners. Radiol AI 2024;6(1):e230256.
- Keicher M. et al. arXiv:2303.12031.
- Wei X. et al. arXiv:2208.10698.
- Wang L. et al. AASCE2019. Med Image Anal 2021;72:102115. DOI 10.1016/j.media.2021.102115.
- Shao Z. et al. CurvNet. arXiv:2411.12604.
- Yang J., Wang J., Meng M. LaNet. arXiv:2405.19645.
- Nguyen H.T. et al. VinDr-SpineXR. arXiv:2106.12930.
- Zhang J. et al. Front Bioeng Biotechnol 2023. DOI 10.3389/fbioe.2023.1194009.
- SpineFM. ISBI 2025. arXiv:2411.00326.
- Codella N. et al. MedImageInsight. arXiv:2410.06542.
- Zhang S. et al. BiomedCLIP. arXiv:2303.00915.
- Pérez-García F. et al. RAD-DINO. Nat Mach Intell 2025. DOI 10.1038/s42256-024-00965-w. arXiv:2401.10815.
- Pai S. et al. CT-FM. arXiv:2501.09001.
- Blankemeier L. et al. Merlin. Nature 2026. DOI 10.1038/s41586-026-10181-8. arXiv:2406.06512.
- Dong H. et al. MRI-CORE. arXiv:2506.12186.
- Dancette C. et al. Curia. arXiv:2509.06830.
- Google. MedGemma Technical Report. arXiv:2507.05201.
- Li Y. et al. MedDINOv3. arXiv:2509.02379.
- Singla N. et al. XR-0. arXiv:2509.12146.
- Bethlehem R.A.I. et al. Brain charts. Nature 2022. [M]
- Normative Modelling in Neuroimaging. arXiv:2509.07237. [U authors]
- Graf R. et al. VIBESegmentator. Eur Radiol 2025. DOI 10.1007/s00330-025-12035-9. arXiv:2406.00125.
- Graf R. et al. DAE embeddings spine MRI. iMIMIC 2024. arXiv:2410.10220.
- Cai Y. et al. MedIAnomaly. Med Image Anal 2025. arXiv:2404.04518.
- Bungert T.J., Kobelke L., Jaeger P.F. Silent failures. arXiv:2307.14729.
- Kahl K.-C. et al. ValUES. ICLR 2024. arXiv:2401.08501.
- Mehrtens H., Bucher T.-C., Brinker T.J. arXiv:2506.18162.
- Angelopoulos A.N. et al. Learn then Test. arXiv:2110.01052.
- Angelopoulos A.N., Bates S. arXiv:2107.07511.
- Lee W. et al. LDCTIQAC. Med Image Anal 2025;99:103343. DOI 10.1016/j.media.2024.103343.
- Zhao M. et al. SpineBench / SpineMed-450k. ICLR 2026. arXiv:2510.03160.
- Zhang C. et al. SpineBench (MLLM VQA). arXiv:2510.12267.
- Palau B. et al. Beyond Fluency. arXiv:2608.07117.
- Nguyen Van H. et al. GateSPINE. arXiv:2609.40091.
- Yeasin M. et al. Auto-Rad. J Clin Med 2024;13(23):7092.
- Ma J. et al. Efficient MedSAMs. arXiv:2412.16085.
- Lu H. et al. QAT SAM deployment. arXiv:2412.11186.
- Masoud M. et al. Brainchop. arXiv:2310.16162.
- Microsoft Open Source Blog. ONNX Runtime Web + WebGPU. 2024-02-29.
- Hugging Face. Transformers.js v3. 2024-10-22.

### Open verification items
- The RSNA 2024 and 2022 1st-place writeups were not readable on Kaggle in this session. Confirm them from the original writeups before describing them as "the" winning architecture.
- Still to check: the exact licenses of the TotalSegmentator sub-task weights, the CT-FM and Merlin weights, the official MedImageInsight release, and the STU-Net repository.
- Not fetched: BUU-LSPINE, the NFBC1966 SpineNet validation (PMC9990601), the Sci Rep 2025 vertebral-height paper, and the AJNR rescan paper details.
- The exact form of the RSNA 2024 metric (severity weights 1/2/4 plus the any-severe term) is from memory. Confirm it on the Kaggle evaluation page.
