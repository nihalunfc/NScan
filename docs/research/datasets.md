# Public Spine Imaging Datasets: Curated Catalogue

Status as of 2026-10-16. Licences and access routes were checked against the hosting pages (Zenodo, Kaggle/RSNA, AWS Open Data Registry, PhysioNet, Mendeley Data, GitHub, OSF, NLM, TCIA/IDC) during this session.

How the verification markers are used:

- **[V]**: confirmed on the hosting page or the paper in this session.
- **[U]**: could not be confirmed. Examples are a page that did not render a licence field, a host that was offline or blocked, or a fact taken from memory or secondary sources. Check every [U] item before you depend on it.
- Licence names are copied exactly as the host shows them. "Not stated" means the host page showed no licence. It does not mean the data is public domain.

Ground rule for this project: a CC BY-NC*, "non-commercial" or DUA licence lets you use the data for research and for training research models. It does **not** cover a commercial product. Keep a provenance column in every training manifest.

---

## 1. Summary table

| # | Dataset | Modality | Region | Size | Labels | Licence | Open download (no login) |
|---|---|---|---|---|---|---|---|
| 1 | **SPIDER** | MRI sag T1 + T2 | Lumbar | 218 pts / 447 series | Masks: vertebrae, IVDs, spinal canal; per-IVD Pfirrmann, Modic, endplate/Schmorl, spondylolisthesis, herniation, narrowing, bulging | CC BY 4.0 [V] | **Yes** (Zenodo) |
| 2 | **RSNA 2024 LumbarDISC** (Lumbar Spine Degenerative Classification) | MRI sag T1, sag T2/STIR, ax T2 | Lumbar L1/2–L5/S1 | 2,697 pts / 8,593 series | Stenosis grades (canal, L/R foramen, L/R subarticular) + localiser points | Non-commercial; no redistribution [V] | No (Kaggle rules or RSNA MIRA) |
| 3 | **RSNA 2022 Cervical Spine Fracture** (RSNA-CSF) | CT | Cervical C1–C7 | 3,112 studies (2,019 train) | Per-study + per-level fracture; bboxes (235 studies); C1–C7 masks on a subset | Non-commercial; no redistribution [V] | No (Kaggle rules or MIRA) |
| 4 | **VerSe'19 / VerSe'20** | CT (MDCT) | Whole spine C1–L5/L6 (+T13) | 374 scans / 355 pts (160 + 300 series, overlapping) | Per-vertebra masks, centroids; VerSe'19 Genant fracture grades | CC BY-SA 4.0 (OSF/GitHub) [V]; TUM site says CC BY-SA 2.0 [V, discrepancy] | **Yes** (S3 links in GitHub README; OSF) |
| 5 | **CTSpine1K** | CT | Whole spine (C1–L6) | 1,005 CT volumes; 11,172 vertebrae | Per-vertebra masks | CC BY-NC-SA [V] | **Yes** (HF, XNAT, Google Drive) |
| 6 | **TotalSegmentator CT v3.0.0** | CT (whole-body) | Whole spine + body | 1,939 CT | 117 structures incl. C1–L5 (+S1), sacrum, spinal cord [classes U] | CC BY 4.0 [V] | **Yes** (Zenodo, 37.4 GB) |
| 7 | **TotalSegmentator MRI v2.0.0** | MRI (any sequence) | Whole-body incl. spine | 616 MRI | 50 structures (vertebrae, IVDs, spinal cord, sacrum [U]) | CC BY-NC-SA 2.0 [V] | **Yes** (Zenodo, 5.1 GB) |
| 8 | **VinDr-SpineXR** | X-ray (AP/lateral) | Cervical/thoracic/lumbar | 10,466 images / 5,000 studies | Bboxes for 13 lesion classes | PhysioNet Restricted Health Data License 1.5.0 [V] | No (PhysioNet account + DUA) |
| 9 | **BUU-LSPINE** | X-ray AP + lateral | Lumbar | 3,600 pts (full); 400 and 2,000 pair subsets | Vertebral corner points / edges; listhesis diagnosis | Custom EULA (research, cite) [V] | Partly: 400 and 2,000 subsets via Google Drive; full set via form |
| 10 | **AASCE 2019 / SpineWeb Dataset 16** | X-ray AP (scoliosis) | Thoracic + lumbar (T1–L5) | 609 train + 98 test | 68 landmarks (4 corners × 17 vertebrae), 3 Cobb angles | Not stated [U] | **No / unclear**: SpineWeb offline; curated labels on Zenodo |
| 11 | **MRSpineSeg** | MRI T2 volumetric | Lumbar/thoracolumbar | 215 (172 labelled) | Masks: 10 vertebrae + 9 IVDs | Not stated [U] | Unclear [U] |
| 12 | **Lumbar Spine MRI Dataset** (Sudirman, Mendeley k57fr854j2) | MRI ax + sag T1/T2 | Lumbar (L3–S1) | 515 pts / 48,345 slices | None in base set; see derived sets (#13) | Licence field blank on page [U] | **Yes** (Mendeley Data) |
| 13 | **Sudirman derived sets**: LSMA-PQR (2026), IVD-height/Pfirrmann (2024) | MRI ax + sag | Lumbar | 515 pts; 4,120 annotated images | 7-structure masks, 1,545 Pfirrmann grades, 1,545 IVD heights, report metadata | Blank; "free to use, cite" [U] | **Yes** (Mendeley Data) |
| 14 | **NHANES II spine X-rays** (NLM) | X-ray lateral C-spine + L-spine | Cervical, lumbar | ~17,000 films | Vertebra coordinates for a subset ("marks"); survey data via WebMIRS | Not stated (US Gov) [U] | **Yes** (data.lhncbc.nlm.nih.gov) |
| 15 | **CTPelvic1K** | CT | Pelvis + lumbar spine/sacrum | ~1,184 CT (7 sub-sets) [U] | Masks: lumbar spine, sacrum, L/R hip [classes U] | CC BY 4.0 (Zenodo annotations) [V] | **Yes** (Zenodo; some images from source sites) |
| 16 | **CTSpinoPelvic1K** (2026) | CT | Spine + pelvis + ribs + femora | 802 CT | Per-level vertebrae incl. L6/T13/lumbar ribs; Castellvi LSTV grades (33) | Not stated in abstract [U] | Zenodo (presumably open) [U] |
| 17 | **CSpineSeg** (Duke, 2025) | MRI sag T2 | Cervical | 1,255 exams / 1,232 pts; 481 manually labelled | Masks: vertebral bodies, IVDs | [U] | [U] (believed MIDRC) |
| 18 | **LSpineSMRI** (2025) | MRI ax + sag T2, 1.5 T | Lumbar | 640 pts / 17,440 slices | Stenosis grade A–D | Blank [U] | **Yes** (Mendeley) |
| 19 | **LSS MRI AISSLab** (2026, Sci Data) | MRI sag | Lumbar | 500 pts / 8,500 slices | Foraminal stenosis bboxes + 4-grade; mid-sag masks | Blank; "non-commercial" in text [U] | **Yes** (Mendeley) |
| 20 | **Lumbar 3D Axial Stenosis MRI** (2026) | MRI ax T2 | Lumbar | 500 pts | Bboxes + grades (canal, lateral recess, foramen); masks | Blank [U] | **Yes** (Mendeley) |
| 21 | **Spine-generic** (multi-subject) | MRI T1w, T2w, T2*w, DWI, MT | Cervical cord + spine (healthy) | 260 participants, 42 sites | Cord / GM segmentations, derivatives | CC BY 4.0 [V] | **Yes** (git-annex, ~26 GB) |
| 22 | **Spine-Mets-CT-SEG** (TCIA/IDC) | CT | Thoracolumbar (metastatic) | 55 pts | Vertebral masks, lesion and fracture labels | Not shown on IDC page [U] | **Yes** (IDC) |
| 23 | **Spinal-Multiple-Myeloma-SEG** (2026 ext.) | Dual-energy CT | Lumbar | 72 exams / 67 pts | Trabecular bone masks of lumbar vertebrae | CC BY 4.0 (Zenodo extension) [V]; TCIA base [U] | **Yes** |
| 24 | **Spinal-AI2024** | X-ray (scoliosis) | Thoracolumbar | 20,000 images | COCO instance contours; 3 Cobb angles | Not stated [U] | **Yes** (GitHub); possibly synthetic [U] |
| 25 | **Cervical spine X-ray atlas** (Sci Data 2024) | X-ray lateral | Cervical | 4,963 images | 23 keypoints; 118 parameters; curvature class; asymptomatic vs symptomatic | [U] | [U] |
| 26 | **RadImageNet** | CT/MRI/US | Includes spine MRI [U] | 1.35 M images / 131,872 pts | 165 pathology labels (image-level) | Dataset terms not stated (repo MIT) [U] | No (request form) |
| 27 | **Lumbosacral nerve-root MRI** (Sci Data 2024) | MRI CISS, DESS, T2-TSE | Lumbosacral (healthy) | 14 healthy adults | Nerve-root annotations, 3D cord models | [U] | [U] |
| 28 | **IMBE-SPINES** (Leeds) | CT + MRI, cadaveric | Spine segments | [U] | Images (+ related biomech sets) | CC BY 4.0 [V] | **Yes** |
| 29 | **Whole-Spine T1 MPRAGE** (OpenNeuro ds005616) | MRI T1 3D (healthy) | Whole spine + head/neck | 60 volunteers | Coarse tissue labels (spine, brain, lungs…) | Not in README [U] | **Yes** (OpenNeuro) |
| 30 | **R-D-Reg (MSR) cervical CT–MRI registration** (2026) | CT + MRI | Cervical | [U] | Registration annotations [U] | Not stated [U] | GitHub [U] |
| — | Genodisc / SpineNet training data | MRI | Lumbar | — | — | **Not public** | No |
| — | MIDRC | Mixed | — | — | — | Registration + DUA [U] | No |
| — | PhenSPINE (2026) | MRI 4 sequences | Spine | 250 pts / 16,813 images | Pathology diagnosis | Release not stated [U] | No/unclear |

---

## 2. Tiered recommendation

### Tier 1: open now, no credentials (start downloading)

| Priority | Dataset | Why |
|---|---|---|
| 1 | **SPIDER** (CC BY 4.0) | Best openly licensed lumbar MRI set with **both** 3-class instance masks (vertebrae, IVD, canal) **and** degenerative grades (Pfirrmann, Modic, etc.). Multi-centre, T1 and T2. The core of the MRI segmentation and grading work. |
| 2 | **TotalSegmentator CT v3.0.0** (CC BY 4.0) | 1,939 CTs with per-vertebra labels. The licence allows commercial use. Large and varied, so it suits CT pretraining and level labelling. |
| 3 | **VerSe'19/'20** (CC BY-SA 4.0) | Gold-standard per-vertebra CT masks and centroids, with anatomical variants (T13, L6, LSTV). VerSe'19 includes Genant fracture grades. Share-alike applies to derivatives. |
| 4 | **CTSpine1K** (CC BY-NC-SA) | Largest dedicated vertebra-segmentation CT set (1,005 volumes). Research use only. |
| 5 | **TotalSegmentator MRI v2.0.0** (CC BY-NC-SA 2.0) | Sequence-agnostic MRI, whole-body context, spine structures. Non-commercial. |
| 6 | **Spine-generic** (CC BY 4.0) | Healthy multi-site, multi-vendor cervical MRI. Use it as the **normative reference** for cord and canal measures. |
| 7 | **NHANES II X-rays** (NLM) | ~17k lateral C- and L-spine radiographs from a population survey (1976–80), linked to survey data. Useful for X-ray pretraining and population-level degenerative norms. Licence not stated (U.S. Government collection). |
| 8 | Mendeley lumbar MRI family (Sudirman 515-pt base + LSMA-PQR, LSpineSMRI, LSS AISSLab, 3D axial stenosis) | Adds axial MRI stenosis, Pfirrmann and disc-height labels. **The licence field did not render for any of them**, so confirm it on the page (Mendeley's default is usually CC BY 4.0, but some descriptions say "non-commercial"). |
| 9 | CTPelvic1K (CC BY 4.0), CTSpinoPelvic1K (licence U) | Lumbosacral junction, sacrum and LSTV (Castellvi) labels. Use them for spinopelvic parameters. |
| 10 | Spine-Mets-CT-SEG, Spinal-Multiple-Myeloma-SEG | Pathological vertebrae (metastases, myeloma) for robustness and lesion tasks. |

### Tier 2: free registration, Kaggle rules or request form

| Dataset | Route | Notes |
|---|---|---|
| **RSNA 2024 LumbarDISC** | Kaggle competition (join and accept rules) or RSNA MIRA `mira.rsna.org/dataset/6` | The largest public multi-site lumbar MRI set with stenosis grades. Non-commercial; no redistribution. **Top priority for degenerative grading.** |
| **RSNA 2022 Cervical Spine Fracture** | Kaggle or MIRA `mira.rsna.org/dataset/4` | 3,112 CT studies with fracture labels. The only large public C-spine fracture set. Non-commercial. |
| **BUU-LSPINE** | 400-pair sample and 2,000-pair set via Google Drive from the project page; full 3,600 via Google Form | EULA requires citation and no re-identification. The best open lumbar X-ray landmark set. |
| **VerSe via TUM site** | `deep-spine.de` registration form + DUA | An alternative to the S3 links. |
| **RadImageNet** | Request at radimagenet.com | Pretraining only (image-level labels). Dataset licence not published [U]. |
| **AASCE 2019 / SpineWeb 16** | SpineWeb portal is **offline** (confirmed on a Slicer forum post). Curated annotations are on Zenodo 4413665, but the images must come from the organisers or existing copies. | Standard Cobb-angle benchmark. Access unverifiable [U]. |
| **MRSpineSeg** | Challenge site `spinesegmentation-challenge.com` | Current availability is unverified [U]. |
| **CSpineSeg** | Hosting not confirmed [U] | Largest cervical MRI segmentation set (2025). |

### Tier 3: credentialed, DUA or not public

| Dataset | Route | Notes |
|---|---|---|
| **VinDr-SpineXR** | PhysioNet: create an account and sign the PhysioNet Restricted Health Data Use Agreement 1.5.0 | 10,466 X-rays with 13 lesion classes. Restricted licence; no redistribution. |
| **MIDRC** | Registration + DUA [U] | Check for spine content (possibly CSpineSeg) [U]. |
| **Genodisc / SpineNet** | Data not public. SpineNet code and weights are under non-commercial terms of access. | Use only as a pretrained grader for pseudo-labels, and only if the licence allows it. |
| **PhenSPINE** | Not stated as released | Track it for future release. |

---

## 3. Per-dataset details

### 3.1 SPIDER: Lumbar spine segmentation in MR images [V]
- **Modality / region:** Sagittal T1 and T2 lumbar MRI, from 4 Dutch hospitals; low-back-pain patients.
- **Size:** 218 patients, 447 series. A hidden test set is held by the SPIDER Grand Challenge.
- **Labels:** Instance masks for vertebrae, IVDs and spinal canal. `radiological_gradings.csv` holds per-IVD Modic, upper/lower endplate changes / Schmorl nodes, spondylolisthesis, disc herniation, narrowing, bulging and Pfirrmann (1–5). `overview.csv` holds sex, age, scanner and acquisition parameters, and the train/val split.
- **Licence:** CC BY 4.0.
- **Access:** https://zenodo.org/records/10159290 (v4; DOI 10.5281/zenodo.10159290). Files: images.zip 3.7 GB, masks.zip 58 MB, two CSVs. No login. An unofficial resized HF mirror exists (`huggingface.co/datasets/cdoswald/SPIDER`, CC BY 4.0, re-split). Prefer the Zenodo original.
- **Paper:** van der Graaf JW, et al. *Lumbar spine segmentation in MR images: a dataset and a public benchmark.* Scientific Data 11, 264 (2024). DOI 10.1038/s41597-024-03090-w; arXiv:2306.12217.
- **Best for:** Multi-structure lumbar MRI segmentation together with degenerative grading, under a permissive licence.

### 3.2 RSNA 2024 LumbarDISC (Lumbar Spine Degenerative Classification) [V]
- **Modality:** Sagittal T1, sagittal "T2-like" (T2/STIR/Dixon) and axial T2 MRI.
- **Size:** 2,697 patients (one study each), 8,593 series, from 8 institutions in 6 countries. Split: 1,981 train, 272 public test, 444 private test. Only the train labels are in the Kaggle download.
- **Labels:** Grades at L1/2–L5/S1 for spinal canal, L/R neural foraminal and L/R subarticular stenosis. Grades were collected on a 4-point scale and released as 3 classes (normal/mild, moderate, severe). Each grade has (x, y, instance) localiser coordinates. Counts: 13,474 canal, 26,919 foraminal, 26,285 subarticular grades.
- **Licence:** "Non-commercial purposes only", including academic research and education. No re-identification, no redistribution, citation required (AWS registry licence text). The paper says the data is "freely available to all researchers for noncommercial use". No named CC licence.
- **Access:** (a) Kaggle: https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification. Sign in, join, accept the rules, then `kaggle competitions download -c rsna-2024-lumbar-spine-degenerative-classification`. (b) RSNA MIRA https://mira.rsna.org/dataset/6. (c) AWS S3 `lumbar-spine-degenerative-classification` (us-west-2), listed as **Controlled Access** via MIRA. Docs: https://github.com/RSNA/AI-Challenge-Data/wiki/RSNA-Lumbar-Spine-Degenerative-Classification-Dataset
- **Paper:** Richards TJ, …, Talbott JF. *The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset.* Radiology: Artificial Intelligence 8(2), 2026. DOI 10.1148/ryai.250480; arXiv:2506.09162.
- **Best for:** Training and benchmarking stenosis grading. Has the largest multi-site label volume.

### 3.3 RSNA 2022 Cervical Spine Fracture Detection (RSNA-CSF) [V]
- **Modality:** Non-contrast cervical spine CT, from 12 sites on 6 continents.
- **Size:** 3,112 studies (2,019 train, 304 public test, 789 private test). 1,445 (about 46%) are fracture-positive.
- **Labels:** Patient-level and per-vertebra (C1–C7) fracture labels. Bounding boxes on 235 positive training studies. C1–C7 segmentations on a subset of the training set (the exact count was not re-verified [U]).
- **Licence:** Non-commercial (academic research and education), no redistribution, cite. Note that the AWS licence text has a copy-paste error naming the "Brain CT Hemorrhage Dataset".
- **Access:** Kaggle https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection (accept rules); MIRA https://mira.rsna.org/dataset/4; AWS S3 `cervical-spine-fracture` (controlled). Docs: https://github.com/RSNA/AI-Challenge-Data/wiki/RSNA-Cervical-Spine-Fracture-Detection
- **Paper:** Lin HM, Colak E, Richards T, et al. *The RSNA Cervical Spine Fracture CT Dataset.* Radiology: Artificial Intelligence 5(5): e230034 (2023). DOI 10.1148/ryai.230034.
- **Best for:** Cervical fracture detection and localisation on CT.

### 3.4 VerSe'19 / VerSe'20 [V]
- **Modality / region:** MDCT, cervical to lumbar (and sacral partial). VerSe'20 deliberately includes anatomical variants: T13, L6, transitional vertebrae.
- **Size:** 374 scans from 355 patients in total. VerSe'19 is 160 series from 141 patients; VerSe'20 is 300 series. The two partly overlap through BIDS IDs below 499.
- **Labels:** Per-vertebra masks (`seg-vert_msk.nii.gz`) and centroids (`seg-subreg_ctd.json`; labels 1–25 = C1–L6, 28 = T13). VerSe'19 has vertebra-level **Genant fracture grades** (per the HealthiVert-GAN paper: 1,436 normal, 142 mild, 96 moderate, 51 severe vertebrae).
- **Licence:** The GitHub README and OSF wiki state **CC BY-SA 4.0**. The TUM `deep-spine.de` page lists VerSe'19 as CC BY-SA 2.0, and its download-form DUA says CC BY-SA 2.0 [discrepancy]. Either way the licence is attribution + share-alike and allows commercial use.
- **Access:** No login. Direct `.zip` links on `s3.bonescreen.de` are listed in https://github.com/anjany/verse (restructured format, recommended). Also OSF https://osf.io/nqjyw/ (VerSe'19) and https://osf.io/t98fz/ (VerSe'20), and the TUM form at https://deep-spine.de/.
- **Papers:** Sekuboyina A, et al. *VerSe: A Vertebrae labelling and segmentation benchmark for multi-detector CT images.* Medical Image Analysis 73:102166 (2021) [vol/page U], arXiv:2001.09193. Löffler MT, et al. *A Vertebral Segmentation Dataset with Fracture Grading.* Radiology: AI 2(4):e190138 (2020), DOI 10.1148/ryai.2020190138. Liebl H, et al. *A computed tomography vertebral segmentation dataset with anatomical variations and multi-vendor scanner data.* Scientific Data 8:284 (2021) [details U].
- **Best for:** CT vertebra labelling and segmentation with variants. The standard benchmark.

### 3.5 CTSpine1K [V]
- **Size:** 1,005 CT volumes (610 train, 197 public test, 198 private test), more than 500k labelled slices, 11,172 vertebrae.
- **Sources:** TCIA CT Colonography, HNSCC-3DCT-RT, MSD Task03 (liver), and a COVID-19 CT set. Most scans are abdominal or thoracic, so expect fewer cervical levels.
- **Labels:** Per-vertebra masks, C1–L6 (labels 1–25).
- **Licence:** CC BY-NC-SA (stated for all sub-datasets; the paper gives 4.0).
- **Access:** HF https://huggingface.co/datasets/alexanderdann/CTSpine1K (not gated; ~162 GB). XNAT https://xnat.health-ri.nl/data/archive/projects/africai_miccai2024_ctspine1k. GitHub https://github.com/MIRACLE-Center/CTSpine1K (Google Drive / Baidu links).
- **Paper:** Deng Y, Wang C, Hui Y, et al., Zhou SK. *CTSpine1K: A Large-Scale Dataset for Spinal Vertebrae Segmentation in Computed Tomography.* MELBA, MICCAI Open Data special issue, 2025, pp. 824–832. arXiv:2105.14711.
- **Best for:** Scaling CT vertebra segmentation (non-commercial).

### 3.6 TotalSegmentator CT [V]
- **Versions:** **v3.0.0** has 1,939 CTs (Zenodo, published 2026-09-10, 37.4 GB, `Totalsegmentator_dataset_v300.zip`), at https://zenodo.org/records/6802613. v2.0.1 has 1,228 CTs, 117 structures, 23.6 GB: https://zenodo.org/records/10047292.
- **Labels:** 117 structures. These include the individual vertebrae C1–L5 and sacrum (v1 list confirmed). v2 adds `vertebrae_S1` and `spinal_cord` [U, from TotalSegmentator docs]. Labels are model-assisted and then refined, so they are not fully manual.
- **Licence:** CC BY 4.0. No login.
- **Paper:** Wasserthal J, Breit HC, Meyer MT, et al. *TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images.* Radiology: AI 5(5):e230024 (2023) [DOI 10.1148/ryai.230024, U]. arXiv:2208.05868.
- **Best for:** Large, permissively licensed CT spine pretraining and whole-body context (ribs, pelvis) for level counting.

### 3.7 TotalSegmentator MRI [V]
- **Size:** 616 MRIs (v2.0.0, 2025-01-21; up from 298), 5.1 GB, https://zenodo.org/records/14710732. Clinical routine data covering many sequences, scanners and pathologies. Some images come from IDC.
- **Labels:** 50 structures from the "total" task. Includes vertebrae, intervertebral discs, spinal cord and sacrum [U: the class list was not shown on Zenodo].
- **Licence:** **CC BY-NC-SA 2.0** (unlike the CT set).
- **Paper:** Akinci D'Antonoli T, …, Wasserthal J. *TotalSegmentator MRI: Robust Sequence-independent Segmentation of Multiple Anatomic Structures in MRI.* Radiology 2025, DOI 10.1148/radiol.241613. arXiv:2405.19492.
- **Best for:** Sequence-agnostic MRI spine segmentation pretraining.

### 3.8 VinDr-SpineXR [V]
- **Size:** 10,466 X-rays from 5,000 studies (train 8,389 / 4,000; test 2,077 / 1,000). Vietnamese hospitals.
- **Labels:** Bounding boxes for 13 classes: ankylosis, disc space narrowing, enthesophytes, foraminal stenosis, fracture, osteophytes, sclerotic lesion, spondylolysthesis, subchondral sclerosis, surgical implant, vertebral collapse, foreign body, other lesions. Plus "No finding".
- **Licence / access:** PhysioNet **Restricted Health Data License 1.5.0**. Requires a PhysioNet account and signing the Restricted Health Data Use Agreement 1.5.0. https://physionet.org/content/vindr-spinexr/ (v1.0.0).
- **Paper:** Nguyen HT, Pham HH, Nguyen NT, et al. *VinDr-SpineXR: A deep learning framework for spinal lesions detection and classification from radiographs.* MICCAI 2021. arXiv:2106.12930.
- **Best for:** Multi-lesion detection on spine radiographs.

### 3.9 BUU-LSPINE [V]
- **Size:** 3,600 patients (AP + lateral lumbar radiographs, Burapha University, Thailand). Public subsets: 400 pairs (sample; 400 patients, ages 6–89) and 2,000 pairs.
- **Labels:** Upper and lower edge points of each lumbar vertebra (corner landmarks), stored in CSV. Physician diagnosis of antero-, retro- and L/R laterolisthesis. The 2,000-pair set adds side-bending/rotation (AP) and flexion/extension (lateral) labels.
- **Licence:** End-User Licence Agreement with the Faculty of Informatics, Burapha University: no re-identification, cite the dataset publications, no endorsement, access can be revoked. No CC licence.
- **Access:** https://services.informatics.buu.ac.th/spine/. Sample and 2,000-pair sets via Google Drive; full set via Google Form, with approval and delivery by email.
- **Paper:** Klinwichit P, et al. *BUU-LSPINE: A Thai Open Lumbar Spine Dataset for Spondylolisthesis Detection.* Applied Sciences 13(15):8646 (2023) [author list U]. DOI 10.3390/app13158646 [U, derived from MDPI URL].
- **Best for:** Lumbar X-ray vertebral corner landmarks, slip measurement and spondylolisthesis.

### 3.10 AASCE 2019 / SpineWeb Dataset 16 [partly V]
- **Size:** 609 AP spinal X-rays for training (adolescent idiopathic scoliosis) plus 98 test images. 68 landmarks per image (4 corners × 17 vertebrae, T1–L5) and 3 Cobb angles (PT, MT, TL).
- **Access:** The original SpineWeb portal (`spineweb.digitalimaginggroup.ca`) is **no longer accessible** (3D Slicer forum, 2025). Curated corrected annotations, but not the images, are at https://zenodo.org/records/4413665 (licence not shown [U]). Image access today [U]: ask the organisers or use copies already held by groups.
- **Papers:** Wu H, Bailey C, Rasoulinejad P, Li S. *Automatic landmark estimation for adolescent idiopathic scoliosis assessment using BoostNet.* MICCAI 2017, DOI 10.1007/978-3-319-66182-7_15. Wang L, et al. *Evaluation and comparison of accurate automated spinal curvature estimation algorithms with spinal anterior-posterior X-ray images: The AASCE2019 challenge.* Medical Image Analysis 72:102115 (2021), DOI 10.1016/j.media.2021.102115.
- **Best for:** Cobb-angle and landmark benchmarking (legacy standard).
- **Alternative:** Spinal-AI2024 (GitHub `Ernestchenchen/Spinal-AI2024`, 20,000 images, COCO contours and 3 Cobb angles, licence not stated). Its images appear to be generated by the CurvNet data engine [U]; treat it as synthetic until confirmed. Paper: arXiv:2411.12604.

### 3.11 SpineWeb collections (general)
SpineWeb (Dataset 1–19: CT vertebra segmentation, MR IVD, scoliosis X-ray, etc.) was the historic hub. The portal is **offline** as of 2025. Several of its sets live on elsewhere: AASCE annotations (Zenodo 4413665), the xVertSeg and IVD MICCAI challenges [U], and VerSe (which superseded the CSI 2014/2016 sets). Use the replacements listed here rather than trying to rebuild SpineWeb.

### 3.12 MRSpineSeg [partly V]
- **Size:** 215 T2-weighted volumetric spine MRIs. 172 training images have masks; 43 test images do not.
- **Labels:** 10 vertebrae (L5–T9 plus sacrum) and 9 IVDs [exact list U], plus background.
- **Access:** Released through the China Society of Image and Graphics challenge, https://www.spinesegmentation-challenge.com. Current availability and licence are **unverified**. The NeuroPoly TotalSpineSeg README links it via paperswithcode.
- **Paper:** Pang S, et al. *SpineParseNet: Spine Parsing for Volumetric MR Image by a Two-Stage Segmentation Framework With Semantic Image Representation.* IEEE TMI 40(1), 2021 [details U].
- **Best for:** An extra lumbar T2 segmentation source; check terms first.

### 3.13 Lumbar Spine MRI Dataset (Sudirman et al., Mendeley) and derivatives
- **Base set** (DOI 10.17632/k57fr854j2.2, v2, 2019-04-03): 515 symptomatic back-pain patients, sagittal and axial T1/T2 DICOM, 48,345 slices. Axial slices cover the lowest 3 discs. No labels are documented on the page.
- **Pfirrmann / IVD-height set** (DOI 10.17632/x6ggzp2ycn.1, 2024): 515 T2 mid-sagittal slices with manual segmentation labels, ResNet-50 auto-segmentations, IVD mid-height and Pfirrmann predictions (supports a PLOS ONE 2024 paper).
- **LSMA-PQR** (DOI 10.17632/p3r4xd2488.2, 2026-05-18): 515 patients, 4,120 images (3,090 axial, 1,030 sagittal) at 384×384. 7-structure masks, 1,545 radiologist-validated Pfirrmann grades, 1,545 disc-height measurements, and structured metadata from 515 radiology reports. This is the closest thing to a **public spine MRI and report** dataset.
- **Licence:** The Mendeley pages rendered a blank licence field for all of them [U]. LSMA-PQR says "free to use with a request to cite". Check the licence badge in a browser.
- **Access:** https://data.mendeley.com/datasets/k57fr854j2 (and the IDs above). Downloads usually need no login.
- **Papers (base set):** Sudirman S, et al. Mendeley Data 2019. Related boundary-delineation papers by Natalia F, Al Kafri A, et al. [U].
- **Best for:** Axial lumbar MRI anatomy, Pfirrmann and disc height, and report-linked metadata.

### 3.14 NHANES II spine X-rays (NLM / LHNCBC) [V]
- **Size:** About 17,000 digitised lateral cervical and lumbar films from NHANES II (1976–1980), collected to assess osteoarthritis and degenerative disc disease. Cervical images are 1463×1755 px and lumbar images 2048×2487 px, both at 146 dpi.
- **Labels:** A `marks/` directory holds vertebra coordinates for a subset. Demographic and survey variables are available via WebMIRS (registration required).
- **Access:** https://data.lhncbc.nlm.nih.gov/public/NHANES/X-rays/README.html. Subdirectories: `fullres` (12-bit .nh2 raw), `tif8`, `tif8roi`, `marks`. No login.
- **Licence:** Not stated on the page [U]. It is a U.S. Government (NCHS/NLM) collection, so it is likely public domain, but confirm.
- **Best for:** Large-scale lateral radiograph pretraining and population-level degenerative prevalence.

### 3.15 CTPelvic1K and CTSpinoPelvic1K
- **CTPelvic1K** [V]: Zenodo https://zenodo.org/records/4588403 (CC BY 4.0, ~17 GB). Masks for sub-datasets 1–5 (images come from source collections such as MSD, KiTS19, CERVIX, ABDOMEN, COLONOG) and images + masks for new clinical sets 6–7. Classes: lumbar spine, sacrum, left hip, right hip [U]. Paper: Liu P, Han H, Du Y, et al. *Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models.* IJCARS 2021. Relevant for the sacrum and lumbosacral junction (spinopelvic parameters).
- **CTSpinoPelvic1K** (new, arXiv:2609.22760, 2026-09-19): 802 CTs that join CTSpine1K and CTPelvic1K labels and add ribs and femora in one frame. Labels anchored on the lowest rib-bearing vertebra and S1, with L6, T13 and lumbar-rib classes and Castellvi LSTV grades for 33 records (rib labels are reviewed pseudolabels). Zenodo DOI 10.5281/zenodo.22139642. Licence not stated in the abstract [U]; it inherits the NC-SA terms of the CTSpine1K labels at minimum [U]. Best for LSTV-aware level counting.

### 3.16 Osteoporotic and pathological vertebral fracture sets
- **VerSe'19 Genant grades** (see 3.4): the only fully open per-vertebra Genant-graded CT set found.
- **RSNA-CSF** (3.3): traumatic cervical fractures.
- **VinDr-SpineXR** (3.8): "fracture" and "vertebral collapse" boxes on X-ray.
- **Spine-Mets-CT-SEG** [V]: 55 patients with metastatic spine disease; vertebral masks plus lesion and fracture annotations; longitudinal radiotherapy CT. IDC https://portal.imaging.datacommons.cancer.gov/collections/spine_mets_ct_seg, TCIA DOI 10.7937/kh36-ds04. Licence not shown on the IDC page [U] (TCIA collections are commonly CC BY 4.0). Paper: medRxiv 10.1101/2024.10.14.24314447.
- **Spinal-Multiple-Myeloma-SEG** [V]: 72 dual-energy CT exams from 67 patients; trabecular bone masks of lumbar vertebrae. Base data on TCIA (DOI 10.7937/k4qv-hh78); segmentation extension on Zenodo (DOI 10.5281/zenodo.21628232, CC BY 4.0). arXiv:2608.01482.
- **Gap:** No large open osteoporotic fracture set on **lateral radiographs** with Genant grades was found. Private sets dominate (for example, the 502-CT private set in HealthiVert-GAN, arXiv:2503.05990). Plan to build one from NHANES II or VinDr-SpineXR, or pseudo-label opportunistic CT.

### 3.17 2024–2026 newcomers
| Dataset | Status | Notes |
|---|---|---|
| RSNA LumbarDISC paper (Radiology: AI 2026) | V | Formal citation for the 2024 Kaggle data. |
| TotalSegmentator CT v3.0.0 (Sept 2026) | V | 1,939 CTs, CC BY 4.0. |
| TotalSegmentator MRI v2.0.0 (Jan 2025) | V | 616 MRIs, CC BY-NC-SA 2.0. |
| CSpineSeg (Duke; Zhou L, …, Calabrese E. Scientific Data 12:1695, 2025; DOI 10.1038/s41597-025-05975-w) | Partly V | 1,255 cervical MRI exams / 1,232 patients; 481 manually labelled (vertebral bodies + IVDs). Hosting and licence [U]; believed MIDRC-hosted, so confirm. Best public cervical MRI segmentation set. |
| LSS MRI AISSLab (Sci Data 2026; DOI 10.1038/s41597-026-07138-x; Mendeley 10.17632/rgb77xm3jf.4) | Partly V | 500 patients; foraminal stenosis bboxes and grades; mid-sagittal masks. |
| Lumbar 3D Axial Stenosis MRI (Mendeley 10.17632/wjxkrkxhb8.1, 2026-07) | Partly V | 500 patients; canal, recess and foramen stenosis; axial masks. |
| LSpineSMRI (Mendeley 10.17632/kr8ttxsbb8.2, 2025) | Partly V | 640 patients; stenosis grades. |
| LSMA-PQR (Mendeley 2026) | Partly V | Pfirrmann, disc height, report metadata. |
| CTSpinoPelvic1K (arXiv 2609.22760) | Partly V | LSTV / Castellvi. |
| Spinal-Multiple-Myeloma-SEG ext. (arXiv 2608.01482) | V | CC BY 4.0 masks. |
| Spinal-AI2024 (arXiv 2411.12604) | Partly V | 20k scoliosis images, possibly synthetic. |
| Cervical spine X-ray atlas (Scientific Data, June 2024) | Partly V | 4,963 lateral C-spine X-rays, 23 keypoints, 118 parameters, asymptomatic vs symptomatic. Repository and licence [U]. Useful for **cervical alignment norms**. |
| Lumbosacral nerve-root MRI (Liu J, et al. Sci Data 11, Oct 2024; DOI 10.1038/s41597-024-03919-4) | Partly V | 14 healthy adults; CISS/DESS/T2-TSE; nerve-root annotations. Repository [U]. |
| R-D-Reg cervical CT–MRI registration (arXiv 2604.27654) | Partly V | GitHub `ssc1230609-spec/MSR-registration`; licence not stated. |
| PhenSPINE benchmark (arXiv 2607.19696) | Partly V | 250 patients, 16,813 MRI images; release not stated. |
| RadImageNet | Partly V | Request-only. Spine content not confirmed on the GitHub page [U]. Paper: Mei X, et al. Radiology: AI 2022, e210315, DOI 10.1148/ryai.210315. The "RadImageNet-VQA" derivative (Apache 2.0, on HyperAI, lists spine CT/MRI) is a separate dataset. |
| Spine foundation-scale datasets | None found | No public spine-specific dataset above 10k 3D volumes was found. The largest pools are TotalSegmentator CT (1.9k), LumbarDISC (8.6k MRI series), RSNA-CSF (3.1k CT) and NHANES II (17k X-rays). |
| OpenSpineConsortium (openspineconsortium.com) | Not verified | Claims "openly licensed spine and pelvis imaging datasets", but names no people, institutions or datasets. Do not use it as a source of truth; pull from the original hosts. |

### 3.18 Not publicly available
- **Genodisc / SpineNet (Oxford).** The Genodisc training MRIs are not public. SpineNet (https://spinenet.readthedocs.io) ships code and weights under terms of access that **prohibit commercial use**. Papers: Jamaludin A, et al. Eur Spine J 2017 [U]; Windsor R, et al. SpineNetV2, arXiv:2205.01683.
- **MIDRC.** It requires registration and a DUA [U]. Spine content beyond possibly CSpineSeg was not confirmed.
- **"LIDC-like" spine sets:** none found. The nearest equivalents are VerSe (multi-reader, public) and LumbarDISC (multi-annotator).

---

## 4. Normative and healthy-anatomy reference data

These are needed to express measurements as deviations from normal (z-scores by level, sex and age).

### 4.1 Healthy-subject imaging datasets (to derive your own norms)
| Source | Use | Status |
|---|---|---|
| **Spine-generic** (Cohen-Adad J, et al. *Open-access quantitative MRI data of the spinal cord and reproducibility across participants, sites and manufacturers.* Scientific Data 8, 2021; DOI 10.1038/s41597-021-00941-8) | 260 healthy participants, 42 sites. Cord CSA, canal and cord shape norms (cervical). CC BY 4.0. | V |
| **Whole-Spine MRI** (OpenNeuro ds005616) | 60 healthy volunteers, 3D T1 whole spine. Vertebral shape atlas. | V (licence U) |
| **Lumbosacral nerve-root MRI** (Sci Data 2024) | 14 healthy adults. Nerve-root and conus anatomy. | Partly V |
| **Cervical spine X-ray atlas** (Sci Data 2024) | Asymptomatic vs symptomatic lateral C-spine. Cervical lordosis and alignment norms. | Partly V |
| **NHANES II X-rays** | Population sample (not selected for disease). Degenerative prevalence by age. | V |
| **TotalSegmentator CT** | Random clinical sample. After excluding pathology, it supports CT vertebral-height norms, as Palm et al. 2025 did. | V |

### 4.2 Published normative values
| Domain | Reference | Key content | Status |
|---|---|---|---|
| Vertebral body heights (CT, AI-derived) | Palm V, …, Wielpütz MO. *AI-based CT assessment of 3117 vertebrae reveals significant sex-specific vertebral height differences.* Scientific Reports 15:20756 (2025). DOI 10.1038/s41598-025-05091-0 | 262 healthy adults (mean age 32). Ha/Hc/Hp for T1–L5 using TotalSegmentator; sex differences up to 9% (T1–T6); wedge and biconcavity indices | V |
| Vertebral height ratios (radiographs) | O'Neill TW, et al. (European Vertebral Osteoporosis Study Group). *Variation in vertebral height ratios in population studies.* J Bone Miner Res 9:1895–1907 (1994). DOI 10.1002/jbmr.5650091209 | T4–L4 anterior/central/posterior ratios; the paper argues for **sex- and population-specific** norms | V (title U) |
| Fracture grading | Genant HK, Wu CY, van Kuijk C, Nevitt MC. *Vertebral fracture assessment using a semiquantitative technique.* J Bone Miner Res 8(9):1137–1148 (1993) | Grade 0–3 thresholds (20–25%, 25–40%, >40% height loss) | U |
| Cervical canal | Ulbrich EJ, et al. *Normative MR cervical spinal canal dimensions.* Radiology 271(1):172–182 (2014). DOI 10.1148/radiol.13120370 | 140 healthy volunteers. Canal and cord dimensions by level, age and sex | V |
| Cervical canal + vertebral bodies (population MRI) | *Reference values for the cervical spinal canal and the vertebral bodies by MRI in a general population.* PLoS ONE (2019), PMC6764695 | General-population MRI norms (believed to be the SHIP cohort) | Partly V (authors/DOI U) |
| Disc degeneration in asymptomatics | Brinjikji W, et al. *Systematic literature review of imaging features of spinal degeneration in asymptomatic populations.* AJNR 36(4):811–816 (2015). DOI 10.3174/ajnr.A4173 | Prevalence by age: disc degeneration 37% at age 20 to 96% at age 80; bulge 30% to 84%; protrusion 29% to 43%; annular fissure 19% to 29% (33 studies, 3,110 people). **Essential for calibrating "abnormal" calls.** | V |
| Disc volume and shape vs age | Pfirrmann CWA, Metzdorf A, Elfering A, Hodler J, Boos N. *Effect of aging and degeneration on disc volume and shape: a quantitative study in asymptomatic volunteers.* J Orthop Res 24(5):1086–1094 (2006). DOI 10.1002/jor.20113 | Disc height and volume norms in asymptomatic volunteers (discs do not simply shrink with age) | V |
| Disc grading scale | Pfirrmann CW, et al. *Magnetic resonance classification of lumbar intervertebral disc degeneration.* Spine 26(17):1873–1878 (2001) | Pfirrmann grades 1–5 (used by SPIDER and LSMA-PQR) | U |
| Endplate marrow | Modic MT, et al. *Degenerative disk disease: assessment of changes in vertebral body marrow with MR imaging.* Radiology 166:193–199 (1988) | Modic types 1–3 | U |
| Stenosis morphology | Schizas C, et al. *Qualitative grading of severity of lumbar spinal stenosis based on the morphology of the dural sac on MRI.* Spine 35(21):1919–1924 (2010) | Grades A–D (used by LSpineSMRI) | U |
| Pelvic incidence | Legaye J, Duval-Beaupère G, Hecquet J, Marty C. *Pelvic incidence: a fundamental pelvic parameter for three-dimensional regulation of spinal sagittal curves.* Eur Spine J 7(2):99–103 (1998). DOI 10.1007/s005860050038 | PI = PT + SS; PI–LL harmony | V (DOI) |
| Spinopelvic norms (adult asymptomatic) | Vialle R, Levassor N, Rillardon L, Templier A, Skalli W, Guigui P. *Radiographic analysis of the sagittal alignment and balance of the spine in asymptomatic subjects.* J Bone Joint Surg Am 87(2):260–267 (2005) | 300 asymptomatic adults: PI ≈ 55° ± 11, PT ≈ 13°, SS ≈ 41°, LL ≈ 61°, TK ≈ 41° (approximate; check the table) | U |
| Sagittal shape types | Roussouly P, et al. *Classification of the normal variation in the sagittal alignment of the human lumbar spine and pelvis in the standing position.* Spine 30(3):346–353 (2005) | Roussouly types 1–4 for normal lordosis variants | U |
| Vertebral geometry (cadaveric) | Panjabi MM, et al. *Human lumbar vertebrae: quantitative three-dimensional anatomy.* Spine 17(3):299–306 (1992); *Thoracic human vertebrae…* Spine 16(8):888–901 (1991). Zhou SH, et al. *Geometrical dimensions of the lower lumbar vertebrae.* Eur Spine J 9:242–248 (2000) | Pedicle, endplate, canal and body dimensions per level | U |
| Opportunistic CT BMD | Pickhardt PJ, et al. *Opportunistic screening for osteoporosis using abdominal computed tomography scans obtained for other indications.* Ann Intern Med 158(8):588–595 (2013) | L1 trabecular HU thresholds (about 160 HU for 90% sensitivity) | U |

**Practical approach:** Build per-level, per-sex, age-binned reference distributions from (a) TotalSegmentator CT plus VerSe, excluding fractured or pathological vertebrae, for CT vertebral heights and wedge indices; (b) SPIDER plus LumbarDISC normal/mild levels for MRI disc height and canal area, adjusting for age with Brinjikji prevalence; (c) spine-generic for cervical cord and canal. Check each against the published values above.

---

## 5. Access checklist (actions)

1. **Zenodo (no login):** SPIDER 10159290; TotalSegmentator CT 6802613 (v3.0.0) and MRI 14710732; CTPelvic1K 4588403; AASCE annotations 4413665; CTSpinoPelvic1K 22139642; Myeloma-SEG ext 21628232.
2. **GitHub / S3:** VerSe (`github.com/anjany/verse`, S3 zips); CTSpine1K (HF `alexanderdann/CTSpine1K`); spine-generic (`git annex get`).
3. **Kaggle (account + accept rules):** `rsna-2024-lumbar-spine-degenerative-classification`, `rsna-2022-cervical-spine-fracture-detection`. Record the rule acceptance date and the non-commercial terms.
4. **Forms:** BUU-LSPINE full set (Google Form), RadImageNet (radimagenet.com), VerSe TUM form (optional).
5. **Credentialed:** PhysioNet account and DUA for VinDr-SpineXR.
6. **Resolve [U] items:** Mendeley licences (open in a browser), CSpineSeg hosting, MRSpineSeg availability, AASCE image source, CTSpinoPelvic1K licence, NHANES II terms.

---

## 6. References

1. van der Graaf JW, van Hooff ML, Buckens CFM, et al., Lessmann N. Lumbar spine segmentation in MR images: a dataset and a public benchmark. *Sci Data* 2024;11:264. doi:10.1038/s41597-024-03090-w. arXiv:2306.12217. Data: doi:10.5281/zenodo.10159290.
2. Richards TJ, Flanders AE, Colak E, et al., Talbott JF. The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset. *Radiol Artif Intell* 2026;8(2). doi:10.1148/ryai.250480. arXiv:2506.09162.
3. Lin HM, Colak E, Richards T, et al. The RSNA Cervical Spine Fracture CT Dataset. *Radiol Artif Intell* 2023;5(5):e230034. doi:10.1148/ryai.230034.
4. Sekuboyina A, et al. VerSe: A Vertebrae labelling and segmentation benchmark for multi-detector CT images. *Med Image Anal* 2021 [vol/pages U]. arXiv:2001.09193.
5. Löffler MT, Sekuboyina A, Jacob A, et al., Kirschke JS. A Vertebral Segmentation Dataset with Fracture Grading. *Radiol Artif Intell* 2020;2(4):e190138. doi:10.1148/ryai.2020190138.
6. Liebl H, et al. A computed tomography vertebral segmentation dataset with anatomical variations and multi-vendor scanner data. *Sci Data* 2021 [details U].
7. Deng Y, Wang C, Hui Y, et al., Zhou SK. CTSpine1K: A Large-Scale Dataset for Spinal Vertebrae Segmentation in Computed Tomography. *MELBA* 2025 (MICCAI Open Data special issue):824–832. arXiv:2105.14711.
8. Wasserthal J, Breit HC, Meyer MT, et al. TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images. *Radiol Artif Intell* 2023. arXiv:2208.05868 [DOI 10.1148/ryai.230024, U].
9. Akinci D'Antonoli T, et al., Wasserthal J. TotalSegmentator MRI: Robust Sequence-independent Segmentation of Multiple Anatomic Structures in MRI. *Radiology* 2025. doi:10.1148/radiol.241613. arXiv:2405.19492.
10. Nguyen HT, Pham HH, Nguyen NT, Nguyen HQ, Huynh TQ, Dao M, Vu V. VinDr-SpineXR: A deep learning framework for spinal lesions detection and classification from radiographs. *MICCAI* 2021. arXiv:2106.12930. Data: PhysioNet vindr-spinexr v1.0.0.
11. Klinwichit P, et al. BUU-LSPINE: A Thai Open Lumbar Spine Dataset for Spondylolisthesis Detection. *Appl Sci* 2023;13(15):8646 [authors/DOI U].
12. Wu H, Bailey C, Rasoulinejad P, Li S. Automatic landmark estimation for adolescent idiopathic scoliosis assessment using BoostNet. *MICCAI* 2017:127–135. doi:10.1007/978-3-319-66182-7_15.
13. Wang L, Xie C, Lin Y, et al., Li S. Evaluation and comparison of accurate automated spinal curvature estimation algorithms with spinal anterior-posterior X-Ray images: The AASCE2019 challenge. *Med Image Anal* 2021;72:102115. doi:10.1016/j.media.2021.102115.
14. Pang S, et al. SpineParseNet: Spine Parsing for Volumetric MR Image by a Two-Stage Segmentation Framework With Semantic Image Representation. *IEEE Trans Med Imaging* 2021 [details U].
15. Sudirman S, Al Kafri A, Natalia F, et al. Lumbar Spine MRI Dataset. *Mendeley Data* v2, 2019. doi:10.17632/k57fr854j2.2.
16. Sudirman S. Lumbar spine MRI annotation with IVD height and Pfirrmann grade predictions (PLOS ONE 2024). *Mendeley Data* v1. doi:10.17632/x6ggzp2ycn.1.
17. LSMA-PQR: Lumbar Spine Multi-view Annotations with Pfirrmann grading, Quantitative measurements and structured Radiological reports. *Mendeley Data* v2, 2026. doi:10.17632/p3r4xd2488.2.
18. LSpineSMRI: A Comprehensive Dataset of Non-Contrast Lumbar Spine Stenosis MRI Examinations. *Mendeley Data* v2, 2025. doi:10.17632/kr8ttxsbb8.2.
19. Medical Spine Sagittal MRI Dataset for Segmentation and Foraminal Stenosis detection. *Sci Data* 2026. doi:10.1038/s41597-026-07138-x. Data: doi:10.17632/rgb77xm3jf.4.
20. Medical Lumbar Spine 3D Axial MRI Dataset for Stenosis Detection, Severity Classification, and Anatomical Segmentation. *Mendeley Data* v1, 2026. doi:10.17632/wjxkrkxhb8.1.
21. Zhou L, Wiggins W, Zhang J, et al., Mazurowski MA, Calabrese E. The Duke University Cervical Spine MRI Segmentation Dataset (CSpineSeg). *Sci Data* 2025;12:1695. doi:10.1038/s41597-025-05975-w.
22. Liu P, Han H, Du Y, et al., Zhou SK. Deep learning to segment pelvic bones: large-scale CT datasets and baseline models. *Int J Comput Assist Radiol Surg* 2021. Data: Zenodo 4588403.
23. Schwing G, et al. CTSpinoPelvic1K: spine, pelvis, ribs and femora in one coordinate frame, annotated for lumbosacral transitional anatomy. arXiv:2609.22760 (2026). Data: doi:10.5281/zenodo.22139642.
24. Nohel M, Valek V, Krejci K, Jakubicek R, Dostal M, Chmelik J. Spinal-Multiple-Myeloma-SEG: A Dual-Energy CT Dataset Extended with Trabecular Bone Segmentation of Lumbar Vertebrae. arXiv:2608.01482 (2026). Data: doi:10.7937/k4qv-hh78; doi:10.5281/zenodo.21628232.
25. Spine-Mets-CT-SEG. *The Cancer Imaging Archive*. doi:10.7937/kh36-ds04. Paper: medRxiv doi:10.1101/2024.10.14.24314447.
26. Cohen-Adad J, et al. Open-access quantitative MRI data of the spinal cord and reproducibility across participants, sites and manufacturers. *Sci Data* 2021;8. doi:10.1038/s41597-021-00941-8.
27. Liu J, Zhang W, Zhou Y, Xu L, Chu YH, Jia F. An open-access lumbosacral spine MRI dataset with enhanced spinal nerve root structure resolution. *Sci Data* 2024;11. doi:10.1038/s41597-024-03919-4.
28. A high-quality dataset featuring classified and annotated cervical spine X-ray atlas. *Sci Data* 2024 (June) [authors/DOI U].
29. Mei X, et al. RadImageNet: An Open Radiologic Deep Learning Research Dataset for Effective Transfer Learning. *Radiol Artif Intell* 2022;e210315. doi:10.1148/ryai.210315.
30. Chen et al. CurvNet / SG-LRA (Spinal-AI2024). arXiv:2411.12604 [authors U].
31. Windsor R, Jamaludin A, Kadir T, Zisserman A. SpineNetV2: Automated Detection, Labelling and Radiological Grading of Clinical MR Scans. arXiv:2205.01683.
32. Vu DN, et al. PhenSPINE: A Standardized Benchmark for Spine Pathology Diagnosis. arXiv:2607.19696 (2026).
33. Zhang B, et al. MSR: Hybrid Field Modeling for CT-MRI Rigid-Deformable Registration of the Cervical Spine with an Annotated Dataset. arXiv:2604.27654 (2026).
34. IMBE-SPINES-DATASET: High resolution CT and MR images of cadaveric spines. University of Leeds. doi:10.5518/1835.
35. Zaim Ahmad MS, Ab Aziz NA, Lim HS, Ghazali AK. Datasets for artificial intelligence-based spine analysis: a scoping review. *JOIV* 2024;8(4):2511. doi:10.62527/joiv.8.4.3042.
36. Palm V, et al., Wielpütz MO. AI-based CT assessment of 3117 vertebrae reveals significant sex-specific vertebral height differences. *Sci Rep* 2025;15:20756. doi:10.1038/s41598-025-05091-0.
37. O'Neill TW, et al. Variation in vertebral height ratios in population studies. *J Bone Miner Res* 1994;9:1895–1907. doi:10.1002/jbmr.5650091209.
38. Ulbrich EJ, Schraner C, Boesch C, et al. Normative MR cervical spinal canal dimensions. *Radiology* 2014;271(1):172–182. doi:10.1148/radiol.13120370.
39. Brinjikji W, Luetmer PH, Comstock B, et al. Systematic literature review of imaging features of spinal degeneration in asymptomatic populations. *AJNR* 2015;36(4):811–816. doi:10.3174/ajnr.A4173.
40. Pfirrmann CWA, Metzdorf A, Elfering A, Hodler J, Boos N. Effect of aging and degeneration on disc volume and shape: a quantitative study in asymptomatic volunteers. *J Orthop Res* 2006;24(5):1086–1094. doi:10.1002/jor.20113.
41. Legaye J, Duval-Beaupère G, Hecquet J, Marty C. Pelvic incidence: a fundamental pelvic parameter for three-dimensional regulation of spinal sagittal curves. *Eur Spine J* 1998;7(2):99–103. doi:10.1007/s005860050038.
42. Vialle R, et al. Radiographic analysis of the sagittal alignment and balance of the spine in asymptomatic subjects. *J Bone Joint Surg Am* 2005;87(2):260–267 [U].
43. Roussouly P, et al. Classification of the normal variation in the sagittal alignment of the human lumbar spine and pelvis in the standing position. *Spine* 2005;30(3):346–353 [U].
44. Genant HK, Wu CY, van Kuijk C, Nevitt MC. Vertebral fracture assessment using a semiquantitative technique. *J Bone Miner Res* 1993;8(9):1137–1148 [U].
45. Pfirrmann CW, Metzdorf A, Zanetti M, Hodler J, Boos N. Magnetic resonance classification of lumbar intervertebral disc degeneration. *Spine* 2001;26(17):1873–1878 [U].
46. Modic MT, Steinberg PM, Ross JS, Masaryk TJ, Carter JR. Degenerative disk disease: assessment of changes in vertebral body marrow with MR imaging. *Radiology* 1988;166:193–199 [U].
47. Schizas C, et al. Qualitative grading of severity of lumbar spinal stenosis based on the morphology of the dural sac on magnetic resonance images. *Spine* 2010;35(21):1919–1924 [U].
48. Panjabi MM, et al. Human lumbar vertebrae: quantitative three-dimensional anatomy. *Spine* 1992;17(3):299–306; Thoracic human vertebrae: quantitative three-dimensional anatomy. *Spine* 1991;16(8):888–901 [U].
49. Zhou SH, et al. Geometrical dimensions of the lower lumbar vertebrae: analysis of data from digitised CT images. *Eur Spine J* 2000;9:242–248 [U].
50. Pickhardt PJ, et al. Opportunistic screening for osteoporosis using abdominal computed tomography scans obtained for other indications. *Ann Intern Med* 2013;158(8):588–595 [U].
51. NHANES II digitized spine X-rays. U.S. National Library of Medicine, LHNCBC. https://data.lhncbc.nlm.nih.gov/public/NHANES/X-rays/README.html

---
*Verification notes:* The Zenodo, Crossref and Mendeley APIs were unreachable from the sandbox, so checks went through web page fetches. Mendeley and Nature article pages did not render licence fields. The web-search budget ran out before the classic grading-scale and spinopelvic references (marked [U]) could be re-checked; their bibliographic details come from memory and are widely cited.
