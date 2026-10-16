# N Scanning: literature reference log

Entries: 296 unique works across 6 topics. Each entry records which reading passes were completed (pass 1 abstract and metadata, pass 2 methods/data/results, pass 3 limitations and reuse). BibTeX for every entry is collected in `references.bib`.

Reading depth: 141 entries read in three passes, 86 in two, 64 in one (abstract or metadata), and 5 logged from prior knowledge and not yet checked online (marked 0/3; verify before citing). Anything marked unverified must be checked before it goes into the paper.

Companion files: `datasets.md` (public spine datasets, licences and access) and `literature_synthesis.md` (state of the art, baselines and research gaps).

## Contents

- 01. Segmentation, localisation and vertebra labelling (47 entries)
- 02. Degenerative disease and clinical grading (49 entries)
- 03. Fractures, bone health and spinal alignment (43 entries)
- 04. Foundation models, architectures and vision-language (49 entries)
- 05. Uncertainty, image quality, abstention and normative anatomy (51 entries)
- 06. Reviews, reporting guidelines, validation and deployment (57 entries)

## 01. Segmentation, localisation and vertebra labelling

#### A. Classic and early deep-learning vertebra localisation / identification (CT)

### R001. Glocker 2012 - Arbitrary field-of-view vertebra localisation
- Full title: Automatic Localization and Identification of Vertebrae in Arbitrary Field-of-View CT Scans
- Authors: Ben Glocker, J. Feulner, Antonio Criminisi et al. (+ D. R. Haynor, E. Konukoglu)
- Year / Venue / Type: 2012 / MICCAI 2012 (LNCS 7512, Part III, pp. 590-598) / conference
- DOI / arXiv / URL: DOI 10.1007/978-3-642-33454-2_73 (VERIFIED via OpenAlex 2026-10-16: pp. 590–598); https://www.microsoft.com/en-us/research/?p=162775
- Access: paywalled (Springer); abstract open on Microsoft Research
- Passes: 1/3 (abstract + key numbers from MSR page; 2026-10-16 DOI/pages verified via OpenAlex and MSR page re-read (200 CT scans, median error <6 mm, id rate 81%). Full text: Springer paywalled; MSR states a corrected PDF exists but no URL was retrievable — not upgraded)
- Modality & anatomy: CT, whole spine (arbitrary FOV)
- Data: 200 CT scans (then the largest reported)
- Method: regression forest for coarse spine detection + generative probabilistic model of shape and appearance (HMM-like chain) for vertebra localisation/identification
- Key results: median localisation error < 6 mm; identification rate 81%
- Code / weights / license: none
- Useful for us: Seminal formulation of "label whatever part of the spine is visible" - our system must handle partial FOV; cite as origin of arbitrary-FOV labelling.
- Limitations / notes: classical features; struggled with pathological spines (motivated the 2013 paper).
- BibTeX:
```bibtex
@inproceedings{Glocker2012ArbitraryFOV,
  title     = {Automatic Localization and Identification of Vertebrae in Arbitrary Field-of-View {CT} Scans},
  author    = {Glocker, Ben and Feulner, Johannes and Criminisi, Antonio and Haynor, David R. and Konukoglu, Ender},
  booktitle = {Medical Image Computing and Computer-Assisted Intervention -- MICCAI 2012},
  series    = {Lecture Notes in Computer Science},
  volume    = {7512},
  pages     = {590--598},
  publisher = {Springer},
  year      = {2012}
}
```

### R002. Glocker 2013 - Dense classification from sparse annotations (CSI2014 spine dataset origin)
- Full title: Vertebrae Localization in Pathological Spine CT via Dense Classification from Sparse Annotations
- Authors: Ben Glocker, Darko Zikic, Ender Konukoglu et al. (+ D. R. Haynor, A. Criminisi)
- Year / Venue / Type: 2013 / MICCAI 2013 (LNCS 8150, Part II, pp. 262-270) / conference
- DOI / arXiv / URL: DOI 10.1007/978-3-642-40763-5_33 (VERIFIED via OpenAlex 2026-10-16: pp. 262–270; authors Glocker, Zikic, Konukoglu, Haynor, Criminisi); https://www.microsoft.com/en-us/research/publication/vertebrae-localization-in-pathological-spine-ct-via-dense-classification-from-sparse-annotations/
- Access: paywalled (Springer); abstract + PDF on MSR page
- Passes: 1/3 (abstract); numeric results taken from secondary comparison tables (Btrfly/DI2IN papers: 74% id-rate, 13.2 mm on the 302-scan split); 2026-10-16 DOI/pages verified via OpenAlex — full text Springer paywalled, not upgraded
- Modality & anatomy: CT, whole spine, pathological (scoliosis, kyphosis, implants)
- Data: 224 pathological spine CTs + 200 mostly abdominal CTs; this data became the public "Spineweb / CSI 2014" 302-scan vertebra-centroid benchmark
- Method: classification forests; sparse centroid annotations converted to dense probabilistic labels; centroid estimation from dense voxel votes
- Key results: (as reported by later papers on the 242/60 split) id-rate 74.0%, mean localisation error 13.2 mm
- Code / weights / license: dataset public via SpineWeb (license unverified)
- Useful for us: Origin of the most-used pre-VerSe benchmark; dense-from-sparse label trick is relevant for weak centroid supervision in our X-ray/MRI data.
- Limitations / notes: classical; inferior to later CNNs.
- BibTeX:
```bibtex
@inproceedings{Glocker2013DenseClassification,
  title     = {Vertebrae Localization in Pathological Spine {CT} via Dense Classification from Sparse Annotations},
  author    = {Glocker, Ben and Zikic, Darko and Konukoglu, Ender and Haynor, David R. and Criminisi, Antonio},
  booktitle = {Medical Image Computing and Computer-Assisted Intervention -- MICCAI 2013},
  series    = {Lecture Notes in Computer Science},
  volume    = {8150},
  pages     = {262--270},
  publisher = {Springer},
  year      = {2013}
}
```

### R003. Chen H. 2015 - J-CNN joint learning for vertebra identification
- Full title: Automatic Localization and Identification of Vertebrae in Spine CT via a Joint Learning Model with Deep Neural Networks
- Authors: Hao Chen, Chiyao Shen, Jing Qin et al. (+ Dong Ni, Lin Shi, Jack C.Y. Cheng, Pheng-Ann Heng)
- Year / Venue / Type: 2015 / MICCAI 2015 (LNCS 9349, pp. 515-522) / conference
- DOI / arXiv / URL: 10.1007/978-3-319-24553-9_63 (verified on PolyU portal)
- Access: paywalled (abstract only)
- Passes: 1/3 (abstract; numbers from comparison table in Btrfly paper) [2026-10-16 round 3: full text paywalled (Springer LNCS / IEEE TMI), no open copy located — left at 1/3]
- Modality & anatomy: CT, whole spine
- Data: MICCAI 2014 CSI vertebra localisation/identification challenge data (Glocker 302 scans)
- Method: random-forest initial centroid candidates -> joint CNN (J-CNN) using vertebra appearance + pairwise neighbour relations to classify vertebra type and reject false detections -> shape regression refinement
- Key results: +10.12% id-rate over prior SOTA; on the 60-scan test split: id-rate 84.2%, mean error 8.8 mm (from Sekuboyina 2018 Table 1)
- Code / weights / license: none
- Useful for us: early example of combining appearance with neighbour-relationship priors for labelling.
- Limitations / notes: multi-stage, hand-crafted refinement.
- BibTeX:
```bibtex
@inproceedings{Chen2015JCNN,
  title     = {Automatic Localization and Identification of Vertebrae in Spine {CT} via a Joint Learning Model with Deep Neural Networks},
  author    = {Chen, Hao and Shen, Chiyao and Qin, Jing and Ni, Dong and Shi, Lin and Cheng, Jack C. Y. and Heng, Pheng-Ann},
  booktitle = {Medical Image Computing and Computer-Assisted Intervention -- MICCAI 2015},
  series    = {Lecture Notes in Computer Science},
  volume    = {9349},
  pages     = {515--522},
  publisher = {Springer},
  year      = {2015},
  doi       = {10.1007/978-3-319-24553-9_63}
}
```

### R004. Yang 2017 - DI2IN with message passing and sparsity regularisation
- Full title: Automatic Vertebra Labeling in Large-Scale 3D CT using Deep Image-to-Image Network with Message Passing and Sparsity Regularization
- Authors: Dong Yang, Tao Xiong, Daguang Xu et al.
- Year / Venue / Type: 2017 / IPMI 2017 (LNCS 10265) / conference
- DOI / arXiv / URL: arXiv:1705.05998; DOI 10.1007/978-3-319-59050-9_50 (from Springer link in search results)
- Access: preprint open
- Passes: 3/3 full text (arXiv PDF)
- Modality & anatomy: CT, whole spine
- Data: public 302-scan Glocker dataset (Set 1: 112/112; Set 2: 242/60) + 1000+ in-house CTs for training only
- Method: 3D encoder-decoder (DI2IN) with deep supervision regressing one Gaussian heatmap per vertebra; message passing along chain graph between neighbouring vertebra heatmaps; L1 sparse shape-dictionary refinement of centroids
- Key results: Set 2: 8.6 mm / 85% id-rate; with +1000 scans: 6.4 mm / 90% id-rate; ~3 s per case on Titan X
- Code / weights / license: not released (Siemens research)
- Useful for us: Demonstrates the value of large training sets for labelling; chain-graph message passing is a lightweight anatomical prior we could reuse.
- Limitations / notes: in-house data not public; high error variance; shape prior assumes regular spine (breaks in scoliosis).
- BibTeX:
```bibtex
@inproceedings{Yang2017DI2IN,
  title     = {Automatic Vertebra Labeling in Large-Scale {3D} {CT} Using Deep Image-to-Image Network with Message Passing and Sparsity Regularization},
  author    = {Yang, Dong and Xiong, Tao and Xu, Daguang and Huang, Qiangui and Liu, David and Zhou, S. Kevin and Xu, Zhoubing and Park, JinHyeong and Chen, Mingqing and Tran, Trac D. and Chin, Sang Peter and Metaxas, Dimitris and Comaniciu, Dorin},
  booktitle = {Information Processing in Medical Imaging (IPMI 2017)},
  series    = {Lecture Notes in Computer Science},
  volume    = {10265},
  pages     = {633--644},
  publisher = {Springer},
  year      = {2017},
  doi       = {10.1007/978-3-319-59050-9_50}
}
```
(Note: full author list and page range from memory/dblp listing; verify before final bibliography.)

### R005. Sekuboyina 2018 - Btrfly Net
- Full title: Btrfly Net: Vertebrae Labelling with Energy-based Adversarial Learning of Local Spine Prior
- Authors: Anjany Sekuboyina, Markus Rempfler, Jan Kukačka et al. (+ G. Tetteh, A. Valentinitsch, J. S. Kirschke, B. H. Menze)
- Year / Venue / Type: 2018 / MICCAI 2018 / conference
- DOI / arXiv / URL: arXiv:1804.01307
- Access: preprint open
- Passes: 3/3 full text (ar5iv)
- Modality & anatomy: CT, whole spine
- Data: 302-scan public dataset (242 train / 60 test); xVertSeg qualitative only
- Method: 2D butterfly network on sagittal + coronal MIPs with fused arms; 25-channel heatmaps; energy-based adversarial prior (3D conv autoencoder discriminator) during training only
- Key results: Btrfly_pe id-rate 86.1%, mean dist 7.4 mm (vs DI2IN* 85.0%/8.6 mm; Chen 84.2%/8.8 mm; Glocker 74%/13.2 mm)
- Code / weights / license: unverified
- Useful for us: Projection-based (2D MIP) labelling is cheap and relevant to radiograph-like views; adversarial anatomical prior idea for plausibility checking.
- Limitations / notes: MIP fails on full-body scans with ribcage occlusion; higher localisation variance.
- BibTeX:
```bibtex
@inproceedings{Sekuboyina2018Btrfly,
  title     = {Btrfly Net: Vertebrae Labelling with Energy-Based Adversarial Learning of Local Spine Prior},
  author    = {Sekuboyina, Anjany and Rempfler, Markus and Kuka{\v{c}}ka, Jan and Tetteh, Giles and Valentinitsch, Alexander and Kirschke, Jan S. and Menze, Bjoern H.},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2018},
  series    = {Lecture Notes in Computer Science},
  volume    = {11073},
  publisher = {Springer},
  year      = {2018},
  eprint    = {1804.01307},
  archivePrefix = {arXiv}
}
```

### R006. Payer 2019 - SpatialConfiguration-Net (SCN)
- Full title: Integrating spatial configuration into heatmap regression based CNNs for landmark localization
- Authors: Christian Payer, Darko Štern, Horst Bischof, Martin Urschler
- Year / Venue / Type: 2019 / Medical Image Analysis 54:207-219 (journal); MIDL 2019 extended abstract (arXiv:1908.00748)
- DOI / arXiv / URL: 10.1016/j.media.2019.03.007; arXiv:1908.00748
- Access: journal paywalled; MIDL abstract open
- Passes: 2/3 (MIDL abstract full text; journal abstract only). Spine CT numbers for SCN are reported in the journal version, which could not be opened (unverified here).
- Modality & anatomy: hand X-ray (895 radiographs, 37 landmarks) in MIDL abstract; journal adds further datasets incl. spine CT (unverified detail)
- Data: see above
- Method: two-component FCN: local-appearance heatmaps (accurate but ambiguous) x spatial-configuration heatmaps (coarse but unambiguous), element-wise product; Gaussian heatmap regression
- Key results: outperforms U-Net/RF baselines especially with few training images (10-100)
- Code / weights / license: Payer's MedicalDataAugmentationTool repositories on GitHub (unverified URL)
- Useful for us: Core building block of VerSe 2019 winner; directly applicable to vertebra landmark detection in X-ray (AASCE) and MRI with small data.
- Limitations / notes: heatmap maxima assume single instance per landmark; transitional vertebrae need extra classes.
- BibTeX:
```bibtex
@article{Payer2019SCN,
  title   = {Integrating Spatial Configuration into Heatmap Regression Based {CNNs} for Landmark Localization},
  author  = {Payer, Christian and {\v{S}}tern, Darko and Bischof, Horst and Urschler, Martin},
  journal = {Medical Image Analysis},
  volume  = {54},
  pages   = {207--219},
  year    = {2019},
  doi     = {10.1016/j.media.2019.03.007}
}
```

### R007. Lessmann 2019 - Iterative FCN with instance memory
- Full title: Iterative fully convolutional neural networks for automatic vertebra segmentation and identification
- Authors: Nikolas Lessmann, Bram van Ginneken, Pim A. de Jong, Ivana Išgum
- Year / Venue / Type: 2019 / Medical Image Analysis 53:142-155 (pages unverified) / journal
- DOI / arXiv / URL: 10.1016/j.media.2019.02.005; arXiv:1804.04383; PubMed 30771712
- Access: preprint open
- Passes: 3/3 full text (ar5iv; last 850 chars unread)
- Modality & anatomy: CT (thoracolumbar, lumbar, low-dose chest NLST, xVertSeg fractures) and T2 MR (vertebral bodies T11-L5)
- Data: CSI2014 thoracolumbar (15), xVertSeg (15), NLST low-dose chest CT (55), lumbar CT (10), lumbar MR (23)
- Method: 3D patch U-Net-like FCN (128^3 @1 mm) with binary instance-memory channel; traverses spine one vertebra at a time; label regression head + max-likelihood label sequence; completeness classifier
- Key results: overall Dice 94.9%, ASSD 0.2 mm, identification 93%, completeness 97%; thoracolumbar CT Dice 96.3%; lumbar CT id 100%
- Code / weights / license: not released with paper (unverified); approach reused as SPIDER IIS baseline (code public there)
- Useful for us: Instance-by-instance traversal handles arbitrary vertebra counts and partial FOV; completeness flag is a direct analogue of our "inconclusive / request better scan" logic.
- Limitations / notes: 4-5 days training; binary memory cannot relabel; MR set only vertebral bodies.
- BibTeX:
```bibtex
@article{Lessmann2019IterativeFCN,
  title   = {Iterative Fully Convolutional Neural Networks for Automatic Vertebra Segmentation and Identification},
  author  = {Lessmann, Nikolas and van Ginneken, Bram and de Jong, Pim A. and I{\v{s}}gum, Ivana},
  journal = {Medical Image Analysis},
  volume  = {53},
  pages   = {142--155},
  year    = {2019},
  doi     = {10.1016/j.media.2019.02.005}
}
```

### R008. Chen Y. 2019/2020 - FCN + Hidden Markov Model labelling
- Full title: Vertebrae Identification and Localization Utilizing Fully Convolutional Networks and a Hidden Markov Model
- Authors: Yizhi Chen, Yunhe Gao, Kang Li et al. (+ Liang Zhao, Jun Zhao)
- Year / Venue / Type: 2020 (online 2019) / IEEE Transactions on Medical Imaging 39(2):387-399 / journal
- DOI / arXiv / URL: 10.1109/TMI.2019.2927289; PMID 31283477
- Access: paywalled (abstract only, via OpenAlex)
- Passes: 1/3 abstract only [2026-10-16 round 3: full text paywalled (Springer LNCS / IEEE TMI), no open copy located — left at 1/3]
- Modality & anatomy: CT, whole spine
- Data: MICCAI 2014 CSI dataset
- Method: spine-level 3D FCN on downscaled input + auxiliary network for local detail; HMM imposes sequential label constraints
- Key results: id-rate 94.67% (within 20 mm), mean id-rate 87.97%, mean localisation error 2.56 mm (test)
- Code / weights / license: none known
- Useful for us: HMM over vertebra sequence = cheap post-hoc consistency layer for our labelling output.
- Limitations / notes: details from abstract only. (This is the "Chen/Zheng" line requested; note also Zheng/ Chen et al. other works not separately verified.)
- BibTeX:
```bibtex
@article{Chen2020FCNHMM,
  title   = {Vertebrae Identification and Localization Utilizing Fully Convolutional Networks and a Hidden {Markov} Model},
  author  = {Chen, Yizhi and Gao, Yunhe and Li, Kang and Zhao, Liang and Zhao, Jun},
  journal = {IEEE Transactions on Medical Imaging},
  volume  = {39},
  number  = {2},
  pages   = {387--399},
  year    = {2020},
  doi     = {10.1109/TMI.2019.2927289}
}
```

#### B. VerSe challenge (CT) and its winners

### R009. Payer 2020 - Coarse-to-fine SCN + U-Net (VerSe 2019 winner)
- Full title: Coarse to Fine Vertebrae Localization and Segmentation with SpatialConfiguration-Net and U-Net
- Authors: Christian Payer, Darko Štern, Horst Bischof, Martin Urschler
- Year / Venue / Type: 2020 / VISAPP 2020 (VISIGRAPP), vol. 5, pp. 124-133 / conference
- DOI / arXiv / URL: DOI 10.5220/0008975201240133 (unverified - recalled); https://www.scitepress.org/Papers/2020/89752/89752.pdf
- Access: open (SciTePress PDF)
- Passes: 3/3 full text
- Modality & anatomy: CT, whole spine (C1-L6)
- Data: VerSe 2019 (80 train, test1 40, test2 40)
- Method: (1) spine-centreline heatmap U-Net at 8 mm; (2) SCN per-vertebra heatmaps at 2 mm, landmark selection by longest anatomically valid sequence (12.5-50 mm spacing); (3) per-vertebra binary U-Net at 1 mm, merged by max response
- Key results: test1 id 95.65%, PE 4.27 mm, Dice 0.909, HD 6.35 mm; test2 id 94.25%, PE 4.80 mm, Dice 0.898
- Code / weights / license: Docker submitted to VerSe; public code in christianpayer/MedicalDataAugmentationTool-VerSe (unverified URL)
- Useful for us: Strong, well-documented three-stage reference pipeline for CT; spacing constraints are reusable plausibility rules.
- Limitations / notes: ~4 min/volume; out-of-distribution failures (legs-only volume); cervical under-represented.
- BibTeX:
```bibtex
@inproceedings{Payer2020CoarseToFine,
  title     = {Coarse to Fine Vertebrae Localization and Segmentation with {SpatialConfiguration-Net} and {U-Net}},
  author    = {Payer, Christian and {\v{S}}tern, Darko and Bischof, Horst and Urschler, Martin},
  booktitle = {Proceedings of the 15th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications (VISIGRAPP 2020) - Volume 5: VISAPP},
  pages     = {124--133},
  publisher = {SciTePress},
  year      = {2020}
}
```

### R010. Sekuboyina 2021 - VerSe benchmark paper
- Full title: VerSe: A Vertebrae labelling and segmentation benchmark for multi-detector CT images
- Authors: Anjany Sekuboyina, Malek E. Husseini, Amirhossein Bayat et al. (~40 authors)
- Year / Venue / Type: 2021 / Medical Image Analysis 73:102166 (volume/article no. from search snippets; OpenAlex confirms journal/year/DOI) / journal + challenge
- DOI / arXiv / URL: 10.1016/j.media.2021.102166; arXiv:2001.09193
- Access: preprint open
- Passes: 3/3 (arXiv abstract, arXiv v4 full PDF via LRDE mirror for methods/results/limitations)
- Modality & anatomy: CT, whole spine
- Data: VerSe'19 + VerSe'20: 374 scans / 355 patients / 4,505 vertebrae; 11 teams (2019) + 13 teams (2020)
- Method: challenge summary; winners: 2019 Payer (SCN pipeline), 2020 Chen D. (DeepReasoningAI: 3D U-Net spine localisation, patch-wise binary U-Net, 3D ResNet-50 vertebra classifier)
- Key results: VerSe'20 best: id-rate 95.61% (public) / 96.58% (hidden), Dice 91.72% / 91.23%
- Code / weights / license: data + evaluation code on GitHub (anjany/verse) and OSF; CC BY-SA 4.0 (per Liebl 2021)
- Useful for us: The reference CT benchmark and metric definitions (id-rate within 20 mm, Dice, HD); documents failure modes (one-label shift, missing L5 anchor, L6/T13 transitional vertebrae) that our "deviation from normal" module must handle.
- Limitations / notes: no inter-rater data; runtime not evaluated; methods drop ~3% cross-iteration.
- BibTeX:
```bibtex
@article{Sekuboyina2021VerSe,
  title   = {{VerSe}: A Vertebrae Labelling and Segmentation Benchmark for Multi-detector {CT} Images},
  author  = {Sekuboyina, Anjany and Husseini, Malek E. and Bayat, Amirhossein and L{\"o}ffler, Maximilian and Liebl, Hans and others},
  journal = {Medical Image Analysis},
  volume  = {73},
  pages   = {102166},
  year    = {2021},
  doi     = {10.1016/j.media.2021.102166}
}
```
- Also relevant to: Fractures, bone health and spinal alignment

### R011. Löffler 2020 - VerSe'19 dataset with fracture grading
- Full title: A Vertebral Segmentation Dataset with Fracture Grading
- Authors: Maximilian T. Löffler, Anjany Sekuboyina, Alina Jacob, Anna-Lena Grau, Andreas Scharr, Malek El Husseini, Mareike Kallweit, Claus Zimmer, Thomas Baum, Jan S. Kirschke (VERIFIED, pubs.rsna.org)
- Year / Venue / Type: 2020 / Radiology: Artificial Intelligence 2(4):e190138 / dataset paper (article CC BY 4.0)
- DOI / arXiv / URL: 10.1148/ryai.2020190138; data https://osf.io/nqjyw/
- Access: open (RSNA)
- Passes: 3/3 (2026-10-16: full text on pubs.rsna.org — data, annotation, fracture grading, BMD, splits, licence, limitations)
- Modality & anatomy: CT, whole spine (220 cervical, 884 thoracic, 621 lumbar vertebrae)
- Data: 160 series / 141 patients / 1,725 vertebrae, TUM, inpatient CT 2013–2017, 5 MDCT scanners (Philips, Siemens), 120 kVp, bone kernel, 0.9–1 mm; age >30 (mean 66.1 ± 15; 49 M / 92 F); 91 patients with >=1 osteoporotic fracture; no bone metastases. Splits: train 80 series (862 vertebrae, with masks/labels), public validation 40 (434), secret test 40 (429); patient-disjoint.
- Method: human–machine hybrid annotation — automated pipeline (FCN spine localisation, Btrfly Net labelling, U-Net patch segmentation, retrained iteratively) -> correction by one of four medical students -> one of two neuroradiologists (ITK-SNAP); metal/cement excluded from masks. Fractures: Genant semiquantitative grading by consensus of two radiologists (5 and 17 y) on thoracolumbar vertebrae — mild 20–<25%, moderate 25–<40%, severe >=40% height loss; wedge/biconcave/crush; Scheuermann/developmental deformities not graded as fractures. Opportunistic lumbar BMD via asynchronous calibration: mean 77.8 ± 53.6 mg/cm³ (F 63.4, M 104.9; fracture 58.7 vs no fracture 115.3).
- Key results: n/a (dataset). Wedge-type and grade-1 fractures predominate (per-grade counts only in supplementary figures).
- Code / weights / license: data CC BY-SA 4.0 (VERIFIED in text); NIfTI images/masks, JSON labels, Excel fracture grades
- Useful for us: Genant semiquantitative grades per vertebra = labels for our fracture/deviation module; BMD metadata for osteoporosis; Genant height-loss thresholds are directly computable from vertebral height measurements.
- Limitations / notes: single centre (TUM); age >30 only; metastases/tumours and many variants excluded; bone kernel only; resolution <=1 mm may be coarse for cervical spine; masks approved by a single rater (no multi-rater variability); CT only.
- BibTeX:
```bibtex
@article{Loffler2020VerSeDataset,
  title   = {A Vertebral Segmentation Dataset with Fracture Grading},
  author  = {L{\"o}ffler, Maximilian T. and Sekuboyina, Anjany and Jacob, Alina and Grau, Anna-Lena and Scharr, Andreas and El Husseini, Malek and Kallweit, Mareike and Zimmer, Claus and Baum, Thomas and Kirschke, Jan S.},
  journal = {Radiology: Artificial Intelligence},
  volume  = {2},
  number  = {4},
  pages   = {e190138},
  year    = {2020},
  doi     = {10.1148/ryai.2020190138}
}
```
- Also relevant to: Fractures, bone health and spinal alignment

### R012. Liebl 2021 - VerSe'20 dataset with anatomical variants
- Full title: A computed tomography vertebral segmentation dataset with anatomical variations and multi-vendor scanner data
- Authors: Hans Liebl, David Schinz, Anjany Sekuboyina et al. (16 authors)
- Year / Venue / Type: 2021 / Scientific Data 8:284 / dataset paper
- DOI / arXiv / URL: 10.1038/s41597-021-01060-0; arXiv:2103.06360
- Access: open
- Passes: 3/3 (arXiv abstract; Springer/Nature full text for validation, limitations, license)
- Modality & anatomy: CT, whole spine
- Data: 300 subjects, 4,142 vertebrae; 4 scanner vendors; 77 enumeration abnormalities, 161 transitional vertebrae (6 T13, 47 L6 in challenge sets)
- Method: semi-automated human-in-the-loop masks, corrected by students, approved by neuroradiologist; variants rated by 2 neuroradiologists
- Key results: VerSe'20 best id-rate 95.6%, localisation error < 2 mm, Dice 91.7%
- Code / weights / license: CC BY-SA 4.0
- Useful for us: Only public CT set with systematically annotated enumeration anomalies/transitional vertebrae - essential for "deviation from normal anatomy" evaluation.
- Limitations / notes: sacrum not segmented; metastases and dislocated fractures excluded; ~1 mm annotation accuracy.
- BibTeX:
```bibtex
@article{Liebl2021VerSe20,
  title   = {A Computed Tomography Vertebral Segmentation Dataset with Anatomical Variations and Multi-Vendor Scanner Data},
  author  = {Liebl, Hans and Schinz, David and Sekuboyina, Anjany and Malagutti, Luca and L{\"o}ffler, Maximilian T. and Bayat, Amirhossein and others},
  journal = {Scientific Data},
  volume  = {8},
  pages   = {284},
  year    = {2021},
  doi     = {10.1038/s41597-021-01060-0}
}
```
- Also relevant to: Fractures, bone health and spinal alignment

#### C. Large CT datasets and whole-body segmenters

### R013. Deng 2021/2024 - CTSpine1K
- Full title: CTSpine1K: A Large-Scale Dataset for Spinal Vertebrae Segmentation in Computed Tomography
- Authors: Yang Deng, Ce Wang, Yuan Hui et al. (incl. S. Kevin Zhou)
- Year / Venue / Type: arXiv 2021; MELBA (MICCAI 2024 special issue) per arXiv v4 / dataset paper
- DOI / arXiv / URL: arXiv:2105.14711; GitHub MIRACLE-Center/CTSpine1K
- Access: preprint open
- Passes: 3/3 full text (arXiv HTML v4)
- Modality & anatomy: CT (colonography, head-neck, liver, COVID chest) - whole spine segments
- Data: 1,005 volumes, 11,172 vertebrae, >500k slices; 25 classes C1-L6; splits 610/197/198 + 41 VerSe cases
- Method: dataset + nnU-Net 3D full-res benchmark
- Key results: vertebra Dice 0.869 (public test), 0.840 (private), 0.619 on VerSe (domain gap); L6 Dice 0
- Code / weights / license: CC BY-NC-SA 4.0 (non-commercial); trained model on GitHub
- Useful for us: Largest public vertebra-level CT set for pretraining; quantifies cross-domain drop - motivates our OOD/"request better scan" logic.
- Limitations / notes: non-commercial license; few pathologies; count discrepancies in paper.
- BibTeX:
```bibtex
@article{Deng2024CTSpine1K,
  title   = {{CTSpine1K}: A Large-Scale Dataset for Spinal Vertebrae Segmentation in Computed Tomography},
  author  = {Deng, Yang and Wang, Ce and Hui, Yuan and Li, Qian and Li, Jun and Luo, Shiwei and Sun, Mengke and Quan, Quan and Yang, Shuxin and Hao, You and Liu, Pengbo and Xiao, Honghu and Zhao, Chunpeng and Wu, Xinbao and Zhou, S. Kevin},
  journal = {Machine Learning for Biomedical Imaging (MELBA)},
  year    = {2024},
  note    = {arXiv:2105.14711; MICCAI 2024 special issue (volume/pages unverified)}
}
```

### R014. Wasserthal 2023 - TotalSegmentator (CT)
- Full title: TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images
- Authors: Jakob Wasserthal, Hanns-Christian Breit, Manfred T. Meyer et al.
- Year / Venue / Type: 2023 / Radiology: Artificial Intelligence 5(5):e230024 (vol/issue unverified) / journal
- DOI / arXiv / URL: 10.1148/ryai.230024; arXiv:2208.05868
- Access: open
- Passes: 3/3 (arXiv abstract + full text supplement details)
- Modality & anatomy: CT whole body incl. 24 vertebrae C1-L5 + sacrum
- Data: 1,204 CTs (Basel, 8 sites, 16 scanners); 104 structures (59 bones); aging study 4,004 CTs
- Method: nnU-Net 1.5 mm (5 sub-models, 4000 epochs, no mirroring) and 3 mm fast model
- Key results: Dice 0.943 overall (1.5 mm), NSD 0.966; external comparison 0.932 vs 0.871; 1-3.5 min per CT on RTX 3090
- Code / weights / license: github.com/wasserth/TotalSegmentator; dataset Zenodo 10.5281/zenodo.6802613 (license: Apache-2.0 code; weights for some tasks need licence - unverified)
- Useful for us: Off-the-shelf CT vertebra masks/labels as a baseline and pseudo-label generator; widely cited.
- Limitations / notes: confuses neighbouring vertebrae/ribs when only partial spine visible; per-vertebra Dice only in supplement JSON.
- BibTeX:
```bibtex
@article{Wasserthal2023TotalSegmentator,
  title   = {{TotalSegmentator}: Robust Segmentation of 104 Anatomic Structures in {CT} Images},
  author  = {Wasserthal, Jakob and Breit, Hanns-Christian and Meyer, Manfred T. and Pradella, Maurice and Hinck, Daniel and Sauter, Alexander W. and Heye, Tobias and Boll, Daniel T. and Cyriac, Joshy and Yang, Shan and Bach, Michael and Segeroth, Martin},
  journal = {Radiology: Artificial Intelligence},
  volume  = {5},
  number  = {5},
  pages   = {e230024},
  year    = {2023},
  doi     = {10.1148/ryai.230024}
}
```
- Also relevant to: Foundation models, architectures and vision-language

### R015. D'Antonoli 2025 - TotalSegmentator MRI
- Full title: TotalSegmentator MRI: Robust Sequence-independent Segmentation of Multiple Anatomic Structures in MRI
- Authors: Tugba Akinci D'Antonoli, Lucas K. Berger, Ashraya K. Indrakanti, Nathan Vishwanathan, Jakob Weiss, Matthias Jung, Zeynep Berkarda, Alexander Rau, Marco Reisert, Thomas Küstner, Alexandra Walter, Elmar M. Merkle, Daniel T. Boll, Hanns-Christian Breit, Andrew Phillip Nicoli, Martin Segeroth, Joshy Cyriac, Shan Yang, Jakob Wasserthal (19 authors, VERIFIED via arXiv PDF + OpenAlex). CORRECTED: the memory-recalled list ("... Sauter A, Bach M, Wasserthal J") was wrong.
- Year / Venue / Type: 2025 (2025-02-01) / Radiology 314(2):e241613 (VERIFIED via OpenAlex) / journal
- DOI / arXiv / URL: 10.1148/radiol.241613; arXiv:2405.19492
- Access: preprint open; journal paywalled
- Passes: 3/3 (2026-10-16: arXiv full PDF — data, classes, annotation, training, metrics, limitations; journal metadata via OpenAlex)
- Modality & anatomy: MRI of any sequence/contrast (T1, T2, PD, ...) + CT; 80 structures. Spine classes: vertebrae as ONE merged class (no per-level labels), intervertebral discs, spinal cord, sacrum; no spinal-canal class.
- Data: 1,143 exams (616 MRI, 527 CT); train 1,088; internal MRI test 55; external AMOS (20) and CHAOS (20); CT test 89 (from TotalSegmentator CT); MRI from University Hospital Basel PACS 2011–2023 + 116 from Imaging Data Commons; 30 scanners, 3 vendors, 4 sites; aging study 8,672 abdominal T1 MRIs. (Paper has internal count inconsistencies: 576 vs 616 vs 561 MRIs.)
- Method: annotation by two radiologists (12 and 7 y) on Nora, bootstrapped from public models (SynthStrip, MRSegmentator) and iterative nnU-Net retraining; nnU-Net 3d_fullres default, 2,000 epochs, mirroring off, "MR" normalisation for all inputs, joint CT+MRI training; 1.5 mm model (80 structures, 6 sub-models) and 3 mm "MRI-3" model (50 structures).
- Key results: internal MRI test Dice/NSD 0.839/0.907 (all 80), 0.862/0.941 (top 50; MRI-3 0.779/0.858); MRI+CT vs MRI-only training 0.862 vs 0.845; vs MRSegmentator 0.759 and AMOS nnU-Net 0.560 (p<.001); external AMOS Dice 0.886, CHAOS 0.890; on CT test 0.966 vs TotalSegmentator CT 0.970. Per-structure spine Dice only in supplementary Fig. S2 / GitHub JSON (not read).
- Code / weights / license: https://github.com/wasserth/TotalSegmentator (licence not stated in paper — check repo); dataset Zenodo record 14710732 (paper also cites 10.5281/zenodo.11367004); web tool totalsegmentator.com
- Useful for us: sequence-agnostic MRI baseline for vertebra/disc/cord masks (useful as a weak pre-segmenter or for ROI cropping); evidence that adding CT to training helps MRI segmentation.
- Limitations / notes: vertebrae NOT separated by level (cannot be used for labelling); mostly body/abdominal MRI; worse on thick slices (>6 mm) and small structures; MRI weaker than CT; retrospective.
- BibTeX:
```bibtex
@article{DAntonoli2025TotalSegMRI,
  title   = {{TotalSegmentator MRI}: Robust Sequence-independent Segmentation of Multiple Anatomic Structures in {MRI}},
  author  = {D'Antonoli, Tugba Akinci and Berger, Lucas K. and Indrakanti, Ashraya K. and Vishwanathan, Nathan and Weiss, Jakob and Jung, Matthias and Berkarda, Zeynep and Rau, Alexander and Reisert, Marco and K{\"u}stner, Thomas and Walter, Alexandra and Merkle, Elmar M. and Boll, Daniel T. and Breit, Hanns-Christian and Nicoli, Andrew Phillip and Segeroth, Martin and Cyriac, Joshy and Yang, Shan and Wasserthal, Jakob},
  journal = {Radiology},
  year    = {2025},
  volume  = {314},
  number  = {2},
  pages   = {e241613},
  doi     = {10.1148/radiol.241613}
}
```
- Also relevant to: Foundation models, architectures and vision-language

#### D. Lumbar spine MRI segmentation (vertebrae, discs, canal)

### R016. van der Graaf 2024 - SPIDER dataset and benchmark
- Full title: Lumbar spine segmentation in MR images: a dataset and a public benchmark
- Authors: Jasper W. van der Graaf, Miranda L. van Hooff, Constantinus F. M. Buckens et al. (incl. N. Lessmann)
- Year / Venue / Type: 2024 / Scientific Data 11 (art. 264, unverified) / dataset + continuous challenge
- DOI / arXiv / URL: 10.1038/s41597-024-03090-w; arXiv:2306.12217; https://spider.grand-challenge.org/
- Access: open
- Passes: 3/3 full text
- Modality & anatomy: lumbar MRI, sagittal T1, T2, T2-SPACE
- Data: 257 studies / 544 series from 4 Dutch hospitals; public 218 patients / 447 series; 3,125 vertebrae, 3,147 IVDs, 447 canals; sequestered test 39 studies / 97 series; per-IVD radiological gradings (Modic, endplate/Schmorl, spondylolisthesis, herniation, narrowing, bulging, Pfirrmann 1-5)
- Method: baselines: Iterative Instance Segmentation (extends Lessmann 2019 to IVD + canal; patches 64x192x192 @2x0.6x0.6 mm) and nnU-Net 3D full-res
- Key results (test Dice): vertebrae 0.93 (IIS) / 0.92 (nnU-Net); IVD 0.84 / 0.86; canal 0.92 / 0.92; detection ~100%
- Code / weights / license: CC-BY 4.0 data (Zenodo 10.5281/zenodo.10159290); SPIDER-Baseline-IIS code + weights; evaluation code
- Useful for us: Primary public lumbar MRI dataset with segmentation AND degenerative gradings - training/eval for our MRI branch and grading heads.
- Limitations / notes: labels are bottom-up counts, not anatomical (LSTV issue); annotation-loop bias; Dutch LBP population only.
- BibTeX:
```bibtex
@article{vanderGraaf2024SPIDER,
  title   = {Lumbar Spine Segmentation in {MR} Images: A Dataset and a Public Benchmark},
  author  = {van der Graaf, Jasper W. and van Hooff, Miranda L. and Buckens, Constantinus F. M. and Rutten, Matthieu and van Susante, Job L. C. and Kroeze, Robert Jan and de Kleuver, Marinus and van Ginneken, Bram and Lessmann, Nikolas},
  journal = {Scientific Data},
  volume  = {11},
  pages   = {264},
  year    = {2024},
  doi     = {10.1038/s41597-024-03090-w}
}
```
(Authors 4-9 and article number recalled; verify.)

### R017. Pang 2021 - SpineParseNet (MRSpineSeg dataset)
- Full title: SpineParseNet: Spine Parsing for Volumetric MR Image by a Two-Stage Segmentation Framework With Semantic Image Representation
- Authors: Shumao Pang, Chunlan Pang, Lei Zhao, Yangfan Chen, Zhihai Su, Yujia Zhou, Meiyan Huang, Wei Yang, Hai Lu, Qianjin Feng (VERIFIED via official GitHub README citation)
- Year / Venue / Type: 2021 (online Sept 2020) / IEEE Transactions on Medical Imaging 40(1):262-273 / journal (VERIFIED via README)
- DOI / arXiv / URL: 10.1109/TMI.2020.3025087; code https://github.com/pangshumao/SpineParseNet (VERIFIED exists; 45 stars); data via https://www.spinesegmentation-challenge.com (MRSpineSeg Challenge, China Society of Image and Graphics)
- Access: paywalled (abstract via OpenAlex); code public
- Passes: 2/3 (2026-10-16: GitHub README; dataset details via Huang et al. arXiv:2203.12151 which uses the same data; TMI full text still not read)
- Modality & anatomy: T2-weighted sagittal lumbar(+lower thoracic) MRI
- Data: 215 volumes (README lists Case1–Case215); 172 training volumes with public masks, 43 test volumes with hidden masks (scored via challenge site). 19 structures: 10 vertebrae (T9–T12, lumbar, sacrum; Huang et al. tables list "L1–L6", i.e. possibly a transitional L6 — check) + 9 discs (T9/T10–L5/S); not all scans contain all structures. In-plane 0.30–0.59 mm, slice spacing 4.40–5.50 mm, 880–990 px matrix, 12–18 sagittal slices (very anisotropic). Source centre/scanner not named in secondary source.
- Method: stage 1: 3D graph-convolutional segmentation network (GCSN) projecting features to a graph whose nodes are spinal structures; stage 2: 2D residual U-Net refinement
- Key results: own paper (abstract): mean Dice 87.32% (vertebrae), 87.78% (IVDs), 87.49% (all 19). On the MRSpineSeg hidden test set as reported by Huang et al. 2022: SpineParseNet overall mean DSC 89.22% (vs their semi-supervised hybrid net 87.91%).
- Code / weights / license: code on GitHub (no licence stated in README); dataset licence not stated
- Useful for us: second public lumbar MRI parsing set (MRSpineSeg, 172 labelled) for external validation of level-wise vertebra/disc segmentation; graph reasoning over the vertebra/disc sequence.
- Limitations / notes: thick sagittal slices (4.4–5.5 mm) limit 3D use; single source (Chinese); hidden test masks; label set includes thoracic levels only down from T9.
- BibTeX:
```bibtex
@article{Pang2021SpineParseNet,
  title   = {{SpineParseNet}: Spine Parsing for Volumetric {MR} Image by a Two-Stage Segmentation Framework With Semantic Image Representation},
  author  = {Pang, Shumao and Pang, Chunlan and Zhao, Lei and Chen, Yangfan and Su, Zhihai and Zhou, Yujia and Huang, Meiyan and Yang, Wei and L{\"u}, Hai and Feng, Qianjin},
  journal = {IEEE Transactions on Medical Imaging},
  volume  = {40},
  number  = {1},
  pages   = {262--273},
  year    = {2021},
  doi     = {10.1109/TMI.2020.3025087}
}
```

### R018. Möller 2024/2025 - SPINEPS whole-spine T2w MRI semantic + instance segmentation
- Full title: SPINEPS: automatic whole spine segmentation of T2-weighted MR images using a two-phase approach to multi-class semantic and instance segmentation (journal title); arXiv title "SPINEPS -- Automatic Whole Spine Segmentation of T2-weighted MR images using a Two-Phase Approach to Multi-class Semantic and Instance Segmentation"
- Authors: Hendrik Möller, Robert Graf, Joachim Schmitt, Benjamin Keinert, Matan Atad, Anjany Sekuboyina, Felix Streckenbach, Hanna Schön, Florian Kofler, Thomas Kroencke, Stefanie Bette, Stefan N. Willich, Thomas Keil, Thoralf Niendorf, Tobias Pischon, Beate Endemann, Bjoern Menze, Daniel Rueckert, Jan S. Kirschke (order VERIFIED from arXiv PDF; earlier entry had Schön before Atad — corrected)
- Year / Venue / Type: 2025 / European Radiology 35:1178–1189 (VERIFIED on SpringerLink; issue no. not shown) / journal, open access CC BY 4.0; preprint arXiv:2402.16368 (2024)
- DOI / arXiv / URL: 10.1007/s00330-024-11155-y; arXiv:2402.16368
- Access: open (journal CC BY 4.0 + preprint)
- Passes: 3/3 (2026-10-16: arXiv PDF full text — data/label generation/architecture/metrics/limitations; SpringerLink journal page — venue, pages, licence, journal-abstract numbers)
- Modality & anatomy: sagittal T2w MRI, whole spine (C2–sacrum; C1 not segmented)
- Data: SPIDER 218 subjects (63% F; lumbar T1w+T2w; test split 39/218 = 18%; three vertebra-subregion labels added with an in-house model); German National Cohort (NAKO) 1,966 subjects of which 1,423 got automated annotations (mean age 53, 49% F; 543 excluded where MR-to-CT translation failed); NAKO test = 11 randomly chosen subjects manually corrected by experts; 15 in-house T2w subjects for qualitative OOD review. NAKO labels built automatically: nnU-Net trained on 180 manual NAKO masks (Streckenbach et al.) for corpus/IVD/canal/sacrum + Spinal Cord Toolbox for cord + diffusion MR-to-CT translation (Graf et al., SEG-19) segmented by Bonescreen SpineR into nine vertebral substructures; merged with endplate relabelling of transition voxels.
- Method: Phase 1 semantic: 3D nnU-Net, patch 256×256×64, 1000 epochs, batch 2, 3-fold ensemble, mirroring disabled (left/right labels), NAKO spacing 0.75×0.75×1.65 mm. 14 labels: corpus, arcus, spinous process, inferior articular L/R, superior articular L/R, costal/transverse process L/R, endplate, IVD, spinal canal, spinal cord, sacrum. Phase 2 instance: 3D U-Net on 248×304×64 cutouts centred on each corpus centre of mass, input = semantic mask only (not image), predicts 3 vertebrae (above/centre/below); overlapping predictions merged by inter-Dice so no vertebra is skipped/merged; IVD/endplate inherit label of vertebra above; post-processing hole filling. Augmentations: scaling, erosion, down/up-sampling, label dropout, vertical crop, horizontal flip.
- Key results: arXiv version, SPIDER test (baseline nnU-Net -> SPINEPS): global vertebra DSC 0.924->0.938, IVD 0.891->0.904, canal 0.922->0.934; instance vertebra DSC 0.907->0.929, RQ 0.953->0.992, SQ 0.856->0.882, PQ 0.819->0.875, ASSD 0.533->0.264 mm; instance IVD DSC 0.873->0.896, PQ 0.77->0.81. NAKO test (automated annotations / GNC-trained / GNC+SPIDER): vertebra 0.855/0.90/0.92, IVD 0.942/0.960/0.967, canal 0.928/0.947/0.958, cord 0.932/0.959/0.966, corpus 0.904/0.942/0.96 (ASSD 0.756/0.341/0.195). Journal abstract (revised numbers): SPIDER instance vertebra Dice 0.933 vs 0.911, ASSD 0.21 vs 0.435 (p<0.001); NAKO-only model avg global Dice 0.918 on NAKO+in-house test; adding SPIDER -> instance substructure Dice 0.778->0.803, global 0.918->0.931. CITE THE JOURNAL NUMBERS.
- Code / weights / license: paper states models and approach are public (footnote link not captured in text); GitHub "Hendrik-code/spineps" still unverified; journal CC BY 4.0. NAKO data access restricted.
- Useful for us: CENTRAL — best open whole-spine T2w MRI segmenter with posterior-element substructures (articular processes -> facet analysis; canal/cord -> stenosis measurements); its semantic-mask-only instance phase is modality-agnostic in principle (CT/X-ray transfer idea).
- Limitations / notes: NAKO is a healthy population cohort (pathology, post-operative spines under-represented); NAKO thick slices (3.3 mm); lateral-most voxels sometimes missed (costal/transverse processes weakest); no C1; T2w sagittal only; NAKO test only 11 subjects; comparison tables vs Li et al./Sáenz-Gamboa not directly comparable; no runtime reported.
- BibTeX:
```bibtex
@article{Moller2025SPINEPS,
  title   = {{SPINEPS}: Automatic Whole Spine Segmentation of {T2}-weighted {MR} Images Using a Two-Phase Approach to Multi-class Semantic and Instance Segmentation},
  author  = {M{\"o}ller, Hendrik and Graf, Robert and Schmitt, Joachim and Keinert, Benjamin and Atad, Matan and Sekuboyina, Anjany and Streckenbach, Felix and Sch{\"o}n, Hanna and Kofler, Florian and Kroencke, Thomas and Bette, Stefanie and Willich, Stefan N. and Keil, Thomas and Niendorf, Thoralf and Pischon, Tobias and Endemann, Beate and Menze, Bjoern and Rueckert, Daniel and Kirschke, Jan S.},
  journal = {European Radiology},
  year    = {2025},
  volume  = {35},
  pages   = {1178--1189},
  doi     = {10.1007/s00330-024-11155-y},
  note    = {arXiv:2402.16368}
}
```

### R019. Graf 2023 - Diffusion MRI-to-CT translation for spinal segmentation
- Full title: Denoising diffusion-based MRI to CT image translation enables automated spinal segmentation
- Authors: Robert Graf, Joachim Schmitt, Sarah Schlaeger et al.
- Year / Venue / Type: 2023 / European Radiology Experimental (DOI 10.1186/s41747-023-00385-2) / journal
- DOI / arXiv / URL: 10.1186/s41747-023-00385-2; arXiv:2308.09345
- Access: open
- Passes: 2/3 (abstract with numbers)
- Modality & anatomy: T1w/T2w MRI -> synthetic CT; lumbar/whole spine
- Data: 263 paired CT/MR series (in-house); external MRSpineSeg volumes
- Method: Pix2Pix, DDIM (image/noise modes), CUT, SynDiff; landmark registration (>=2 landmarks per vertebra); public CT segmenter on synthetic CT
- Key results: 2D Dice 0.77; 3D diffusion/Pix2Pix Dice 0.80; paired beats unpaired
- Code / weights / license: unverified
- Useful for us: Route to transfer CT segmenters (VerSe-trained) to MRI; also a cross-modality idea for our "request a better scan" logic (what CT would show).
- Limitations / notes: needs paired data for best results.
- BibTeX:
```bibtex
@article{Graf2023DiffusionMR2CT,
  title   = {Denoising Diffusion-Based {MRI} to {CT} Image Translation Enables Automated Spinal Segmentation},
  author  = {Graf, Robert and Schmitt, Joachim and Schlaeger, Sarah and M{\"o}ller, Hendrik Kristian and Sideri-Lampretsa, Vasiliki and Sekuboyina, Anjany and Krieg, Sandro Manuel and Wiestler, Benedikt and Menze, Bjoern and Rueckert, Daniel and Kirschke, Jan Stefan},
  journal = {European Radiology Experimental},
  volume  = {7},
  pages   = {70},
  year    = {2023},
  doi     = {10.1186/s41747-023-00385-2}
}
```
(Volume/article number and authors after first three recalled - verify.)

### R020. Graf 2024/2025 - VIBESegmentator (full-body MRI incl. spine)
- Full title: v4 (2025-09-08) PDF title "TotalVibeSegmentator: Full Body MRI Segmentation for the NAKO and UK Biobank"; earlier versions titled "VIBESegmentator: ..." (cite with version)
- Authors: Robert Graf, Paul-Sören Platzek, Evamaria Olga Riedel, Constanze Ramschütz, Sophie Starck, Hendrik Kristian Möller, Matan Atad, Henry Völzke, Robin Bülow, Carsten Oliver Schmidt, Julia Rüdebusch, Matthias Jung, Marco Reisert, Jakob Weiss, Maximilian Löffler, Fabian Bamberg, Bene Wiestler, Johannes C. Paetzold, Daniel Rueckert, Jan Stefan Kirschke (20, VERIFIED arXiv abs)
- Year / Venue / Type: 2024 (v1 2024-05-31; v4 2025-09-08) / arXiv preprint (eess.IV; no journal-ref listed) / preprint
- DOI / arXiv / URL: arXiv:2406.00125
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv abs + v4 full PDF — data, classes, label creation, training, metrics, comparisons, limitations). NOTE: numbers below are from v4 and differ from the earlier-version abstract previously logged (2,897 series/626 subjects; Dice 0.90; AMOS 0.81)
- Modality & anatomy: MRI, 13 contrasts (VIBE water/in/out-of-phase, T2w HASTE, PD, 6-point Dixon, sagittal T2w TSE for spine); torso/whole body. Spine: vertebral bodies and posterior elements as separate classes, IVD, spinal cord, spinal canal; vertebra instances (C3–L5, ~22–25) produced but not evaluated
- Data (v4): training 1,704 series / 158 subjects (NAKO + UK Biobank VIBE + extra NAKO sequences); internal test 12 subjects (6 NAKO, 6 UKBB, 50% F); external: 1,000-image output check, independent NAKO ground truths, AMOS. 71 semantic classes (20 organs, 10 muscles, 19 vessels, 16 bones, 3 body-composition, 3 spinal).
- Method: initial labels from CT TotalSegmentator run on manipulated water images + SPINEPS (vertebrae) + body-composition net; manual correction in ITK-SNAP by three radiologists (2–3 y) supervised by a senior (22 y); iterative nnU-Net train–correct loop; single-contrast input; flipping disabled; heavy elastic deformation; 1.4 mm in-plane, 3 mm slices; post-processing by connected components and volume thresholds
- Key results (v4): internal Dice 0.92 ± 0.04 overall; vertebral body 0.94, IVD 0.90, spinal cord 0.89; AMOS (OOD) 0.76 ± 0.19; on the internal test, TotalSegmentator MRI 0.68 ± 0.17 vs 0.92 ± 0.09 (43 shared structures) and MRSegmentator 0.76 ± 0.11 vs 0.93 ± 0.05 (36 structures), p<0.001 (border definitions differ)
- Code / weights / license: github.com/robert-graf/TotalVibeSegmentator, Apache-2.0 (code + weights); corrected training data not public (on request with NAKO/UKBB access)
- Useful for us: Large-cohort pseudo-label bootstrapping strategy; covers spine on non-spine-dedicated MRI.
- Limitations / notes: not spine-dedicated; few pathologies in training; vertebra instance labels unstable (off-by-one, merged, split) and NOT evaluated; left–right confusion noted; low-contrast/thick-slice (3 mm) data; AMOS lower than some MR models.
- BibTeX:
```bibtex
@misc{Graf2024VIBESegmentator,
  title         = {{VIBESegmentator}: Full Body {MRI} Segmentation for the {NAKO} and {UK Biobank}},
  author        = {Graf, Robert and Platzek, Paul-S{\"o}ren and Riedel, Evamaria Olga and others},
  year          = {2024},
  eprint        = {2406.00125},
  archivePrefix = {arXiv},
  primaryClass  = {eess.IV}
}
```

### R021. Windsor 2020 - Vertebra detection & labelling in whole-spine MRI
- Full title: A Convolutional Approach to Vertebrae Detection and Labelling in Whole Spine MRI
- Authors: Rhydian Windsor, Amir Jamaludin, Timor Kadir, Andrew Zisserman
- Year / Venue / Type: 2020 / MICCAI 2020, LNCS, pp. 712–722 (VERIFIED via OpenAlex) / conference
- DOI / arXiv / URL: 10.1007/978-3-030-59725-2_69 (VERIFIED); arXiv:2007.02606
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — datasets, method, results tables, scoliosis application, limitations; venue/pages/DOI via OpenAlex)
- Modality & anatomy: sagittal MRI (T1, T2, FLAIR, TIRM, STIR); whole, lumbar, cervical, thoracic FOVs; levels C2–S1
- Data: OWS (Oxford whole spine) 710 scans / 196 patients from an orthopaedic PACS, 60/20/20 patient split, S1–C2 corners annotated, levels from one radiologist-labelled scan per patient; test 37 scans / 888 vertebrae. External tests: Genodisc 421 lumbar scans (2,947 vertebrae); Zukić SpineWeb 17 scans (154 vertebrae).
- Method: 2D U-Net per sagittal slice (224×224) -> 13 channels: 5 landmark heatmaps (centroid + 4 corners, weighted L1) + 8 vector-field channels that group corners to centroids; quadrilaterals merged across slices by IoU > 0.5 (~1 s/scan GPU). Labelling: 3D appearance CNN (224×224×16 crops) -> softmax over 24 levels; probability-height map refined by a context FCN (trained with random dropping of detections); beam search enforcing order (no repeats, penalised skips, small penalty for ±1 lumbar variants); temperature scaling T = 10.
- Key results: OWS precision/recall 99.0/98.1%, IDR 96.5% (±1: 97.3%), localisation error 2.4 ± 1.3 mm; Genodisc 99.7/99.7%, IDR 98.4% (vs Lootus 86.9%), LE 1.6 mm; Zukić 99.3/98.7%, IDR 90.9% (±1: 98.7%); LSTM labelling baseline worse (e.g. 90.1% IDR Genodisc). Scoliosis detection on Genodisc (198/3,542 scans positive) from polynomial-fit centroid curvature: AUC 0.636–0.689.
- Code / weights / license: not stated in paper (method later packaged in SpineNetV2, SEG-22)
- Useful for us: FOV-agnostic MRI labelling with explicit handling of lumbar-count variants — matches our need to label cervical/thoracic/lumbar-only scans; corner landmarks reusable for morphometry.
- Limitations / notes: commonest failure S2 detected as S1 shifting all labels by one; worst accuracy at extreme levels (C2, S1); vertebral bodies only (no posterior elements); single-radiologist level labels; scoliosis AUCs modest.
- BibTeX:
```bibtex
@inproceedings{Windsor2020ConvVertebraeMRI,
  title     = {A Convolutional Approach to Vertebrae Detection and Labelling in Whole Spine {MRI}},
  author    = {Windsor, Rhydian and Jamaludin, Amir and Kadir, Timor and Zisserman, Andrew},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2020},
  year      = {2020},
  pages     = {712--722},
  doi       = {10.1007/978-3-030-59725-2_69},
  eprint    = {2007.02606},
  archivePrefix = {arXiv}
}
```
- Also relevant to: Degenerative disease and clinical grading

### R022. Windsor 2022 - SpineNetV2
- Full title: SpineNetV2: Automated Detection, Labelling and Radiological Grading Of Clinical MR Scans
- Authors: Rhydian Windsor, Amir Jamaludin, Timor Kadir, Andrew Zisserman
- Year / Venue / Type: 2022 (dated 5 May 2022) / technical report (arXiv); no journal version mentioned in the report
- DOI / arXiv / URL: arXiv:2205.01683
- Access: preprint open
- Passes: 3/3 (2026-10-16: full PDF text read via arXiv — methods/data/metrics and runtime/limitations extracted; some table cells (canal, foraminal, listhesis, herniation BA) not legible in text extraction)
- Modality & anatomy: clinical sagittal spinal MRI (T1, T2, STIR, TIRM) for detection/labelling (whole spine, S1–C2); lumbar sagittal T2 for grading
- Data: Oxford Whole Spine (OWS) 196 patients, ~710 scans (report says 710 in text, 719 in Fig. 6), S1–C2 corners annotated by a non-specialist — detection/labelling only; Genodisc: 6 international centres, 2,279 patients / 2,819 lumbar sagittal T1+T2 scans, T2 graded by an expert radiologist; patient-level split (stated "80:20:20"); external test Zukić et al. SpineWeb set (17 lumbar scans, 154 vertebrae). Test sizes: OWS 37 scans / 888 vertebrae; Genodisc 421 scans / 2,947 vertebrae.
- Method: detection by "vector field regression" — U-Net predicts 5 keypoint channels (4 vertebral-body corners + centroid) and 8 vector-field grouping channels; per-slice detections grouped into 3D by IoU > 0.25. Labelling: VGG-F appearance network (23-way S1–C3 probability) + U-Net context network refining a probability-height map, decoded by penalised beam search (100 sequences); BiLSTM labelling baseline. Grading: shared ResNet34 (text inconsistently says ResNet32) disc-volume backbone -> 512-d features -> 8 two-layer MLP heads, balanced cross-entropy.
- Key results: detection precision/recall OWS 99.0/98.1%, Zukić 99.3/98.7% (prior 98.7/92.9%), Genodisc precision 99.7%; identification rate OWS 96.5% (±1 level 97.3%), Genodisc 98.4% (99.7%; Lootus baseline 86.9%), Zukić 90.9% (98.7%; prior 87.0%); localisation error ~1.6–2.4 mm. Grading balanced accuracy V1→V2: Pfirrmann (5-class) 71.0→70.9; disc narrowing (4-class) 76.1→76.3; upper/lower endplate defects 82.9→84.9 / 87.8→89.6; upper/lower marrow change 89.2→88.9 / 88.4→88.2; central canal stenosis now 4-class (was binary), foraminal stenosis L/R, spondylolisthesis, herniation binary (values not legible). Only balanced accuracy reported — no kappa. Runtime: lumbar detect+label ~2–3 s GPU / 25 s CPU; whole spine 5 s / 120 s; grading 1 s GPU / 4 s CPU (V1 ~5 min); peak GPU memory 1.6 GB lumbar / 2.5 GB whole spine.
- Code / weights / license: PyTorch; online demo for T2 lumbar scans by request; NO code repository or licence named in the report (a GitHub repo rwindsor1/SpineNetV2 is commonly cited — still unverified). UPDATE 2026-10-16: public software "SpineNet v2.0.0" documented at spinenet.readthedocs.io (©2022 R. Windsor) — detection/labelling (T1/T2/STIR; lumbar, cervical, whole spine) + T2 lumbar grading T12/L1–L5/S1; licence link points to github.com/rwindsor1/SpineNet; terms of access prohibit commercial use (more permissive licence on request); weights downloadable after agreeing to terms.
- Useful for us: end-to-end detect-label-grade reference; corner-keypoint + vector-field grouping is a reusable vertebra detector that also yields landmarks for morphometry (slip, disc height); balanced-accuracy numbers are a baseline for Pfirrmann/endplate/marrow grading.
- Limitations / notes: not peer reviewed; "research tool, not for clinical use"; Modic changes graded only as binary "marrow change" (no type); evaluation limited to balanced accuracy; internal inconsistencies (backbone names, scan counts); detection/labelling validated on small test sets; training data (Genodisc) not public.
- BibTeX:
```bibtex
@misc{Windsor2022SpineNetV2,
  title         = {{SpineNetV2}: Automated Detection, Labelling and Radiological Grading of Clinical {MR} Scans},
  author        = {Windsor, Rhydian and Jamaludin, Amir and Kadir, Timor and Zisserman, Andrew},
  year          = {2022},
  eprint        = {2205.01683},
  archivePrefix = {arXiv},
  primaryClass  = {eess.IV}
}
```
- Also relevant to: Degenerative disease and clinical grading

#### E. Further CT vertebra labelling methods (post-VerSe)

### R023. Meng 2022 - Graph optimisation + anatomic consistency cycle
- Full title: Vertebrae localization, segmentation and identification using a graph optimization and an anatomic consistency cycle
- Authors: Di Meng, Edmond Boyer, Sergi Pujades
- Year / Venue / Type: 2021-2022 / arXiv (v3 June 2022); peer-reviewed version (MLMI 2022 / CMIG) unverified
- DOI / arXiv / URL: arXiv:2110.12177
- Access: preprint open
- Passes: 2/3 (full body text for methods/results; metadata from abs page)
- Modality & anatomy: CT, whole spine
- Data: VerSe 2020
- Method: deep networks for vertebra masks + statistical priors on vertebra volumes and inter-vertebral distances; graph search for sequence labelling; anatomic consistency cycle; handles T13, L6, missing T12
- Key results: VerSe20 public id 96.59%, MLD 2.21 mm, Dice 92.53%; hidden id 95.38%, Dice 91.11%; transitional-vertebra scans Dice 91.04%/89.70% (best among compared); identification 70.5% (single mask) -> 97.36% after graph optimisation
- Code / weights / license: released (URL unverified)
- Useful for us: Explicit modelling of transitional vertebrae + statistical priors = template for our anatomical-deviation checks.
- Limitations / notes: venue unverified.
- BibTeX:
```bibtex
@misc{Meng2022GraphConsistency,
  title         = {Vertebrae Localization, Segmentation and Identification Using a Graph Optimization and an Anatomic Consistency Cycle},
  author        = {Meng, Di and Boyer, Edmond and Pujades, Sergi},
  year          = {2022},
  eprint        = {2110.12177},
  archivePrefix = {arXiv},
  primaryClass  = {eess.IV}
}
```

### R024. Masuzawa 2020 - Cascaded CNNs for arbitrary-FOV CT
- Full title: Automatic Segmentation, Localization, and Identification of Vertebrae in 3D CT Images Using Cascaded Convolutional Neural Networks
- Authors: Naoto Masuzawa, Yoshiro Kitamura, Keigo Nakamura, Satoshi Iizuka, Edgar Simo-Serra (VERIFIED arXiv PDF)
- Year / Venue / Type: 2020 / arXiv preprint — paper states no venue and an OpenAlex search found no peer-reviewed version; the earlier "MICCAI 2020" label is UNSUPPORTED — cite as arXiv
- DOI / arXiv / URL: arXiv:2009.13798
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — data, method, Tables 1–2, limitations; venue search via OpenAlex)
- Modality & anatomy: CT, arbitrary FOV
- Data: training 1,035 CT volumes (head 181, chest 477, abdomen 270, leg 107; multiple vendors; leg scans to suppress false positives); evaluation: CSI 2014 (15 healthy young-adult CTs) for segmentation; Glocker 302-scan pathological set for localisation/identification; reference masks from manual correction of automatic outputs
- Method: stage 1 3D FCN (Roth-style; 1 mm isotropic, 160³ crops, bootstrapped CE on hardest 10% voxels) segments cervical/thoracic/lumbar regions -> bounding boxes; stage 2 iterative instance network (Lessmann-style memory channel, Dice loss) segments one vertebra at a time; labels assigned by counting from the C/T or T/L boundary; centroids from masks
- Key results: CSI 2014 Dice 96.6%, ASSD 0.10 mm, HD 2.11 mm (Janssens 95.7/0.37/4.32; Lessmann 94.9/0.19); 302-scan set mean localisation error 8.3 ± 7.6 mm, identification rate 84% (Glocker 12.4 mm/70%; Yang 9.1/80%; Yang+1000 8.5/83%); by region: cervical 5.7 mm/89%, thoracic 9.3/79%, lumbar 9.8/85%
- Code / weights / license: none known
- Useful for us: region-first then instance-iterative design.
- Limitations / notes: gains over prior work small and on mixed baselines; thoracic weakest; counting-from-boundary labelling propagates errors; no code; not peer reviewed.
- BibTeX:
```bibtex
@misc{Masuzawa2020Cascaded,
  title         = {Automatic Segmentation, Localization, and Identification of Vertebrae in {3D} {CT} Images Using Cascaded Convolutional Neural Networks},
  author        = {Masuzawa, Naoto and Kitamura, Yoshiro and Nakamura, Keigo and Iizuka, Satoshi and Simo-Serra, Edgar},
  year          = {2020},
  eprint        = {2009.13798},
  archivePrefix = {arXiv}
}
```

### R025. McCouat & Glocker 2019 - Two-stage CNN centroid detection with dense annotations
- Full title: Vertebrae Detection and Localization in CT with Two-Stage CNNs and Dense Annotations
- Authors: James McCouat, Ben Glocker
- Year / Venue / Type: 2019 (submitted 2019-10-14, v1 only) / arXiv preprint — no venue, comments or journal-ref on arXiv; the "MICCAI 2019 MSKI workshop" label remains UNVERIFIED
- DOI / arXiv / URL: arXiv:1910.05911
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv abs + full PDF — dense-label construction, architecture, results table, limitations, code)
- Modality & anatomy: CT
- Data: Glocker/BioMedia public spine CT set — 242 train / 60 test pathological, arbitrary-FOV scans, resampled 1 mm isotropic
- Method: sparse centroids -> dense labels as discs around line segments between adjacent centroid midpoints (radii from Busscher et al. vertebra dimensions). Stage 1 3D U-Net (64×64×80 patches, weighted CE 0.1/0.9) segments vertebra vs background (val Dice 0.961); stage 2 2D U-Net on 8-slice stacks (8×80×320) with large 5×20 bottleneck kernels regresses a continuous level value per pixel (masked L1) capturing ordering; outputs multiplied, centroid = median of voting pixels (threshold max(3000, 0.4R³))
- Key results (60 test scans): all — id rate 85.8%, mean error 5.60 ± 7.10 mm (Liao 88.3% / 6.47 mm; Chen 84.2% / 8.82 mm); cervical 90.6% / 3.93 mm; thoracic 79.8% / 6.61 mm; lumbar 92.0% / 5.39 mm. Best localisation error but lower id rate than Liao et al. ~40 s/scan inference (K80).
- Code / weights / license: GitHub jfm15/SpineFinder (licence not stated in paper)
- Useful for us: dense-from-sparse label generation for centroid-only datasets.
- Limitations / notes: lower identification rate than Liao et al. (no explicit level classification); thoracic weakest (worst scan 17.6 mm); T6/T7 under-represented; random cropping; not peer reviewed.
- BibTeX:
```bibtex
@misc{McCouat2019TwoStage,
  title         = {Vertebrae Detection and Localization in {CT} with Two-Stage {CNNs} and Dense Annotations},
  author        = {McCouat, James and Glocker, Ben},
  year          = {2019},
  eprint        = {1910.05911},
  archivePrefix = {arXiv}
}
```

#### F. X-ray vertebra landmarks, detection and segmentation

### R026. Wang 2021 - AASCE 2019 challenge (Cobb angle from AP X-ray)
- Full title: Evaluation and comparison of accurate automated spinal curvature estimation algorithms with spinal anterior-posterior X-Ray images: The AASCE2019 challenge
- Authors: Liansheng Wang, Cong Xie, Yi Lin et al. (17 authors; incl. Hong-Yu Zhou, Kailin Chen)
- Year / Venue / Type: 2021 / Medical Image Analysis 72:102115 / challenge paper
- DOI / arXiv / URL: 10.1016/j.media.2021.102115; PMID 34134084
- Access: paywalled (metadata only; abstract not retrievable here)
- Passes: 0.5/3 (metadata only; abstract not accessible)
- Modality & anatomy: AP spinal radiographs (thoracic + lumbar, 17 vertebrae, 68 corner landmarks per image per the SpineWeb dataset 16 - unverified)
- Data: AASCE / SpineWeb dataset 16 (609 AP X-rays from Wu et al. 2017 - unverified)
- Method: challenge comparison of Cobb-angle estimation algorithms (landmark, segmentation and direct-regression approaches)
- Key results: unverified (SMAPE-based ranking)
- Code / weights / license: dataset via SpineWeb (license unverified)
- Useful for us: Standard benchmark for X-ray vertebra corner landmarks and Cobb angle - our X-ray branch's deviation metric.
- Limitations / notes: need full text before citing numbers.
- BibTeX:
```bibtex
@article{Wang2021AASCE,
  title   = {Evaluation and Comparison of Accurate Automated Spinal Curvature Estimation Algorithms with Spinal Anterior-Posterior {X}-Ray Images: The {AASCE2019} Challenge},
  author  = {Wang, Liansheng and Xie, Cong and Lin, Yi and Zhou, Hong-Yu and Chen, Kailin and others},
  journal = {Medical Image Analysis},
  volume  = {72},
  pages   = {102115},
  year    = {2021},
  doi     = {10.1016/j.media.2021.102115}
}
```
- Also relevant to: Fractures, bone health and spinal alignment

### R027. Yi 2020 - Vertebra-focused landmark detection for scoliosis
- Full title: Vertebra-Focused Landmark Detection for Scoliosis Assessment
- Authors: Jingru Yi, Pengxiang Wu, Qiaoying Huang, Hui Qu, Dimitris N. Metaxas (VERIFIED)
- Year / Venue / Type: 2020 / IEEE ISBI 2020, pp. 736–740 (VERIFIED via OpenAlex) / conference
- DOI / arXiv / URL: 10.1109/ISBI45749.2020.9098675 (VERIFIED); arXiv:2001.03187; code https://github.com/yijingru/Vertebra-Landmark-Detection
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — data, method, results, failure cases; venue via OpenAlex)
- Modality & anatomy: AP spinal X-ray (AASCE data)
- Data: AASCE MICCAI 2019 challenge training set — 580 AP spinal radiographs (~2500×1000 px), split 348/116/116; 17 thoracolumbar vertebrae × 4 corners = 68 landmarks per image (clinician-annotated)
- Method: CenterNet-style — ResNet34 (ImageNet) encoder–decoder, input 1024×512, output 256×128; vertebra-centre heatmap (focal loss), centre sub-pixel offset (L1) and 4 corner offset vectors from each centre (L1), which preserves landmark order; Adam 2.5e-4, 100 epochs
- Key results (test): Cobb-angle SMAPE 10.81 (PT 6.26, MT 18.04, TL 23.42) vs segmentation-based 16.48 and regression-based 23.43; mean landmark error 50.11 (units not stated) vs 74.07/77.94; 5.65 FPS on K40
- Code / weights / license: GitHub yijingru/Vertebra-Landmark-Detection (licence not stated in paper)
- Useful for us: Simple, open, order-preserving vertebra corner detector; corners give endplate angles, wedge ratios and listhesis distances.
- Limitations / notes: single dataset (580 images, AP only); can skip a vertebra whose appearance is less distinct; landmark-error units unspecified.
- BibTeX:
```bibtex
@inproceedings{Yi2020VertebraFocused,
  title     = {Vertebra-Focused Landmark Detection for Scoliosis Assessment},
  author    = {Yi, Jingru and Wu, Pengxiang and Huang, Qiaoying and Qu, Hui and Metaxas, Dimitris N.},
  booktitle = {IEEE 17th International Symposium on Biomedical Imaging (ISBI)},
  year      = {2020},
  pages     = {736--740},
  doi       = {10.1109/ISBI45749.2020.9098675},
  eprint    = {2001.03187},
  archivePrefix = {arXiv}
}
```

### R028. Klinwichit 2023 - BUU-LSPINE lumbar X-ray dataset
- Full title: BUU-LSPINE: A Thai Open Lumbar Spine Dataset for Spondylolisthesis Detection
- Authors: Podchara Klinwichit, Watcharaphong Yookwan, Sornsupha Limchareon, Krisana Chinnasarn, Jun-Su Jang, Athita Onuean (VERIFIED, MDPI page)
- Year / Venue / Type: 2023 / Applied Sciences 13(15):8646 / dataset paper (article CC BY)
- DOI / arXiv / URL: 10.3390/app13158646; dataset https://services.informatics.buu.ac.th/spine/
- Access: open (MDPI)
- Passes: 3/3 (2026-10-16: MDPI full text — data, annotation scheme, splits, methods/metrics, limitations)
- Modality & anatomy: lumbar radiographs, AP + lateral (LA)
- Data: 3,600 patients × (AP + LA) = 7,200 JPG images + CSV ground truth, Burapha University Hospital (Thailand); sex/age kept; 621 spondylolisthesis cases; exclusions: low quality/noise, devices over lumbar region, missing or highly damaged vertebrae; LA views flipped to face left. Pixel spacing included in data (values not given in paper); collection years not reported.
- Annotation: radiologists and orthopaedic doctors (KIOM, BUU) + review by CV experts and a consensus meeting; number of annotators and inter-annotator agreement NOT reported. Each vertebral endplate = a 2-point line (upper "a", lower "b"): AP 10 lines (L1–L5), LA 11 lines (+S1a). Per-level listhesis label 0–4 on lower endplate line (Meyerding-based; anterolisthesis, retrolisthesis, lateral listhesis); LSTV (sacralisation / lumbarisation) recorded on S1a row.
- Method: 11 detectors compared (YOLOv5 best, 640×640) for vertebra boxes; 11 CNN regressors for corner points (ResNet152V2 best on AP, DenseNet201 on LA); 3 classifiers for listhesis on adjacent-vertebra pairs (SVM best), with under-sampling to smallest class; 80/20 splits.
- Key results: YOLOv5 precision 81.93% (AP) / 83.45% (LA), recall 95.82% / 95.72%; corner error 4.63 mm AP (8.83% of 52.45 mm mean width) / 4.91 mm LA (12.11% of 40.54 mm); listhesis accuracy 95.14% (AP) / 92.26% (LA).
- Code / weights / license: dataset downloadable from BUU site (dataset-specific licence not stated; article CC BY); code not stated
- Useful for us: CENTRAL for the X-ray branch — largest open lumbar radiograph set with endplate corner landmarks, per-level listhesis grades and LSTV labels; corner points let us compute Meyerding slip % directly.
- Limitations / notes: single hospital; no annotator agreement; corner errors (~5 mm, 9–12% of width) are large relative to 25% Meyerding bands; model assumes 5 lumbar vertebrae (LSTV causes labelling errors); heavy under-sampling for listhesis classes.
- BibTeX:
```bibtex
@article{Klinwichit2023BUULSPINE,
  title   = {{BUU-LSPINE}: A Thai Open Lumbar Spine Dataset for Spondylolisthesis Detection},
  author  = {Klinwichit, Podchara and Yookwan, Watcharaphong and Limchareon, Sornsupha and Chinnasarn, Krisana and Jang, Jun-Su and Onuean, Athita},
  journal = {Applied Sciences},
  volume  = {13},
  number  = {15},
  pages   = {8646},
  year    = {2023},
  doi     = {10.3390/app13158646}
}
```
- Also relevant to: Fractures, bone health and spinal alignment

### R029. Nguyen 2021 - VinDr-SpineXR
- Full title: VinDr-SpineXR: A deep learning framework for spinal lesions detection and classification from radiographs
- Authors: Hieu T. Nguyen, Hieu H. Pham, Nghia T. Nguyen, Ha Q. Nguyen, Thang Q. Huynh, Minh Dao, Van Vu (VERIFIED, arXiv PDF)
- Year / Venue / Type: 2021 / MICCAI 2021, LNCS (Springer), pp. 291–301 (VERIFIED via OpenAlex) / conference + dataset
- DOI / arXiv / URL: 10.1007/978-3-030-87240-3_28 (VERIFIED); arXiv:2106.12930; dataset https://vindr.ai/datasets/spinexr ; code https://github.com/vinbigdata-medical/vindr-spinexr
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — data, labels, methods, per-lesion AP, limitations; venue/pages via OpenAlex)
- Modality & anatomy: spine radiographs (cervical/thoracic/lumbar; view types not stated)
- Data: 10,468 images / 5,000 studies (one section says 10,469) from several Vietnamese primary hospitals' PACS, 2010/2011–2020; dev 4,000 studies (8,390 images), test 1,000 studies (2,078 images), stratified study-level split; ~62% female. Each image annotated by ONE of three radiologists (>10 y). 13 box categories (counts): osteophytes 15,562; disc space narrowing 1,155; surgical implant 536; foraminal stenosis 482; spondylolisthesis 349; vertebral collapse 337; other lesions 311; subchondral sclerosis 110; enthesophytes 67; sclerotic lesion 29; foreign body 21; fracture 12; ankylosis 7.
- Method: abnormal/normal classifier = ensemble of DenseNet-121/169/201 (Youden threshold 0.2808); detectors Faster R-CNN, RetinaNet, EfficientDet, Sparse R-CNN for 7 lesion classes (osteophytes, disc space narrowing, implant, foraminal stenosis, spondylolisthesis, vertebral collapse, other); fusion rule keeps all boxes if classifier positive, else only boxes >0.5.
- Key results: classifier AUROC 88.61% (95% CI 87.19–90.02), sensitivity 83.07%, specificity 79.32%, F1 81.06%; best single detector Sparse R-CNN mAP@0.5 33.15; whole framework 33.56. Per-lesion AP (framework): implant ~62.5 highest, "other lesions" ~4.2 lowest.
- Code / weights / license: dataset via vindr.ai (also widely mirrored on PhysioNet — not confirmed in paper; licence not stated in paper); code on GitHub
- Useful for us: large open X-ray set with lesion boxes (osteophytes, listhesis, disc space narrowing, foraminal stenosis); low mAP shows difficulty — motivates uncertainty/abstention.
- Limitations / notes: single reader per image, no agreement statistics; extreme class imbalance (rare classes merged); boxes only — no vertebra-level labels or landmarks; modest detection performance; demographics/scanners not analysed.
- BibTeX:
```bibtex
@inproceedings{Nguyen2021VinDrSpineXR,
  title     = {{VinDr-SpineXR}: A Deep Learning Framework for Spinal Lesions Detection and Classification from Radiographs},
  author    = {Nguyen, Hieu T. and Pham, Hieu H. and Nguyen, Nghia T. and Nguyen, Ha Q. and Huynh, Thang Q. and Dao, Minh and Vu, Van},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2021},
  series    = {Lecture Notes in Computer Science},
  publisher = {Springer},
  pages     = {291--301},
  year      = {2021},
  doi       = {10.1007/978-3-030-87240-3_28},
  eprint    = {2106.12930},
  archivePrefix = {arXiv}
}
```

#### G. Cervical spine

### R030. Lin 2023 - RSNA Cervical Spine Fracture CT dataset
- Full title: The RSNA Cervical Spine Fracture CT Dataset
- Authors: Hui Ming Lin, Errol Colak, Tyler Richards et al. (19+ authors)
- Year / Venue / Type: 2023 / Radiology: Artificial Intelligence 5(5) (e230034) / dataset paper
- DOI / arXiv / URL: 10.1148/ryai.230034
- Access: open (RSNA)
- Passes: 2/3 (RSNA page summary + key points)
- Modality & anatomy: cervical spine CT (C1-C7, some thoracic)
- Data: 3,112 CTs from 12 institutions / 9 countries; 1,445 fracture-positive; study-level C1-C7 fracture labels; 235 with fracture boxes; subset with vertebral segmentation masks (labels 1-7 C1-C7, 8-19 thoracic); Kaggle split 2,019/304/789
- Method: dataset for RSNA 2022 Kaggle challenge
- Key results: n/a
- Code / weights / license: free for non-commercial research (Kaggle)
- Useful for us: Multi-centre cervical CT with vertebra masks + fracture labels - fills the cervical gap of VerSe.
- Limitations / notes: masks only on a subset.
- BibTeX:
```bibtex
@article{Lin2023RSNACSpine,
  title   = {The {RSNA} Cervical Spine Fracture {CT} Dataset},
  author  = {Lin, Hui Ming and Colak, Errol and Richards, Tyler and others},
  journal = {Radiology: Artificial Intelligence},
  volume  = {5},
  number  = {5},
  pages   = {e230034},
  year    = {2023},
  doi     = {10.1148/ryai.230034}
}
```
- Also relevant to: Fractures, bone health and spinal alignment

#### H. General 3D segmentation backbones (used for spine)

### R031. Isensee 2021 - nnU-Net
- Full title: nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation (journal); preprint title "Automated Design of Deep Learning Methods for Biomedical Image Segmentation" (arXiv:1904.08128)
- Authors: Fabian Isensee, Paul F. Jaeger, Simon A. A. Kohl, Jens Petersen, Klaus H. Maier-Hein (VERIFIED arXiv abs)
- Year / Venue / Type: 2021 (online Dec 2020) / Nature Methods 18(2):203-211 / journal
- DOI / arXiv / URL: 10.1038/s41592-020-01008-z; journal preprint arXiv:1904.08128 (v1 2019-04-17, v2 2020-04-02); earlier MSD preprint arXiv:1809.10486
- Access: paywalled journal; preprint open
- Passes: 3/3 (2026-10-16: arXiv:1904.08128v2 abstract + full PDF — design framework, configurations, training recipe, results, limitations)
- Modality & anatomy: generic; 19 datasets / 49 tasks from 10 challenges (brain, heart, liver, kidney, prostate, lung, pancreas, abdominal organs, MS lesions, EM, etc.) — NO spine dataset in the paper
- Data: MSD + KiTS19, ACDC, LiTS, BCV, SegTHOR, CHAOS, ISBI MS, CREMI, etc.
- Method: "dataset fingerprint" -> rule-based pipeline: fixed (plain U-Net template, conv–instance norm–leaky ReLU, Dice+CE loss with deep supervision, SGD Nesterov 0.99, lr 0.01 poly 0.9, 1000 epochs × 250 minibatches, fixed augmentation, 33.3% foreground oversampling); rule-based (target spacing, patch/batch size, topology, normalisation, cascade trigger when full-res patch <12.5% of median image); empirical (choice/ensemble of 2D, 3D full-res, 3D cascade via 5-fold CV; non-largest-component suppression post-processing).
- Key results: new SOTA in 29 of 49 tasks, otherwise close to top; ablations show the default configuration ranks first aggregated across 10 datasets; architectural variants matter less than configuration (KiTS19 top-15 all U-Net-like).
- Code / weights / license: github.com/MIC-DKFZ/nnUNet (Apache-2.0)
- Useful for us: default backbone and training recipe; used by TotalSegmentator, CTSpine1K, SPIDER, SPINEPS, TotalSpineSeg baselines; mirroring augmentation must be disabled for left/right spine labels (as SPINEPS and TotalSegmentator MRI did).
- Limitations / notes: Dice-centred design may not suit tasks needing other metrics (e.g. instance/labelling accuracy for vertebrae); heuristics derived from 10 datasets; dataset properties outside the fingerprint can give suboptimal results (e.g. CREMI rank 6/39).
- BibTeX:
```bibtex
@article{Isensee2021nnUNet,
  title   = {{nnU-Net}: A Self-Configuring Method for Deep Learning-Based Biomedical Image Segmentation},
  author  = {Isensee, Fabian and Jaeger, Paul F. and Kohl, Simon A. A. and Petersen, Jens and Maier-Hein, Klaus H.},
  journal = {Nature Methods},
  volume  = {18},
  number  = {2},
  pages   = {203--211},
  year    = {2021},
  doi     = {10.1038/s41592-020-01008-z}
}
```
- Also relevant to: Foundation models, architectures and vision-language

### R032. Isensee 2024 - nnU-Net Revisited
- Full title: nnU-Net Revisited: A Call for Rigorous Validation in 3D Medical Image Segmentation
- Authors: Fabian Isensee, Tassilo Wald, Constantin Ulrich et al.
- Year / Venue / Type: 2024 / MICCAI 2024 (LNCS) per common citation (arXiv lists no journal-ref; venue unverified) / conference
- DOI / arXiv / URL: arXiv:2404.09556
- Access: preprint open
- Passes: 3/3 (abstract, full HTML tables, limitations)
- Modality & anatomy: generic CT/MRI (no spine dataset)
- Data: BTCV, ACDC, LiTS, BraTS2021, KiTS2023, AMOS2022; 5-fold CV
- Method: fair benchmark of CNN (nnU-Net, ResEnc M/L/XL, MedNeXt, STU-Net), Transformer (SwinUNETR, nnFormer, CoTr), Mamba (U-Mamba) and Auto3DSeg on A100-40GB
- Key results: ResEnc L avg ~87.6 Dice; MedNeXt L k5 ~88.2 (but 233 h training); SwinUNETR ~83.7; U-Mamba gains vanish vs No-Mamba ablation
- Code / weights / license: nnU-Net ResEnc presets (Apache-2.0)
- Useful for us: Justifies choosing nnU-Net ResEnc (M/L) as our segmentation backbone and warns against unvalidated architecture claims - cite in methods.
- Limitations / notes: from-scratch, limited-size datasets; pretraining not fully explored.
- BibTeX:
```bibtex
@inproceedings{Isensee2024nnUNetRevisited,
  title     = {{nnU-Net} Revisited: A Call for Rigorous Validation in {3D} Medical Image Segmentation},
  author    = {Isensee, Fabian and Wald, Tassilo and Ulrich, Constantin and Baumgartner, Michael and Roy, Saikat and Maier-Hein, Klaus and J{\"a}ger, Paul F.},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2024},
  year      = {2024},
  eprint    = {2404.09556},
  archivePrefix = {arXiv}
}
```

### R033. Roy 2023 - MedNeXt
- Full title: MedNeXt: Transformer-driven Scaling of ConvNets for Medical Image Segmentation
- Authors: Saikat Roy, Gregor Koehler, Constantin Ulrich, Michael Baumgartner, Jens Petersen, Fabian Isensee, Paul F. Jaeger, Klaus Maier-Hein (VERIFIED arXiv abs)
- Year / Venue / Type: 2023 / MICCAI 2023 (venue confirmed on first author's publication page; LNCS volume/pages/DOI still unverified) / conference
- DOI / arXiv / URL: arXiv:2303.09975 (v1 2023-03-17; v5 2024-06-02)
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv abs + full PDF v5 — datasets/training/model sizes/all result tables and constraints; venue via author page; earlier pass used nnU-Net Revisited benchmark)
- Modality & anatomy: generic 3D CT/MRI (abdomen organs, kidney tumour, brain tumour) — no spine task
- Data: BTCV (CT, 30 cases, 13 classes; text inconsistently says 18), AMOS22 (CT, 200, 15 classes), KiTS19 (CT, 210, 2 classes), BraTS21 (MRI, 1,251, 3 classes); 5-fold CV 80:20 + public leaderboards for test
- Method: fully convolutional ConvNeXt-style 3D encoder-decoder inside the nnU-Net framework (same schedule/augmentation/inference): depthwise conv + expansion + GELU + GroupNorm blocks, residual ConvNeXt up/down-sampling blocks, UpKern (initialise k5 network by trilinearly upsampling k3 kernels), compound scaling of depth/width/kernel. Sizes (k3/k5 at 128³): S 5.6/5.9 M params, B 10.5/11.0, M 17.6/18.3, L 61.8/63.0 M (500/564 GFLOPs). 1000 epochs × 250 batches, patch 128³, batch 2, AdamW lr 1e-3, 1.0 mm isotropic resampling, AMP + gradient checkpointing.
- Key results: 5-fold CV average DSC/SDC: nnU-Net 88.39/88.78; SwinUNETR 86.41/86.08; UNETR 82.36/81.00; MedNeXt-S k3 88.66, B k3 88.87, M k5 89.09, L k5 89.22/89.85. Per-dataset DSC MedNeXt-L k5 vs nnU-Net: BTCV 84.82 vs 83.56, AMOS22 89.87 vs 88.88, KiTS19 90.71 vs 89.88, BraTS21 91.46 vs 91.23 (gains small on tumour tasks). Leaderboards (L k5 ensemble): AMOS22 DSC 91.77 (rank 1 on 2023-03-09), BTCV 88.76, KiTS19 91.02, BraTS21 88.01. Ablation: UpKern k5 84.23 vs from-scratch k5 84.03 vs k3 trained 2× 84.00 (BTCV). Independent benchmark (nnU-Net Revisited, SEG-32): top average Dice 88.16 (k5).
- Code / weights / license: https://github.com/MIC-DKFZ/MedNeXt (licence not stated in paper — check repo); also integrated in nnU-Net ecosystem
- Useful for us: strongest CNN alternative to default nnU-Net for spine CT/MRI segmentation if compute allows; UpKern trick reusable for large-kernel models.
- Limitations / notes: no spine dataset evaluated; margins over nnU-Net are small (~0.5–1 DSC) and largest for organ tasks; large kernels need UpKern; k5 ~3× slower per epoch (e.g. S: 117 vs 364 s/epoch); training needs AMP + checkpointing; internal inconsistency in BTCV count.
- BibTeX:
```bibtex
@inproceedings{Roy2023MedNeXt,
  title     = {{MedNeXt}: Transformer-Driven Scaling of {ConvNets} for Medical Image Segmentation},
  author    = {Roy, Saikat and Koehler, Gregor and Ulrich, Constantin and Baumgartner, Michael and Petersen, Jens and Isensee, Fabian and J{\"a}ger, Paul F. and Maier-Hein, Klaus H.},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2023},
  year      = {2023},
  eprint    = {2303.09975},
  archivePrefix = {arXiv}
}
```

### R034. Huang 2023 - STU-Net
- Full title: STU-Net: Scalable and Transferable Medical Image Segmentation Models Empowered by Large-Scale Supervised Pre-training
- Authors: Ziyan Huang, Haoyu Wang, Zhongying Deng, Jin Ye, Yanzhou Su, Hui Sun, Junjun He, Yun Gu, Lixu Gu, Shaoting Zhang, Yu Qiao (VERIFIED, arXiv PDF)
- Year / Venue / Type: 2023 (v1 2023-04-13) / arXiv preprint (no peer-reviewed venue stated)
- DOI / arXiv / URL: arXiv:2304.06716
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — model sizes, pretraining data, downstream tables, vertebra-specific results, compute; earlier pass used nnU-Net Revisited numbers)
- Modality & anatomy: generic; pretrained on TotalSegmentator (includes all vertebrae)
- Data: pretraining on TotalSegmentator CT (1,204 volumes, 104 structures incl. all vertebrae; split 1,081/57/65; 1.5 mm isotropic; 4,000 epochs); direct inference on 14 datasets (2,494 cases incl. VerSe2020); fine-tuning on AutoPET, AMOS22 (CT+MR), FLARE22
- Method: nnU-Net-based residual U-Net scaled in depth and width: S 14.6 M, B 58.3 M, L 440 M, H 1.46 B params (0.13–12.6 TFLOPs at 128³)
- Key results: TotalSegmentator validation mean DSC S 83.74 / B 87.12 / L 88.71 / H 90.06 vs nnU-Net 86.76; vertebrae subgroup H 90.43 vs nnU-Net 86.97. Direct inference (14 sets) nnU-Net 76.37 vs B 80.71, L 82.83, H 84.02 — BUT on VerSe2020 STU-Net is worse (B 62.01, L 65.35, H 66.65 vs nnU-Net 67.82). Fine-tuning average nnU-Net 77.06 vs H-ft 80.69. nnU-Net Revisited (SEG-32): STU-Net L avg ~86.9.
- Code / weights / license: github.com/Ziyan-Huang/STU-Net with pretrained weights (licence not stated in paper — check repo)
- Useful for us: TotalSegmentator-pretrained weights already "know" vertebrae - good initialisation for fine-tuning on VerSe/SPIDER.
- Limitations / notes: CT-only pretraining from one dataset; headline numbers on validation not test; underperforms nnU-Net on VerSe2020 direct inference (domain shift on vertebra labelling); L/H need A100 80 GB-class GPUs.
- BibTeX:
```bibtex
@misc{Huang2023STUNet,
  title         = {{STU-Net}: Scalable and Transferable Medical Image Segmentation Models Empowered by Large-Scale Supervised Pre-training},
  author        = {Huang, Ziyan and Wang, Haoyu and Deng, Zhongying and Ye, Jin and Su, Yanzhou and Sun, Hui and He, Junjun and Gu, Yun and Gu, Lixu and Zhang, Shaoting and Qiao, Yu},
  year          = {2023},
  eprint        = {2304.06716},
  archivePrefix = {arXiv}
}
```

### R035. Hatamizadeh 2022 - UNETR
- Full title: UNETR: Transformers for 3D Medical Image Segmentation
- Authors: Ali Hatamizadeh, Yucheng Tang, Vishwesh Nath, Dong Yang, Andriy Myronenko, Bennett A. Landman, Holger R. Roth, Daguang Xu (VERIFIED)
- Year / Venue / Type: 2022 / IEEE/CVF WACV 2022, pp. 1748–1758 (VERIFIED via OpenAlex) / conference
- DOI / arXiv / URL: 10.1109/WACV51458.2022.00181 (VERIFIED); arXiv:2103.10504 (v3 2021-10-09)
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv v3 full PDF — architecture, data, training, results, complexity; venue via OpenAlex)
- Modality & anatomy: generic CT/MRI (BTCV, MSD brain tumour, spleen)
- Data: BTCV 30 abdominal CTs, 13 organs (5-fold CV; free competition up to 80 volumes); MSD brain tumour 484 multimodal MRI (3 classes); MSD spleen 41 CT; MSD split 80:15:5
- Method: ViT-B/16-style encoder (16³ patches, 12 layers, hidden 768, learnable position embedding, no class token) with features from layers 3/6/9/12 fed via skips to a CNN decoder; Dice + CE; AdamW 1e-4, 20k iterations, 96³ (CT) / 128³ (brain) crops, no pretraining
- Key results: BTCV standard average Dice 0.856 in table (text says 85.3%) vs nnU-Net 0.802, CoTr 0.844, TransUNet 0.838; free competition 0.891 (text 0.899) vs nnU-Net-v2 0.884; MSD spleen Dice 0.964 / HD95 1.33; brain 0.711 / 8.82. Params 92.6 M, 41 GFLOPs, 12.1 s inference vs nnU-Net 19.1 M / 413 GFLOPs / 10.3 s. Independent re-benchmark (nnU-Net Revisited, SEG-32) shows it underperforms CNNs.
- Code / weights / license: MONAI (Apache-2.0)
- Useful for us: Transformer baseline to cite; nnU-Net Revisited shows it underperforms CNNs.
- Limitations / notes: table/text inconsistencies in BTCV averages; 16³ patch size fixed by memory; evaluated on only two datasets; later fair benchmarks show nnU-Net-style CNNs outperform it.
- BibTeX:
```bibtex
@inproceedings{Hatamizadeh2022UNETR,
  title     = {{UNETR}: Transformers for {3D} Medical Image Segmentation},
  author    = {Hatamizadeh, Ali and Tang, Yucheng and Nath, Vishwesh and Yang, Dong and Myronenko, Andriy and Landman, Bennett and Roth, Holger R. and Xu, Daguang},
  booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
  pages     = {1748--1758},
  year      = {2022},
  doi       = {10.1109/WACV51458.2022.00181},
  note      = {IEEE Xplore pagination per OpenAlex; the earlier value 574--584 (likely CVF open-access pagination) not verified}
}
```

### R036. Hatamizadeh 2022 - Swin UNETR
- Full title: Swin UNETR: Swin Transformers for Semantic Segmentation of Brain Tumors in MRI Images
- Authors: Ali Hatamizadeh, Vishwesh Nath, Yucheng Tang, Dong Yang, Holger R. Roth, Daguang Xu (names VERIFIED from arXiv PDF; order per arXiv)
- Year / Venue / Type: 2022 / BrainLes 2021 workshop (LNCS 12962) per common citation — STILL UNVERIFIED (PDF states no venue; OpenAlex lookup rate-limited) / workshop paper (BraTS 2021 challenge entry, team NVOptNet)
- DOI / arXiv / URL: arXiv:2201.01266
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv v1 full PDF — architecture, data, training, CV/validation/test results; venue not confirmed)
- Modality & anatomy: brain MRI (BraTS 2021)
- Data: BraTS 2021 — 1,251 training subjects (4 MRI contrasts, 1 mm, skull-stripped), 5-fold CV; 219 validation cases via server; hidden test
- Method: Swin transformer encoder (2×2×2 patches, embedding C=48, 4 stages × 2 blocks, window 7, heads 3/6/12/24, shifted windows) + residual CNN decoder with skips at every resolution; 62 M params, 395 GFLOPs; soft Dice, lr 8e-4 warmup + cosine, 800 epochs, 128³ crops; 10-model ensemble
- Key results: 5-fold CV average Dice 0.913 (ET 0.891 / WT 0.933 / TC 0.917) vs nnU-Net 0.908, SegResNet 0.907, TransBTS 0.891; BraTS21 validation Dice 0.858/0.926/0.885; test 0.853/0.927/0.876. nnU-Net Revisited (SEG-32): ~83.7 average Dice — lowest of strong baselines under fair comparison.
- Code / weights / license: MONAI
- Useful for us: Common transformer baseline in spine papers; cite as comparison.
- Limitations / notes: brain tumour only; no ablations; baselines on authors' own splits; internal inconsistencies (embedding dim, ET margin); margin over nnU-Net small (0.5 Dice) and reversed in independent benchmarks.
- BibTeX:
```bibtex
@misc{Hatamizadeh2022SwinUNETR,
  title         = {Swin {UNETR}: Swin Transformers for Semantic Segmentation of Brain Tumors in {MRI} Images},
  author        = {Hatamizadeh, Ali and Nath, Vishwesh and Tang, Yucheng and Yang, Dong and Roth, Holger and Xu, Daguang},
  year          = {2022},
  eprint        = {2201.01266},
  archivePrefix = {arXiv}
}
```

### R037. Ma 2024 - U-Mamba
- Full title: U-Mamba: Enhancing Long-range Dependency for Biomedical Image Segmentation
- Authors: Jun Ma, Feifei Li, Bo Wang
- Year / Venue / Type: 2024 (v1 2024-01-09) / arXiv preprint (eess.IV; no venue stated)
- DOI / arXiv / URL: arXiv:2401.04722
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv v1 full PDF — architecture, datasets, Tables 3–4, caveats; plus nnU-Net Revisited critique)
- Modality & anatomy: abdominal CT/MR, endoscopy, microscopy
- Data: 3D FLARE22 abdomen CT (50 train / 50 test, 13 organs); 3D AMOS22 abdomen MRI (60 / 50, authors labelled test); 2D EndoVis17 instruments (1,800 / 1,200 frames); 2D NeurIPS22 cell microscopy (1,000 / 101)
- Method: U-Mamba block = two residual conv blocks + Mamba (SSM) block with gated parallel branches; U-Mamba_Bot (bottleneck only) and U-Mamba_Enc (all encoder blocks); implemented inside nnU-Net (SGD, Dice+CE, TTA off)
- Key results: CT DSC Bot 0.8683 / Enc 0.8638 vs nnU-Net 0.8615, SegResNet 0.7927, SwinUNETR 0.7594, UNETR 0.6824; MRI DSC Enc 0.8501 / Bot 0.8453 vs nnU-Net 0.8309; endoscopy and microscopy similar small gains. nnU-Net Revisited: U-Mamba Bot ~87.05 avg and gains vanish versus a no-Mamba ablation.
- Code / weights / license: https://wanglab.ai/u-mamba.html (code, models, data; licence not stated in paper)
- Useful for us: cite as Mamba representative; likely not worth adopting.
- Limitations / notes: margins over nnU-Net (≈0.007 DSC on CT) are well within SD (~0.08); transformer baselines trained from scratch on 1 GPU; text/table inconsistency for endoscopy; independent benchmark attributes gains to the residual nnU-Net backbone, not Mamba.
- BibTeX:
```bibtex
@misc{Ma2024UMamba,
  title         = {{U-Mamba}: Enhancing Long-range Dependency for Biomedical Image Segmentation},
  author        = {Ma, Jun and Li, Feifei and Wang, Bo},
  year          = {2024},
  eprint        = {2401.04722},
  archivePrefix = {arXiv}
}
```

### R038. Xing 2024 - SegMamba
- Full title: SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation (v4 PDF heading: "SegMamba: Mamba for 3D Medical Image Segmentation")
- Authors: Zhaohu Xing, Tian Ye, Yijun Yang, Guang Liu, Lei Zhu (VERIFIED, arXiv v4)
- Year / Venue / Type: 2024 (v4 2024-09-15) / MICCAI 2024 per common citation — UNVERIFIED (arXiv PDF names no venue) / conference
- DOI / arXiv / URL: arXiv:2401.13560
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv v4 full PDF — architecture, datasets, results, efficiency; venue not confirmed)
- Modality & anatomy: brain MRI (BraTS2023), airway CT (AIIB2023), colorectal cancer CT (new CRC-500)
- Data: BraTS2023 1,251 MRI; AIIB2023 120 CT; CRC-500 500 CT (512×512, 94–238 slices); 70/10/20 split each
- Method: U-shaped net with TSMamba encoder blocks: gated spatial convolution (GSC) -> tri-orientated Mamba (forward, reverse, inter-slice sequences summed) ; feature-level uncertainty estimation in skips; conv decoder
- Key results: BraTS2023 avg Dice 91.32 vs UX-Net 89.69, SwinUNETR-V2 89.39, MedNeXt 88.04, SwinUNETR 88.23 (HD95 3.56); AIIB IoU 88.59; CRC-500 Dice 48.46 vs SegResNet 46.10 (ablation baseline 45.34). Inference 1.51 cases/s vs UX-Net 1.92. NO nnU-Net comparison.
- Code / weights / license: github.com/ge-xing/SegMamba
- Useful for us: Mamba alternative for very long spine volumes (whole-spine CT) - citation only.
- Limitations / notes: no nnU-Net baseline (critical given nnU-Net Revisited findings); no variance/repeat statistics; slower and more inference memory than UX-Net; inconsistencies in token-count description; citation only.
- BibTeX:
```bibtex
@misc{Xing2024SegMamba,
  title         = {{SegMamba}: Long-range Sequential Modeling Mamba for {3D} Medical Image Segmentation},
  author        = {Xing, Zhaohu and Ye, Tian and Yang, Yijun and Liu, Guang and Zhu, Lei},
  year          = {2024},
  eprint        = {2401.13560},
  archivePrefix = {arXiv}
}
```

#### I. Foundation / promptable segmentation models

### R039. Kirillov 2023 - Segment Anything (SAM)
- Full title: Segment Anything
- Authors: Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, Ross Girshick (VERIFIED arXiv)
- Year / Venue / Type: 2023 / ICCV 2023 / conference
- DOI / arXiv / URL: arXiv:2304.02643
- Access: open
- Passes: 3/3 (2026-10-16: arXiv abs + full PDF — model, data engine, zero-shot results, limitations, licences; ICCV venue not re-checked)
- Modality & anatomy: natural images
- Data: SA-1B: 1.1B masks on 11M images; data engine — assisted-manual 4.3M masks/120k images, semi-automatic +5.9M/180k, fully automatic 32×32 point grid (99.1% of masks automatic)
- Method: MAE-pretrained ViT-H/16 image encoder (1024² input -> 64² embedding; ~636M params; ViT-L 308M, ViT-B 91M) + prompt encoder (points, boxes, masks, exploratory text) + light two-layer transformer mask decoder outputting 3 candidate masks with confidence (~50 ms)
- Key results: zero-shot single-point mIoU better than RITM on 16/23 datasets (all 23 with oracle mask choice); human quality ratings 7–9/10; none of the 23 datasets is radiological (closest: nucleus microscopy)
- Code / weights / license: model Apache-2.0; SA-1B under a research licence (not fully open)
- Useful for us: Basis for MedSAM/MedSAM2/SAM-Med3D; promptable correction UI for radiologists.
- Limitations / notes: 2D natural images; misses fine structures, spurious small components, soft boundaries; heavy encoder not real-time; text prompting immature; domain tools can outperform — motivates medical adaptations (MedSAM, SAM-Med3D).
- BibTeX:
```bibtex
@inproceedings{Kirillov2023SAM,
  title     = {Segment Anything},
  author    = {Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  pages     = {4015--4026},
  year      = {2023}
}
```
- Also relevant to: Foundation models, architectures and vision-language

### R040. Ma 2024 - MedSAM
- Full title: Segment Anything in Medical Images
- Authors: Jun Ma, Yuting He, Feifei Li et al. (6 authors)
- Year / Venue / Type: 2024 / Nature Communications 15:654 / journal
- DOI / arXiv / URL: 10.1038/s41467-024-44824-z; arXiv:2304.12306
- Access: open
- Passes: 3/3 (2026-10-16: Nature Communications full text — data, model, training, results, limitations; author list/licence sections not captured)
- Modality & anatomy: 10 modalities incl. CT, MRI, X-ray
- Data: 1,570,263 image–mask pairs, 10 modalities (CT, MRI, X-ray, dermoscopy, endoscopy, ultrasound, mammography, OCT, pathology, other), >30 cancer types; 86 internal (80/10/10) + 60 external validation tasks; no spine/vertebra task reported in text
- Method: SAM ViT-B fine-tuned with bounding-box prompts (0–20 px jitter); prompt encoder frozen, image encoder (89.7M) + mask decoder (4.06M) trained; Dice + CE; AdamW 1e-4, batch 160, 150 epochs on 20× A100-80GB; no augmentation; 2D slice-wise
- Key results: ranked first on most internal and external tasks vs SAM and modality-specific U-Net / DeepLabV3+; e.g. nasopharynx cancer (external) median DSC 87.8%; SAM last on almost all internal tasks; MedSAM-assisted annotation cut time by ~82% (adrenal tumours, 2 experts)
- Code / weights / license: github.com/bowang-lab/MedSAM (Apache-2.0, unverified)
- Useful for us: Box-prompted 2D segmentation for X-ray vertebrae and for clinician-in-the-loop corrections.
- Limitations / notes: 2D only; modality imbalance (CT/MRI/endoscopy dominate); box prompts ambiguous for branching structures; weak boundaries still hard; no instance labelling (vertebra levels) — useful mainly as an annotation accelerator.
- BibTeX:
```bibtex
@article{Ma2024MedSAM,
  title   = {Segment Anything in Medical Images},
  author  = {Ma, Jun and He, Yuting and Li, Feifei and Han, Lin and You, Chenyu and Wang, Bo},
  journal = {Nature Communications},
  volume  = {15},
  pages   = {654},
  year    = {2024},
  doi     = {10.1038/s41467-024-44824-z}
}
```
- Also relevant to: Foundation models, architectures and vision-language

### R041. Ma 2025 - MedSAM2
- Full title: MedSAM2: Segment Anything in 3D Medical Images and Videos
- Authors: Jun Ma, Zongxin Yang (equal), Sumin Kim, Bihui Chen, Mohammed Baharoon, Adibvafa Fallahpour, Reza Asakereh, Hongwei Lyu, Bo Wang (VERIFIED arXiv PDF)
- Year / Venue / Type: 2025 (v1 2025-04-04) / arXiv preprint (eess.IV; no venue stated)
- DOI / arXiv / URL: arXiv:2504.03600; https://medsam2.github.io/
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — model, data, holdout results, human-in-the-loop study, limitations)
- Modality & anatomy: 3D CT/MRI/PET and video
- Data: ~455k 3D image–mask pairs (CT 363,161; MRI 77,154; PET 14,818) + ~76k video frames (endoscopy 56,462; ultrasound 19,232); 3D holdout of 40 tasks; no spine tasks
- Method: SAM2.1-Tiny (image encoder ~28M + ~10.9M other) fine-tuned end-to-end at 512×512; box prompts; volumes treated as video with 8-frame memory bank
- Key results: 3D holdout median DSC CT organs 88.84%, CT lesions 86.68%, MRI organs 87.06%, MRI lesions 88.37%, PET lesions 87.22% (EfficientMedSAM-Top1 83.55 / 77.95 / – / 82.25); CAMUS LV 96.13%; hard polyps 92.22% where SAM2.1 drops 6–10 pts. Human-in-the-loop: 5,000 CT lesions (526 -> 74 s/lesion), 3,984 liver MRI lesions (520 -> 65 s), 251,550 echo frames (102 -> 8.4 s/frame) — >85% cost reduction claimed
- Code / weights / license: github.com/bowang-lab/MedSAM2 (+ 3D Slicer plugin bowang-lab/MedSAMSlicer); software licence not stated in paper
- Useful for us: Annotation acceleration for our in-house spine labels; slice-propagation suits sagittal MRI.
- Limitations / notes: box prompts poor for thin/branching structures; no explicit 3D continuity; fixed 8-frame memory can lose targets; GPU required; no vertebra/level labelling — candidate annotation accelerator for our spine labels.
- BibTeX:
```bibtex
@misc{Ma2025MedSAM2,
  title         = {{MedSAM2}: Segment Anything in {3D} Medical Images and Videos},
  author        = {Ma, Jun and Yang, Zongxin and Kim, Sumin and others},
  year          = {2025},
  eprint        = {2504.03600},
  archivePrefix = {arXiv}
}
```
- Also relevant to: Foundation models, architectures and vision-language

### R042. Wang 2023/2024 - SAM-Med3D
- Full title: SAM-Med3D: Towards General-purpose Segmentation Models for Volumetric Medical Images
- Authors: Haoyu Wang, Sizheng Guo, Jin Ye, Zhongying Deng, Junlong Cheng, Tianbin Li, Jianpin Chen, Yanzhou Su, Ziyan Huang, Yiqing Shen, Bin Fu, Shaoting Zhang, Junjun He, Yu Qiao (VERIFIED arXiv v3)
- Year / Venue / Type: 2023 (v3 2024-09-14) / arXiv preprint (no venue stated)
- DOI / arXiv / URL: arXiv:2310.15161
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv v3 full PDF — data, architecture, benchmarks, vertebra ablation, caveats)
- Modality & anatomy: 3D CT/MRI etc.
- Data: SA-Med3D-140K — 22K 3D images, 143K masks, 245 categories, 70 public + 24 private datasets, 28 modalities (CT, US, 26 MR sequences); 131K train / 12K validation masks (validation from 16 public datasets, 58% from unseen sources); stage-2 fine-tuning on ~75K curated masks
- Method: fully 3D SAM (3D ViT image encoder, 3D prompt encoder, 3D mask decoder, 3D positional encodings) trained from scratch (not from SAM weights), 800 epochs + curated fine-tuning
- Key results: overall Dice on 16-dataset validation 76.27 (1 point/volume) and 80.71 (10 points) vs SAM 16.15 and SAM-Med2D 36.83 (per-slice prompts). Vs task-specific nnU-Net: TotalSegmentator 84.68/87.59 vs 85.22; AMOS-CT 79.94/83.99 vs 88.87; AMOS-MR 75.41/81.13 vs 86.92. Bone group 83.38 (1 pt). Vertebrae ablation: baseline 66.05 -> 78.84 after VerSe20 fine-tuning -> 85.98 with all 44 datasets.
- Code / weights / license: github.com/uni-medical/SAM-Med3D (paper prints github.com/unimedical/SAM-Med3D; licence not stated)
- Useful for us: 3D point-prompt correction of vertebra masks.
- Limitations / notes: below task-specific nnU-Net at 1 point on several benchmarks; lesions and ultrasound weak; single-dataset fine-tuning hurts others; vertebra performance needs domain fine-tuning; no level identity.
- BibTeX:
```bibtex
@misc{Wang2023SAMMed3D,
  title         = {{SAM-Med3D}: Towards General-purpose Segmentation Models for Volumetric Medical Images},
  author        = {Wang, Haoyu and Guo, Sizheng and Ye, Jin and others},
  year          = {2023},
  eprint        = {2310.15161},
  archivePrefix = {arXiv}
}
```
- Also relevant to: Foundation models, architectures and vision-language

### R043. Isensee 2025 - nnInteractive
- Full title: nnInteractive: Redefining 3D Promptable Segmentation
- Authors: Fabian Isensee, Maximilian Rokuss, Lars Krämer, Stefan Dinkelacker, Ashis Ravindran, Florian Stritzke, Benjamin Hamm, Tassilo Wald, Moritz Langenberg, Constantin Ulrich, Jonathan Deissler, Ralf Floca, Klaus Maier-Hein (VERIFIED arXiv PDF)
- Year / Venue / Type: 2025 (v1 2025-03-11) / arXiv preprint (no venue stated)
- DOI / arXiv / URL: arXiv:2503.08373
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — data, prompts, architecture, benchmarks, runtime, user study)
- Modality & anatomy: CT, MRI, PET, 3D microscopy
- Data: >120 public 3D datasets, 64,518 volumes, 717,148 objects (CT, MRI, 3D US, PET, 3D microscopy; includes VerSe and SpineMets-CT-SEG among training sources); 5% held out; SuperVoxel pseudo-labels (p=0.2)
- Method: nnU-Net ResEnc-L backbone with prompts as early input channels (positive/negative points, scribbles, boxes, lasso, on any plane); AutoZoom ROI expansion (×1.5 per step up to ×4) for large structures
- Key results (RadioActive benchmark): single point +10.1 Dice over ScribblePrompt; single 3D box +14.9 over SAM2; single scribble +23.8; interactive refinement +11.2 over ScribblePrompt and +14.9 over SegVol; expert scribbles on MS-CMRSeg 87.29 (80.98 ScribblePrompt). Prompt AUC: lasso 83.42 > 2D box 80.74 > scribbles 79.12 > points 71.76. <10 GB VRAM; 120–200 ms small objects (RTX 4090). User study (12 lesions): Dice vs specialist 0.794, 179 s vs 635 s manual (72% faster). VISTA3D excluded (closed-set).
- Code / weights / license: Napari plugin, MITK integration and Python backend (github.com/MIC-DKFZ/nnInteractive per earlier pass); licence not stated in paper — check repo/weights terms
- Useful for us: Best-in-class 3D promptable tool for radiologist correction loop in our system.
- Limitations / notes: mostly simulated interactions; tiny user study; points weakest prompt; large objects slower; no spine-specific results — useful as an annotation tool for our vertebra/disc/canal labels.
- BibTeX:
```bibtex
@misc{Isensee2025nnInteractive,
  title         = {{nnInteractive}: Redefining {3D} Promptable Segmentation},
  author        = {Isensee, Fabian and Rokuss, Maximilian and Kr{\"a}mer, Lars and others},
  year          = {2025},
  eprint        = {2503.08373},
  archivePrefix = {arXiv}
}
```

### R044. He 2024 - VISTA3D
- Full title: VISTA3D: A Unified Segmentation Foundation Model For 3D Medical Imaging
- Authors: Yufan He, Pengfei Guo, Yucheng Tang, Andriy Myronenko, Vishwesh Nath, Ziyue Xu, Dong Yang, Can Zhao, Benjamin Simon, Mason J. Belue, Stephanie A. Harmon, Barış Türkbey, Daguang Xu, Wenqi Li (VERIFIED)
- Year / Venue / Type: 2025 / IEEE/CVF CVPR 2025, pp. 20863–20873 (VERIFIED via OpenAlex); arXiv 2024 / conference
- DOI / arXiv / URL: 10.1109/CVPR52734.2025.01943 (VERIFIED); arXiv:2406.05285
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full PDF — data, architecture, results incl. VerSe, limitations; venue via OpenAlex)
- Modality & anatomy: CT; 127 classes (includes individual vertebrae - unverified)
- Data: 11,454 CT volumes (public + in-house; 64/16/20 split per source); TotalSegmentator pseudo-labels for 117 classes + SAM-feature supervoxels; 127 supported classes; benchmarked on 14 datasets incl. VerSe
- Method: MONAI SegResNet shared encoder (128³ patches); automatic branch with learnable class embeddings (one class prompted at a time, sigmoid); interactive branch with 3D SAM-style point encoder + zero-shot embedding; supervoxels from SAM features (3 views, SLIC) distilled for zero-shot; merge rule applies edits only to clicked components
- Key results: average Dice across datasets auto 0.711 (nnU-Net 0.718, Auto3DSeg 0.706), single point 0.760, auto+point 0.792. VerSe vertebrae: auto 0.825 vs nnU-Net 0.828, TotalSegmentator 0.832; point 0.896; auto+point 0.906. Faster than TotalSegmentator (1m07s vs 4m34s for 333×333×603 on V100). ~20,000 V100 GPU-hours training.
- Code / weights / license: github.com/Project-MONAI/VISTA
- Useful for us: MONAI-native alternative CT segmenter with interactive correction.
- Limitations / notes: CT only; automatic mode no better than nnU-Net/TotalSegmentator on VerSe; weak auto performance on tumours; TotalSegV2 comparison biased; heavy training compute; licence not stated in paper.
- BibTeX:
```bibtex
@inproceedings{He2025VISTA3D,
  title         = {{VISTA3D}: A Unified Segmentation Foundation Model for {3D} Medical Imaging},
  author        = {He, Yufan and Guo, Pengfei and Tang, Yucheng and Myronenko, Andriy and Nath, Vishwesh and Xu, Ziyue and Yang, Dong and Zhao, Can and Simon, Benjamin and Belue, Mason J. and Harmon, Stephanie A. and T{\"u}rkbey, Bar{\i}{\c{s}} and Xu, Daguang and Li, Wenqi},
  booktitle     = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages         = {20863--20873},
  year          = {2025},
  doi           = {10.1109/CVPR52734.2025.01943},
  eprint        = {2406.05285},
  archivePrefix = {arXiv}
}
```

### R045. Tang 2022 - Self-supervised pre-training of Swin UNETR
- Full title: Self-Supervised Pre-Training of Swin Transformers for 3D Medical Image Analysis
- Authors: Yucheng Tang, Dong Yang, Wenqi Li, Holger R. Roth, Bennett Landman, Daguang Xu, Vishwesh Nath, Ali Hatamizadeh (VERIFIED via OpenAlex/arXiv)
- Year / Venue / Type: 2022 / IEEE/CVF CVPR 2022, pp. 20698–20708 (VERIFIED via OpenAlex) / conference
- DOI / arXiv / URL: 10.1109/CVPR52688.2022.02007 (VERIFIED); arXiv:2111.14791
- Access: open
- Passes: 3/3 (2026-10-16: arXiv v2 full PDF — pretraining data, proxy tasks, results, ablations, limitations; venue via OpenAlex)
- Modality & anatomy: CT (multi-region)
- Data: self-supervised pretraining on 5,050 unlabelled CTs (LUNA16 888, TCIA Covid19 761, LIDC 475, HNSCC 1,287, TCIA Colon 1,599 — chest, head/neck, abdomen/pelvis; no spine-dedicated set); fine-tuning on BTCV (13 organs) and all 10 MSD tasks
- Method: Swin UNETR encoder (4 stages, C=48, 2³ patches) pretrained with three equally weighted proxy tasks — masked volume inpainting (30%), 3D rotation prediction, contrastive coding — then fine-tuned with CNN decoder
- Key results: BTCV average Dice 0.918 in Table 1 (text says 0.908) vs UNETR 0.891, nnU-Net 0.888; MSD average Dice 78.68% / NSD 89.28% vs nnU-Net 77.89% / 88.09%. Ablations: scratch 83.43% -> all proxy tasks 84.72% (BTCV CV); ~10% gain with 10% labels, +1.3% with all labels; pretrained model with 60% labels matches scratch with 100% (≥40% annotation saving).
- Code / weights / license: MONAI (pretrained weights public)
- Useful for us: Source of the widely-used Swin UNETR pretrained CT weights; SSL pretraining baseline.
- Limitations / notes: CT-only pretraining (MRI tasks trained from scratch); internal inconsistencies (BTCV average, iteration count, scan counts); later independent benchmarks (nnU-Net Revisited) do not confirm transformer superiority.
- BibTeX:
```bibtex
@inproceedings{Tang2022SwinUNETRSSL,
  title     = {Self-Supervised Pre-Training of {Swin} Transformers for {3D} Medical Image Analysis},
  author    = {Tang, Yucheng and Yang, Dong and Li, Wenqi and Roth, Holger R. and Landman, Bennett and Xu, Daguang and Nath, Vishwesh and Hatamizadeh, Ali},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {20698--20708},
  year      = {2022},
  doi       = {10.1109/CVPR52688.2022.02007},
  note      = {Pages per IEEE Xplore/OpenAlex; earlier value 20730--20740 (likely CVF pagination) not verified}
}
```

#### J. 2024-2026 newcomers (MRI whole-spine, cord)

### R046. Warszawer 2025 - TotalSpineSeg
- Full title: TotalSpineSeg: Robust Spine Segmentation with Landmark-Based Labeling in MRI (ResearchGate preprint, per README); conference version "TotalSpineSeg: Robust Spine Segmentation and Labeling Across Multiple MRI Contrasts", ISMRM & ISMRT Annual Meeting 2025 (Honolulu), abstract 0624
- Authors (ISMRM 2025, VERIFIED via Polytechnique Montréal repository): Yehuda Warszawer, Nathan Molinier, Jan Valošek, Emanuel Shirbint, Pierre-Louis Benveniste, Tobias Granberg, Russell Ouellette, Charidimos Tsagkas, Virginie Callot, Feroze B. Mohamed, Josef Bednařík, Kristin P. O'Grady, Anat Achiron, Julien Cohen-Adad
- Year / Venue / Type: 2025 / ISMRM 2025 Proceedings (DOI 10.58530/2025/0624) + ResearchGate preprint (DOI 10.13140/RG.2.2.31318.56649); earlier ISMRM 2024 abstract ("Fully Automatic Vertebrae and Spinal Cord Segmentation Using a Hybrid Approach Combining nnU-Net and Iterative Algorithm") / conference abstract + software
- DOI / arXiv / URL: 10.58530/2025/0624; 10.13140/RG.2.2.31318.56649; https://github.com/neuropoly/totalspineseg (also on PyPI)
- Access: open (GitHub README); abstract/preprint text not opened
- Passes: 2/3 (2026-10-16: README re-read — labels, model steps, training data, limitations; ISMRM 2025 record (authors/DOI) via Polytechnique Montréal repository; no peer-reviewed full paper found; no performance numbers available)
- Modality & anatomy: MRI (T1w, T2w, STIR, MTS, T2*; sagittal and axial; range of resolutions) and CT; whole spine
- Data: whole-spine dataset (OpenNeuro ds005616), SPIDER, Spine Generic single- and multi-subject; sacrum labels from GoldAtlas, SynthRAD2023, MRSpineSeg, TotalSegmentator; labels via PAM50 template registration (Spinal Cord Toolbox) + manual correction (sizes not stated in README)
- Method: nnU-Net two-step hybrid: step 1 predicts 4 semantic classes (cord, canal, discs, vertebrae) + 5 landmarks (incl. C1), then an iterative algorithm extracts odd-numbered discs; step 2 takes MRI + odd-disc map (2 channels) and predicts 10 classes, then an algorithm assigns individual vertebra/disc labels; single-step comparison model also provided. Localiser-based labelling option when C1/sacrum not in FOV.
- Output labels: cord (1), canal (2), vertebrae C1–L5 (11–45), sacrum (50), discs C2–C3 to L5–S (63–100)
- Key results: no quantitative numbers in README; ISMRM abstract not read
- Code / weights / license: LGPL-3.0 (code + weights)
- Useful for us: contrast- and orientation-agnostic MRI segmentation with anatomical level names, incl. axial input and canal/cord — complements SPINEPS (sagittal T2 only); canal mask enables stenosis measurements.
- Limitations / notes: no peer-reviewed paper or published metrics; README warns it is not a validated tool for cord cross-sectional area and was not tested on cord compression/lesions; LGPL licence implications for distribution.
- BibTeX:
```bibtex
@misc{Warszawer2025TotalSpineSeg,
  title  = {{TotalSpineSeg}: Robust Spine Segmentation with Landmark-Based Labeling in {MRI}},
  author = {Warszawer, Yehuda and Molinier, Nathan and Valo{\v{s}}ek, Jan and others},
  year   = {2025},
  doi    = {10.13140/RG.2.2.31318.56649},
  note   = {Preprint (ResearchGate); software: https://github.com/neuropoly/totalspineseg}
}
```

### R047. Bédard 2025 - Contrast-agnostic soft spinal-cord segmentation
- Full title: Towards contrast-agnostic soft segmentation of the spinal cord (VERIFIED via OpenAlex)
- Authors: Sandrine Bédard, Enamundram Naga Karthik, Charidimos Tsagkas, Emanuele Pravatà, Cristina Granziera, Andrew C. Smith, Kenneth A. Weber II, Julien Cohen-Adad (VERIFIED)
- Year / Venue / Type: 2025 (online 2025-01-21) / Medical Image Analysis 101:103473 (VERIFIED via OpenAlex) / journal
- DOI / arXiv / URL: 10.1016/j.media.2025.103473; arXiv:2310.15402
- Access: preprint open
- Passes: 3/3 (2026-10-16: arXiv full manuscript — data, soft-label method, model, Tables 2–3, limitations; journal metadata via OpenAlex)
- Modality & anatomy: spinal cord MRI, 6 contrasts (cervical focus)
- Data: Spine Generic Public Database — 267 healthy participants scanned, 243 with all contrasts -> 1,458 volumes (split 145/49/49 participants), 6 contrasts (T1w, T2w, T2*w, MT-on, GRE-T1w, DWI), Siemens/GE/Philips. Unseen tests: chronic traumatic SCI T2w (n=80), MS MP2RAGE (103 HC + 180 MS), radiculopathy GRE-EPI (24 patients + 28 controls)
- Method: soft labels = per-contrast binary cord masks registered to T2w, FOV-weighted averaged, mapped back; nnU-Net-3d_fullres-style U-Net with NormReLU output trained with adaptive wing (regression) loss and augmentation applied to soft masks (MONAI + PyTorch Lightning)
- Key results: Dice averaged over contrasts 0.96 ± 0.01 vs sct_deepseg_sc 0.95, nnUNet2D 0.95, PropSeg 0.85, DeepSeg3D 0.85; lowest mean absolute CSA error 1.64 ± 1.42 mm²; significantly reduced CSA variability across contrasts (p<0.05). Unseen: SCI 0.86 (nnUNet3D 0.87), MS MP2RAGE 0.93 (nnUNet3D 0.24), radiculopathy EPI 0.90 (tie)
- Code / weights / license: github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord (v2.0); integrated in Spinal Cord Toolbox >= v6.2 (licence not stated in paper; SCT itself LGPL-3.0 — unverified)
- Useful for us: Cord cross-sectional area is a quantitative "deviation from normal" for cervical myelopathy/stenosis; soft masks handle partial volume.
- Limitations / notes: trained on healthy cervical/upper-thoracic cords only (no lumbar); centre cropping assumes centred cord (fails in scoliosis/lumbar FOV); fixed 0.5 threshold; limited pathology validation; DWI and MT-on worst CSA agreement.
- BibTeX:
```bibtex
@article{Bedard2025ContrastAgnosticSC,
  title   = {Towards Contrast-Agnostic Soft Segmentation of the Spinal Cord},
  author  = {B{\'e}dard, Sandrine and Karthik, Enamundram Naga and Tsagkas, Charidimos and Pravat{\`a}, Emanuele and Granziera, Cristina and Smith, Andrew C. and Weber, Kenneth A. and Cohen-Adad, Julien},
  journal = {Medical Image Analysis},
  year    = {2025},
  volume  = {101},
  pages   = {103473},
  doi     = {10.1016/j.media.2025.103473}
}
```

---

## 02. Degenerative disease and clinical grading

#### A. Grading-scale source papers (definitions we must implement / cite)

### R048. Pfirrmann disc degeneration grading
- Full title: Magnetic resonance classification of lumbar intervertebral disc degeneration
- Authors: Pfirrmann CWA, Metzdorf A, Zanetti M, Hodler J, Boos N (VERIFIED via OpenAlex)
- Year / Venue / Type: 2001 / Spine 26(17):1873–1878 / journal article (classification + reliability study)
- DOI / arXiv / URL: 10.1097/00007632-200109010-00011
- Access: paywalled (abstract and grade table widely reproduced)
- Passes: 2/3 (metadata via Crossref; grade definitions via secondary reproduction; 2026-10-16 full abstract re-read via OpenAlex — data and kappas now verified; full-text grade table not opened)
- Modality & anatomy: MRI, sagittal T2-weighted, lumbar intervertebral discs
- Data (VERIFIED): 300 lumbar discs from 60 patients (33 M/27 F; mean age 40, range 10–83), routine sagittal T2; 3 independent observers
- Method: 5-grade algorithm based on disc structure (homogeneous/inhomogeneous), distinction nucleus vs annulus, T2 signal intensity (hyperintense → black), disc height. Grade I: homogeneous, bright, normal height; II: inhomogeneous ± horizontal bands, clear nucleus/annulus distinction, normal height; III: inhomogeneous, grey, unclear distinction, normal/slightly reduced height; IV: inhomogeneous, grey–dark grey, distinction lost, normal/moderately reduced height; V: inhomogeneous, black, distinction lost, collapsed disc space.
- Key results (VERIFIED): grade distribution I 14, II 82, III 72, IV 68, V 64; intra-observer kappa 0.84–0.90, inter-observer 0.69–0.81; complete agreement 83.8% of discs, 1-grade difference 15.9%, >=2 grades 1.3%.
- Code / weights / license: n/a
- Useful for us: canonical per-disc degeneration label (Pfirrmann 1–5); used by SpineNet, many datasets; our "deviation from normal" for discs can be expressed as Pfirrmann grade + age-expected distribution.
- Limitations / notes: ordinal, subjective; ceiling effects in elderly; modified 8-grade version: Griffith 2007 (DG12).
- BibTeX:
```bibtex
@article{Pfirrmann2001Classification,
  author  = {Pfirrmann, Christian W. A. and Metzdorf, Alexander and Zanetti, Marco and Hodler, Juerg and Boos, Norbert},
  title   = {Magnetic Resonance Classification of Lumbar Intervertebral Disc Degeneration},
  journal = {Spine},
  year    = {2001},
  volume  = {26},
  number  = {17},
  pages   = {1873--1878},
  doi     = {10.1097/00007632-200109010-00011}
}
```

### R049. Modic endplate / vertebral marrow changes
- Full title: Degenerative disk disease: assessment of changes in vertebral body marrow with MR imaging
- Authors: Modic MT, Steinberg PM, Ross JS, et al. (Masaryk TJ, Carter JR)
- Year / Venue / Type: 1988 / Radiology 166(1):193–199 / journal article
- DOI / arXiv / URL: 10.1148/radiology.166.1.3336678
- Access: paywalled (abstract read)
- Passes: 2/3 (metadata Crossref; abstract via QxMD summary)
- Modality & anatomy: MRI T1/T2, lumbar vertebral endplates/marrow adjacent to discs
- Data: lumbar MRI of 474 consecutive patients; histology in 3 cases per type; longitudinal follow-up 16 patients
- Method: descriptive classification. Type 1: low T1, high T2 (4% of patients) — fissured endplates with vascularised fibrous tissue; Type 2: high T1, iso/slightly high T2 (16%) — yellow (fatty) marrow replacement. (Type 3, low T1/low T2 sclerosis, defined in companion Modic 1988 Radiology 168:177–186 paper — not separately logged.)
- Key results: all marrow changes associated with degenerative disc disease at the same level; 5/6 type 1 converted to type 2 over 14 months–3 years; type 2 stable over 2–3 years in 10 patients.
- Code / weights / license: n/a
- Useful for us: defines Modic 1/2/3 labels (endplate-level target); requires both T1 and T2 → our "request better scan" logic should ask for T1 when Modic assessment is needed and only T2 is present.
- Limitations / notes: small histology sample; mixed types (1/2) exist.
- BibTeX:
```bibtex
@article{Modic1988Degenerative,
  author  = {Modic, Michael T. and Steinberg, Paul M. and Ross, Jeffrey S. and Masaryk, Thomas J. and Carter, John R.},
  title   = {Degenerative Disk Disease: Assessment of Changes in Vertebral Body Marrow with {MR} Imaging},
  journal = {Radiology},
  year    = {1988},
  volume  = {166},
  number  = {1},
  pages   = {193--199},
  doi     = {10.1148/radiology.166.1.3336678}
}
```

### R050. Schizas morphological grading of central stenosis
- Full title: Qualitative grading of severity of lumbar spinal stenosis based on the morphology of the dural sac on magnetic resonance images
- Authors: Schizas C, Theumann NH, Burn A, Tansey RJ, Wardlaw D, Smith FW, Kulik G (VERIFIED via OpenAlex)
- Year / Venue / Type: 2010 / Spine 35(21):1919–1924 / journal article
- DOI / arXiv / URL: 10.1097/BRS.0b013e3181d359bd
- Access: paywalled (definitions via Radiopaedia/secondary)
- Passes: 2/3 (metadata Crossref; grade definitions via Radiopaedia rID-92649; 2026-10-16 full abstract via OpenAlex — data, kappas, clinical relevance verified; full text not opened)
- Modality & anatomy: MRI axial T2, lumbar central canal
- Data (VERIFIED): axial T2 MRI of 95 subjects — 37 surgically treated symptomatic LSS, 31 conservatively treated symptomatic LSS (mean follow-up 2.5 and 3.1 y), 27 LBP patients; dural sac cross-sectional area (DSCA) also measured digitally; Oswestry Disability Index
- Method: 7 grades based on rootlet/CSF ratio: A1–A4 (no/minor stenosis; CSF clearly visible, rootlets dorsal or central), B (moderate; rootlets fill sac but still individually visible, grainy CSF), C (severe; no rootlets recognisable, homogeneous grey, posterior epidural fat still present), D (extreme; no rootlets, epidural fat obliterated).
- Key results (VERIFIED; CORRECTED — inter-observer agreement is only MODERATE, not substantial): mean intra-observer kappa 0.65, inter-observer 0.44 (substantial only among physicians of the originating unit); surgical patients had smallest DSCA and more C/D grades; DSCA thresholds over-diagnosed stenosis in 35 and under-diagnosed in 12 patients relative to morphology grade; no relation of grade to baseline ODI or surgical result; C/D more likely to fail conservative treatment, A/B less likely to need surgery.
- Code / weights / license: n/a
- Useful for us: morphology-based grade independent of absolute area — good candidate for explainable stenosis output; maps to mild/moderate/severe.
- Limitations / notes: grade C correlates with failure of conservative treatment in later work; A-subgrades rarely used clinically.
- BibTeX:
```bibtex
@article{Schizas2010Qualitative,
  author  = {Schizas, Constantin and Theumann, Nicolas and Burn, Alexandre and Tansey, Rosamond and Wardlaw, Douglas and Smith, Francis W. and Kulik, Gerit},
  title   = {Qualitative Grading of Severity of Lumbar Spinal Stenosis Based on the Morphology of the Dural Sac on Magnetic Resonance Images},
  journal = {Spine},
  year    = {2010},
  volume  = {35},
  number  = {21},
  pages   = {1919--1924},
  doi     = {10.1097/BRS.0b013e3181d359bd}
}
```

### R051. Lee central canal stenosis grading (0–3)
- Full title: A new grading system of lumbar central canal stenosis on MRI: an easy and reliable method
- Authors: Lee GY, Lee JW, Choi HS, et al. (Oh KJ, Kang HS)
- Year / Venue / Type: 2011 / Skeletal Radiology 40(8):1033–1039 (erratum 40(8):1127, doi 10.1007/s00256-011-1153-z) / journal article
- DOI / arXiv / URL: 10.1007/s00256-011-1102-x
- Access: paywalled
- Passes: 2/3 (metadata Crossref; definitions via Radiopaedia; 2026-10-16 metadata re-confirmed via OpenAlex (online 2011-01-31, PMID 21286714) — abstract not in OpenAlex, kappa values still unverified)
- Modality & anatomy: MRI axial T2, lumbar central canal at disc level
- Data: unverified
- Method: 4 grades on obliteration of anterior CSF space and separability of cauda equina: 0 none (anterior CSF not obliterated); 1 mild (mild obliteration, all roots separable); 2 moderate (moderate obliteration, some roots aggregated); 3 severe (marked compression, roots as one bundle).
- Key results: reported as easy and reliable (high inter-observer kappa — exact values unverified)
- Code / weights / license: n/a
- Useful for us: 4-level scheme closely matching the RSNA 2024 labels (normal/mild, moderate, severe — exact RSNA criteria in DG31 Appendix C not yet read); use by Hallinan 2021 NOT confirmed (see DG30). This is the grading our canal-stenosis head should emulate.
- Limitations / notes: companion Lee S 2010 AJR system for foraminal stenosis.
- BibTeX:
```bibtex
@article{Lee2011NewGrading,
  author  = {Lee, Guen Young and Lee, Joon Woo and Choi, Hee Seok and Oh, Kyoung-Jin and Kang, Heung Sik},
  title   = {A new grading system of lumbar central canal stenosis on {MRI}: an easy and reliable method},
  journal = {Skeletal Radiology},
  year    = {2011},
  volume  = {40},
  number  = {8},
  pages   = {1033--1039},
  doi     = {10.1007/s00256-011-1102-x}
}
```

### R052. Lumbar disc nomenclature 2.0 (Fardon et al.)
- Full title: Lumbar disc nomenclature: version 2.0. Recommendations of the combined task forces of the North American Spine Society, the American Society of Spine Radiology and the American Society of Neuroradiology
- Authors: Fardon DF, Williams AL, Dohring EJ, Murtagh FR, Rothman SLG, Sze G (VERIFIED via OpenAlex for the Spine J version)
- Year / Venue / Type: 2014 / The Spine Journal 14(11):2525–2545; co-published Spine 39(24):E1448–E1465 (doi 10.1097/BRS.0b013e3182a8866d) and summarised in AJNR 35(11):2029 / consensus nomenclature
- DOI / arXiv / URL: 10.1016/j.spinee.2014.04.022
- Access: open (AJNR intro open; full text on publisher sites)
- Passes: 2/3 (metadata Crossref; AJNR introduction read; definitions via secondary summary; 2026-10-16 abstract re-read via OpenAlex — diagnostic categories: normal, congenital/developmental variation, degeneration, trauma, infection/inflammation, neoplasia, morphologic variants of uncertain significance + glossary; AJNR editorial confirms v2.0 revised herniation-vs-asymmetric-bulge distinction, 'annular fissure' replaces 'annular tear', refined acute/chronic herniation. Open PDF at thespinejournalonline.com (S1529943014004094) failed to fetch — exact numeric definitions still from secondary source)
- Modality & anatomy: imaging (mainly MRI/CT), lumbar disc
- Data: n/a (consensus)
- Method: standard definitions: normal; bulge (>25% of disc circumference); herniation (localised displacement <25% of circumference) subdivided into protrusion (base wider than the displaced portion in every plane) vs extrusion (displaced material wider than base in at least one plane, or no continuity); sequestration (free fragment); migration; annular fissure (preferred over "tear"); axial zones central / subarticular / foraminal / extraforaminal and craniocaudal levels (disc, suprapedicular, pedicular, infrapedicular). Definitions explicitly carry no implication of cause, symptoms or treatment.
- Key results: n/a
- Code / weights / license: n/a
- Useful for us: vocabulary for the report generator (findings text must use these terms); zone/level scheme for localising herniations.
- Limitations / notes: updates Fardon & Milette 2001 (Spine 26(5):E93–E113).
- BibTeX:
```bibtex
@article{Fardon2014LumbarDisc,
  author  = {Fardon, David F. and Williams, Alan L. and Dohring, Edward J. and Murtagh, F. Reed and Gabriel Rothman, Stephen L. and Sze, Gordon K.},
  title   = {Lumbar disc nomenclature: version 2.0: Recommendations of the combined task forces of the {North American Spine Society}, the {American Society of Spine Radiology} and the {American Society of Neuroradiology}},
  journal = {The Spine Journal},
  year    = {2014},
  volume  = {14},
  number  = {11},
  pages   = {2525--2545},
  doi     = {10.1016/j.spinee.2014.04.022}
}
```

### R053. Kellgren–Lawrence radiographic osteoarthrosis grading (incl. spine)
- Full title: Radiological Assessment of Osteo-Arthrosis
- Authors: Kellgren JH, Lawrence JS
- Year / Venue / Type: 1957 / Annals of the Rheumatic Diseases 16(4):494–502 / journal article (classic)
- DOI / arXiv / URL: 10.1136/ard.16.4.494
- Access: open (PMC archive)
- Passes: 1/3 (metadata Crossref; content from prior knowledge not re-verified) [2026-10-16 round 3: not upgraded — paywalled/archival (Ann Rheum Dis 1957); ard.bmj.com fetch failed]
- Modality & anatomy: plain radiographs; joints including cervical and lumbar spine (disc and apophyseal joints)
- Data: population radiographs (details unverified)
- Method: 0–4 ordinal grade (none, doubtful, minimal, moderate, severe) based on osteophytes, joint/disc space narrowing, sclerosis, deformity; spine-specific criteria for intervertebral disc degeneration via osteophytes and space narrowing.
- Key results: n/a (classification)
- Code / weights / license: —
- Useful for us: radiograph-only degeneration score when MRI not available (X-ray branch of our system).
- Limitations / notes: low reliability for spine compared with knee; superseded in spine research by Lane/ Wilke-type radiographic scores.
- BibTeX:
```bibtex
@article{Kellgren1957Radiological,
  author  = {Kellgren, J. H. and Lawrence, J. S.},
  title   = {Radiological Assessment of Osteo-Arthrosis},
  journal = {Annals of the Rheumatic Diseases},
  year    = {1957},
  volume  = {16},
  number  = {4},
  pages   = {494--502},
  doi     = {10.1136/ard.16.4.494}
}
```

### R054. Lee S et al. 2010 — foraminal stenosis grading (0–3)
- Full title: A Practical MRI Grading System for Lumbar Foraminal Stenosis
- Authors: Lee S (Seung-Hun), Lee JW, Yeom JS, Kim KJ, Kim HJ, Chung SK, Kang HS (VERIFIED via OpenAlex)
- Year / Venue / Type: 2010 / AJR Am J Roentgenol 194(4):1095–1098 / journal article
- DOI / arXiv / URL: 10.2214/AJR.09.2772
- Access: open (AJR free archive — unverified) / abstract
- Passes: 2/3 (2026-10-16: full abstract via OpenAlex — grade definitions and kappas confirmed; full text not opened)
- Modality & anatomy: MRI sagittal T1/T2 through neural foramina, lumbar
- Data: 576 foramina in 96 patients, L3–L4 to L5–S1, sagittal MRI; two experienced radiologists; intra-observer by one reader
- Method (definitions CONFIRMED in abstract): grade 0 normal; 1 mild — perineural fat obliteration in two opposing directions (vertical or transverse) without nerve root morphological change; 2 moderate — perineural fat obliteration in all four directions without root morphology change; 3 severe — nerve root collapse or morphological change.
- Key results (VERIFIED): inter-observer kappa per level/side 0.905–1.0 (R L3–4 1.0, L L3–4 0.905, R L4–5 0.929, L L4–5 0.942, R L5–S1 0.919, L L5–S1 0.909); intra-observer 0.800–1.00. Reader 1 graded 33/6/7 foramina as grade 1/2/3 (most normal) — very low prevalence of grades 2–3, so near-perfect kappa is on a skewed sample.
- Code / weights / license: —
- Useful for us: standard sagittal foraminal grading; closely matches the RSNA 2024 neural foraminal narrowing labels (exact RSNA criteria in DG31 Appendix C not yet read). Note: use by Hallinan 2021 (DG30) is NOT confirmed — no Lee reference visible in its reference list.
- Limitations / notes: only 2 readers from the originating group, single centre, few moderate/severe foramina; kappas far higher than independent multi-reader studies (cf. DG42 foraminal kappa 0.58) — cite both.
- BibTeX:
```bibtex
@article{Lee2010Practical,
  author  = {Lee, Seunghun and Lee, Joon Woo and Yeom, Jin Sup and Kim, Ki-Jeong and Kim, Hyun-Jib and Chung, Soo Kyo and Kang, Heung Sik},
  title   = {A Practical {MRI} Grading System for Lumbar Foraminal Stenosis},
  journal = {American Journal of Roentgenology},
  year    = {2010},
  volume  = {194},
  number  = {4},
  pages   = {1095--1098},
  doi     = {10.2214/AJR.09.2772}
}
```

### R055. Pfirrmann et al. 2004 — nerve root compromise grading
- Full title: MR Image–based Grading of Lumbar Nerve Root Compromise due to Disk Herniation: Reliability Study with Surgical Correlation
- Authors: Pfirrmann CWA, Dora CF, Schmid MR, Zanetti M, Hodler J, Boos N (VERIFIED via OpenAlex)
- Year / Venue / Type: 2004 / Radiology 230(2):583–588 / journal article
- DOI / arXiv / URL: 10.1148/radiol.2302021289
- Access: paywalled
- Passes: 2/3 (2026-10-16: abstract via OpenAlex — data and reliability numbers; grade names in abstract range "no compromise" to "compression"; individual grade definitions still from prior knowledge)
- Modality & anatomy: lumbar MRI axial, nerve roots (lateral recess)
- Data: 500 nerve roots in 250 symptomatic patients on routine MRI; three independent observers; 94 roots graded at surgery (VERIFIED)
- Method: 4 grades — 0 normal (no contact), 1 contact (disc contacts root, no deviation), 2 deviation (root displaced), 3 compression (root compressed).
- Key results (VERIFIED): intra-observer kappa 0.72–0.77; inter-observer kappa 0.62–0.67; correlation of MRI grade with surgical grade r = 0.86
- Code / weights / license: —
- Useful for us: target labels for subarticular/lateral recess nerve-root compromise; complements RSNA "subarticular stenosis".
- Limitations / notes: —
- BibTeX:
```bibtex
@article{Pfirrmann2004NerveRoot,
  author  = {Pfirrmann, Christian W. A. and Dora, Claudio and Schmid, Marius R. and Zanetti, Marco and Hodler, Juerg and Boos, Norbert},
  title   = {{MR} Image-based Grading of Lumbar Nerve Root Compromise due to Disk Herniation: Reliability Study with Surgical Correlation},
  journal = {Radiology},
  year    = {2004},
  volume  = {230},
  number  = {2},
  pages   = {583--588},
  doi     = {10.1148/radiol.2302021289}
}
```

### R056. Weishaupt et al. 1999 — facet joint osteoarthritis grading on MRI vs CT
- Full title: MR imaging and CT in osteoarthritis of the lumbar facet joints
- Authors: Weishaupt D, Zanetti M, Boos N, Hodler J
- Year / Venue / Type: 1999 / Skeletal Radiology 28(4):215–219 / journal article
- DOI / arXiv / URL: 10.1007/s002560050503
- Access: paywalled
- Passes: 1/3 (metadata re-confirmed via OpenAlex 2026-10-16 (Skeletal Radiol 28(4):215–219, published 1999-05-19); abstract not available in OpenAlex — definitions/results still from prior knowledge) [2026-10-16 round 3: not upgraded — Skeletal Radiol full text paywalled; abstract not in OpenAlex]
- Modality & anatomy: MRI and CT, lumbar facet joints
- Data: unverified
- Method: 4-grade (0–3) facet OA scale adapted from Pathria: 0 normal joint space (2–4 mm); 1 narrowing (<2 mm) and/or small osteophytes and/or mild articular process hypertrophy; 2 narrowing + moderate osteophytes/hypertrophy/subarticular erosions; 3 narrowing + large osteophytes/severe hypertrophy/severe erosions/subchondral cysts.
- Key results: moderate-to-good agreement between MRI and CT (values unverified)
- Code / weights / license: —
- Useful for us: facet arthropathy target definition usable on both CT and MRI → cross-modality label.
- Limitations / notes: verify numbers.
- BibTeX:
```bibtex
@article{Weishaupt1999Facet,
  author  = {Weishaupt, Dominik and Zanetti, Marco and Boos, Norbert and Hodler, Juerg},
  title   = {{MR} imaging and {CT} in osteoarthritis of the lumbar facet joints},
  journal = {Skeletal Radiology},
  year    = {1999},
  volume  = {28},
  number  = {4},
  pages   = {215--219},
  doi     = {10.1007/s002560050503}
}
```

### R057. Michigan State University (MSU) classification of lumbar disc herniation
- Full title: MSU Classification for herniated lumbar discs on MRI: toward developing objective criteria for surgical selection
- Authors: Mysliwiec LW, Cholewicki J, Winkelpleck MD, Eis GP
- Year / Venue / Type: 2010 / European Spine Journal 19(7):1087–1093 / journal article
- DOI / arXiv / URL: 10.1007/s00586-009-1274-4
- Access: open (PMC, per Springer OA — unverified)
- Passes: 1/3 (metadata re-confirmed via OpenAlex 2026-10-16 incl. full title "MSU Classification for herniated lumbar discs on MRI: toward developing objective criteria for surgical selection", PMID 20084410; abstract not in OpenAlex — definitions/results still from prior knowledge) [2026-10-16 round 3: not upgraded — Eur Spine J; open copy likely on PMC but PMC/Europe PMC blocked (captcha/429) and SpringerLink fetch failed]
- Modality & anatomy: MRI axial T2 at level of maximal herniation, lumbar
- Data: surgical cohort (size unverified)
- Method: size grade 1/2/3 relative to the intra-facet line (1: ≤50% of the distance from disc to intra-facet line; 2: >50% up to the line; 3: beyond the line) combined with location zones A (central), B (lateral/paracentral), C (far lateral/foraminal), e.g. "2-AB".
- Key results: high inter-/intra-rater reliability and correlation with surgical decision reported (values unverified)
- Code / weights / license: —
- Useful for us: geometric, measurable herniation size/location scheme — directly computable from a segmentation of disc + facets, making it ideal for an automated "quantified deviation" output.
- Limitations / notes: verify reliability numbers from full text.
- BibTeX:
```bibtex
@article{Mysliwiec2010MSU,
  author  = {Mysliwiec, Lawrence Walter and Cholewicki, Jacek and Winkelpleck, Michael D. and Eis, Greg P.},
  title   = {{MSU} Classification for herniated lumbar discs on {MRI}: toward developing objective criteria for surgical selection},
  journal = {European Spine Journal},
  year    = {2010},
  volume  = {19},
  number  = {7},
  pages   = {1087--1093},
  doi     = {10.1007/s00586-009-1274-4}
}
```

### R058. Kang Y et al. 2011 — cervical canal stenosis MRI grading (0–3)
- Full title: New MRI Grading System for the Cervical Canal Stenosis
- Authors: Kang Y, Lee JW, Koh YH, Hur S, Kim SJ, Chai JW, Kang HS (VERIFIED via OpenAlex); PMID 21700974
- Year / Venue / Type: 2011 / AJR Am J Roentgenol 197(1):W134–W140 / journal article
- DOI / arXiv / URL: 10.2214/AJR.10.5560
- Access: paywalled / AJR archive
- Passes: 2/3 (2026-10-16: full abstract via OpenAlex — definitions and agreement statistics; full text not opened)
- Modality & anatomy: cervical MRI sagittal T2
- Data: 82 patients (37 M/45 F; mean age 65.2, range 60–86), sagittal T2; six radiologists independently
- Method (CONFIRMED in abstract: 0 none, 1 >50% subarachnoid obliteration, 2 cord deformity, 3 cord signal change): grade 0 no stenosis; 1 obliteration of >50% of subarachnoid space without cord deformity; 2 cord deformity (compression) without signal change; 3 cord T2 hyperintensity near the compressed level.
- Key results (VERIFIED): inter-observer ICC 0.716–0.802; all four grades: 63–64% agreement, kappa 0.60–0.62; any stenosis (0 vs 1–3): kappa 0.51–0.59; insignificant (0–1) vs significant (2–3): kappa 0.57–0.66; cord signal change (3 vs 0–2): kappa 0.70–0.73; intra-observer ICC 0.768.
- Code / weights / license: —
- Useful for us: standard cervical stenosis label used by subsequent cervical DL work (e.g., Hallinan-group cervical models — not verified here).
- Limitations / notes: —
- BibTeX:
```bibtex
@article{Kang2011Cervical,
  author  = {Kang, Yusuhn and Lee, Joon Woo and Koh, Young Hwan and Hur, Saebeom and Kim, Su Jin and Chai, Jee Won and Kang, Heung Sik},
  title   = {New {MRI} Grading System for the Cervical Canal Stenosis},
  journal = {American Journal of Roentgenology},
  year    = {2011},
  volume  = {197},
  number  = {1},
  pages   = {W134--W140},
  doi     = {10.2214/AJR.10.5560}
}
```

### R059. Griffith et al. 2007 — modified (8-grade) Pfirrmann
- Full title: Modified Pfirrmann Grading System for Lumbar Intervertebral Disc Degeneration
- Authors: Griffith JF, Wang YXJ, Antonio GE, Choi KC, Yu ASY, Ahuja AT, Leung PC (VERIFIED via OpenAlex)
- Year / Venue / Type: 2007 / Spine 32(24):E708–E712 / journal article
- DOI / arXiv / URL: 10.1097/BRS.0b013e31815a59a0
- Access: paywalled
- Passes: 2/3 (2026-10-16: full structured abstract via OpenAlex; full-text grade table not opened)
- Modality & anatomy: MRI T2 sagittal lumbar discs (elderly cohort)
- Data: 260 lumbar discs from 52 elderly subjects (26 M/26 F; mean age 73, range 67–83); 3 independent readers; 24-image reference panel
- Method: 8-grade scale comparing nucleus/inner annulus signal to CSF and presacral fat, plus disc height loss (<30%, 30–60%, >60%) — designed to improve discrimination in elderly where original Pfirrmann saturates.
- Key results (VERIFIED): grade distribution (mean of readers) G2 0.39%, G3 22%, G4 21.5%, G5 25.3%, G6 19.1%, G7 7.1%, G8 4.8%; intra-observer weighted kappa 0.79–0.91; inter-observer weighted kappa 0.65–0.67; complete inter-observer agreement 66% of discs, 91% of disagreements within 1 grade (intra: 85% agreement, 84% of disagreements 1 grade).
- Code / weights / license: —
- Useful for us: finer-grained ordinal target → closer to a continuous "degeneration deviation" score.
- Limitations / notes: less adopted than 5-grade; validated only in elderly; exact per-grade criteria must be taken from the full text. Note "within-1-grade" agreement is the natural tolerance metric for our ordinal outputs.
- BibTeX:
```bibtex
@article{Griffith2007Modified,
  author  = {Griffith, James F. and Wang, Yi-Xiang J. and Antonio, Gregory E. and Choi, Kai Chow and Yu, Alfred and Ahuja, Anil T. and Leung, Ping Chung},
  title   = {Modified {Pfirrmann} Grading System for Lumbar Intervertebral Disc Degeneration},
  journal = {Spine},
  year    = {2007},
  volume  = {32},
  number  = {24},
  pages   = {E708--E712},
  doi     = {10.1097/BRS.0b013e31815a59a0}
}
```

### R060. Meyerding spondylolisthesis grading (classic)
- Full title: Spondylolisthesis
- Authors: Meyerding HW
- Year / Venue / Type: 1932 / Surgery, Gynecology & Obstetrics 54:371–377 / journal article (classic; no DOI)
- DOI / arXiv / URL: none (pre-DOI); citation details from secondary sources — unverified
- Access: not online
- Passes: 1/3 (2026-10-16: grade definitions confirmed against Radiopaedia 'Spondylolisthesis grading system' (slip A / inferior vertebral body AP length B: I 0–25%, II 26–50%, III 51–75%, IV 76–100%, V >100% spondyloptosis; I–II low-grade, III–V high-grade). Original 1932 citation details (Surg Gynecol Obstet 54:371–377) still UNVERIFIED — not online) [2026-10-16 round 3: not upgraded — classic 1932 paper not online]
- Modality & anatomy: lateral radiograph (also applied on sagittal MRI/CT), lumbar
- Data: n/a
- Method: slip as % of the AP width of the inferior vertebral endplate: grade I 0–25%, II 26–50%, III 51–75%, IV 76–100%, (V >100% spondyloptosis, later addition).
- Key results: n/a
- Code / weights / license: —
- Useful for us: directly computable from vertebral corner landmarks → quantitative slip % is a natural "deviation from normal" measure across X-ray, CT and MRI.
- Limitations / notes: verify citation (volume/pages) before final bibliography.
- BibTeX:
```bibtex
@article{Meyerding1932Spondylolisthesis,
  author  = {Meyerding, H. W.},
  title   = {Spondylolisthesis},
  journal = {Surgery, Gynecology \& Obstetrics},
  year    = {1932},
  volume  = {54},
  pages   = {371--377},
  note    = {Citation details unverified}
}
```

### R061. Fardon & Milette 2001 — original lumbar disc nomenclature
- Full title: Nomenclature and classification of lumbar disc pathology. Recommendations of the Combined task Forces of the North American Spine Society, American Society of Spine Radiology, and American Society of Neuroradiology
- Authors: Fardon DF, Milette PC
- Year / Venue / Type: 2001 / Spine 26(5):E93–E113 (VERIFIED via OpenAlex 2026-10-16) / consensus
- DOI / arXiv / URL: 10.1097/00007632-200103010-00006 (VERIFIED via OpenAlex) (Crossref shows Fardon's companion editorial in the same issue: 10.1097/00007632-200103010-00007, Spine 26(5):461–462 — verified)
- Access: paywalled
- Passes: 1/3 (2026-10-16: bibliographic metadata verified via OpenAlex; full text paywalled, not opened) [2026-10-16 round 3: not upgraded — Spine full text paywalled]
- Modality & anatomy: imaging, lumbar disc
- Data: n/a
- Method: first combined-task-force nomenclature (bulge/protrusion/extrusion/sequestration), superseded by DG05
- Key results: n/a
- Code / weights / license: —
- Useful for us: historical citation for nomenclature; cite DG05 as the current standard.
- Limitations / notes: verify.
- BibTeX:
```bibtex
@article{Fardon2001Nomenclature,
  author  = {Fardon, David F. and Milette, Pierre C.},
  title   = {Nomenclature and classification of lumbar disc pathology: Recommendations of the Combined Task Forces of the {North American Spine Society}, {American Society of Spine Radiology}, and {American Society of Neuroradiology}},
  journal = {Spine},
  year    = {2001},
  volume  = {26},
  number  = {5},
  pages   = {E93--E113},
  doi     = {10.1097/00007632-200103010-00006}
}
```

### R062. Modic et al. 1988 — Imaging of degenerative disk disease (Modic type 3)
- Full title: Imaging of degenerative disk disease
- Authors: Modic MT, Masaryk TJ, Ross JS, Carter JR
- Year / Venue / Type: 1988 / Radiology 168(1):177–186 / journal article (review)
- DOI / arXiv / URL: 10.1148/radiology.168.1.3289089 (verified via Crossref)
- Access: paywalled
- Passes: 1/3 (metadata verified via Crossref; content from prior knowledge) [2026-10-16 round 3: metadata re-confirmed on pubs.rsna.org (Modic MT, Masaryk TJ, Ross JS, Carter JR; 168(1):177–186); abstract behind paywall — left at 1/3]
- Modality & anatomy: MRI, lumbar disc + endplates
- Data: n/a
- Method: overview of MR appearance of disc degeneration; commonly cited as source of Modic type 3 (low T1/low T2, subchondral sclerosis)
- Key results: n/a
- Code / weights / license: —
- Useful for us: cite with DG02 for the full Modic 1/2/3 scheme.
- Limitations / notes: verify.
- BibTeX:
```bibtex
@article{Modic1988Imaging,
  author  = {Modic, Michael T. and Masaryk, Thomas J. and Ross, Jeffrey S. and Carter, John R.},
  title   = {Imaging of degenerative disk disease},
  journal = {Radiology},
  year    = {1988},
  volume  = {168},
  number  = {1},
  pages   = {177--186},
  doi     = {10.1148/radiology.168.1.3289089}
}
```

### R063. Pathria et al. 1987 — CT facet osteoarthritis grading
- Full title: Osteoarthritis of the facet joints: accuracy of oblique radiographic assessment
- Authors: Pathria M, Sartoris DJ, Resnick D
- Year / Venue / Type: 1987 / Radiology 164(1):227–230 / journal article
- DOI / arXiv / URL: 10.1148/radiology.164.1.3588910 (verified via Crossref)
- Access: paywalled
- Passes: 2/3 (2026-10-16: abstract via pubs.rsna.org — design, prevalence, agreement, accuracy; full text paywalled so per-grade definitions still from prior knowledge)
- Modality & anatomy: CT and oblique radiographs, lumbar facets
- Data (VERIFIED): 50 consecutive LBP patients with oblique lumbar radiographs and transaxial CT within 8 months; L3–4, L4–5, L5–S1 facets; two independent blinded radiologists; CT as reference
- Method: 4-point facet OA scale applied to both modalities (scale named in abstract; detailed grade wording 0 normal / 1 narrowing / 2 narrowing + sclerosis or hypertrophy / 3 severe with osteophytes is from prior knowledge — confirm in full text); basis of Weishaupt (DG09)
- Key results (VERIFIED): CT — 68% of joints abnormal, 28% moderate/severe; inter-observer exact agreement 57% (radiographs) and 63% (CT), within one grade 39% and 35%; oblique radiographs vs CT: any disease sens 55% / spec 69%; moderate–severe vs none–mild sens 23% / spec 94% — radiographs insensitive.
- Code / weights / license: —
- Useful for us: CT facet grading definition.
- Limitations / notes: small n; exact-grade agreement only ~60% even on CT — a low human ceiling for facet grading; title is about radiograph accuracy, the CT grading is the reference scale.
- BibTeX:
```bibtex
@article{Pathria1987Facet,
  author  = {Pathria, M. and Sartoris, D. J. and Resnick, D.},
  title   = {Osteoarthritis of the facet joints: accuracy of oblique radiographic assessment},
  journal = {Radiology},
  year    = {1987},
  volume  = {164},
  number  = {1},
  pages   = {227--230},
  doi     = {10.1148/radiology.164.1.3588910}
}
```

### R064. Kettler & Wilke 2006 — review of disc/facet degeneration grading systems
- Full title: Review of existing grading systems for cervical or lumbar disc and facet joint degeneration
- Authors: Kettler A, Wilke HJ
- Year / Venue / Type: 2006 / European Spine Journal 15(6):705–718 (VERIFIED via Crossref; online 2005-09-20) / review. Note: Crossref also lists a same-title 1-page item 10.1007/s00586-006-1077-9, Eur Spine J 15(6):719 (likely erratum — not opened)
- DOI / arXiv / URL: 10.1007/s00586-005-0954-y (VERIFIED via Crossref 2026-10-16)
- Access: open (PMC — unverified)
- Passes: 1/3 (2026-10-16: bibliographic metadata verified via Crossref; abstract/full text not re-opened — fetch budget exhausted; content fields still from prior knowledge) [2026-10-16 round 3: not upgraded — bronze OA per OpenAlex (Springer PDF, PMC3489462, OpenAlex-hosted PDF) but all three fetches failed (Springer error, Europe PMC 429) — retry later]
- Modality & anatomy: radiograph, CT, MRI; cervical and lumbar
- Data: review of dozens of grading systems
- Method: narrative/systematic review
- Key results: many systems, few validated for reliability; recommends standardisation
- Code / weights / license: —
- Useful for us: single citation summarising the zoo of grading systems; justifies our choice of the most reliable ones.
- Limitations / notes: verify.
- BibTeX:
```bibtex
@article{Kettler2006Review,
  author  = {Kettler, Annette and Wilke, Hans-Joachim},
  title   = {Review of existing grading systems for cervical or lumbar disc and facet joint degeneration},
  journal = {European Spine Journal},
  year    = {2006},
  volume  = {15},
  number  = {6},
  pages   = {705--718},
  doi     = {10.1007/s00586-005-0954-y}
}
```

### R065. Wiltse, Newman & Macnab 1976 — classification of spondylolysis/spondylolisthesis
- Full title: Classification of spondylolisis and spondylolisthesis
- Authors: Wiltse LL, Newman PH, Macnab I
- Year / Venue / Type: 1976 / Clinical Orthopaedics and Related Research 117:23–29 (unverified)
- DOI / arXiv / URL: unverified
- Access: paywalled
- Passes: 1/3 (2026-10-16: type definitions confirmed against Radiopaedia 'Wiltse classification' — I dysplastic; II isthmic with subtypes a lytic, b elongated pars, c acute pars fracture; III degenerative; IV post-traumatic (fracture outside pars); V pathological; VI iatrogenic. Radiopaedia cites a 1981 Wiltse paper rather than 1976 — bibliographic details (CORR 117:23–29, 1976) still UNVERIFIED) [2026-10-16 round 3: not upgraded — CORR 1976 paywalled/not online]
- Modality & anatomy: radiographs, lumbar
- Data: n/a
- Method: aetiological types I dysplastic, II isthmic, III degenerative, IV traumatic, V pathological (VI iatrogenic added later)
- Key results: n/a
- Code / weights / license: —
- Useful for us: aetiology categories to complement Meyerding severity (DG13) in reports.
- Limitations / notes: verify.
- BibTeX:
```bibtex
@article{Wiltse1976Classification,
  author  = {Wiltse, L. L. and Newman, P. H. and Macnab, I.},
  title   = {Classification of spondylolisis and spondylolisthesis},
  journal = {Clinical Orthopaedics and Related Research},
  year    = {1976},
  volume  = {117},
  pages   = {23--29},
  note    = {Metadata unverified}
}
```

---

#### B. AI grading systems — SpineNet family and DeepSPINE

### R066. SpineNet (Eur Spine J, ISSLS prize 2017)
- Full title: ISSLS PRIZE IN BIOENGINEERING SCIENCE 2017: Automation of reading of radiological features from magnetic resonance images (MRIs) of the lumbar spine without human intervention is comparable with an expert radiologist
- Authors: Jamaludin A, Lootus M, Kadir T, et al. (Zisserman A, Urban J, Battié MC, Fairbank J, McCall I; Genodisc Consortium)
- Year / Venue / Type: 2017 / European Spine Journal 26(5):1374–1383 / journal article
- DOI / arXiv / URL: 10.1007/s00586-017-4956-3
- Access: open (SpringerLink)
- Passes: 3/3 full text (via SpringerLink)
- Modality & anatomy: MRI sagittal T2, lumbar T12–S1
- Data: Genodisc project (UK, Hungary, Slovenia, Italy; routine clinical, heterogeneous scanners); 2,009 patients, 12,018 discs (1,806 train / 203 test); single expert radiologist labels; 121 patients re-read for intra-rater agreement. Labels: Pfirrmann (1–5), disc narrowing (1–4), spondylolisthesis, central canal stenosis, upper/lower endplate defects, upper/lower marrow (Modic) changes.
- Method: vertebra detection + labelling, then multi-task CNN on disc volumes; "evidence hotspots" for localisation.
- Key results: disc detection/labelling 95.6%; Pfirrmann class-average accuracy 70.1% vs radiologist intra-rater 70.4%; reliability 0.88 (system vs radiologist) vs 0.91 (intra-rater). Spondylolisthesis kappa 0.59 vs intra-rater 0.79.
- Code / weights / license: SpineNet (later open-sourced as SpineNetV2, see DG22)
- Useful for us: benchmark for "human-level" multi-feature grading; demonstrates that intra-rater agreement is the ceiling; evidence-hotspot visualisation idea for explainable reports.
- Limitations / notes: single reader ground truth; sagittal-only (canal stenosis normally needs axial); system over-calls pathology; rare-class imbalance (469 spondylolisthesis discs of ~12k); failures with transitional vertebrae.
- BibTeX:
```bibtex
@article{Jamaludin2017ISSLS,
  author  = {Jamaludin, Amir and Lootus, Meelis and Kadir, Timor and Zisserman, Andrew and Urban, Jill and Batti{\'e}, Michele C. and Fairbank, Jeremy and McCall, Iain and {Genodisc Consortium}},
  title   = {{ISSLS PRIZE IN BIOENGINEERING SCIENCE 2017}: Automation of reading of radiological features from magnetic resonance images ({MRIs}) of the lumbar spine without human intervention is comparable with an expert radiologist},
  journal = {European Spine Journal},
  year    = {2017},
  volume  = {26},
  number  = {5},
  pages   = {1374--1383},
  doi     = {10.1007/s00586-017-4956-3}
}
```

### R067. SpineNet (Medical Image Analysis 2017)
- Full title: SpineNet: Automated classification and evidence visualization in spinal MRIs
- Authors: Jamaludin A, Kadir T, Zisserman A
- Year / Venue / Type: 2017 / Medical Image Analysis 41:63–73 / journal article
- DOI / arXiv / URL: 10.1016/j.media.2017.07.002
- Access: open accepted manuscript on ORA Oxford (CC BY-NC-ND 4.0; uuid:6caacb46-d262-4902-92cd-b9c30aee8520); publisher paywalled
- Passes: 3/3 (2026-10-16: ORA accepted-manuscript full text — data, architecture, results table, hotspot method, limitations; abstract re-read on ORA)
- Modality & anatomy: MRI sagittal T2, lumbar discs
- Data: 2,009 patients, 12,018 lumbar discs (T12/L1–L5/S1), T2 sagittal from various centres/machines (slice 2.6–6.0 mm, median 4 mm); all labels by ONE expert radiologist; split 80:10:10 by patient (1,602/204/203; 1,217 test discs); intra-rater subset 121 patients / 726 discs labelled twice. (Dataset not named "Genodisc" in this manuscript.)
- Method: multi-task CNN from modified VGG-M (input 112×224×9 disc volume; Conv1 7×7×9), shared Conv1–5 then task branches, summed class-weighted softmax losses ignoring missing labels, SGD, ~1,000 epochs, heavy augmentation + 54-way test-time averaging; disc volumes cut between detected adjacent vertebrae; "evidence hotspots" = 9-channel gradient saliency averaged over augmentations (qualitative only)
- Key results (balanced/average per-class accuracy, test; model vs radiologist intra-rater): Pfirrmann (5-class) 71.2 vs 70.4; disc narrowing 73.9 vs 72.0; upper/lower endplate defects 84.8 / 87.3 vs 80.7 / 83.3; upper/lower marrow changes 90.1 / 89.0 vs 92.5 / 91.4. CORRECTION: the journal paper reports SIX tasks — spondylolisthesis and central canal stenosis (listed earlier from the abstract summary) are not among the evaluated tasks in this manuscript. Vs Lootus et al. (different protocol): Pfirrmann ±1 96.1% vs 87.4%.
- Code / weights / license: SpineNet v2.0.0 software documented at spinenet.readthedocs.io (licence link to github.com/rwindsor1/SpineNet; non-commercial terms of access; weights download section) — see DG22
- Useful for us: weak-label → localisation paradigm, citation for multi-task disc grading.
- Limitations / notes: single-radiologist labels (ceiling = intra-rater agreement ~70% for Pfirrmann); lumbar T2 sagittal only; marrow changes binary subset of Modic (needs T1 for typing); hotspots not quantitatively validated; text/table inconsistency on narrowing classes.
- BibTeX:
```bibtex
@article{Jamaludin2017SpineNet,
  author  = {Jamaludin, Amir and Kadir, Timor and Zisserman, Andrew},
  title   = {{SpineNet}: Automated classification and evidence visualization in spinal {MRIs}},
  journal = {Medical Image Analysis},
  year    = {2017},
  volume  = {41},
  pages   = {63--73},
  doi     = {10.1016/j.media.2017.07.002}
}
```

### R068. External validation of SpineNet — Northern Finland Birth Cohort 1966
- Full title: External validation of SpineNet, an open-source deep learning model for grading lumbar disk degeneration MRI features, using the Northern Finland Birth Cohort 1966
- Authors: McSweeney TP, Tiulpin A, Saarakkala S, et al. (Niinimäki J, Windsor R, Jamaludin A, Kadir T, Karppinen J, Määttä J)
- Year / Venue / Type: 2023 / Spine 48(7):484–491 / journal article
- DOI / arXiv / URL: 10.1097/BRS.0000000000004572
- Access: open (PMC9990601; Oulu repository)
- Passes: 2/3 (abstract + repository record; full text blocked by PMC captcha)
- Modality & anatomy: MRI sagittal T2 lumbar
- Data: NFBC1966, 1,331 participants with lumbar MRI and consensus gradings (population cohort, not training data)
- Method: SpineNet out-of-the-box vs consensus human grading
- Key results: balanced accuracy 78% (Pfirrmann) and 86% (Modic); Pfirrmann Lin CCC 0.86, Cohen kappa 0.68; 20.83% of discs graded differently but only 0.85% by >1 grade; Modic kappa 0.74 (0.76 in LBP subset).
- Code / weights / license: SpineNet open-source
- Useful for us: population-cohort external validation; disagreement mostly ±1 grade → justify reporting with uncertainty / adjacent-grade tolerance.
- Limitations / notes: single cohort (same birth year, Finnish).
- BibTeX:
```bibtex
@article{McSweeney2023External,
  author  = {McSweeney, Terence P. and Tiulpin, Aleksei and Saarakkala, Simo and Niinim{\"a}ki, Jaakko and Windsor, Rhydian and Jamaludin, Amir and Kadir, Timor and Karppinen, Jaro and M{\"a}{\"a}tt{\"a}, Juhani},
  title   = {External Validation of {SpineNet}, an Open-Source Deep Learning Model for Grading Lumbar Disk Degeneration {MRI} Features, Using the {Northern Finland Birth Cohort 1966}},
  journal = {Spine},
  year    = {2023},
  volume  = {48},
  number  = {7},
  pages   = {484--491},
  doi     = {10.1097/BRS.0000000000004572}
}
```

### R069. External validation of SpineNet — Schulthess Clinic (elderly surgical cohort)
- Full title: External validation of the deep learning system "SpineNet" for grading radiological features of degeneration on MRIs of the lumbar spine
- Authors: Grob A, Loibl M, Jamaludin A, et al. (Winklhofer S, Fairbank JCT, Fekete T, Porchet F, Mannion AF)
- Year / Venue / Type: 2022 / European Spine Journal 31(8):2137–2148 / journal article
- DOI / arXiv / URL: 10.1007/s00586-022-07311-x
- Access: open (SpringerLink; ZORA)
- Passes: 3/3 full text summary
- Modality & anatomy: MRI lumbar L1/2–L5/S1
- Data: 882 patients (mean age 72 ± 8.8) with degenerative disorders, 4,410 segments, from two trials (LSOS, APROPOS) 2011–2019; external MRI institutes; one expert radiologist reference.
- Method: SpineNet vs radiologist; kappa, Spearman, Lin CCC, class-average accuracy
- Key results: Pfirrmann kappa 0.72 (per level 0.63–0.77), CAA 55%; spondylolisthesis kappa 0.63, CAA 56%; central canal stenosis kappa 0.60 (per level 0.17–0.57), CAA 43%. SpineNet over-called Pfirrmann, under-called stenosis.
- Code / weights / license: —
- Useful for us: shows domain-shift degradation in elderly stenosis patients; motivates axial input and calibration.
- Limitations / notes: single reader; the all-level kappa exceeds the per-level ranges (possible reporting inconsistency).
- BibTeX:
```bibtex
@article{Grob2022External,
  author  = {Grob, Alexandra and Loibl, Markus and Jamaludin, Amir and Winklhofer, Sebastian and Fairbank, Jeremy C. T. and Fekete, Tamás and Porchet, François and Mannion, Anne F.},
  title   = {External validation of the deep learning system ``{SpineNet}'' for grading radiological features of degeneration on {MRIs} of the lumbar spine},
  journal = {European Spine Journal},
  year    = {2022},
  volume  = {31},
  number  = {8},
  pages   = {2137--2148},
  doi     = {10.1007/s00586-022-07311-x}
}
```

### R070. External validation of SpineNetV2 (11 features)
- Full title: External validation of SpineNetV2 on a comprehensive set of radiological features for grading lumbosacral disc pathologies
- Authors: Nigru AS, Benini S, Bonetti M, Bragaglio G, Frigerio M, Maffezzoni F, Leonardi R (VERIFIED via OpenAlex + DOAJ)
- Year / Venue / Type: 2024 (online 2024-10-28; Dec 2024 issue) / North American Spine Society Journal 20:100564 / journal article (VERIFIED)
- DOI / arXiv / URL: 10.1016/j.xnsj.2024.100564 (VERIFIED via OpenAlex 2026-10-16); PMC11617751; DOAJ record e1ce5924f92948528879f67b239eaaa5
- Access: open
- Passes: 2/3 (abstract via DOAJ; 2026-10-16 abstract re-read via OpenAlex + DOAJ, DOI confirmed; per-feature numbers are only in full text — not read)
- Modality & anatomy: MRI sagittal T2 lumbosacral
- Data: 353 patients, 1,747 discs (mean age 54 ± 15.4, 44.5% female), single private imaging centre in Italy, Sept 2021–Feb 2023; two expert radiologists.
- Method: SpineNetV2 grading of 11 features (Pfirrmann, narrowing, central canal stenosis, spondylolisthesis, upper/lower endplate defects, upper/lower marrow changes, L/R foraminal stenosis, herniation) vs two expert radiologists; metrics accuracy, balanced accuracy, precision, F1, MCC, Brier score, Lin CCC, Cohen kappa
- Key results: agreement >0.7 for most features; lower for foraminal stenosis and disc herniation (limitations of sagittal-only images).
- Code / weights / license: SpineNetV2 open
- Useful for us: confirms that herniation and foraminal stenosis require axial input — supports our multi-view design and "ask for axial T2" behaviour.
- Limitations / notes: single centre.
- BibTeX:
```bibtex
@article{Nigru2024ExternalSpineNetV2,
  author  = {Nigru, Alemu Sisay and Benini, Sergio and Bonetti, Matteo and Bragaglio, Graziella and Frigerio, Michele and Maffezzoni, Federico and Leonardi, Riccardo},
  title   = {External validation of {SpineNetV2} on a comprehensive set of radiological features for grading lumbosacral disc pathologies},
  journal = {North American Spine Society Journal},
  year    = {2024},
  volume  = {20},
  pages   = {100564},
  doi     = {10.1016/j.xnsj.2024.100564}
}
```

### R071. DeepSPINE (MLHC 2018)
- Full title: Deep Spine: Automated Lumbar Vertebral Segmentation, Disc-level Designation, and Spinal Stenosis Grading Using Deep Learning
- Authors: Lu J-T, Pedemonte S, Bizzo B, et al. (Doyle S, Andriole KP, Michalski MH, Gonzalez RG, Pomerantz SR)
- Year / Venue / Type: 2018 / Proceedings of the 3rd Machine Learning for Healthcare Conference, PMLR 85:403–419 / conference
- DOI / arXiv / URL: arXiv:1807.10215; https://proceedings.mlr.press/v85/lu18a.html
- Access: open
- Passes: 3/3 full text (arXiv HTML)
- Modality & anatomy: lumbar MRI, sagittal T2 + axial T2
- Data: MGH, 7,108 exams (Apr 2016–Oct 2017, 57 radiologists) → 22,796 disc levels / 4,075 patients; labels mined from free-text reports by regex/NLP into normal/mild/moderate/severe (intermediates merged upward); split 15,957/3,419/3,420.
- Method: U-Net vertebral segmentation on mid-sagittal slice → polynomial spine curve → disc-aligned axial (360×360×8) and sagittal (160×320×25) volumes → multi-input multi-task ResNeXt-50 (2D axial + 3D sagittal branches) with 3 heads (central, left/right foraminal), weighted CE.
- Key results: 4-class class-average accuracy: central 70.6%, foraminal 67.1%; mild+moderate merged: 80.4% / 78.1%; binary AUC 0.983 (central), 0.961 (foraminal); axial+sagittal > either alone.
- Code / weights / license: none released
- Useful for us: report-mining for weak labels at scale; spine-curve-based disc-aligned resampling; intermediate grades are hardest (reader variability).
- Limitations / notes: single institution; noisy single-reader labels; no kappa vs radiologists; scoliosis problematic.
- BibTeX:
```bibtex
@inproceedings{Lu2018DeepSPINE,
  author    = {Lu, Jen-Tang and Pedemonte, Stefano and Bizzo, Bernardo and Doyle, Sean and Andriole, Katherine P. and Michalski, Mark H. and Gonzalez, R. Gilberto and Pomerantz, Stuart R.},
  title     = {Deep Spine: Automated Lumbar Vertebral Segmentation, Disc-Level Designation, and Spinal Stenosis Grading using Deep Learning},
  booktitle = {Proceedings of the 3rd Machine Learning for Healthcare Conference},
  series    = {Proceedings of Machine Learning Research},
  volume    = {85},
  pages     = {403--419},
  year      = {2018},
  publisher = {PMLR}
}
```

---

#### C. AI for lumbar stenosis grading, facet/multi-finding AI, and the RSNA 2024 challenge

### R072. Hallinan et al. 2021 — DL for central canal, lateral recess and foraminal stenosis
- Full title: Deep Learning Model for Automated Detection and Classification of Central Canal, Lateral Recess, and Neural Foraminal Stenosis at Lumbar Spine MRI
- Authors: Hallinan JTPD, Zhu L, Yang K, Makmur A, Algazwi DAR, Thian YL, Lau S, Choo YS, Eide SE, Yap QV, Chan YH, Tan JH, Kumar N, Ooi BC, Yoshioka H, Quek ST (16, VERIFIED on pubs.rsna.org)
- Year / Venue / Type: 2021 / Radiology 300(1):130–138 / journal article
- DOI / arXiv / URL: 10.1148/radiol.2021204289
- Access: paywalled (abstract read on pubs.rsna.org)
- Passes: 2/3 (abstract with numbers; 2026-10-16 re-check of pubs.rsna.org: author list, figure captions and reference list — full text paywalled, so grading criteria/backbones/limitations still not read)
- Modality & anatomy: MRI lumbar, axial T2 + sagittal T1
- Data: 446 studies / 446 patients (Sept 2015–Sept 2018, Singapore; mean age 52 ± 19; 240 women); split 80/9/11 (internal test 50); external test 100 MRIs. Exclusions: instrumentation, poor quality, post-gadolinium, scoliosis. Reference: MSK radiologist with 31 y experience; comparators two subspecialists (5 and 9 y).
- Method: two-stage CNN — ROI detection then 4-class grading (normal, mild, moderate, severe); axial T2 for central canal and lateral recess, sagittal T1 for foramina (figure captions). CORRECTION: the memory-logged "Lee-type grading" is NOT confirmed — reference list cites Bartynski & Lin 2003 (lateral recess), Schizas 2010 (DG03) and Andreisek 2014, and no Lee reference was visible; backbones not named in visible text (Faster R-CNN and ResNet are cited).
- Key results: central canal detection recall >99%; foraminal detection recall 84.5% (model) vs 83.9%/97.1% radiologists; dichotomous (normal/mild vs moderate/severe) Gwet kappa internal: central 0.98/0.98/0.96, lateral recess 0.92/0.95/0.92, foramina 0.94/0.95/0.89 (radiologist1/radiologist2/model as listed); external kappa 0.95–0.96.
- Code / weights / license: not released (unverified)
- Useful for us: reference design for three-region stenosis grading with dichotomised clinically relevant threshold (moderate+); uses Gwet kappa — adopt for skewed class distributions.
- Limitations / notes: small (446), single country; scoliosis excluded; dichotomised metrics flatter; foraminal hardest.
- BibTeX:
```bibtex
@article{Hallinan2021DeepLearning,
  author  = {Hallinan, James Thomas Patrick Decourcy and Zhu, Lei and Yang, Kaiyuan and Makmur, Andrew and Algazwi, Diyaa Abdul Rauf and Thian, Yee Liang and Lau, Samuel and Choo, Yun Song and Eide, Sterling Ellis and Yap, Qai Ven and Chan, Yiong Huak and Tan, Jiong Hao and Kumar, Naresh and Ooi, Beng Chin and Yoshioka, Hiroshi and Quek, Swee Tian},
  title   = {Deep Learning Model for Automated Detection and Classification of Central Canal, Lateral Recess, and Neural Foraminal Stenosis at Lumbar Spine {MRI}},
  journal = {Radiology},
  year    = {2021},
  volume  = {300},
  number  = {1},
  pages   = {130--138},
  doi     = {10.1148/radiol.2021204289}
}
```

### R073. RSNA LumbarDISC dataset paper (RSNA 2024 challenge data)
- Full title: The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset
- Authors: Richards TJ, Flanders AE, Colak E, Prevedello LM, Ball RL, Kitamura F, Mongan J, Vazirabad M, Lin H-M, Kendell A, Kanthawang T, Angkurawaranon S, Altinmakas E, Dogan H, de Aguiar Kuriki PE, Somasundaram A, Ruston C, Bulja D, Spahovic N, Sommer J, Jiang S, Farina EMJM, Nunes EC, Brassil M, McNamara M, Ortiz J, Peoples J, Uytana VL, Kam A, Dola VNS, Murphy D, Vu D, Dataset Contributor Group, Dataset Annotator Group, Competition Data Notebook Group, Talbott JF (full list verified on arXiv abs page)
- Year / Venue / Type: 2026 (journal) / Radiology: Artificial Intelligence 8(2):e250480 ("Data Resources" article; Crossref print date 2026-03-01); preprint arXiv:2506.09162v1 (eess.IV, cs.CV; submitted 2025-06-10; CC BY-NC-SA 4.0)
- DOI / arXiv / URL: 10.1148/ryai.250480 (VERIFIED via Crossref); arXiv:2506.09162 (10.48550/arXiv.2506.09162); data: https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification and https://mira.rsna.org/dataset/6 ; also listed on AWS Open Data registry (RSNA-LSDD)
- Access: open (preprint); journal version via pubs.rsna.org
- Passes: 3/3 (2026-10-16: arXiv abs page; arXiv PDF full text read twice — pass 2 methods/data/splits/label counts, pass 3 limitations/QC/access; journal record checked on pubs.rsna.org + Crossref. Appendix C grading definitions not extractable from PDF text — likely a figure/table; competition metric NOT described in the paper)
- Modality & anatomy: lumbar MRI; L1/L2–L5/S1. Sequences: sagittal "T2-like" (spin-echo T2, STIR or Dixon) -> spinal canal grading; sagittal T1 -> neural foraminal grading; axial T2 (continuous stack or disc-parallel, >=3 disc levels) -> subarticular recess grading. Site minimum: sag T1, sag fat-sat T2, continuous axial T2.
- Data: 2,697 patients (1,381 M / 1,316 F; age 57.1 ± 16.0 y, range 18–89), 8,593 series, 8 institutions in 6 countries (Thailand, Bosnia and Herzegovina, Australia, Turkey, USA, Brazil; "5 continents"); per-site 94–631 cases. Splits: train 1,981 studies; public test 272; private test 444 (test stratified by site, age group, sex, per-level severity; moderate/severe at L1/2, L2/3, L5/S1 oversampled in test). Inclusion: outpatient non-contrast lumbar MRI, age >=18, prior surgery without hardware allowed. Exclusion: lumbosacral hardware, active non-degenerative pathology (tumour/infection), severe scoliosis, diagnostic-limiting artefact or motion, incomplete FOV, large canal mass.
- Method (annotation): volunteer neuroradiologists/MSK radiologists + 2nd-year neuroradiology fellows recruited via RSNA/ASNR/ASSR (~55 names in annotator group); each annotator graded ONE location type only; qualification on 10 practice cases (25 labels each) requiring >=60% agreement with committee consensus. Grading 4-point (normal, mild, moderate, severe) collapsed to 3 (normal/mild, moderate, severe). Training studies annotated ONCE; public/private test studies received 1–3 extra reads until 2 annotators agreed (consensus). Tool: MD.ai. One (x,y) point localiser per label: thecal-sac midline (canal), foramen centre, within recess (subarticular), placed at disc level; L5/S1 labelled beforehand by a committee member. QC scripts for L/R mismatches, spatial outliers, missing labels; image collages to check exclusions and sequence labels.
- Key results (label distribution): spinal canal 13,474 grades = 85.4% normal/mild, 8.8% moderate, 5.9% severe; foramina 26,919 grades = R 78.3/17.3/4.4%, L 77.2/18.1/4.6%; subarticular 26,285 grades = R 69.4/19.6/10.9%, L 69.5/19.2/11.3%. Moderate/severe counts by level L1/2→L5/S1 (Table 2): foramen mod 36/97/181/259/197, sev 13/17/55/94/111; subarticular mod 91/150/240/275/167, sev 26/86/174/275/112; canal mod 35/66/89/73/22, sev 8/30/65/79/20.
- Code / weights / license: data free for non-commercial research (DICOM + CSV: train.csv, label coordinates, series descriptions); preprint text CC BY-NC-SA 4.0.
- Useful for us: CENTRAL — primary public training/validation set for multi-condition, multi-level lumbar grading (25 targets/study = 5 levels × 5 condition-sides). Point localisers give free supervision for a level-localisation stage. Use the per-level counts to justify class weighting and to warn about sparse severe cases at upper levels.
- Limitations / notes: (1) training labels are SINGLE-reader -> label noise ceiling; only test sets have 2-reader consensus; (2) no inter-rater kappa reported (only the 60% qualification threshold and 2-agree rule); (3) few high-grade cases at L1/2, L2/3; (4) test sets enriched for moderate/severe — not natural prevalence, so calibration/PPV do not transfer; (5) deliberately loose protocol -> acquisition heterogeneity; (6) normal and mild merged — cannot train a 4-grade model; (7) private-test labels hidden (Kaggle) — external users can only evaluate on train CV unless via late-submission scoring. Open question: exact grading definitions (Appendix C) must be read from the journal supplement before we cite thresholds.
- BibTeX:
```bibtex
@article{Richards2026LumbarDISC,
  author  = {Richards, Tyler J. and Flanders, Adam E. and Colak, Errol and Prevedello, Luciano M. and Ball, Robyn L. and Kitamura, Felipe and Mongan, John and Vazirabad, Maryam and Lin, Hui-Ming and Kendell, Anne and others and Talbott, Jason F.},
  title   = {The {RSNA} Lumbar Degenerative Imaging Spine Classification ({LumbarDISC}) Dataset},
  journal = {Radiology: Artificial Intelligence},
  year    = {2026},
  volume  = {8},
  number  = {2},
  pages   = {e250480},
  doi     = {10.1148/ryai.250480},
  note    = {Preprint: arXiv:2506.09162}
}
```

### R074. RSNA 2024 Lumbar Spine Degenerative Classification AI Challenge (Kaggle) + top solutions
- Full title: RSNA 2024 Lumbar Spine Degenerative Classification (Kaggle competition) / RSNA Lumbar Spine Degenerative Classification AI Challenge
- Authors: RSNA with ASNR (supported by Vision Radiology); organisers per DG31
- Year / Venue / Type: 2024 / Kaggle + RSNA AI Image Challenge / challenge
- DOI / arXiv / URL: https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification ; https://www.rsna.org/artificial-intelligence/ai-image-challenge/lumbar-spine-degenerative-classification-ai-challenge ; winner write-ups: Kaggle discussion IDs 540091 (1st Avengers), 539452 (2nd IanPan-Kevin-Yuji-Bartley), 539453 (3rd SonySpine), 539443 (SPINE CHART), 539472 (Two people), 541813 (NVSpine), 539486 (HLIP), 539548 (K_mataro), 539690 (Adam Narai) — all under .../rsna-2024-lumbar-spine-degenerative-classification/discussion/<id>
- Access: open
- Passes: 3/3 (2026-10-16: RSNA challenge page; final standings via clist.by; secondary summary (zenn.dev/mkj/articles/ba630a8837ee72); PRIMARY sources: official GitHub READMEs of 2nd (brendanartley/RSNA-2024-Competition; i-pan/rsna-lspine; yujiariyasu/rsna_2024_lumbar_spine_degenerative_classification), 3rd (Moyasii/Kaggle-2024-RSNA-Pub) and 4th (tattaka/rsna-2024-lumbar-spine-degenerative-classification-public) place; repo list via albumentations.ai adoption page. Kaggle write-ups and evaluation page still JS-only — 1st-place details and metric text remain secondary)
- Modality & anatomy: lumbar MRI (sag T1, sag T2/STIR, axial T2), L1/L2–L5/S1
- Data: as DG31 (train 1,981 studies; hidden public 272 / private 444 test)
- Method / metric: 25 labels per study (5 conditions [spinal canal; L/R neural foraminal; L/R subarticular] × 5 levels), 3 classes each (75 probabilities). Metric = sample-weighted log loss averaged over conditions with weights normal/mild 1, moderate 2, severe 4, PLUS an "any_severe_spinal" binary term (per study, max severe probability over spinal-canal levels vs. whether any level is severe) — per secondary summary; confirm against Kaggle evaluation page before quoting.
- Key results: 1,874 teams (record for an RSNA challenge); $50,000 shared by 9 prize teams. Final private-LB scores (clist.by, 2 d.p.): ranks 1–3 = 0.39 (Avengers; IanPan-Kevin-Yuji-Bartley; SonySpine s & tkmn & Moyashii), ranks 4–9 = 0.40 (SPINE CHART, Two people, NVSpine, HLIP, K_mataro, Adam Narai), ranks 10–12 = 0.41 — i.e. the top is very flat. Educational Merit Awards: Avengers and SonySpine.
  - 1st (Avengers): two-stage. Stage 1: 3D ConvNeXt predicts the best slice (instance number) per level, then 2D ConvNeXt regresses disc coordinates at 512×512; Stage 2: ConvNeXt-small + EfficientNetV2-S crop encoders with bi-LSTM and attention-based MIL; L1 loss for regression, CE for classification + auxiliary loss; shift augmentation probability tuned to stage-1 error rate.
  - 2nd (IanPan-Kevin-Yuji-Bartley): ensemble of three members' pipelines — (a) YOLOX disc detection -> ConvNeXt-S classifier; (b) CNN-transformer slice identification (distance regression + classification) -> keypoint regression -> coordinate-based crops (3–5 adjacent slices as channels, 27 slice/spatial offset crops) with 2D CNN / attention pooling / MIL heads, backbones MaxViT, CoAtNet, NFNet, CSN-ResNet101; (c) sagittal-only, central 24 frames, 2D backbone + attention head localisation, encoder + LSTM + attention pooling, manifold mixup, 9-rotation TTA, 50:50 labelled/pseudo-labelled data. Team findings: dropping high-loss (noisy) training samples gave a major gain; multiplying severe probabilities by 1.25 improved the weighted log loss.
  - 3rd (SonySpine): CenterNet-style detector (EfficientNet-B6/B4 + FPN) -> 2D encoder with attention, centre and side classifiers, "split LR" handling, manual label correction + pseudo-labels.
  - Primary-repo details (VERIFIED from READMEs): 2nd place, Artley part — sagittal only (T2 for spinal + subarticular, T1 for foraminal); stage 1 attention-head 2D model on 8 middle frames predicts 10 coordinates (2/disc), within 5 px of GT ~99.1%; crop height = mean inter-level distance; stage 2 encoder -> LSTM -> attention pooling on 24 (T1) or 5–16 (T2) frames; loss 0.5×labels + 0.5×pseudo-labels; noisy labels removed by confident learning on an out-of-fold team ensemble; 9-rotation TTA; an axial-T2 pipeline gave only +0.01–0.02 CV and was not used; 1× A100 40 GB, ~24 h; external Kaggle "lumbar-coordinate-pretraining-dataset" (corrected coordinates). 3rd place — axial + sagittal keypoint detectors -> crops -> centre and side classifiers, pseudo-labels; MIT licence; some models need 48 GB VRAM. 4th place (SPINE CHART, tattaka part) — keypoint stage 1 with CaFormer/ConvNeXt/ResNet-RS-50/SwinV2 on 256×256 volumes; stage 2 CaFormer-S18/ResNet-RS-50/SwinV2-T at original resolution; uses the lumbar coordinate dataset; MIT; 4× RTX A4000. No README reports CV/LB numbers. Ian Pan repo: MIT (README not rendered).
  - Cross-team pattern: localise (slice + keypoint) -> crop -> grade; attention/LSTM/MIL aggregation over slices; heavy use of a community external coordinate dataset (Kaggle discussion 524500); official keypoint labels contained many errors and were corrected or filtered.
- Code / weights / license: public code — 2nd: github.com/brendanartley/RSNA-2024-Competition (no licence stated), github.com/i-pan/rsna-lspine (MIT), github.com/yujiariyasu/rsna_2024_lumbar_spine_degenerative_classification (not opened); 3rd: github.com/Moyasii/Kaggle-2024-RSNA-Pub (MIT; weights on Kaggle dataset akinosora/rsna2024-lsdc-3rd-models-pub); 4th: github.com/tattaka/rsna-2024-lumbar-spine-degenerative-classification-public (MIT); 13th: github.com/claverru/RSNA-lumbar. 1st-place code not located. Competition data non-commercial.
- Useful for us: CENTRAL — benchmark protocol and metric; the two-stage localise-then-grade design with slice selection is the practical SOTA; "noisy single-reader labels -> loss-based filtering" and "severe-probability rescaling" are directly reusable ideas; the flat top-LB (0.39–0.41) suggests we are near the label-noise ceiling and should report kappa/AUC alongside log loss.
- Limitations / notes: leaderboard metric (weighted log loss) rewards calibration and post-hoc probability scaling, not ordinal agreement — report both log loss and per-condition kappa/AUC; private-test labels hidden; no published peer-reviewed winners' analysis found yet (search 2026-10-16). TODO: read primary write-ups when Kaggle renders, and exact metric text.
- BibTeX:
```bibtex
@misc{RSNA2024LumbarChallenge,
  author       = {{Radiological Society of North America} and {American Society of Neuroradiology}},
  title        = {{RSNA} 2024 Lumbar Spine Degenerative Classification},
  year         = {2024},
  howpublished = {Kaggle competition},
  url          = {https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification}
}
```

### R075. Won et al. 2020 — CNN grading of lumbar spinal stenosis
- Full title: Spinal Stenosis Grading in Magnetic Resonance Imaging Using Deep Convolutional Neural Networks
- Authors: Won D, Lee HJ, Lee SJ, Park SH (VERIFIED via OpenAlex)
- Year / Venue / Type: 2020 / Spine 45(12):804–812 / journal article (VERIFIED)
- DOI / arXiv / URL: 10.1097/BRS.0000000000003377
- Access: paywalled
- Passes: 2/3 (2026-10-16: full structured abstract via OpenAlex inverted index; full text paywalled)
- Modality & anatomy: lumbar MRI axial, L4–5 only, central canal
- Data: 542 L4–5 axial MR images; two experts independently localised the canal centre and graded stenosis (grade scale not specified in abstract); 10-fold CV
- Method: per-expert pipelines: Faster R-CNN detects patch near the canal -> VGG classifier predicts stenosis grade; one model trained on each expert's labels
- Key results: expert-vs-expert agreement accuracy 77.5% / F1 75%; expert 1 vs model-1 83% / 75.4%; expert 2 vs model-2 77.9% / 74.9%; expert-expert differences significant, expert-model differences not significant.
- Code / weights / license: not stated
- Useful for us: early detect-then-grade stenosis design explicitly benchmarked against inter-expert agreement (~77% accuracy) — the "human ceiling" framing we need; shows models inherit their annotator's bias (train-on-one-expert).
- Limitations / notes: single level (L4–5), single slice images, small dataset, single centre (Korea; not stated in abstract), only accuracy/F1 (no kappa).
- BibTeX:
```bibtex
@article{Won2020SpinalStenosis,
  author  = {Won, Dongkyu and Lee, Hyun-Joo and Lee, Suk-Joong and Park, Sang Hyun},
  title   = {Spinal Stenosis Grading in Magnetic Resonance Imaging Using Deep Convolutional Neural Networks},
  journal = {Spine},
  year    = {2020},
  volume  = {45},
  number  = {12},
  pages   = {804--812},
  doi     = {10.1097/BRS.0000000000003377}
}
```

### R076. Lehnen et al. 2021 — CNN detection of degenerative changes on lumbar MRI
- Full title: Detection of Degenerative Changes on MR Images of the Lumbar Spine with a Convolutional Neural Network: A Feasibility Study
- Authors: Lehnen NC, Haase R, Faber J, Rüber T, Vatter H, Radbruch A, Schmeel FC (VERIFIED, DZNE repository record)
- Year / Venue / Type: 2021 / Diagnostics (MDPI) 11(5):902 (VERIFIED) / journal article
- DOI / arXiv / URL: 10.3390/diagnostics11050902 (VERIFIED); PMID 34069362; PMCID PMC8158737
- Access: open (MDPI, CC BY)
- Passes: 3/3 (2026-10-16: bibliographic record via pub.dzne.de; full text via mdpi.com — methods, results table, limitations, COI. Prior 0/3 metadata was correct except it lacked DOI/full author list)
- Modality & anatomy: lumbar MRI (Philips 1.5 T/3 T; sag T1 SE, sag + axial T2 TSE, sag T2 SPAIR/mDixon), Th12/L1–S1
- Data: 146 consecutive LBP patients (single centre, Bonn; 81 M/65 F; mean age 48.7, range 19–70; 421/567 screened excluded: age >70, prior surgery, trauma, cancer); 888 segments for herniation/bulge/stenosis, 1,036 for nerve-root compression. Reference: ONE radiologist (5 y spine experience) with reports and history; nomenclature 2.0 (DG05), Meyerding (DG13), Lee et al. stenosis; dural-sac area thresholds 75–100 mm² relative, <75 mm² absolute stenosis (vendor thresholds).
- Method: commercial CoLumbo (SmartSoft Ltd., Varna, Bulgaria) — 2D U-Net-based CNN per plane, trained by the vendor on 1,500 studies from three European centres (1.5 T); preclinical CPU version, mean 9 min 25 s per study.
- Key results (accuracy vs reader): vertebra/disc labelling 100%; herniation 86.8% (58 TP / 19 FN); extrusion 86.5% (41/46 detected); bulging 75.6% (69 TP / 64 FN); canal stenosis 98.1% (27 TP / 9 FN); nerve-root compression 90.5% (42 TP / 17 FN); spondylolisthesis 87.6% (4 FN, 106 FP, PPV 13.1%). Sensitivity 52–89%, specificity 80–99%, PPV 13–75% across findings. Prevalence in reference: herniation 8.7%, extrusion 5.2%, bulge 15.0%, stenosis 3.9%, root compression 5.7%, listhesis 2.3% (all grade I). No AUC/kappa.
- Code / weights / license: proprietary (CoLumbo); authors received a free research version; CNN developed/trained by the vendor; authors declare no conflicts, no external funding.
- Useful for us: multi-finding detection comparator from a commercial product; dural-sac area thresholds as quantitative stenosis definition; illustrates the low-PPV problem on low-prevalence findings — argues for calibrated probabilities and reporting PPV at clinical prevalence.
- Limitations / notes: single reader, single centre, small n, retrospective; vendor-developed model; low PPVs (partly because reader omitted clinically insignificant findings); segmentation accuracy not assessed; abstract rounds numbers differently from results (cite results section).
- BibTeX:
```bibtex
@article{Lehnen2021Degenerative,
  author  = {Lehnen, Nils Christian and Haase, Robert and Faber, Jennifer and R{\"u}ber, Theodor and Vatter, Hartmut and Radbruch, Alexander and Schmeel, Frederic Carsten},
  title   = {Detection of Degenerative Changes on {MR} Images of the Lumbar Spine with a Convolutional Neural Network: A Feasibility Study},
  journal = {Diagnostics},
  year    = {2021},
  volume  = {11},
  number  = {5},
  pages   = {902},
  doi     = {10.3390/diagnostics11050902}
}
```

### R077. Bharadwaj et al. 2023 — interpretable DL for stenosis and facet arthropathy from axial MRI
- Full title: Deep learning for automated, interpretable classification of lumbar spinal stenosis and facet arthropathy from axial MRI
- Authors: Bharadwaj UU (first), … Christine M, Li S, Chou D, Chin CT, Link TM, Pedoia V, Majumdar S (senior) — names confirmed on UCSF ci2 news page; exact order beyond first/last unverified
- Year / Venue / Type: 2023 (DOI year) / European Radiology (venue confirmed; volume/pages unverified — Crossref 429, SpringerLink fetch failed) / journal article
- DOI / arXiv / URL: 10.1007/s00330-023-09483-6 (from UCSF ci2 news link to SpringerLink); PMC10566647 (seen in search results; PMC blocked by captcha)
- Access: paywalled
- Passes: 1/3 (2026-10-16: UCSF ci2 news page — title, venue, DOI link, author names, data size; journal abstract/full text NOT read) [2026-10-16 round 3: not upgraded — Eur Radiol (Springer) and PMC10566647 both unreachable (Springer fetch error, PMC captcha)]
- Modality & anatomy: lumbar MRI axial T2; central canal, lateral recess, foramina, facet joints
- Data: 200 axial lumbar MRI studies (UCSF, acquired 2008–2019) split into train/val/test (split sizes not given on news page)
- Method: axial T2 slices -> V-Net segmentation of disc and dural sac -> classification of central canal stenosis, neural foraminal stenosis and facet arthropathy (interpretable via masks); other details unverified
- Key results: news page: performance "comparable to inter-reader agreement"; no numbers read yet — TODO read abstract
- Code / weights / license: unverified
- Useful for us: one of few AI papers that grade facet arthropathy — relevant to Weishaupt-style labels.
- Limitations / notes: verify all.
- BibTeX:
```bibtex
@article{Bharadwaj2023Interpretable,
  author  = {Bharadwaj, Upasana Upadhyay and others},
  title   = {Deep learning for automated, interpretable classification of lumbar spinal stenosis and facet arthropathy from axial {MRI}},
  journal = {European Radiology},
  year    = {2023},
  doi     = {10.1007/s00330-023-09483-6},
  note    = {Volume/pages and full author list unverified}
}
```

### R078. Lewandrowski et al. 2020 — DL-generated reports for routine lumbar MRI (RadBot reliability)
- Full title: Reliability Analysis of Deep Learning Algorithms for Reporting of Routine Lumbar MRI Scans
  (CORRECTED 2026-10-16 — the memory-logged title "Feasibility of deep learning algorithms for reporting in routine spine magnetic resonance imaging" and venue "Journal of Spine Surgery" were WRONG)
- Authors: Lewandrowski KU, Muraleedharan N, Eddy SA, Sobti V, Reece BD, Ramírez León JF, Shah S (VERIFIED)
- Year / Venue / Type: 2020 / International Journal of Spine Surgery 14(s3):S98–S107 (Dec 2020; online 2020-10-29) (VERIFIED on ijssurgery.com) / journal article
- DOI / arXiv / URL: 10.14444/7132 (VERIFIED)
- Access: open (ijssurgery.com PDF)
- Passes: 3/3 (2026-10-16: full PDF (early-online version) read — methods, results, limitations, COI; final citation from journal landing page)
- Modality & anatomy: lumbar MRI, T12/L1–L5/S1
- Data: 65 patients, 383 disc levels, one imaging centre (mean age 42.2 ± 11.8 y; 51.5% male); reference = original board-certified radiologist reports (one radiologist per scan)
- Method: Multus RadBot — "self-learning" deep neural network + NLP model that generates verbal and written reports (architecture not specified). Findings: central canal stenosis (4 grades) and L/R foraminal stenosis, collapsed to normal vs stenosis for analysis.
- Key results: stenosis reported at 64.2% of levels by RadBot vs 60.6% by radiologists; sensitivity 73.3%, specificity 88.4%, PPV 80.3%, NPV 83.7%; Cohen's kappa 0.627 overall (L2–L3 0.738, L3–L4 0.606); Cronbach's alpha 0.772; AUC 0.808 (95% CI 0.760–0.857).
- Code / weights / license: proprietary (Multus Medical LLC)
- Useful for us: prior art for automated lumbar MRI report generation and for agreement-with-report evaluation (kappa vs free-text reports); a weak baseline to beat.
- Limitations / notes: reference = clinical report assumed error-free, single reader; binary dichotomisation; retrospective single-centre, small n; architecture undisclosed; several authors affiliated with the vendor (Multus Medical) — conflict not explicitly declared in paper. Treat as low-evidence.
- BibTeX:
```bibtex
@article{Lewandrowski2020RadBot,
  author  = {Lewandrowski, Kai-Uwe and Muraleedharan, Narendran and Eddy, Steven Allen and Sobti, Vikram and Reece, Brian D. and Ram{\'i}rez Le{\'o}n, Jorge Felipe and Shah, Sandeep},
  title   = {Reliability Analysis of Deep Learning Algorithms for Reporting of Routine Lumbar {MRI} Scans},
  journal = {International Journal of Spine Surgery},
  year    = {2020},
  volume  = {14},
  number  = {s3},
  pages   = {S98--S107},
  doi     = {10.14444/7132}
}
```

---

#### D. Inter-reader agreement and variability (the human ceiling)

### R079. Carrino et al. 2009 — reliability of lumbar MRI findings (SPORT)
- Full title: Lumbar Spine: Reliability of MR Imaging Findings
- Authors: Carrino JA, Lurie JD, Tosteson ANA, et al. (Tosteson TD, Carragee EJ, Kaiser J, Grove MR, Blood E, Pearson LH, Weinstein JN, Herzog R)
- Year / Venue / Type: 2009 / Radiology 250(1):161–170 / journal article
- DOI / arXiv / URL: 10.1148/radiol.2493071999
- Access: paywalled (abstract/summary read on pubs.rsna.org)
- Passes: 2/3
- Modality & anatomy: lumbar MRI
- Data: 111 randomly selected SPORT MRIs (age 18–87, mean 53); 4 independent readers; 40 re-read ≥1 month later
- Method: weighted kappa
- Key results: inter-observer: disc degeneration 0.66, spondylolisthesis 0.55, Modic 0.59, facet arthropathy 0.54, posterior HIZ 0.44; Modic extent 0.43–0.57. Intra-observer: disc degeneration 0.74, facet 0.69, HIZ 0.67, spondylolisthesis 0.66, Modic 0.64.
- Code / weights / license: —
- Useful for us: quantitative human ceiling (κ≈0.45–0.66 inter-reader) to contextualise model kappa.
- Limitations / notes: stenosis/herniation reliability reported in companion Lurie 2008 papers (not verified here).
- BibTeX:
```bibtex
@article{Carrino2009Reliability,
  author  = {Carrino, John A. and Lurie, Jon D. and Tosteson, Anna N. A. and Tosteson, Tor D. and Carragee, Eugene J. and Kaiser, Jay and Grove, Margaret R. and Blood, Emily and Pearson, Loretta H. and Weinstein, James N. and Herzog, Richard},
  title   = {Lumbar Spine: Reliability of {MR} Imaging Findings},
  journal = {Radiology},
  year    = {2009},
  volume  = {250},
  number  = {1},
  pages   = {161--170},
  doi     = {10.1148/radiol.2493071999}
}
```

### R080. Herzog et al. 2017 — variability across 10 MRI centres
- Full title: Variability in diagnostic error rates of 10 MRI centers performing lumbar spine MRI examinations on the same patient within a 3-week period
- Authors: Herzog R, Elgort DR, Flanders AE, Moley PJ
- Year / Venue / Type: 2017 (print; OpenAlex lists online year 2016) / The Spine Journal 17(4):554–561 / prospective observational study (VERIFIED via OpenAlex)
- DOI / arXiv / URL: 10.1016/j.spinee.2016.11.009
- Access: paywalled
- Passes: 2/3 (2026-10-16: full structured abstract via OpenAlex; full text paywalled)
- Modality & anatomy: lumbar MRI
- Data: one 63-year-old woman with LBP and right L5 radicular symptoms, scanned at 10 MRI centres within 3 weeks plus reference MRIs immediately before and after; reference diagnosis by consensus of two subspecialist spine radiologists
- Method: findings per motion segment tabulated from the 10 reports; percent agreement, Fleiss kappa; TP/FP/FN vs reference (25 reference findings)
- Key results (VERIFIED): 49 distinct findings reported across the 10 reports; none reported by all 10, only one by 9/10; 32.7% appeared in only one report; global Fleiss kappa 0.20 ± 0.06 (poor); mean interpretive errors 12.5 ± 3.2 per exam (FN 10.9 ± 2.9 of 25, FP 1.6 ± 0.9); mean sensitivity 56.4% ± 11.7 (miss rate 43.6%).
- Code / weights / license: —
- Useful for us: motivates standardised, automated, reproducible reporting; illustrates acquisition + interpretation variability.
- Limitations / notes: n = 1 patient; confounds acquisition differences with reader differences; reference standard is itself a 2-reader consensus. Co-author Flanders is also an RSNA LumbarDISC organiser (DG31).
- BibTeX:
```bibtex
@article{Herzog2017Variability,
  author  = {Herzog, Richard and Elgort, Daniel R. and Flanders, Adam E. and Moley, Peter J.},
  title   = {Variability in diagnostic error rates of 10 {MRI} centers performing lumbar spine {MRI} examinations on the same patient within a 3-week period},
  journal = {The Spine Journal},
  year    = {2017},
  volume  = {17},
  number  = {4},
  pages   = {554--561},
  doi     = {10.1016/j.spinee.2016.11.009}
}
```

### R081. Lurie et al. 2008 — reliability of MRI features of lumbar spinal stenosis (SPORT)
- Full title: Reliability of Readings of Magnetic Resonance Imaging Features of Lumbar Spinal Stenosis
- Authors: Lurie JD, Tosteson AN, Tosteson TD, et al. (Carragee E, Carrino J, Kaiser J, Blanco Sequeiros RT, Lecomte AR, Grove MR, Blood EA, Pearson LH, Weinstein JN, Herzog R)
- Year / Venue / Type: 2008 (2008-06-15) / Spine 33(14):1605–1610 / journal article (reliability study) — year/vol/issue re-confirmed on Weill Cornell VIVO; PMID 18552677, PMCID PMC2754786
- DOI / arXiv / URL: 10.1097/BRS.0b013e3181791af3
- Access: paywalled
- Passes: 2/3 (2026-10-16: full abstract with numbers via Weill Cornell VIVO record; full text not opened)
- Modality & anatomy: lumbar MRI, central/lateral recess/foraminal stenosis
- Data: 58 randomly selected SPORT spinal-stenosis MRIs; 4 independent readers (3 radiologists, 1 orthopaedic surgeon); 20 MRIs re-read by each reader >=1 month later; 2 further radiologists for quantitative measurements
- Method: weighted kappa (qualitative features), ICC (quantitative measurements)
- Key results (VERIFIED): inter-reader kappa — central stenosis 0.73 (95% CI 0.69–0.77); foraminal stenosis 0.58 (0.53–0.63); nerve-root impingement 0.51 (0.42–0.59); subarticular (lateral recess) stenosis 0.49 (0.42–0.55), lowest with marked reader-pair variability. Intra-reader > inter-reader for all features. Quantitative inter-reader ICCs 0.58–0.90; mean absolute thecal-sac-area difference 128 mm² (13%) (abstract prints "mm").
- Code / weights / license: —
- Useful for us: CENTRAL human ceiling for exactly the three RSNA 2024 targets: central ~0.73 > foraminal ~0.58 > subarticular ~0.49 — mirrors the per-condition difficulty seen in RSNA 2024 models; companion to Carrino 2009 (DG40).
- Limitations / notes: small n (58); surgical-candidate cohort (spectrum bias); grading definitions per full text not checked.
- BibTeX:
```bibtex
@article{Lurie2008Reliability,
  author  = {Lurie, Jon D. and Tosteson, Anna N. and Tosteson, Tor D. and Carragee, Eugene and Carrino, John and Kaiser, Jay and Blanco Sequeiros, Roberto T. and Lecomte, Amy Rosen and Grove, Margaret R. and Blood, Emily A. and Pearson, Loretta H. and Weinstein, James N. and Herzog, Richard},
  title   = {Reliability of Readings of Magnetic Resonance Imaging Features of Lumbar Spinal Stenosis},
  journal = {Spine},
  year    = {2008},
  volume  = {33},
  number  = {14},
  pages   = {1605--1610},
  doi     = {10.1097/BRS.0b013e3181791af3}
}
```

### R082. Lurie et al. 2008 — reliability of MRI readings for lumbar disc herniation (SPORT)
- Full title: Reliability of magnetic resonance imaging readings for lumbar disc herniation in the Spine Patient Outcomes Research Trial (SPORT) (VERIFIED)
- Authors: Lurie JD, Tosteson ANA, Tosteson TD, Carragee E, Carrino J, Kaiser J, Blanco Sequeiros RT, Lecomte AR, Grove MR, Blood EA, Pearson LH, Herzog R, Weinstein JN (VERIFIED, Weill Cornell VIVO). CORRECTED: memory-logged authors "Doman DM, Spratt KF" were WRONG.
- Year / Venue / Type: 2008 (2008-04-20) / Spine 33(9):991–998 (VERIFIED via VIVO + OpenAlex). CORRECTED: memory-logged "2009, Spine 34(1):51" was WRONG / reliability study
- DOI / arXiv / URL: 10.1097/BRS.0b013e31816c8379 (VERIFIED); PMID 18427321; PMCID PMC2745940
- Access: open author manuscript on PMC (captcha-blocked here)
- Passes: 2/3 (2026-10-16: full abstract with numbers via VIVO record; pages via OpenAlex; full text not opened)
- Modality & anatomy: lumbar MRI, intervertebral disc herniation
- Data: 60 randomly selected SPORT IDH MRIs; 4 independent readers (3 radiologists, 1 orthopaedic surgeon) for ratings; 2 further radiologists for quantitative measurements; 20 MRIs re-read >=1 month later (intra-reader)
- Method: inter-/intra-reader agreement, linearly weighted kappa for categorical ratings; ICC for area measurements
- Key results: inter-reader kappa: disc morphology 0.81 (95% CI 0.78–0.85); thecal sac compression 0.54 (0.37–0.68); nerve-root impingement 0.47 (0.36–0.56). ICC: spinal canal and thecal sac cross-sectional areas 0.87–0.96; disc fragment area 0.65–0.83; mean absolute measurement differences ~15–20%.
- Code / weights / license: —
- Useful for us: human ceiling for herniation sub-typing (morphology kappa ~0.8) and especially for nerve-root impingement (~0.5) — AI kappa near these values is human-level; area measurements far more reliable than categorical grades, supporting quantitative outputs.
- Limitations / notes: small sample (60); SPORT cohort = surgical candidates with confirmed IDH (spectrum bias); kappa definitions per full text not checked.
- BibTeX:
```bibtex
@article{Lurie2008HerniationReliability,
  author  = {Lurie, Jon D. and Tosteson, Anna N. A. and Tosteson, Tor D. and Carragee, Eugene and Carrino, John and Kaiser, Jay and Blanco Sequeiros, Roberto T. and Lecomte, Amy Rosen and Grove, Margaret R. and Blood, Emily A. and Pearson, Loretta H. and Herzog, Richard and Weinstein, James N.},
  title   = {Reliability of magnetic resonance imaging readings for lumbar disc herniation in the {Spine Patient Outcomes Research Trial (SPORT)}},
  journal = {Spine},
  year    = {2008},
  volume  = {33},
  number  = {9},
  pages   = {991--998},
  doi     = {10.1097/BRS.0b013e31816c8379}
}
```

---

#### E. Degenerative findings in asymptomatic people (defining "normal" and "deviation from normal")

### R083. Brinjikji et al. 2015 — prevalence in asymptomatic populations
- Full title: Systematic Literature Review of Imaging Features of Spinal Degeneration in Asymptomatic Populations
- Authors: Brinjikji W, Luetmer PH, Comstock B, et al. (13 authors incl. Deyo RA, Kallmes DF, Jarvik JG)
- Year / Venue / Type: 2015 / AJNR Am J Neuroradiol 36(4):811–816 / systematic review
- DOI / arXiv / URL: 10.3174/ajnr.A4173
- Access: open (ajnr.org)
- Passes: 3/3 (abstract, methods, limitations read; Table 2 body not rendered)
- Modality & anatomy: MRI (32 studies) and CT (1), lumbar
- Data: 33 studies, 3,110 asymptomatic individuals (study n 8–412); literature to April 2014
- Method: generalised linear mixed-effects model for age-specific prevalence by decade (20s–80s)
- Key results: disc degeneration 37% at age 20 → 96% at 80; disc bulge 30% → 84%; protrusion 29% → 43%; annular fissure 19% → 29%; disc signal loss >50% over 40 and 86% by 60; facet degeneration 4–9% in 20s–30s rising sharply; spondylolisthesis 23% at 60 rising further; height loss and bulge rise ~1%/year.
- Code / weights / license: —
- Useful for us: CRUCIAL prior for "deviation from normal" — report age-conditioned prevalence alongside each finding (e.g., "disc bulge: seen in ~60% of asymptomatic 50-year-olds") to avoid over-medicalisation.
- Limitations / notes: volunteers, no severity grading, heterogeneous nomenclature over 25 years, single readers in many studies.
- BibTeX:
```bibtex
@article{Brinjikji2015Systematic,
  author  = {Brinjikji, W. and Luetmer, P. H. and Comstock, B. and Bresnahan, B. W. and Chen, L. E. and Deyo, R. A. and Halabi, S. and Turner, J. A. and Avins, A. L. and James, K. and Wald, J. T. and Kallmes, D. F. and Jarvik, J. G.},
  title   = {Systematic Literature Review of Imaging Features of Spinal Degeneration in Asymptomatic Populations},
  journal = {American Journal of Neuroradiology},
  year    = {2015},
  volume  = {36},
  number  = {4},
  pages   = {811--816},
  doi     = {10.3174/ajnr.A4173}
}
```

### R084. Brinjikji et al. 2015 — findings more prevalent with low back pain (meta-analysis)
- Full title: MRI Findings of Disc Degeneration are More Prevalent in Adults with Low Back Pain than in Asymptomatic Controls: A Systematic Review and Meta-Analysis
- Authors: Brinjikji W, Diehn FE, Jarvik JG, et al. (Carr CM, Kallmes DF, Murad MH, Luetmer PH)
- Year / Venue / Type: 2015 / AJNR 36(12):2394–2399 / systematic review + meta-analysis
- DOI / arXiv / URL: 10.3174/ajnr.A4498
- Access: open (ajnr.org)
- Passes: 3/3
- Modality & anatomy: lumbar MRI, adults ≤50 y
- Data: 14 of 280 studies; 3,097 individuals (1,193 asymptomatic, 1,904 symptomatic)
- Method: random-effects meta-analysis of 10+ findings
- Key results: ORs (symptomatic vs asymptomatic): disc bulge 7.54, spondylolysis 5.06, extrusion 4.38, Modic 1 4.01, protrusion 2.65, degeneration 2.24 (all significant); not significant: any Modic 1.62, central canal stenosis 20.58 (CI 0.05–798.77), HIZ 2.10, annular fissure 1.79, spondylolisthesis 1.59.
- Code / weights / license: —
- Useful for us: evidence-weighting for which findings matter clinically in younger patients; supports flagging extrusion/Modic 1 as more clinically meaningful than fissures.
- Limitations / notes: heterogeneity (I²>50%), presence-only, cross-sectional; not for diagnosis.
- BibTeX:
```bibtex
@article{Brinjikji2015MRIFindings,
  author  = {Brinjikji, W. and Diehn, F. E. and Jarvik, J. G. and Carr, C. M. and Kallmes, D. F. and Murad, M. H. and Luetmer, P. H.},
  title   = {{MRI} Findings of Disc Degeneration are More Prevalent in Adults with Low Back Pain than in Asymptomatic Controls: A Systematic Review and Meta-Analysis},
  journal = {American Journal of Neuroradiology},
  year    = {2015},
  volume  = {36},
  number  = {12},
  pages   = {2394--2399},
  doi     = {10.3174/ajnr.A4498}
}
```

### R085. Jensen et al. 1994 — lumbar MRI in people without back pain
- Full title: Magnetic Resonance Imaging of the Lumbar Spine in People without Back Pain
- Authors: Jensen MC, Brant-Zawadzki MN, Obuchowski NA, Modic MT, Malkasian D, Ross JS (VERIFIED via OpenAlex)
- Year / Venue / Type: 1994 (1994-07-14) / New England Journal of Medicine 331(2):69–73 / journal article (VERIFIED)
- DOI / arXiv / URL: 10.1056/NEJM199407143310201
- Access: paywalled (free archive abstract)
- Passes: 2/3 (2026-10-16: full abstract via OpenAlex; full text not opened)
- Modality & anatomy: lumbar MRI, 5 lumbar discs
- Data: 98 asymptomatic people; 27 symptomatic abnormal scans mixed in to reduce reader bias (VERIFIED)
- Method: two neuroradiologists read independently, blinded to clinical status; each disc classified normal / bulge / protrusion / extrusion; non-disc findings recorded
- Key results (VERIFIED; averages of two readers): only 36% had normal discs at all levels; bulge at >=1 level 52%; protrusion 27%; extrusion 1%; >1 abnormal disc 38%; bulges (not protrusions) increased with age; Schmorl's nodes 19%, annular defects 14%, facet arthropathy 8%; no sex difference.
- Code / weights / license: —
- Useful for us: classic evidence that bulges/protrusions are common without pain but extrusions are rare (1%) — supports weighting extrusion as a strong "abnormal" signal; uses the bulge/protrusion/extrusion nomenclature our labels follow.
- Limitations / notes: small sample; pre-dates nomenclature 2.0 (DG05) definitions; single centre.
- BibTeX:
```bibtex
@article{Jensen1994MRI,
  author  = {Jensen, Maureen C. and Brant-Zawadzki, Michael N. and Obuchowski, Nancy and Modic, Michael T. and Malkasian, Dennis and Ross, Jeffrey S.},
  title   = {Magnetic Resonance Imaging of the Lumbar Spine in People without Back Pain},
  journal = {New England Journal of Medicine},
  year    = {1994},
  volume  = {331},
  number  = {2},
  pages   = {69--73},
  doi     = {10.1056/NEJM199407143310201}
}
```

### R086. Jensen TS et al. 2008 — Modic changes: prevalence and association with LBP (systematic review)
- Full title: Vertebral endplate signal changes (Modic change): a systematic literature review of prevalence and association with non-specific low back pain
- Authors: Jensen TS, Karppinen J, Sorensen JS, Niinimäki J, Leboeuf-Yde C (VERIFIED via OpenAlex 2026-10-16; vol/issue/pages 17(11):1407–1422 also re-confirmed; abstract not available in OpenAlex)
- Year / Venue / Type: 2008 / European Spine Journal 17(11):1407–1422 / systematic review
- DOI / arXiv / URL: 10.1007/s00586-008-0770-2
- Access: open (PMC — unverified)
- Passes: 1/3 (metadata Crossref; abstract fetch blocked) [2026-10-16 round 3: not upgraded — Eur Spine J (Springer) — open copy likely on PMC but unreachable here]
- Modality & anatomy: lumbar MRI, endplates
- Data: pooled studies of LBP and non-LBP populations (counts unverified)
- Method: systematic review
- Key results: widely cited: median Modic prevalence ~43% in non-specific LBP patients vs ~6% in general/asymptomatic populations, positive association with LBP (unverified in this pass)
- Code / weights / license: —
- Useful for us: Modic prior prevalence for "deviation from normal" and clinical-relevance weighting.
- Limitations / notes: verify numbers.
- BibTeX:
```bibtex
@article{Jensen2008Modic,
  author  = {Jensen, Tue Secher and Karppinen, Jaro and Sorensen, Joan S. and Niinim{\"a}ki, Jaakko and Leboeuf-Yde, Charlotte},
  title   = {Vertebral endplate signal changes ({Modic} change): a systematic literature review of prevalence and association with non-specific low back pain},
  journal = {European Spine Journal},
  year    = {2008},
  volume  = {17},
  number  = {11},
  pages   = {1407--1422},
  doi     = {10.1007/s00586-008-0770-2}
}
```

### R087. Nakashima et al. 2015 — cervical MRI abnormalities in 1,211 asymptomatic subjects
- Full title: Abnormal Findings on Magnetic Resonance Images of the Cervical Spines in 1211 Asymptomatic Subjects
- Authors: Nakashima H, Yukawa Y, Suda K, Yamagata M, Ueta T, Kato F (VERIFIED via OpenAlex)
- Year / Venue / Type: 2015 / Spine 40(6):392–398 / cross-sectional study (VERIFIED)
- DOI / arXiv / URL: 10.1097/BRS.0000000000000775
- Access: paywalled
- Passes: 2/3 (2026-10-16: full structured abstract via OpenAlex; full text paywalled)
- Modality & anatomy: cervical MRI
- Data: 1,211 healthy volunteers aged 20–70, prospectively enrolled, ~100 per decade per sex (VERIFIED)
- Method: measured AP cord diameter, disc bulging, cord diameter and axial cord cross-sectional area; graded disc bulging, spinal cord compression (SCC) and increased cord signal intensity by age/sex
- Key results (VERIFIED): disc bulging 87.6% overall, increasing with age in frequency, severity and number of levels; even in the 20s 73.3% of men and 78.0% of women had bulging; SCC 5.3%, increased cord signal 2.3%, both rising after age 50; SCC mostly 1 level (58%) or 2 levels (38%), predominantly C5–C6 (41%) and C6–C7 (27%).
- Code / weights / license: —
- Useful for us: cervical normative prevalence by age/level for "deviation from normal" — bulging is normal at any age; cord compression and T2 cord signal are rare (<6%) and should be flagged.
- Limitations / notes: Japanese single-region cohort; the bulging grading scheme used should be checked in full text before mapping to Kang grades (DG11).
- BibTeX:
```bibtex
@article{Nakashima2015Cervical,
  author  = {Nakashima, Hiroaki and Yukawa, Yasutsugu and Suda, Kota and Yamagata, Masatsune and Ueta, Takayoshi and Kato, Fumihiko},
  title   = {Abnormal Findings on Magnetic Resonance Images of the Cervical Spines in 1211 Asymptomatic Subjects},
  journal = {Spine},
  year    = {2015},
  volume  = {40},
  number  = {6},
  pages   = {392--398},
  doi     = {10.1097/BRS.0000000000000775}
}
```

### R088. Boden et al. 1990 — abnormal lumbar MRI in asymptomatic subjects
- Full title: Abnormal magnetic-resonance scans of the lumbar spine in asymptomatic subjects. A prospective investigation
- Authors: Boden SD, Davis DO, Dina TS, Patronas NJ, Wiesel SW (VERIFIED via OpenAlex)
- Year / Venue / Type: 1990 / Journal of Bone and Joint Surgery Am 72(3):403–408 (verified via Crossref + OpenAlex) / prospective study
- DOI / arXiv / URL: 10.2106/00004623-199072030-00013 (verified)
- Access: paywalled
- Passes: 2/3 (2026-10-16: full abstract via OpenAlex; full text not opened)
- Modality & anatomy: lumbar MRI
- Data: 67 individuals who had never had LBP, sciatica or neurogenic claudication (VERIFIED)
- Method: three neuroradiologists read independently, blinded to symptom status (the abstract does NOT state that symptomatic scans were mixed in — earlier memory-logged claim removed)
- Key results (VERIFIED; CORRECTED): about one-third of all subjects had a substantial abnormality. Age <60: 20% herniated nucleus pulposus, one subject with stenosis. Age >=60: ~57% abnormal scans — 36% herniated nucleus pulposus, 21% spinal stenosis. Disc degeneration or bulging at >=1 level in 35% of those aged 20–39 and in all but one of those aged 60–80. (Earlier entry wrongly said "~20% of <60 y had abnormal scans".)
- Code / weights / license: —
- Useful for us: classic evidence that abnormal imaging is common without symptoms, strongly age-dependent → age-conditioned normative priors.
- Limitations / notes: small n (67); 1990-era MRI and pre-standard nomenclature ("HNP").
- BibTeX:
```bibtex
@article{Boden1990Abnormal,
  author  = {Boden, S. D. and Davis, D. O. and Dina, T. S. and Patronas, N. J. and Wiesel, S. W.},
  title   = {Abnormal magnetic-resonance scans of the lumbar spine in asymptomatic subjects. A prospective investigation},
  journal = {Journal of Bone and Joint Surgery. American Volume},
  year    = {1990},
  volume  = {72},
  number  = {3},
  pages   = {403--408},
  doi     = {10.2106/00004623-199072030-00013}
}
```

### R089. Teraguchi et al. 2014 — disc degeneration prevalence across whole spine (Wakayama Spine Study)
- Full title: Prevalence and distribution of intervertebral disc degeneration over the entire spine in a population-based cohort: the Wakayama Spine Study
- Authors: Teraguchi M, Yoshimura N, Hashizume H, Muraki S, Yamada H, Minamide A, Oka H, Ishimoto Y, Nagata K, Kagotani R, Takiguchi N, Akune T, Kawaguchi H, Nakamura K, Yoshida M (VERIFIED via Semantic Scholar)
- Year / Venue / Type: 2014 (online 2013) / Osteoarthritis and Cartilage 22(1):104–110 (VERIFIED via OpenAlex + Semantic Scholar) / population cohort. Same-title conference abstract exists: Spine J 2013;13(9):S83, doi 10.1016/j.spinee.2013.07.229 — do not confuse
- DOI / arXiv / URL: 10.1016/j.joca.2013.10.019 (VERIFIED)
- Access: bronze open access (publisher PDF at oarsijournal.com per Semantic Scholar; fetch failed)
- Passes: 1/3 (2026-10-16: metadata verified via OpenAlex/Semantic Scholar; abstract elided in both, publisher PDF fetch failed — content fields still from prior knowledge) [2026-10-16 round 3: not upgraded — bronze OA PDF at oarsijournal.com failed to fetch; abstract elided in OpenAlex/Semantic Scholar]
- Modality & anatomy: whole-spine MRI (cervical, thoracic, lumbar)
- Data: ~975 population-based participants (unverified)
- Method: Pfirrmann grade ≥4 as degeneration, by region/age/sex
- Key results: disc degeneration highly prevalent (>70% in <50 y, >90% in ≥50 y at any level — unverified); most frequent at C5/6, T6/7, L4/5 (unverified)
- Code / weights / license: —
- Useful for us: whole-spine normative prevalence by level — needed for level-specific "deviation from normal" priors.
- Limitations / notes: Japanese population; verify numbers.
- BibTeX:
```bibtex
@article{Teraguchi2014Wakayama,
  author  = {Teraguchi, Masatoshi and Yoshimura, Noriko and Hashizume, Hiroshi and Muraki, Shigeyuki and Yamada, Hiroshi and Minamide, Akihito and others and Yoshida, M.},
  title   = {Prevalence and distribution of intervertebral disc degeneration over the entire spine in a population-based cohort: the {Wakayama Spine Study}},
  journal = {Osteoarthritis and Cartilage},
  year    = {2014},
  volume  = {22},
  number  = {1},
  pages   = {104--110},
  doi     = {10.1016/j.joca.2013.10.019}
}
```

### R090. Cheung et al. 2009 — lumbar MRI changes in 1,043 individuals (Hong Kong)
- Full title: Prevalence and pattern of lumbar magnetic resonance imaging changes in a population study of one thousand forty-three individuals
- Authors: Cheung KMC, Karppinen J, Chan D, Ho DWH, Song YQ, Sham P, Cheah KSE, Leong JCY, Luk KDK (VERIFIED via OpenAlex)
- Year / Venue / Type: 2009 / Spine 34(9):934–940 (VERIFIED via OpenAlex) / cross-sectional population study
- DOI / arXiv / URL: 10.1097/BRS.0b013e3181a01b3f (VERIFIED)
- Access: paywalled
- Passes: 2/3 (2026-10-16: metadata + full abstract via OpenAlex; full text paywalled)
- Modality & anatomy: lumbar MRI
- Data: 1,043 southern Chinese volunteers aged 18–55 (VERIFIED)
- Method: two independent observers (consensus on disagreement) graded disc degeneration with the Schneiderman classification (summed into a per-subject total score), herniation, annular tears (HIZ) and Schmorl's nodes; k-means clustering of degeneration patterns; association with back pain
- Key results (abstract, VERIFIED): lumbar disc degeneration in 40% of subjects <30 y, rising to >90% at 50–55 y; total degeneration score positively associated with low back pain; L5–S1 and L4–L5 most affected; skip-level and isolated upper/mid-lumbar patterns observed
- Code / weights / license: —
- Useful for us: Asian population normative data complementary to Brinjikji (mostly Western cohorts).
- Limitations / notes: verify.
- BibTeX:
```bibtex
@article{Cheung2009Prevalence,
  author  = {Cheung, Kenneth M. C. and Karppinen, Jaro and Chan, Danny and others},
  title   = {Prevalence and pattern of lumbar magnetic resonance imaging changes in a population study of one thousand forty-three individuals},
  journal = {Spine},
  year    = {2009},
  volume  = {34},
  number  = {9},
  pages   = {934--940},
  doi     = {10.1097/BRS.0b013e3181a01b3f}
}
```

### R091. Jarvik et al. 2001 — LAIDBack study baseline
- Full title: The Longitudinal Assessment of Imaging and Disability of the Back (LAIDBack) Study: baseline data (VERIFIED)
- Authors: Jarvik JJ, Hollingworth W, Heagerty P, Haynor DR, Deyo RA (VERIFIED, OHSU research portal)
- Year / Venue / Type: 2001 (2001-05-15) / Spine 26(10):1158–1166 (VERIFIED) / prospective cohort (baseline cross-sectional)
- DOI / arXiv / URL: 10.1097/00007632-200105150-00014 (VERIFIED)
- Access: paywalled
- Passes: 2/3 (2026-10-16: metadata + full abstract with numbers via OHSU Elsevier Pure record; full text not opened)
- Modality & anatomy: lumbar MRI (standardised protocol, all five lumbar levels)
- Data: 148 randomly selected, age-stratified VA outpatients with no LBP in the past 4 months; 69 (46%) had never had LBP
- Method: prevalence of MRI findings in people without current LBP/sciatica, relation to age and prior back symptoms
- Key results (VERIFIED): moderate–severe desiccation of >=1 disc 83% (123/148); >=1 bulging disc 64% (95); disc height loss 56% (83); >=1 protrusion 32% (48); >=1 extrusion 6% (9). Authors conclude moderate/severe central stenosis, root compression and extrusions are uncommon in asymptomatic people and likely clinically relevant.
- Code / weights / license: —
- Useful for us: findings that are rare in asymptomatic people (extrusion 6%, root compression, moderate–severe stenosis) should be flagged as most "abnormal"; desiccation/bulge are near-normal at older ages — calibrate "deviation from normal" by age.
- Limitations / notes: VA population (mostly older men — demographic detail not in abstract); small n; later LAIDBack papers address incident findings and predictive value.
- BibTeX:
```bibtex
@article{Jarvik2001LAIDBack,
  author  = {Jarvik, J. J. and Hollingworth, W. and Heagerty, P. and Haynor, D. R. and Deyo, R. A.},
  title   = {The Longitudinal Assessment of Imaging and Disability of the Back ({LAIDBack}) Study: baseline data},
  journal = {Spine},
  year    = {2001},
  volume  = {26},
  number  = {10},
  pages   = {1158--1166},
  doi     = {10.1097/00007632-200105150-00014}
}
```

---

#### F. Cervical degenerative disease AI

### R092. Merali et al. 2021 — DL detection of cervical cord compression
- Full title: A deep learning model for detection of cervical spinal cord compression in MRI scans
- Authors: Merali Z, Wang JZ, Badhiwala JH, Witiw CD, Wilson JR, Fehlings MG (six contributors confirmed by initials on Nature page)
- Year / Venue / Type: 2021 / Scientific Reports 11:10473 / journal article (CC BY 4.0)
- DOI / arXiv / URL: 10.1038/s41598-021-89848-3
- Access: open
- Passes: 3/3 (2026-10-16: full text on nature.com — data, architecture, metrics, limitations, code statement)
- Modality & anatomy: cervical MRI, axial T2-weighted non-fat-saturated (VERIFIED), degenerative cervical myelopathy (DCM)
- Data: 289 surgical DCM patients from AO Spine CSM-NA and CSM-I prospective multicentre cohorts; 9,579 axial T2 images; train/val 201 patients (6,588 images: 4,941 train / 1,647 val), holdout 88 patients (2,991 images), random 75/25 split within each site. Labels: two senior neurosurgical residents per image (compressed vs not), disagreements resolved jointly; inter-rater Cohen's kappa 0.82 (train/val), 0.83 (holdout).
- Method: ResNet-50 (ImageNet pretrained) per-slice binary classifier, 299×299 JPEG input, two 512-unit FC layers + 30% dropout (best of 7 heads), Adam lr 1e-4, batch 16, weighted BCE (positive weight 3.8), early stopping; CAMs for interpretation.
- Key results: holdout AUC 0.94 (Discussion says 0.95), sensitivity 0.88, specificity 0.89, F1 0.82 at threshold 0.5; per-patient median AUC 0.94; no significant AUC differences across age, mJOA, level, scanner subgroups (DeLong p>0.05). Validation accuracy across heads 89.9–92.4%.
- Code / weights / license: code public at https://github.com/zamirmerali/dcm-mri (licence not stated); imaging data not public.
- Useful for us: cervical cord-compression baseline (axial per-slice); human kappa ~0.82 as ceiling; simple transfer-learning recipe.
- Limitations / notes: surgical DCM only (mild DCM and normal spines under-represented); binary per-image label, no grading or level localisation; only two raters; partial vs circumferential compression not distinguished; JPEG conversion; retrospective; many exclusions for unusable MRI formats.
- BibTeX:
```bibtex
@article{Merali2021CervicalCompression,
  author  = {Merali, Zamir and Wang, Justin Z. and Badhiwala, Jetan H. and Witiw, Christopher D. and Wilson, Jefferson R. and Fehlings, Michael G.},
  title   = {A deep learning model for detection of cervical spinal cord compression in {MRI} scans},
  journal = {Scientific Reports},
  year    = {2021},
  volume  = {11},
  pages   = {10473},
  doi     = {10.1038/s41598-021-89848-3}
}
```

---

#### G. Modic-change AI, herniation detection, spondylolisthesis, report generation

### R093. Gao et al. 2022 — DL detection and voxel-wise mapping of Modic changes
- Full title: Automatic detection and voxel-wise mapping of lumbar spine Modic changes with deep learning (VERIFIED, DOAJ record)
- Authors: Gao KT, Tibrewala R, Hess M, Bharadwaj UU, Inamdar G, Link TM, Chin CT, Pedoia V, Majumdar S (order VERIFIED via OpenAlex)
- Year / Venue / Type: 2022 (June) / JOR Spine 5(2):e1204 (VERIFIED via OpenAlex + DOAJ) / journal article
- DOI / arXiv / URL: 10.1002/jsp2.1204 (VERIFIED via OpenAlex 2026-10-16); PMCID PMC9238279
- Access: open (Wiley OA journal; DOAJ-indexed)
- Passes: 2/3 (2026-10-16: DOAJ record with full abstract + UCSF ci2 news page; full text not opened — PMC captcha)
- Modality & anatomy: lumbar MRI sagittal T1 + T2, vertebral bodies/endplates
- Data: 75 lumbar MRI exams (patients with acute-to-chronic LBP, radiculopathy or other lumbar symptoms), retrospective; Modic changes segmented and labelled by two radiologists using combined T1/T2 assessment; second dataset graded by three radiologists for an AI-assisted reading experiment (size not in abstract)
- Method: two deep CNNs ("autoencoder"-type): (1) vertebral-body segmentation on sagittal T1; (2) Modic-change segmentation; then a rule-based signal-intensity algorithm assigns each voxel to a Modic type (voxel-wise type maps, handles mixed/transitional lesions)
- Key results: detection in 85.7% of unseen test samples; sensitivity 0.71 ± 0.072, specificity 0.95 ± 0.022, Cohen's kappa 0.63 vs radiologists; AI assistance raised junior-radiologist vs senior-neuroradiologist agreement from kappa 0.52 to 0.58 (p<0.05)
- Code / weights / license: not stated in abstract (unverified)
- Useful for us: Modic changes as voxel-wise maps (extent/volume, mixed types) rather than a binary label → quantitative deviation measure; rule-based typing from T1/T2 signal is simple and interpretable; shows AI assistance improves inter-reader kappa (evidence for our assistive framing).
- Limitations / notes: very small dataset (75 exams), single institution; moderate sensitivity (0.71); Dice not reported in abstract.
- BibTeX:
```bibtex
@article{Gao2022Modic,
  author  = {Gao, Kenneth T. and Tibrewala, Radhika and Hess, Madeline and Bharadwaj, Upasana Upadhyay and Inamdar, Gaurav and Link, Thomas M. and Chin, Cynthia T. and Pedoia, Valentina and Majumdar, Sharmila},
  title   = {Automatic detection and voxel-wise mapping of lumbar spine {Modic} changes with deep learning},
  journal = {JOR Spine},
  year    = {2022},
  volume  = {5},
  number  = {2},
  pages   = {e1204},
  doi     = {10.1002/jsp2.1204}
}
```

### R094. Tsai et al. 2021 — lumbar disc herniation detection on MRI with DL
- Full title: Lumbar Disc Herniation Automatic Detection in Magnetic Resonance Imaging Based on Deep Learning (VERIFIED)
- Authors: Tsai JY, Hung IYJ, Guo YL, Jan YK, Lin CY, Shih TTF, Chen BB, Lung CW (VERIFIED, Frontiers page)
- Year / Venue / Type: 2021 / Frontiers in Bioengineering and Biotechnology 9:708137 (VERIFIED) / journal article
- DOI / arXiv / URL: 10.3389/fbioe.2021.708137 (VERIFIED); PMC8416668
- Access: open (Frontiers)
- Passes: 3/3 (2026-10-16: Frontiers abstract page + full PDF — methods, Tables 2–3, limitations, data availability)
- Modality & anatomy: lumbar MRI, sagittal T2 only (1.5 T GE, 4 mm slices), L1/2–L5/S1
- Data: 168 male workers aged 20–65 (retrospective, Taiwan); 714 sagittal T2 images (JPEG 512×512; 11 sagittal slices per exam, each LDH shown on 5 symmetric slices); 443 LDH cases by level L1/2 20, L2/3 62, L3/4 112, L4/5 144, L5/S1 105; labels from radiologists' diagnosis records; split 77/20/3% train/val/test; training-set sizes 50/150/350/550 images with augmentation (rotation ±5°, contrast, brightness).
- Method: YOLOv3 single-class (LDH) bounding-box detector with per-level localisation.
- Key results: best ("550-aug") mAP 92.4% (text); overall precision 87.2%, recall 91.7%, F1 89.4%, accuracy 81.1%, IoU 73.6%, Dice 89.4% (Table 3); performance rises monotonically with training images (50-aug F1 70.0%). 84 h training per group; inference ≤3 s.
- Code / weights / license: no code; data on request from corresponding author.
- Useful for us: simple detection-style baseline for herniation localisation; data-size ablation (50→550 images) shows how quickly detection saturates.
- Limitations / notes: male-only occupational cohort; sagittal only; mostly bulge/protrusion (few extrusions/sequestrations); tiny test split (3%); labels from reports not re-reads; internal inconsistencies (Table 2 unlabeled final column; mAP values in text match L1–L2 column; Jaccard text vs table mismatch) — cite cautiously.
- BibTeX:
```bibtex
@article{Tsai2021LDH,
  author  = {Tsai, Jen-Yung and Hung, Isabella Yu-Ju and Guo, Yue Leon and Jan, Yih-Kuen and Lin, Chih-Yang and Shih, Tiffany Ting-Fang and Chen, Bang-Bin and Lung, Chi-Wen},
  title   = {Lumbar Disc Herniation Automatic Detection in Magnetic Resonance Imaging Based on Deep Learning},
  journal = {Frontiers in Bioengineering and Biotechnology},
  year    = {2021},
  volume  = {9},
  pages   = {708137},
  doi     = {10.3389/fbioe.2021.708137}
}
```

### R095. Trinh et al. 2022 — spondylolisthesis detection on radiographs with DL (LumbarNet)
- Full title: Detection of Lumbar Spondylolisthesis from X-ray Images Using Deep Learning Network (VERIFIED)
- Authors: Trinh GM, Shao HC, Hsieh KLC, Lee CY, Liu HW, Lai CW, Chou SY, Tsai PI, Chen KJ, Chang FC, Wu MH, Huang TJ (VERIFIED, MDPI page)
- Year / Venue / Type: 2022 (published 2022-09-16) / Journal of Clinical Medicine 11(18):5450 (VERIFIED) / journal article; preprint at preprints.org 202206.0043
- DOI / arXiv / URL: 10.3390/jcm11185450 (VERIFIED); PMC9501139
- Access: open (MDPI, CC BY)
- Passes: 2/3 (2026-10-16: MDPI article page — abstract + methods to §2.2.1; results tables, dataset description and limitations not rendered)
- Modality & anatomy: lateral lumbar radiographs (true lateral, flexion and extension)
- Data: patient/image counts and split not captured in the rendered text (TODO)
- Method: "LumbarNet" — U-Net with a feature-fusion module in the encoder (512×512×3 input, 29 conv layers, dropout) segments vertebrae and sacrum; contours fitted with quadrilaterals -> 4 corner keypoints per lumbar vertebra + 2 on the sacral plate; slip computed as "P-grade" (Meyerding-like percentage) with piecewise-slope detection and dynamic-shift methods; abnormality threshold 20%.
- Key results (abstract): vertebral segmentation mean IoU 0.88; slip-detection accuracy 88.83%; LumbarNet outperformed plain U-Net.
- Code / weights / license: not stated in rendered text
- Useful for us: X-ray branch template — segment -> corner keypoints -> geometric slip %, i.e. Meyerding computed from landmarks (DG13); flexion/extension views enable instability assessment.
- Limitations / notes: failure cases noted for osteoporotic low-contrast vertebrae, pelvis superimposition and osteophytes; loss/activation description inconsistent (softmax CE vs sigmoid output); dataset size to verify.
- BibTeX:
```bibtex
@article{Trinh2022Spondylolisthesis,
  author  = {Trinh, Giam Minh and Shao, Hao-Chiang and Hsieh, Kevin Li-Chun and Lee, Ching-Yu and Liu, Hsiao-Wei and Lai, Chen-Wei and Chou, Sen-Yi and Tsai, Pei-I and Chen, Kuan-Jen and Chang, Fang-Chieh and Wu, Meng-Huang and Huang, Tsung-Jen},
  title   = {Detection of Lumbar Spondylolisthesis from {X}-ray Images Using Deep Learning Network},
  journal = {Journal of Clinical Medicine},
  year    = {2022},
  volume  = {11},
  number  = {18},
  pages   = {5450},
  doi     = {10.3390/jcm11185450}
}
```

### R096. Han et al. 2018 — automatic report generation in spine radiology
- Full title: Towards Automatic Report Generation in Spine Radiology Using Weakly Supervised Framework
- Authors: Han Z, Wei B, Leung S (Steven — CORRECTED from "Stephanie" in BibTeX), Chung J, Li S (VERIFIED via reference list of the authors' follow-up arXiv:2004.13577)
- Year / Venue / Type: 2018 / MICCAI 2018 proceedings (Frangi AF et al., eds; Springer, Cham), pp. 185–193 (VERIFIED via citing reference); LNCS volume number (11073?) and chapter DOI still unverified / conference
- DOI / arXiv / URL: chapter DOI unverified; follow-up: Han Z, Wei B, Yin Y, Li S, "Unifying Neural Learning and Symbolic Reasoning for Spinal Medical Report Generation", arXiv:2004.13577
- Access: paywalled (follow-up open)
- Passes: 1/3 (2026-10-16: authors/venue/pages confirmed from the follow-up paper's reference list; original 2018 paper NOT opened. Follow-up full text read for context.) [2026-10-16 round 3: not upgraded — Springer LNCS chapter paywalled; no open copy located]
- Modality & anatomy: lumbar MRI sagittal
- Data: original 2018 data unverified; the follow-up (NSL) uses 253 multi-centre, multi-vendor patients, one mid-lumbar sagittal T1/T2 slice each, 80/20 split with 5-fold CV
- Method: weakly supervised detection/classification of neural foramina, discs and vertebrae, then template-based report text (2018 details unverified). Follow-up NSL: adversarial graph network segmentation (foramina, discs, vertebrae) + meta-interpretive learning of disease relations (foraminal stenosis, disc degeneration, vertebral deformity) + first-order-logic labelling filling a fixed report template.
- Key results: 2018 unverified. Follow-up: segmentation pixel accuracy 0.965, Dice 0.879, sensitivity 0.872, specificity 0.903; argues NLG metrics (BLEU etc.) are unsuitable and evaluates components instead.
- Code / weights / license: unverified
- Useful for us: earliest structured-report pipeline for spine MRI; supports our "findings -> controlled vocabulary -> template text" design and component-level (not BLEU) evaluation of reports.
- Limitations / notes: single mid-sagittal slice per patient (follow-up); verify chapter DOI and LNCS volume.
- BibTeX:
```bibtex
@inproceedings{Han2018ReportGeneration,
  author    = {Han, Zhongyi and Wei, Benzheng and Leung, Steven and Chung, Jonathan and Li, Shuo},
  title     = {Towards Automatic Report Generation in Spine Radiology Using Weakly Supervised Framework},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2018},
  editor    = {Frangi, Alejandro F. and others},
  publisher = {Springer},
  address   = {Cham},
  pages     = {185--193},
  year      = {2018},
  note      = {LNCS volume and DOI unverified}
}
```

---

## 03. Fractures, bone health and spinal alignment

#### A. Fracture grading and classification systems (clinical definitions)

### R097. Genant semiquantitative vertebral fracture grading
- Full title: Vertebral fracture assessment using a semiquantitative technique
- Authors: Harry K. Genant, Chun-Ying Wu, Cornelis van Kuijk, Michael C. Nevitt
- Year / Venue / Type: 1993 / Journal of Bone and Mineral Research 8(9):1137-1148 / journal article (seminal method)
- DOI / arXiv / URL: 10.1002/jbmr.5650080915
- Access: paywalled (abstract only)
- Passes: 1/3 abstract only; full bibliographic metadata CONFIRMED via OpenAlex 2026-10-16 (authors Harry K. Genant, Chun-Ying Wu, Cornelis van Kuijk, Michael C. Nevitt; 8(9):1137-1148; PMID 8237484). Paywalled (closed, no OA copy), so full text was skipped. The grade percentage thresholds still need a full-text or secondary citation.
- Modality & anatomy: lateral thoracic and lumbar spine radiographs
- Data: 57 postmenopausal women aged 65-75, three independent observers
- Method: visual semiquantitative (SQ) grading of each vertebra T4-L4: grade 0 normal, grade 1 mild (approx. 20-25% height reduction), grade 2 moderate (25-40%), grade 3 severe (>40%); compared against quantitative morphometry. (Percent thresholds are the standard published Genant definitions; the abstract seen did not list them.)
- Key results: SQ method reliable inter/intra-observer when well-defined criteria used (kappa values not visible in the abstract; unverified)
- Code / weights / license: n/a
- Useful for us: the reference definition for our fracture grading head and for VerSe/other datasets labelled with Genant grades; grade thresholds become our "deviation from normal" scale for vertebral height loss.
- Limitations / notes: subjective; distinguishing grade 1 from normal variants (short vertebral height, Scheuermann) is the main error source.
- BibTeX:
```bibtex
@article{Genant1993Semiquantitative,
  title   = {Vertebral fracture assessment using a semiquantitative technique},
  author  = {Genant, Harry K. and Wu, Chun Y. and van Kuijk, Cornelis and Nevitt, Michael C.},
  journal = {Journal of Bone and Mineral Research},
  volume  = {8},
  number  = {9},
  pages   = {1137--1148},
  year    = {1993},
  doi     = {10.1002/jbmr.5650080915}
}
```
- Also relevant to: Uncertainty, image quality, abstention and normative anatomy

### R098. TLICS (Thoracolumbar Injury Classification and Severity Score)
- Full title: A new classification of thoracolumbar injuries: the importance of injury morphology, the integrity of the posterior ligamentous complex, and neurologic status
- Authors: Vaccaro AR, Lehman RA Jr, Hurlbert RJ, et al.
- Year / Venue / Type: 2005 / Spine 30(20):2325-2333 / journal article (classification system)
- DOI / arXiv / URL: 10.1097/01.brs.0000182986.43345.cb
- Access: paywalled; a full-text PDF copy was read from a university teaching page (cumming.ucalgary.ca)
- Passes: 3/3 full text
- Modality & anatomy: CT/MRI/radiographs, thoracolumbar spine trauma
- Data: preliminary validation on 71 cases (one institution) and 56 Spine Trauma Study Group cases
- Method: additive score. Morphology: compression 1, burst +1, translation/rotation 3, distraction 4. PLC: intact 0, suspected/indeterminate 2, injured 3. Neurology: intact 0, nerve root 2, complete cord/conus 2, incomplete cord/conus 3, cauda equina 3. Total <=3 nonoperative, 4 either, >=5 operative.
- Key results: system proposal; reliability studies pending at publication
- Code / weights / license: n/a
- Useful for us: the scoring rules are directly implementable as a rule layer over image findings (morphology + PLC integrity on MRI); neurology must come from clinical input, so the report should flag it as "not assessable from imaging".
- Limitations / notes: only the most severe level scored; PLC assessment on MRI is subjective; clinical modifiers (osteoporosis, AS) not scored; authors disclose industry funding.
- BibTeX:
```bibtex
@article{Vaccaro2005TLICS,
  title   = {A new classification of thoracolumbar injuries: the importance of injury morphology, the integrity of the posterior ligamentous complex, and neurologic status},
  author  = {Vaccaro, Alexander R. and Lehman, Ronald A. and Hurlbert, R. John and Anderson, Paul A. and Harris, Mitchel and Hedlund, Rune and others},
  journal = {Spine},
  volume  = {30},
  number  = {20},
  pages   = {2325--2333},
  year    = {2005},
  doi     = {10.1097/01.brs.0000182986.43345.cb}
}
```

### R099. TLISS reliability (precursor of TLICS)
- Full title: Reliability of a novel classification system for thoracolumbar injuries: the Thoracolumbar Injury Severity Score
- Authors: Alexander R. Vaccaro, Eli M. Baron, James A. Sanfilippo, Sidney M. Jacoby, et al. (>30 authors; Alan S. Hilibrand last)
- Year / Venue / Type: 2006 / Spine 31(11 Suppl):S62-S69 / journal article
- DOI / arXiv / URL: 10.1097/01.brs.0000218072.25964.a9 (PMID 16685239)
- Access: paywalled (abstract only)
- Passes: 1/3 abstract only (abstract numbers re-confirmed and metadata verified via OpenAlex 2026-10-16: Spine 31(11 Suppl):S62-S69, 2006-05-01). Closed access, no OA copy, so full text was skipped.
- Modality & anatomy: thoracolumbar trauma imaging
- Data: 71 cases, 5 spine surgeons, re-scored after ~1 month
- Method: inter/intra-rater Cohen kappa and Spearman correlation
- Key results: interrater kappa mechanism 0.33, neurology 0.91, PLC 0.35, total score 0.29, treatment 0.52. Intrarater kappa mechanism 0.57, neurology 0.93, PLC 0.48, total 0.46, treatment 0.62. 96.4% agreement with the TLISS treatment recommendation (re-confirmed 2026-10-16).
- Code / weights / license: n/a
- Useful for us: human inter-rater ceiling for PLC status and fracture mechanism; motivates replacing "mechanism" with image morphology (done in TLICS) and justifies reporting uncertainty on PLC.
- Limitations / notes: small sample, surgeons only.
- BibTeX:
```bibtex
@article{Vaccaro2006TLISS,
  title   = {Reliability of a novel classification system for thoracolumbar injuries: the Thoracolumbar Injury Severity Score},
  author  = {Vaccaro, Alexander R. and Baron, Eli M. and Sanfilippo, James and Jacoby, Sidney and Steuve, Jacob and Grossman, Eric and others},
  journal = {Spine},
  volume  = {31},
  number  = {11 Suppl},
  pages   = {S62--S69},
  year    = {2006},
  doi     = {10.1097/01.brs.0000218072.25964.a9}
}
```

### R100. AO Spine thoracolumbar injury classification
- Full title: AOSpine thoracolumbar spine injury classification system: fracture description, neurological status, and key modifiers
- Authors: Alexander R. Vaccaro, F. Cumhur Öner, Christopher K. Kepler, Marcel F. Dvorak, Klaus J. Schnake, Carlo Bellabarba, Maximilian Reinhold, Bizhan Aarabi, Frank Kandziora, Jens R. Chapman, Shanmuganathan Rajasekaran, Michael G. Fehlings, Luiz R. Vialle (AOSpine Spinal Cord Injury & Trauma Knowledge Forum)
- Year / Venue / Type: 2013 / Spine 38(23):2028-2037 / journal article (classification system)
- DOI / arXiv / URL: 10.1097/BRS.0b013e3182a8a381 (CONFIRMED via OpenAlex; online 2013-08-22; PMID 23970107). OpenAlex lists the title without the subtitle.
- Access: paywalled (abstract not readable: PubMed blocked); classification content read from Radiopaedia and AO Foundation poster
- Passes: 1/3 (abstract via OpenAlex 2026-10-16 + classification definitions from secondary sources). Closed access, so full text was skipped.
- Modality & anatomy: CT (morphology) +/- MRI (tension band), thoracolumbar spine
- Data: 40 cases spanning a broad range of injuries, each classified twice by the group members one month apart (number of raters not stated in the abstract)
- Method: Morphology A0-A4 (A0 minor/process; A1 wedge one endplate; A2 split/pincer; A3 incomplete burst; A4 complete burst), B1-B3 (B1 transosseous Chance; B2 posterior tension-band/PLC disruption; B3 hyperextension), C (translation); neurology N0-N4, NX; modifiers M1 (indeterminate tension band), M2 (patient-specific comorbidity).
- Key results: reliability for morphologic type (A compression / B tension-band / C translation) substantial, kappa 0.72. The authors call for further prospective clinical validation.
- Code / weights / license: n/a
- Useful for us: target label schema for a CT trauma classification head (A/B/C + subtypes); M1 maps naturally to our "inconclusive, request MRI" behaviour.
- Limitations / notes: reliability lower for B types and A3 vs A4 distinction (see Kepler 2015 reliability analysis, not read).
- BibTeX:
```bibtex
@article{Vaccaro2013AOSpineTL,
  title   = {{AOSpine} thoracolumbar spine injury classification system: fracture description, neurological status, and key modifiers},
  author  = {Vaccaro, Alexander R. and Oner, Cumhur and Kepler, Christopher K. and Dvorak, Marcel and Schnake, Klaus and Bellabarba, Carlo and others},
  journal = {Spine},
  volume  = {38},
  number  = {23},
  pages   = {2028--2037},
  year    = {2013},
  doi     = {10.1097/BRS.0b013e3182a8a381}
}
```

### R101. AO Spine subaxial cervical injury classification
- Full title: AOSpine subaxial cervical spine injury classification system
- Authors: Alexander R. Vaccaro, John D. Koerner, Kris E. Radcliff, F. Cumhur Öner, Maximilian Reinhold, Klaus J. Schnake, Frank Kandziora, Michael G. Fehlings, Marcel F. Dvorak, Bizhan Aarabi, Shanmuganathan Rajasekaran, Gregory D. Schroeder, Christopher K. Kepler, Luiz R. Vialle
- Year / Venue / Type: 2016 / European Spine Journal 25(7):2173-2184 / journal article
- DOI / arXiv / URL: 10.1007/s00586-015-3831-3
- Access: paywalled (abstract only)
- Passes: 1/3 abstract only; metadata verified via OpenAlex 2026-10-16 (online 2015-02-25; print 2016 25(7):2173-2184; PMID 25716661). The Utrecht repository OA copy (dspace.library.uu.nl/handle/1874/342757) exposed no PDF to the fetcher, so full text was skipped.
- Modality & anatomy: CT, subaxial cervical spine (C3-C7)
- Data: each investigator graded 10 calibration cases then 30 cases twice, one month apart
- Method: morphology A (compression), B (tension band), C (translation), plus facet injury descriptors, neurology, case modifiers
- Key results: intraobserver kappa 0.75, interobserver kappa 0.64
- Code / weights / license: n/a
- Useful for us: label schema for cervical CT fracture subtyping beyond the binary RSNA labels.
- Limitations / notes: expert graders; not validated against outcomes in this paper.
- BibTeX:
```bibtex
@article{Vaccaro2016AOSpineSubaxial,
  title   = {{AOSpine} subaxial cervical spine injury classification system},
  author  = {Vaccaro, Alexander R. and Koerner, John D. and Radcliff, Kris E. and Oner, F. Cumhur and Reinhold, Maximilian and Schnake, Klaus J. and others},
  journal = {European Spine Journal},
  volume  = {25},
  number  = {7},
  pages   = {2173--2184},
  year    = {2016},
  doi     = {10.1007/s00586-015-3831-3}
}
```

#### B. Fracture datasets and AI on CT (osteoporotic and traumatic)

### R102. Automated opportunistic osteoporosis screening in routine CT vs DXA (Bonescreen pipeline)
- Full title: Automatic opportunistic osteoporosis screening in routine CT: improved prediction of patients with prevalent vertebral fractures compared to DXA
- Authors: Löffler MT, Jacob A, Scharr A, et al.
- Year / Venue / Type: 2021 / European Radiology 31:6069-6077 / journal article
- DOI / arXiv / URL: 10.1007/s00330-020-07655-2
- Access: open (Springer)
- Passes: 2/3 (abstract + results from publisher page)
- Modality & anatomy: routine clinical MDCT, thoracolumbar spine
- Data: 192 patients (141 F, 51 M; mean age 70.2), 148 (77%) with prevalent vertebral fractures; single institution (TUM)
- Method: CNN vertebral segmentation -> bone mineral content, trabecular and integral vBMD, CT-derived aBMD with asynchronous calibration; compared with lumbar DXA
- Key results: AUC trabecular vBMD ~0.885, integral vBMD ~0.86 vs DXA aBMD 0.668; adjusted OR per SD 6.9 (auto trabecular vBMD); proposed integral vBMD thresholds <160 mg/cm3 osteoporosis, 160-190 mg/cm3 low bone mass
- Code / weights / license: segmentation available via the Bonescreen/anduin web service (commercial spin-off); code not open (unverified)
- Useful for us: canonical citation for automated opportunistic BMD from any routine CT; thresholds give a normative cut-off for a "bone health" line in our report.
- Limitations / notes: retrospective single-centre, high fracture prevalence (enriched); asynchronous calibration assumptions; note an internal inconsistency in which measure had AUC 0.885 (abstract vs results).
- BibTeX:
```bibtex
@article{Loffler2021OpportunisticCT,
  title   = {Automatic opportunistic osteoporosis screening in routine {CT}: improved prediction of patients with prevalent vertebral fractures compared to {DXA}},
  author  = {L{\"o}ffler, Maximilian T. and Jacob, Alina and Scharr, Andreas and others},
  journal = {European Radiology},
  volume  = {31},
  pages   = {6069--6077},
  year    = {2021},
  doi     = {10.1007/s00330-020-07655-2}
}
```

### R103. Deep-learning opportunistic CT osteoporosis screening with normative values (538k CTs)
- Full title: Deep Learning–based Opportunistic CT Osteoporosis Screening and the Establishment of Normative Values
- Authors: Malte Westerhoff, Soterios Gyftopoulos, Bari Dane, Emilio Vega, Daniel Murdock, Norbert Lindow, Felix Herter, Khaled Bousabarah, Michael P. Recht, Miriam A. Bredella (NYU Langone; Westerhoff, Lindow, Herter and Bousabarah are at Visage Imaging, Berlin)
- Year / Venue / Type: 2025 (online 2025-11-11) / Radiology 317(2) (November 2025) / journal article. Article number not shown on the page.
- DOI / arXiv / URL: 10.1148/radiol.250917 (confirmed on pubs.rsna.org) ; PMID 41217284
- Access: paywalled. The RSNA full-text page rendered abstract, figures captions and main results; the limitations section was not visible.
- Passes: 2/3 (abstract earlier; RSNA article page read 2026-10-16 for authors/affiliations, data and results). Limitations and supplement not read.
- Modality & anatomy: routine clinical CT (all protocols), thoracic and lumbar trabecular bone
- Data: retrospective; 538,946 CT exams from 283,499 patients (mean age 65 ± 15; 51.2% female; 55.5% White); 43 scanner models; 6 tube voltages. Sites and years not stated on the page.
- Method: a CNN places a 3D trabecular ROI per vertebra (T and L spine). Statistical normalisation for kVp and scanner model (formula not visible). Thresholds anchored to WHO-reported osteoporosis prevalence. t tests for group differences.
- Key results: automated ROI placement agreed with radiologist review in >99% of 1,496 vertebrae. 80 vs 120 kVp attenuation differs by 23%; scanner-model differences <10%. Women <50 y are higher than young men; decline with age, faster after menopause. Men > women after 50. Black > Asian > White (all P<.001). Hispanic men > non-Hispanic men. Normative L1 curves only in figures (no numeric HU cut-offs seen).
- Code / weights / license: not stated. Authors declared no funding. 4 of 10 authors are employed by Visage Imaging (the earlier "vendor-affiliated (unverified)" note is now CONFIRMED).
- Useful for us: the largest normative reference for vertebral attenuation and the kVp/scanner correction approach. Directly supports our "quantify deviation from normal" goal for bone density (age/sex/race-specific z-score-like output). The 23% kVp effect means our HU outputs must be kVp-normalised.
- Limitations / notes: HU-based (not calibrated vBMD); thresholds derived from prevalence rather than DXA; vendor involvement; numeric normative tables not obtained (figures/supplement).
- BibTeX:
```bibtex
@article{Westerhoff2025NormativeCT,
  title   = {Deep Learning--based Opportunistic {CT} Osteoporosis Screening and the Establishment of Normative Values},
  author  = {Westerhoff, Malte and Gyftopoulos, Soterios and Dane, Bari and Vega, Emilio and Murdock, Daniel and Lindow, Norbert and Herter, Felix and Bousabarah, Khaled and Recht, Michael P. and Bredella, Miriam A.},
  journal = {Radiology},
  volume  = {317},
  number  = {2},
  year    = {2025},
  doi     = {10.1148/radiol.250917}
}
```

### R104. Automated CT biomarkers (incl. L1 BMD) for outcome prediction
- Full title: Automated CT biomarkers for opportunistic prediction of future cardiovascular events and mortality in an asymptomatic screening population: a retrospective cohort study
- Authors: Pickhardt PJ, Graffy PM, Zea R, et al.
- Year / Venue / Type: 2020 / The Lancet Digital Health / journal article
- DOI / arXiv / URL: 10.1016/S2589-7500(20)30025-X
- Access: open (full-text PDF copy read)
- Passes: 3/3 full text
- Modality & anatomy: low-dose unenhanced abdominal CT (CT colonography), L1 trabecular BMD among five biomarkers
- Data: 9,223 adults, single centre (Univ. Wisconsin), median follow-up 8.8 y
- Method: fully automated algorithms for aortic calcium, L3 muscle density, L1 visceral/subcutaneous fat ratio, liver density, L1 trabecular HU
- Key results: 5-y AUROC for death: aortic calcium 0.743, muscle 0.721, vertebral density 0.646; combined 2-y AUROC 0.811 vs Framingham 0.688
- Code / weights / license: not released
- Useful for us: shows that L1 trabecular HU from an automated pipeline is a prognostic biomarker; supports including an opportunistic bone line in every spine/abdomen CT report.
- Limitations / notes: non-contrast only; ~90% white cohort; single centre; EHR outcome ascertainment.
- BibTeX:
```bibtex
@article{Pickhardt2020CTBiomarkers,
  title   = {Automated {CT} biomarkers for opportunistic prediction of future cardiovascular events and mortality in an asymptomatic screening population: a retrospective cohort study},
  author  = {Pickhardt, Perry J. and Graffy, Peter M. and Zea, Ryan and others},
  journal = {The Lancet Digital Health},
  year    = {2020},
  doi     = {10.1016/S2589-7500(20)30025-X}
}
```
- Also relevant to: Reviews, reporting guidelines, validation and deployment

### R105. Pickhardt 2013: opportunistic osteoporosis screening with L1 attenuation on abdominal CT
- Full title: Opportunistic Screening for Osteoporosis Using Abdominal Computed Tomography Scans Obtained for Other Indications
- Authors: Perry J. Pickhardt, B. Dustin Pooler, Travis Lauder, Alejandro Muñoz del Río, Richard J. Bruce, Neil Binkley (Univ. Wisconsin)
- Year / Venue / Type: 2013 (2013-04-16) / Annals of Internal Medicine 158(8):588-595 / journal article (seminal)
- DOI / arXiv / URL: 10.7326/0003-4819-158-8-201304160-00003 (CONFIRMED via OpenAlex, 2026-10-16) ; PMID 23588747
- Access: paywalled (closed)
- Passes: 1/3 (OpenAlex record with full structured abstract, 2026-10-16). Full text not accessible. The abstract was reconstructed from OpenAlex's inverted index, so check exact wording before quoting.
- Modality & anatomy: routine abdominal CT (with or without IV contrast), trabecular attenuation (HU) T12-L5, focus on L1
- Data: 1,867 adults, 2,067 CT-DXA pairs within 6 months, over 10 years, single academic centre; cross-sectional
- Method: trabecular ROI attenuation (HU) vs DXA BMD reference. Sagittal reformats were reviewed for moderate/severe vertebral fractures.
- Key results (now confirmed): L1 ≤160 HU was 90% sensitive for osteoporosis (vs osteopenia/normal); a 110 HU threshold was >90% specific. PPV ≥68% below 100 HU; NPV 99% above 200 HU. Of 119 patients with ≥1 moderate/severe VF, 62 (52.1%) had non-osteoporotic DXA T-scores (DXA false negatives), and 97% of them had L1 or mean T12-L5 ≤145 HU. Similar performance at all levels; IV contrast did not affect performance.
- Code / weights / license: n/a
- Useful for us: the classic HU thresholds (160 / 110 / 100 / 200 HU; 145 HU in fracture patients) that most opportunistic-screening AI uses. Our CT bone line can report L1 HU against these cut-offs. The DXA-false-negative fracture finding argues for reporting fractures and HU together.
- Limitations / notes: single centre; costs/benefits of thresholds not assessed (authors). Later work shows contrast phase and kVp do affect HU (see FA10), unlike this paper's finding.
- BibTeX:
```bibtex
@article{Pickhardt2013Opportunistic,
  title   = {Opportunistic Screening for Osteoporosis Using Abdominal Computed Tomography Scans Obtained for Other Indications},
  author  = {Pickhardt, Perry J. and Pooler, B. Dustin and Lauder, Travis and Mu{\~n}oz del R{\'i}o, Alejandro and Bruce, Richard J. and Binkley, Neil},
  journal = {Annals of Internal Medicine},
  volume  = {158},
  number  = {8},
  pages   = {588--595},
  year    = {2013},
  doi     = {10.7326/0003-4819-158-8-201304160-00003}
}
```

### R106. Automated vertebrae localization, segmentation and osteoporotic VCF detection pipeline (CT)
- Full title: An Automated Vertebrae Localization, Segmentation, and Osteoporotic Compression Fracture Detection Pipeline for Computed Tomographic Imaging
- Authors: İlkay Yıldız Potter, Edward Kenneth Rodriguez, Jim S. Wu, Ara Nazarian, Ashkan Vaziri (BIDMC / Harvard)
- Year / Venue / Type: 2024 (online 2024-05-08) / Journal of Imaging Informatics in Medicine 37(5):2428-2443 (confirmed via OpenAlex) / journal article
- DOI / arXiv / URL: 10.1007/s10278-024-01135-5 (CONFIRMED via OpenAlex, 2026-10-16) ; PMID 38717516 ; PMC11522205 (accepted manuscript)
- Access: publisher paywalled; green OA accepted manuscript in PMC (PMC blocked by reCAPTCHA, Europe PMC rate-limited, Springer page not fetchable in this session)
- Passes: 1/3 abstract only; bibliographic metadata fully verified 2026-10-16. Full text still unread (all three access routes failed).
- Modality & anatomy: CT, thoracolumbar spine
- Data: public dataset of 325 spine CTs with segmentation, 126 graded for VCF (81 with, 45 without) - consistent with VerSe-derived data (unverified)
- Method: DL localization + segmentation, then VCF classifier using predicted segments as extra input
- Key results: vertebra-level sensitivity 96%, specificity 81%; subject-level accuracy 100%; adding segmentation improved sensitivity up to 14% and specificity up to 20% (p=0.028)
- Code / weights / license: unverified
- Useful for us: supports a segmentation-first, per-vertebra fracture classifier design (our planned pipeline).
- Limitations / notes: small graded subset; 100% subject-level accuracy on tiny test set is not generalisable.
- BibTeX:
```bibtex
@article{Potter2024VCFPipeline,
  title   = {An Automated Vertebrae Localization, Segmentation, and Osteoporotic Compression Fracture Detection Pipeline for Computed Tomographic Imaging},
  author  = {Y{\i}ld{\i}z Potter, {\.I}lkay and Rodriguez, Edward K. and Wu, Jim S. and Nazarian, Ara and Vaziri, Ashkan},
  journal = {Journal of Imaging Informatics in Medicine},
  volume  = {37},
  number  = {5},
  pages   = {2428--2443},
  year    = {2024},
  doi     = {10.1007/s10278-024-01135-5}
}
```

### R107. CNN detection and AO type-A classification of acute vertebral body fractures on CT
- Full title: Automated detection and classification of acute vertebral body fractures using a convolutional neural network on computed tomography
- Authors: Zhang J, Liu F, Xu J, et al.
- Year / Venue / Type: 2023 / Frontiers in Endocrinology 14 / journal article
- DOI / arXiv / URL: 10.3389/fendo.2023.1132725
- Access: open
- Passes: 3/3 full text
- Modality & anatomy: CT, thoracolumbar spine (acute fractures)
- Data: 1,217 CTs (838 fracture-positive, 379 negative), single centre (Peking University Third Hospital, 2015-2019); labels AO Spine A1-A4 (B/C excluded); endplate and posterior-wall involvement marked. Split numbers in Table 1 inconsistent with total.
- Method: (1) U-Net keypoint vertebral centres + 2-layer GCN for level identification; (2) 3D-ResNet per-vertebra fracture classifier on 128x128x64 VOI; (3) three-branch network (upper endplate, lower endplate, posterior wall) combined into AO subtype
- Key results: vertebra-level sens 95.23%, spec 98.35%, AUC 0.993; patient accuracy 98.96%; AO A-subtype balanced accuracy 79.56%, kappa 0.70; AUC A1 0.904, A2 0.945, A3 0.878, A4 0.942
- Code / weights / license: none released; data "on request"
- Useful for us: decomposition of AO subtype into anatomical sub-findings (endplates, posterior wall) is a good interpretable design to copy; reports per-subtype AUCs for benchmarking.
- Limitations / notes: single centre; no B/C types; A2 rare; A1/A3 confusion; posterior wall hard.
- BibTeX:
```bibtex
@article{Zhang2023AOTypeA,
  title   = {Automated detection and classification of acute vertebral body fractures using a convolutional neural network on computed tomography},
  author  = {Zhang, Jianlun and Liu, Feng and Xu, Jingxu and Zhao, Qingqing and Huang, Chencui and Yu, Yizhou and Yuan, Huishu},
  journal = {Frontiers in Endocrinology},
  volume  = {14},
  pages   = {1132725},
  year    = {2023},
  doi     = {10.3389/fendo.2023.1132725}
}
```

### R108. Detection of vertebral fractures in CT using 3D CNNs
- Full title: Detection of vertebral fractures in CT using 3D Convolutional Neural Networks
- Authors: Joeri Nicolaes, Steven Raeymaeckers, David Robben, Guido Wilms, Dirk Vandermeulen, Cesar Libanati, Marc Debois (UCB Pharma, KU Leuven, UZ Brussel, icometrix; funded by UCB and Amgen)
- Year / Venue / Type: 2019 / arXiv preprint 1911.01816 (later MICCAI workshop / CSI 2019 per some citations: unverified)
- DOI / arXiv / URL: arXiv:1911.01816
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv PDF read 2026-10-16 for data/method/results, then comparisons/limitations/code). Venue still not stated in the PDF.
- Modality & anatomy: CT containing spine (opportunistic)
- Data: 90 CT series (University Hospital Brussels; Siemens/Philips/GE; 120 kVp; ≤0.92 mm in-plane, 1.5 mm slices; mean age 81, 64% female, 12% fracture-negative, >90% abdominal). 969 vertebrae, 184 fractured (85 mild, 64 moderate, 35 severe Genant). One radiologist graded each vertebra; centroids placed manually (MeVisLab, <2 min/scan). Sparse labels were expanded to 3D label images (flattened ellipsoids for fractures, after Glocker et al.); all grades merged into one class.
- Method: DeepMedic dual-pathway 11-layer 3D CNN (~230K params; receptive fields 17^3 / 51^3), 1 mm isotropic input, weighted voxel sampling, cross-entropy, RMSProp, 35 epochs. 3D beat 1-slice and 5-slice 2D variants. Patient level: connected components above probability and size thresholds. Vertebra level: Gaussian-weighted mean probability in a cube around the centroid.
- Key results: stratified 5-fold CV: patient AUC 0.95 ± 0.02 (recall 0.905, specificity 0.938 at the chosen point); vertebra AUC 0.93 ± 0.01. Cited comparators (different test sets): Valentinitsch AUC 0.88, Tomita (FA18) AUC 0.92, Bar (FA16) recall 0.839 / specificity 0.938, Burns sensitivity 95.7% at 0.29 FP/patient.
- Code / weights / license: no release of own code or data; built on the open-source DeepMedic.
- Useful for us: early evidence that report-derived weak labels suffice for 3D fracture detection; voxel-level output gives localisation for the report.
- Limitations / notes: very small single-centre dataset with few thoracic vertebrae; manual (noisy) centroids; grades not separately evaluated; CV only, no external test. Errors concentrated in mild fractures, edge vertebrae, fracture series and other pathologies.
- BibTeX:
```bibtex
@misc{Nicolaes2019FractureCT3D,
  title   = {Detection of vertebral fractures in {CT} using {3D} Convolutional Neural Networks},
  author  = {Nicolaes, Joeri and Raeymaeckers, Steven and Robben, David and Wilms, Guido and Vandermeulen, Dirk and Libanati, Cesar and Debois, Marc},
  year    = {2019},
  eprint  = {1911.01816},
  archivePrefix = {arXiv}
}
```

### R109. Compression fractures detection on CT (CNN + RNN)
- Full title: Compression Fractures Detection on CT
- Authors: Amir Bar, Lior Wolf, Orna Bergman Amitai, Eyal Toledano, Eldad Elnekave (Tel Aviv University; Zebra Medical Vision)
- Year / Venue / Type: 2017 / arXiv 1706.01671 (SPIE Medical Imaging 2017 per common citation: unverified) / preprint
- DOI / arXiv / URL: arXiv:1706.01671
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv PDF read 2026-10-16 for data/method/results and limitations). Venue not stated in the PDF; the SPIE 2017 venue remains unverified.
- Modality & anatomy: CT (chest/abdomen), thoracolumbar spine
- Data: 3,701 adults >50 y with chest/abdominal CT (2,681 negative, 1,020 positive, with bounding boxes). An age/sex-balanced subset of 1,673 studies (849 negative / 824 positive) was used. Labels: Genant reads by 2 radiologists with a third adjudicating. 15% of studies held out as validation; no separate test set. Institution and scanners not stated.
- Method: heuristic spine localisation (spinal cord in axial view, posterior back in coronal view, bone HU threshold) to a virtual sagittal section, then 32x32 sagittal patches. VGG-style CNN (3 conv blocks, FC-512; ±18° rotation augmentation; 15 epochs). Single-layer LSTM (128 cells) over the sequence of patch probabilities gives the study-level label.
- Key results: CNN patch-level validation accuracy 92.9%. Study level (LSTM): accuracy 89.1%, sensitivity 83.9%, specificity 93.8%. No AUC reported.
- Code / weights / license: none
- Useful for us: early opportunistic VCF detection on routine CT (Zebra Medical Vision lineage); justifies the sequence-aggregation idea also used in the RSNA 2022 winner.
- Limitations / notes: validation set only (no independent test); no CIs or vertebra-level metrics; 55% of the cohort discarded for balancing; single source; the authors warn the unbalanced data could let a model learn age/sex shortcuts.
- BibTeX:
```bibtex
@misc{Bar2017CompressionCT,
  title   = {Compression Fractures Detection on {CT}},
  author  = {Bar, Amir and Wolf, Lior and Bergman Amitai, Orna and Toledano, Eyal and Elnekave, Eldad},
  year    = {2017},
  eprint  = {1706.01671},
  archivePrefix = {arXiv}
}
```

### R110. Grading Loss: Genant-aligned metric learning for vertebral fracture detection
- Full title: Grading Loss: A Fracture Grade-based Metric Loss for Vertebral Fracture Detection
- Authors: Husseini M, Sekuboyina A, Loeffler M, et al.
- Year / Venue / Type: 2020 / MICCAI 2020 (venue per common citation, unverified in session); arXiv 2008.07831
- DOI / arXiv / URL: arXiv:2008.07831
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv PDF read 2026-10-16 for data/method/results and limitations). Venue not named in the PDF; MICCAI 2020 remains unverified.
- Modality & anatomy: CT, thoracolumbar spine
- Data: VerSe with fracture grades (FA06), cervical excluded: 1,283 vertebrae from 157 scans (1,133 healthy, 104 grade 2, 46 grade 3). Grade 1 excluded because of inter-rater uncertainty. Train 966 / test 312 vertebrae, 15 random stratified folds. Note: the test-class counts sum to 317, an inconsistency in the paper.
- Method: 2D mid-vertebral reformations (spline through centroids), 112x112 px at 1 mm, plus a Gaussian centroid channel. Small 4-block CNN (5x5 kernels). Pipeline: (1) contrastive pretraining on 5 spine-region classes; (2) quadruplet-style Grading Loss (two triplet-margin separation terms + a clustering term; margins α=1.5 > β=1 > γ=0.5) ordering embeddings by Genant grade; (3) binary fracture classifier. Adam, lr 1e-4.
- Key results: full pipeline F1 81.5 ± 3.8, sensitivity 76.9, specificity 98.5. Baseline (no pretraining) F1 71.2; grading-only 78.6; contrastive-only 77.6; triplet-only 73.6. Frozen-feature linear SVM: grading 65.2 vs contrastive 57.4 / triplet 57.3. No AUC or per-grade results. The introduction says 82%, inconsistent with the 81.5% elsewhere.
- Code / weights / license: no code release mentioned in the paper.
- Useful for us: ordinal/grade-aware loss is directly reusable for our Genant head; addresses class imbalance and subtle grade-1 cases.
- Limitations / notes: small single dataset (only 46 grade-3); grade 1 excluded (the clinically hardest case); 2D only (3D listed as future work); relies on given centroids; no external validation.
- BibTeX:
```bibtex
@misc{Husseini2020GradingLoss,
  title   = {Grading Loss: A Fracture Grade-based Metric Loss for Vertebral Fracture Detection},
  author  = {Husseini, Malek and Sekuboyina, Anjany and Loeffler, Maximilian and Navarro, Fernando and Menze, Bjoern H. and Kirschke, Jan S.},
  year    = {2020},
  eprint  = {2008.07831},
  archivePrefix = {arXiv}
}
```

### R111. Deep neural networks for osteoporotic vertebral fractures on CT (Tomita)
- Full title: Deep neural networks for automatic detection of osteoporotic vertebral fractures on CT scans (title CONFIRMED via OpenAlex, 2026-10-16)
- Authors: Naofumi Tomita, Yvonne Y. Cheung, Saeed Hassanpour (Dartmouth College / Dartmouth-Hitchcock) (CONFIRMED via OpenAlex)
- Year / Venue / Type: 2018 (online 2018-05-07) / Computers in Biology and Medicine 98:8-15 / journal article
- DOI / arXiv / URL: 10.1016/j.compbiomed.2018.05.011 (CONFIRMED via OpenAlex) ; PII S0010482518301185 ; PMID 29758455
- Access: paywalled; abstract not obtainable in this session (OpenAlex has no abstract; PubMed blocked by reCAPTCHA; ScienceDirect blocked)
- Passes: 1/3 (bibliographic metadata verified via OpenAlex; method keywords from OpenAlex topics + Dartmouth news page, 2026-10-16). Abstract and full text not read.
- Modality & anatomy: CT, thoracolumbar spine (opportunistic)
- Data: unverified
- Method: ResNet34 CNN slice-level feature extraction + LSTM sequence aggregation (CNN and LSTM confirmed by OpenAlex keywords; ResNet34 by the Dartmouth news page)
- Key results: abstract not read. As cited by Nicolaes et al. 2019 (FA15): patient-level AUC 0.92. The news page claims performance "matches practicing radiologists".
- Code / weights / license: unverified. A related US patent exists ("System and method for automatic detection of vertebral fractures on imaging scans using deep networks", USPTO 12026876; not read).
- Useful for us: frequently cited early baseline for opportunistic VCF detection on CT (2D CNN + RNN over slices, the same family as the RSNA 2022 winners).
- Limitations / notes: verify numbers from the abstract before citing results.
- BibTeX:
```bibtex
@article{Tomita2018OVFCT,
  title   = {Deep neural networks for automatic detection of osteoporotic vertebral fractures on {CT} scans},
  author  = {Tomita, Naofumi and Cheung, Yvonne Y. and Hassanpour, Saeed},
  journal = {Computers in Biology and Medicine},
  volume  = {98},
  pages   = {8--15},
  year    = {2018},
  doi     = {10.1016/j.compbiomed.2018.05.011}
}
```

#### C. Trauma CT: cervical spine fracture detection and the RSNA 2022 challenge

### R112. Performance of the winning algorithms of the RSNA 2022 challenge
- Full title: Performance of the Winning Algorithms of the RSNA 2022 Cervical Spine Fracture Detection Challenge
- Authors: Ghee Rye Lee, Adam E. Flanders, Tyler Richards, Felipe Kitamura, Errol Colak, Hui Ming Lin, Robyn L. Ball, Jason Talbott, Luciano M. Prevedello
- Year / Venue / Type: 2024 (online 2024-01-03; correction issued 2024-04-05) / Radiology: Artificial Intelligence 6(1) / challenge report
- DOI / arXiv / URL: 10.1148/ryai.230256 (confirmed on pubs.rsna.org)
- Access: RSNA full-text page readable in this session (2026-10-16)
- Passes: 3/3 (abstract earlier; full text on 2026-10-16 for data/evaluation/results, then failure analysis, comparisons and limitations). Per-model scores are in Table 2, an image that was not captured.
- Modality & anatomy: cervical spine CT (non-contrast, 1-mm axial; post-surgical excluded)
- Data: 3,112 CTs from 12 sites on 6 continents (1,445 positive / 1,667 negative). Train 2,019 (961 positive, 1,444 fractures); private test 789 (362 positive, 672 fractures); public test 304 (122 positive, 175 fractures). Stratified by site, age, sex and fracture level. Bounding boxes on 235 exams by 40 ASNR/ASSR volunteer spine radiologists (MD.ai). Other labels from reports with radiologist QA. 883 teams.
- Method: retrospective evaluation of the top-8 Kaggle models (mostly 2.5D or 3D CNNs). Kaggle metric: weighted log loss at patient level and per vertebra C1-C7, with a 7x weight for missing a positive patient. The paper adds per-level and patient AUC, plus F1/sensitivity/specificity at Youden J thresholds; Kruskal-Wallis + Dunn tests.
- Key results: mean of top 8 (patient level): AUC 0.96 (95% CI 0.95-0.96), F1 90%, sensitivity 88% (86-90), specificity 94% (93-96). C4 is significantly worse than C1/C2/C7 (only 7.5% of training fractures at C4). Typical errors: under-calling rare levels, over-calling C2. Prior work: AUC 0.85 (Zhang) and 0.72 (Salehinejad). Best commercial (Small et al.): sensitivity 76%, specificity 97%, F1 81%.
- Code / weights / license: winners' code via the Kaggle leaderboard and discussion pages (licences vary); no separate repository; no funding.
- Useful for us: benchmark numbers to beat or cite for cervical fracture detection, plus the weighted-log-loss and Youden-threshold evaluation protocol. Level imbalance (C4) argues for per-level calibration and uncertainty reporting in our pipeline.
- Limitations / notes (authors): generalisability untested; non-contrast 1-mm CT only, post-surgical excluded; level imbalance; external and clinical validation needed. No reader comparison.
- BibTeX:
```bibtex
@article{Lee2024RSNACSpineWinners,
  title   = {Performance of the Winning Algorithms of the {RSNA} 2022 Cervical Spine Fracture Detection Challenge},
  author  = {Lee, Ghee Rye and Flanders, Adam E. and Richards, Tyler and Kitamura, Felipe and Colak, Errol and Lin, Hui Ming and Ball, Robyn L. and Talbott, Jason and Prevedello, Luciano M.},
  journal = {Radiology: Artificial Intelligence},
  volume  = {6},
  number  = {1},
  year    = {2024},
  doi     = {10.1148/ryai.230256}
}
```

### R113. RSNA 2022 Cervical Spine Fracture Detection: 1st-place Kaggle solution
- Full title: 1st Place Solution (RSNA 2022 Cervical Spine Fracture Detection, Kaggle discussion 362607)
- Authors: Qishen Ha (1st place confirmed by the official RSNA news release "RSNA Announces Results of Cervical Spine Fracture AI Challenge", Nov 2022: 1 Qishen Ha, 2 RAWE, 3 Darragh, 4 Selim Seferbekov, 5 Speedrun, 6 Skecherz, 7 qwer, 8 Harshit Sheoran). Solution description read from a Zenn walkthrough.
- Year / Venue / Type: 2022 / Kaggle competition write-up / challenge solution
- DOI / arXiv / URL: https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection/discussion/362607 ; walkthrough https://zenn.dev/yuto_mo/articles/f9fb1c8297f252
- Access: open (write-up body not rendered to fetcher; walkthrough read in full)
- Passes: 2/3 (secondary description; author/placement verified via the RSNA news page, 2026-10-16). The Kaggle write-up body still does not render for the fetcher.
- Modality & anatomy: cervical CT
- Data: RSNA 2022 (FA19); 87 cases with 3D masks for the segmentation stage
- Method: Stage 1: 3D U-Net (ResNet18d / EfficientNetV2-S encoders, 128^3) segments C1-C7; Stage 2: crop each vertebra, sample 15 slices, 5-channel 2.5D input (+/-2 neighbours) + mask channel; 2D CNN (EffNetV2-S, ConvNeXt-Tiny/Nano/Pico, NFNet-L0) features -> LSTM over slices; per-vertebra and per-patient variants, 5-fold ensembles. Plain 3D CNNs reportedly did not work well.
- Key results: private LB score unverified (the RSNA release gives no scores). Top-8 aggregate performance on the held-out test is in FA20. Prize pool for the top performers was $30,000 total.
- Code / weights / license: Kaggle notebooks (discussion 362787); licence unverified
- Useful for us: proven recipe (segment -> per-vertebra 2.5D CNN + sequence model) we can reuse for per-level fracture probability on CT.
- Limitations / notes: ~7.5 h inference for test set; heavy ensembles; not peer reviewed.
- BibTeX:
```bibtex
@misc{Kaggle2022RSNACSpineFirst,
  title        = {{RSNA} 2022 Cervical Spine Fracture Detection: 1st Place Solution},
  author       = {Ha, Qishen},
  year         = {2022},
  howpublished = {\url{https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection/discussion/362607}},
  note         = {Accessed 2026-10-16}
}
```

### R114. CT cervical spine fracture detection using a commercial CNN (Aidoc)
- Full title: CT Cervical Spine Fracture Detection Using a Convolutional Neural Network
- Authors: J.E. Small, P. Osler, A.B. Paul, M. Kunst (Lahey Hospital and Medical Center, Burlington MA)
- Year / Venue / Type: 2021 / AJNR Am J Neuroradiol 42(7):1341-1347 / journal article
- DOI / arXiv / URL: 10.3174/ajnr.A7094
- Access: open (AJNR full text)
- Passes: 3/3 (abstract earlier; AJNR full text read 2026-10-16 for data/results, then failure analysis/limitations/COI)
- Modality & anatomy: cervical spine CT
- Data: 2015-2018 CTs (before deployment), all with cervical MRI within 48 h. 869 identified, 162 not processable by the CNN (mostly DICOM header issues), final 665 (143 fracture-positive, 522 negative; ~21.5% prevalence). Mostly one site (Philips Ingenuity). Reference: consensus of 2 neuroradiologists with CT, MRI and CNN output.
- Method: FDA-cleared Aidoc C-spine (version not stated): 3D segmentation-based region proposal + false-positive reduction. Detects linear lucency, C1-7 only, no acute vs chronic distinction. Vendor training ~12k studies from 83 sites; validation ~8k from 47 sites.
- Key results: CNN accuracy 92% (90-94), sensitivity 76% (68-83; 109/143), specificity 97%, PPV 87%, NPV 94%, κ 0.76. Radiologists: accuracy 95%, sensitivity 93%, specificity 96%, PPV 87%, NPV 98%, κ 0.87. At 1.9% prevalence the estimated PPV is 30% (CNN) vs 32% (radiologists). The CNN found 7 fractures radiologists missed (4 chronic). Time to result: CNN 3-8 min vs report 33-43 min. Discussion text gives 79% / 96% (inconsistent with Results).
- Code / weights / license: commercial
- Useful for us: real-world baseline showing commercial sensitivity gap; useful for positioning.
- Limitations / notes: CNN misses were fracture-dislocation (translation, not lucency), distraction injuries, distal spinous process fractures and lower-C-spine fractures under beam attenuation. False positives: degenerative change, nutrient foramina, congenital C1 anomaly, laminoplasty. Retrospective, mostly single site; MRI-inclusion inflates prevalence; reference standard saw CNN output (bias); 162 unprocessable exams. No Aidoc COI declared. Lesson for us: model translation/alignment explicitly, not only lucency.
- BibTeX:
```bibtex
@article{Small2021CSpineCNN,
  title   = {{CT} Cervical Spine Fracture Detection Using a Convolutional Neural Network},
  author  = {Small, J. E. and Osler, P. and Paul, A. B. and Kunst, M.},
  journal = {American Journal of Neuroradiology},
  volume  = {42},
  number  = {7},
  pages   = {1341--1347},
  year    = {2021},
  doi     = {10.3174/ajnr.A7094}
}
```

### R115. Failure-mode analysis of a commercial cervical fracture algorithm
- Full title: Diagnostic Accuracy and Failure Mode Analysis of a Deep Learning Algorithm for the Detection of Cervical Spine Fractures
- Authors: A.F. Voter, M.E. Larson, J.W. Garrett, J.-P.J. Yu (University of Wisconsin-Madison)
- Year / Venue / Type: 2021 / AJNR 42(8):1550-1556 / journal article
- DOI / arXiv / URL: 10.3174/ajnr.A7179
- Access: open (AJNR full text)
- Passes: 3/3 (abstract earlier; AJNR full text read 2026-10-16 for data/results, then failure modes/limitations/COI). Table 2 category counts not captured.
- Modality & anatomy: emergent non-contrast cervical CT
- Data: 1,904 consecutive adult emergent non-contrast C-spine CTs (2020-01-20 to 2020-10-08; mean age 60 ± 22; level-I trauma centre + outreach; 9 GE scanner models); 122 fractures (~6.4%). Reference: attending neuroradiologist report, with a third reviewer for discordant cases.
- Method: evaluation of Aidoc C-spine (FDA 510(k) K190896): thin axial + sagittal bone reconstructions, scan-level flag with heat-map key image.
- Key results: sensitivity 54.9% (45.7-63.9; 67/122), specificity 94.1%, PPV 38.7% (106 false-positive studies), NPV 96.8%, concordance 91.5%. Below the FDA-reported sensitivity. Misses: chronic/age-indeterminate fractures, osteophyte and vertebral-body fractures, 5/10 acute transverse-foramen fractures; not associated with scanner/site/sex. False positives: degenerative findings (ossicles, facet degeneration, ligamentum flavum ossification), non-cervical fractures (rib, skull), anatomic variants, motion. Misclassified patients were older (64 vs 60, P=.03).
- Code / weights / license: commercial
- Useful for us: motivates explicit acute vs chronic modelling, external validation and uncertainty-triggered "request better scan / review" behaviour.
- Limitations / notes: single institution, GE only; reference readers saw AI output; no workflow-time analysis; few acute fractures for subgroups; real-world prevalence vs balanced FDA set (a prevalence effect on PPV that we must report). Authors not Aidoc-affiliated; NIH funded.
- BibTeX:
```bibtex
@article{Voter2021CSpineFailure,
  title   = {Diagnostic Accuracy and Failure Mode Analysis of a Deep Learning Algorithm for the Detection of Cervical Spine Fractures},
  author  = {Voter, A. F. and Larson, M. E. and Garrett, J. W. and Yu, J.-P. J.},
  journal = {American Journal of Neuroradiology},
  volume  = {42},
  number  = {8},
  pages   = {1550--1556},
  year    = {2021},
  doi     = {10.3174/ajnr.A7179}
}
```

#### D. Vertebral fracture AI on radiographs and X-ray vertebra labelling

### R116. Deep learning VF detection on plain frontal abdominal radiographs
- Full title: Application of deep learning algorithm to detect and visualize vertebral fractures on plain frontal radiographs
- Authors: Chen HY, Hsu BWY, Yin YK, et al.
- Year / Venue / Type: 2021 / PLOS ONE 16(1):e0245992 / journal article
- DOI / arXiv / URL: 10.1371/journal.pone.0245992
- Access: open
- Passes: 3/3 full text
- Modality & anatomy: frontal (AP) abdominal radiographs, thoracolumbar spine
- Data: 1,306 radiographs (438 VF, 868 non-VF) from a Fracture Liaison Service database, NTUH Hsin-Chu, 2015-2018; VF = >=20% height loss (Genant SQ); only 46.6% of VFs mentioned in original reports
- Method: ImageNet-pretrained ResNeXt-50, 224x224 input, 5-fold CV, Grad-CAM
- Key results: accuracy 73.59%, sensitivity 73.81%, specificity 73.02%, AUC 0.72; 10 clinicians mean accuracy 76.8%
- Code / weights / license: none; data restricted
- Useful for us: quantifies under-reporting of VFs on incidental radiographs (motivation); shows frontal-view-only detection is weak -> our system should request a lateral view when only AP is available.
- Limitations / notes: single centre; low resolution input; Grad-CAM sometimes wrong.
- BibTeX:
```bibtex
@article{Chen2021VFFrontalXray,
  title   = {Application of deep learning algorithm to detect and visualize vertebral fractures on plain frontal radiographs},
  author  = {Chen, Hsuan-Yu and Hsu, Benny Wei-Yun and Yin, Yu-Kai and Lin, Feng-Huei and Yang, Tsung-Han and Yang, Rong-Sen and Lee, Chih-Kuo and Tseng, Vincent S.},
  journal = {PLOS ONE},
  volume  = {16},
  number  = {1},
  pages   = {e0245992},
  year    = {2021},
  doi     = {10.1371/journal.pone.0245992}
}
```

### R117. Can a deep-learning model detect vertebral fractures like subspecialists? (lateral radiographs)
- Full title: Can a Deep-learning Model for the Automated Detection of Vertebral Fractures Approach the Performance Level of Human Subspecialists?
- Authors: Yi-Chu Li, Hung-Hsun Chen, Henry Horng-Shing Lu, Hung-Ta Hondar Wu, Ming-Chau Chang, Po-Hsin Chou (Taipei Veterans General Hospital / NYCU)
- Year / Venue / Type: 2021 (online 2021-02-26) / Clinical Orthopaedics and Related Research 479(7):1598-1612 / journal article (Level II diagnostic)
- DOI / arXiv / URL: 10.1097/CORR.0000000000001685 (CONFIRMED via OpenAlex, 2026-10-16) ; PMID 33651768 ; PMC8208416
- Access: publisher paywalled; green OA copy in PMC (PMC blocked by reCAPTCHA in this session)
- Passes: 1/3 (full structured abstract via OpenAlex, 2026-10-16; earlier digest page). Full text not read.
- CORRECTIONS vs the earlier digest-based entry: accuracy is 93% (773/830), not 92%. Data is 941 patients with 1,101 vertebrae T7-L5 (split 565/188/188), not "6,358 normal, 1,101 fractured". The "grade-1 sensitivity 78%" and "52-patient external set" figures are NOT in the abstract (unverified). Runtime is ~90 s per case.
- Modality & anatomy: lateral thoracolumbar radiographs (T7-L5)
- Data: 1,019 patients >60 y, single institution 2016-2018. 78 excluded (missing CT/MRI, poor quality, myeloma, instrumentation), leaving 941 (mean age 76 ± 12). Reference: independent surgeon + radiologist reads against CT/MRI reports, with consensus for disagreements. Genant grades 1 (<25%), 2 (26-40%), 3 (>40%).
- Method: framework of object detection + preprocessing + classification; ensemble model.
- Key results: test accuracy 93%, sensitivity 91% (129/141), specificity 93% (644/689). Kappa 0.72 thoracic / 0.77 lumbar. AUC by Genant grade: G1 0.919, G2 0.989, G3 0.990. Sensitivity 97% for osteoporotic (T ≤ -2.5) vs 83% for non-osteoporotic fractures. External validation: accuracy 89%, sensitivity 83%, specificity 95%.
- Code / weights / license: not stated in the abstract (unverified)
- Useful for us: per-grade AUC confirms grade-1 (mild) VFs are the hard case. Good target metrics for our radiograph fracture head. The external drop (sensitivity 91% to 83%) is a realistic expectation.
- Limitations / notes: single-centre development; retrospective; reference from reports rather than re-reads; T7 and above not covered.
- BibTeX:
```bibtex
@article{Li2021VFSubspecialists,
  title   = {Can a Deep-learning Model for the Automated Detection of Vertebral Fractures Approach the Performance Level of Human Subspecialists?},
  author  = {Li, Yi-Chu and Chen, Hung-Hsun and Lu, Henry Horng-Shing and Wu, Hung-Ta Hondar and Chang, Ming-Chau and Chou, Po-Hsin},
  journal = {Clinical Orthopaedics and Related Research},
  volume  = {479},
  number  = {7},
  pages   = {1598--1612},
  year    = {2021},
  doi     = {10.1097/CORR.0000000000001685}
}
```

### R118. Multicentre DL classification of acute/chronic/pathologic VCF on radiographs (VCFNet)
- Full title: Deep learning-based artificial intelligence model for classification of vertebral compression fractures: A multicenter diagnostic study
- Authors: Xu F, Xiong Y, Ye G, et al.
- Year / Venue / Type: 2023 / Frontiers in Endocrinology 14:1025749 / journal article
- DOI / arXiv / URL: 10.3389/fendo.2023.1025749
- Access: open
- Passes: 3/3 full text
- Modality & anatomy: lateral lumbar radiographs; labels confirmed by MRI, PET or histopathology
- Data: 1,904 patients, 4 Chinese hospitals, 2,609 vertebrae; 3 external sets (111/217/176 vertebrae) + prospective set (74 vertebrae)
- Method: ResNet-18 transfer learning on bounding-box crops (224x224); human-AI collaboration study with trainee/competent/expert readers
- Key results: reported "accuracy" 0.850 internal, 0.829 prospective, 0.757-0.832 external (these match AUC columns in tables, see note); collaboration-set AUC acute 0.780, chronic 0.809, pathologic 0.734; expert + DL improved to 0.801/0.825/0.751
- Code / weights / license: github.com/Xiongyuchao/VCFNet (licence unverified)
- Useful for us: acute vs chronic vs pathologic distinction on X-ray is clinically key and hard; supports a "recommend MRI (STIR) to establish acuity" output.
- Limitations / notes: manual ROI; accuracy/AUC wording inconsistent; implants and severe scoliosis excluded.
- BibTeX:
```bibtex
@article{Xu2023VCFNet,
  title   = {Deep learning-based artificial intelligence model for classification of vertebral compression fractures: A multicenter diagnostic study},
  author  = {Xu, Fan and Xiong, Yuchao and Ye, Guoxi and Liang, Yingying and Guo, Wei and Deng, Qiuping and others},
  journal = {Frontiers in Endocrinology},
  volume  = {14},
  pages   = {1025749},
  year    = {2023},
  doi     = {10.3389/fendo.2023.1025749}
}
```

### R119. VertXNet (2022): segmentation and identification of lumbar and cervical vertebrae on X-ray
- Full title: VertXNet: Automatic Segmentation and Identification of Lumbar and Cervical Vertebrae from Spinal X-ray Images
- Authors: Yao Chen, Yuanhan Mo, Aimee Readie, et al. (Novartis / Oxford; full list in FA28)
- Year / Venue / Type: 2022 / arXiv 2207.05476 / preprint
- DOI / arXiv / URL: arXiv:2207.05476
- Access: preprint
- Passes: 1/3 abstract only. Not re-read: superseded by FA28 (journal extension of this conference version; FA28 full text describes the same pipeline).
- Modality & anatomy: lateral cervical and lumbar radiographs (ankylosing spondylitis trial data)
- Data: in-house axSpA/AS trial cohort (MEASURE 1 per FA28; size in this version unverified)
- Method: ensemble of U-Net and Mask R-CNN; Mask R-CNN detects "reference" vertebrae to infer labels
- Key results: mean Dice ~0.9
- Code / weights / license: not stated
- Useful for us: X-ray vertebra labelling front end (needed before per-vertebra VF grading and alignment angles).
- Limitations / notes: AS-specific data; superseded by FA28.
- BibTeX:
```bibtex
@misc{Chen2022VertXNet,
  title   = {{VertXNet}: Automatic Segmentation and Identification of Lumbar and Cervical Vertebrae from Spinal X-ray Images},
  author  = {Chen, Yao and Mo, Yuanhan and Readie, Aimee and Ligozio, Gregory and Coroller, Thibaud and Papiez, Bartlomiej W.},
  year    = {2022},
  eprint  = {2207.05476},
  archivePrefix = {arXiv}
}
```

### R120. VertXNet (2023): ensemble method with external validation
- Full title: VertXNet: An Ensemble Method for Vertebrae Segmentation and Identification of Spinal X-Ray
- Authors: Yao Chen, Yuanhan Mo, Aimee Readie, Gregory Ligozio, Indrajeet Mandal, Faiz Jabbar, Thibaud Coroller, Bartłomiej W. Papież (Novartis; Oxford Big Data Institute; Oxford University Hospitals)
- Year / Venue / Type: 2023 / arXiv 2302.03476 / preprint (a published version exists per Oxford repository; venue unverified)
- DOI / arXiv / URL: arXiv:2302.03476
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv PDF read 2026-10-16 for data/method/results, then limitations/code). Published venue still unverified.
- Modality & anatomy: lateral spinal radiographs
- Data: MEASURE 1 (secukinumab axSpA trial): 512 lateral X-rays (293 cervical, 219 lumbar), 80/20 split. PREVENT (external trial): 226 (132 C, 94 L). NHANES II (public): 445 usable of 544 landmark-annotated images (C3-C7, L1-L5 complete; C2/S1 reference vertebrae added by radiologists).
- Method: modified U-Net (binary) + Mask R-CNN (ResNet-50-FPN). Rule-based ensemble: overlap agreement threshold 0.6 to merge masks; overlaps resolved with Mask R-CNN contours; missing vertebrae recovered by an area check; masks sorted vertically. Mask R-CNN detects the reference vertebra (C2 or S1), and the rest are labelled by counting from it.
- Key results: mean Dice 0.90 on MEASURE 1 (Mask R-CNN 0.73, U-Net 0.72); 0.89 PREVENT and 0.88 NHANES II without retraining. Per vertebra: C2-C6 ~0.90, C7 0.881, T1 0.518 (rare), T11/T12 0.84/0.86, L1-L5 0.85-0.87, S1 0.823. Identification accuracy is not reported separately (Dice and Panoptic Quality only).
- Code / weights / license: not stated
- Useful for us: evidence that NHANES II radiographs are a usable public external test set; label-inference trick is reusable.
- Limitations / notes: hand-designed ensemble rules; models trained separately; labelling fails if C2/S1 is missing or misdetected (a key risk for our level-labelling); rare T1/T11/T12 perform worse; axSpA trial populations. No code; NHANES II reference labels were promised but the link is a placeholder.
- BibTeX:
```bibtex
@misc{Chen2023VertXNetEnsemble,
  title   = {{VertXNet}: An Ensemble Method for Vertebrae Segmentation and Identification of Spinal X-Ray},
  author  = {Chen, Yao and Mo, Yuanhan and Readie, Aimee and Ligozio, Gregory and Mandal, Indrajeet and Jabbar, Faiz and Coroller, Thibaud and Papiez, Bartlomiej W.},
  year    = {2023},
  eprint  = {2302.03476},
  archivePrefix = {arXiv}
}
```

### R121. VinDr-SpineXR: spinal lesion detection dataset and framework
- Full title: VinDr-SpineXR: A deep learning framework for spinal lesions detection and classification from radiographs
- Authors: Hieu T. Nguyen, Hieu H. Pham, Nghia T. Nguyen, Ha Q. Nguyen, Thang Q. Huynh, Minh Dao, Van Vu (Vingroup Big Data Institute, HUST, VinUniversity, Yale)
- Year / Venue / Type: 2021 / arXiv 2106.12930 (published at MICCAI 2021 per common citation: unverified) / dataset + method
- DOI / arXiv / URL: arXiv:2106.12930
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv PDF read 2026-10-16 for data/method/results, then limitations). Venue not named in the arXiv PDF; MICCAI 2021 remains unverified.
- Modality & anatomy: spine radiographs (cervical, thoracic, lumbar)
- Data: 10,468 images from 5,000 studies (2010/11-2020, Vietnamese hospitals); 3 radiologists with ≥10 y experience, ONE radiologist per scan. 13 labels: ankylosis, disc space narrowing, enthesophytes, foraminal stenosis, fracture, osteophytes, sclerotic lesion, spondylolisthesis, subchondral sclerosis, surgical implant, vertebral collapse, foreign body, other. 7 localised with boxes: osteophytes, disc space narrowing, surgical implant, foraminal stenosis, spondylolisthesis, vertebral collapse, other lesions. Split: 4,000 studies / 8,390 images train; 1,000 / 2,078 test.
- Method: DenseNet-121/169/201 average ensemble for normal/abnormal (Youden threshold 0.2808); detectors Faster R-CNN, RetinaNet, EfficientDet, Sparse R-CNN. Fusion: keep all boxes if the classifier says abnormal, else only boxes with confidence >0.5.
- Key results: classification AUROC 88.61% (87.19-90.02), sensitivity 83.07%, specificity 79.32%, F1 81.06%. Detection mAP@0.5: Sparse R-CNN 33.15%, framework 33.56%. Sparse R-CNN AP: vertebral collapse 49.30, spondylolisthesis 45.32, osteophytes 48.16, implant 72.20, foraminal stenosis 32.67, disc space narrowing 20.09, other 5.41.
- Code / weights / license: the paper says dataset, code and models are public via the project page and GitHub; no licence stated in the paper. PhysioNet hosting is not mentioned in the paper (still unverified).
- Useful for us: largest public labelled spine X-ray finding dataset; includes fracture and listhesis boxes for our X-ray branch.
- Limitations / notes: single annotator per scan (no agreement data); rare labels (fracture, ankylosis) merged or unmodelled; single source, no external test; heuristic fusion with tiny gain; table inconsistencies (framework below Sparse R-CNN for collapse/implant despite text claims).
- BibTeX:
```bibtex
@misc{Nguyen2021VinDrSpineXR,
  title   = {{VinDr-SpineXR}: A deep learning framework for spinal lesions detection and classification from radiographs},
  author  = {Nguyen, Hieu T. and Pham, Hieu H. and Nguyen, Nghia T. and Nguyen, Ha Q. and Huynh, Thang Q. and Dao, Minh and Vu, Van},
  year    = {2021},
  eprint  = {2106.12930},
  archivePrefix = {arXiv}
}
```

#### E. Scoliosis and Cobb angle estimation (AASCE 2019 and later)

### R122. BoostNet: landmark estimation for AIS (source of the AASCE training data)
- Full title: Automatic Landmark Estimation for Adolescent Idiopathic Scoliosis Assessment Using BoostNet
- Authors: Hongbo Wu, Christopher S. Bailey, Parham Rasoulinejad, Shuo Li (Western University, London ON)
- Year / Venue / Type: 2017 / MICCAI 2017, LNCS 10433, pp. 127-135 (Springer) / conference paper
- DOI / arXiv / URL: 10.1007/978-3-319-66182-7_15 (CONFIRMED via OpenAlex, 2026-10-16)
- Access: paywalled at Springer; full text read from a mirror PDF hosted by HKU (i.cs.hku.hk/fyp/2019/fyp19013/Reference/reference1.pdf)
- Passes: 3/3 (OpenAlex metadata; full-text mirror read for data/method/results and limitations, 2026-10-16)
- Modality & anatomy: AP spinal radiographs, AIS, 17 thoracic + lumbar vertebrae (cervical excluded)
- Data: 481 AP radiographs (431 train/validation, 50 test, patient-disjoint), 68 landmarks per image (4 corners x 17 vertebrae), annotated by the authors. CORRECTION: the earlier entry's "609 radiographs" is the later AASCE/SpineWeb Dataset 16 size, not this paper's.
- Method: CNN features. A BoostLayer replaces outlier features (reconstruction error > 2 SD) with the population mean. A "spinal structured multi-output" layer uses an adjacency dependency matrix as a structural prior. SGD-Nesterov, Keras.
- Key results: test MSE 0.0046 (fraction of image size) with Pearson ρ 0.94, vs ConvNet 0.018/0.84, RFR 0.0052/0.94, SVR 0.006/0.93. Claims >5x MSE reduction over the ConvNet.
- Code / weights / license: the dataset later became SpineWeb Dataset 16 / AASCE (see AL01). No code mentioned.
- Useful for us: dataset-origin citation for AASCE/SpineWeb Dataset 16. The structural adjacency prior on landmarks is an idea for our vertebra-corner regressor.
- Limitations / notes: small test set (50); authors' own annotations with no inter-observer study; Cobb angle not evaluated; the CV SD is larger than its mean (0.00068 ± 0.004), which is odd.
- BibTeX:
```bibtex
@inproceedings{Wu2017BoostNet,
  title     = {Automatic Landmark Estimation for Adolescent Idiopathic Scoliosis Assessment Using {BoostNet}},
  author    = {Wu, Hongbo and Bailey, Christopher S. and Rasoulinejad, Parham and Li, Shuo},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2017},
  series    = {Lecture Notes in Computer Science},
  volume    = {10433},
  pages     = {127--135},
  year      = {2017},
  publisher = {Springer},
  doi       = {10.1007/978-3-319-66182-7_15}
}
```

### R123. MVC-Net: multi-view AIS assessment
- Full title: Automated comprehensive Adolescent Idiopathic Scoliosis assessment using MVC-Net
- Authors: Hongbo Wu, Christopher S. Bailey, Parham Rasoulinejad, Shuo Li (Western University)
- Year / Venue / Type: 2018 (online 2018-05-18) / Medical Image Analysis 48:1-11 (CONFIRMED via OpenAlex 2026-10-16) / journal article
- DOI / arXiv / URL: 10.1016/j.media.2018.05.005 (CONFIRMED via OpenAlex) ; PMID 29803920
- Access: paywalled (not read)
- Passes: 3/3 (OpenAlex metadata; accepted manuscript full text read via an HKU-hosted mirror (i.cs.hku.hk/fyp/2019/fyp19013/Reference/reference4.pdf), 2026-10-16: data/method/results, then ablations/limitations)
- Modality & anatomy: AP + lateral radiographs, AIS
- Data: 526 radiographs from 154 patients (half AP, half lateral), single clinic (London ON), resized to 128x256. 15 T+L vertebrae x 4 corners = 60 landmarks per view. Three Cobb angles (PT, MT, TL) per view. 10-fold patient-wise CV.
- Method: multi-view correlation network combining AP and lateral views for landmark and Cobb estimation
- Key results: direct Cobb circular MAE 4.04° (AP) / 4.07° (LAT) vs best baseline 5.37/5.54 (Wu 2017). SMAPE 35.85% AP / 23.72% LAT; mixed vs baselines, worse when angles are computed from predicted landmarks. Landmark scaled MAE 0.0398 (AP) / 0.0459 (LAT). Ablations favour the X-module, Joint Regression loss (Pearson + log-cosh) and Iterative Landmark-Angle Training.
- Code / weights / license: none mentioned
- Useful for us: precedent for joint AP+lateral modelling (relevant for EOS biplanar inputs).
- Limitations / notes: single clinic, no brace/metal artefacts, no external test; claim of robustness vs inter-observer SD (3.2°) compares different quantities. Note the 15-vertebra/526-image set differs from the 17-vertebra AASCE set.
- Method details (pass 2): X-modules fuse AP and lateral feature maps with learned spatial weighting. Spinal Landmark Estimator uses a structured adjacency output layer (120 coordinates). Cobb Angle Estimator regresses angles from adjusted landmarks. SGD momentum 0.95, lr 0.01, 100 epochs.
- BibTeX:
```bibtex
@article{Wu2018MVCNet,
  title   = {Automated comprehensive Adolescent Idiopathic Scoliosis assessment using {MVC-Net}},
  author  = {Wu, Hongbo and Bailey, Christopher S. and Rasoulinejad, Parham and Li, Shuo},
  journal = {Medical Image Analysis},
  volume  = {48},
  pages   = {1--11},
  year    = {2018},
  doi     = {10.1016/j.media.2018.05.005}
}
```

### R124. MVE-Net: multi-view extrapolation for Cobb angles
- Full title: Accurate Automated Cobb Angles Estimation using Multi-View Extrapolation Net
- Authors: Liansheng Wang, Qiuhao Xu, Stephanie Leung, Jonathan Chung, Bo Chen, Shuo Li
- Year / Venue / Type: 2019 (online 2019-08-09) / Medical Image Analysis 58:101542 (CONFIRMED via OpenAlex 2026-10-16) / journal article
- DOI / arXiv / URL: 10.1016/j.media.2019.101542 (CONFIRMED via OpenAlex)
- Access: paywalled (not read)
- Passes: 0/3 content (bibliographic metadata fully verified via OpenAlex 2026-10-16; no abstract in OpenAlex; ScienceDirect/PubMed blocked; no OA mirror found in a targeted search)
- Modality & anatomy: AP + lateral radiographs
- Data: unverified
- Method: multi-view extrapolation network regressing Cobb angles
- Key results: unverified
- Code / weights / license: unverified
- Useful for us: direct-regression baseline for Cobb angle.
- Limitations / notes: unverified.
- BibTeX:
```bibtex
@article{Wang2019MVENet,
  title   = {Accurate Automated {Cobb} Angles Estimation using Multi-View Extrapolation Net},
  author  = {Wang, Liansheng and Xu, Qiuhao and Leung, Stephanie and Chung, Jonathan and Chen, Bo and Li, Shuo},
  journal = {Medical Image Analysis},
  volume  = {58},
  pages   = {101542},
  year    = {2019},
  doi     = {10.1016/j.media.2019.101542}
}
```

### R125. Ensembles of cascaded networks for spine centreline / Cobb (AASCE entry)
- Full title: Automated Estimation of the Spinal Curvature via Spine Centerline Extraction with Ensembles of Cascaded Neural Networks
- Authors: Dubost F, Collery B, Renaudier A, et al.
- Year / Venue / Type: 2019 (proceedings 2020) / AASCE challenge @ MICCAI 2019; arXiv 1911.01126; published in Springer LNCS CSI 2019 volume (978-3-030-39752-4, chapter unverified) / challenge paper
- DOI / arXiv / URL: arXiv:1911.01126
- Access: preprint
- Passes: 3/3 full text
- Modality & anatomy: AP radiographs, AIS
- Data: 609 training scans (68 landmarks), 61 held out; 100 challenge test scans (3 Cobb angles each)
- Method: two cascaded U-Nets (spine segmentation -> centreline), post-processing (threshold 0.25, CC filtering, heat-equation smoothing), Cobb from centreline tangent slopes at 19 points; ensemble of ensembles (10 subsets)
- Key results: challenge test SMAPE 22.96
- Code / weights / license: none
- Useful for us: landmark-free, centreline-based Cobb computation is robust and interpretable; reusable for curvature on any modality with a spine mask (CT/MRI coronal too).
- Limitations / notes: needed manual cropping of test images; small curves dominate.
- BibTeX:
```bibtex
@misc{Dubost2019SpineCenterline,
  title   = {Automated Estimation of the Spinal Curvature via Spine Centerline Extraction with Ensembles of Cascaded Neural Networks},
  author  = {Dubost, Florian and Collery, Benjamin and Renaudier, Antonin and Roc, Axel and Posocco, Nicolas and Bortsova, Gerda and Niessen, Wiro and de Bruijne, Marleen},
  year    = {2019},
  eprint  = {1911.01126},
  archivePrefix = {arXiv}
}
```

### R126. Vertebra-focused landmark detection for scoliosis
- Full title: Vertebra-Focused Landmark Detection for Scoliosis Assessment
- Authors: Jingru Yi, Pengxiang Wu, Qiaoying Huang, Hui Qu, Dimitris N. Metaxas (Rutgers University)
- Year / Venue / Type: 2020 / IEEE ISBI 2020 (video on ISBI 2020 resource centre; proceedings DOI unverified); arXiv 2001.03187
- DOI / arXiv / URL: arXiv:2001.03187
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv PDF read 2026-10-16 for data/method/results, then limitations/code). ISBI venue not named in the PDF (still unverified).
- Modality & anatomy: AP radiographs, AIS
- Data: 580 AP radiographs from the AASCE 2019 training data (~2500x1000 px), split 348/116/116; 17 vertebrae x 4 corners (68 landmarks).
- Method: ResNet34 encoder-decoder (ImageNet init), 1024x512 input, 256x128 output. Three heads: centre heatmap (focal loss α=2, β=4, size-adaptive Gaussians), centre sub-pixel offset (L1), and 4x2 centre-to-corner vectors (L1). Corner order is preserved by construction. Adam lr 2.5e-4, ≤100 epochs.
- Key results: test SMAPE 10.81 (PT 6.26 / MT 18.04 / TL 23.42) vs segmentation baseline 16.48 and regression baseline 23.43. Landmark error 50.11 (units unstated) vs 74.07 / 77.94. 5.65 FPS on a K40. Note: this is an internal split of the training data, not the official AASCE test set (whose best is 21.71, AL01), so the numbers are not comparable.
- Code / weights / license: https://github.com/yijingru/Vertebra-Landmark-Detection
- Useful for us: widely reused open-source landmark baseline; per-vertebra corners also give vertebral height ratios (VF) and endplate tilts.
- Limitations / notes: can skip vertebrae with weak morphology; TL region worst; single dataset; no ablations, run variance or statistics; baselines not resolution-matched. Code licence not stated in the paper.
- BibTeX:
```bibtex
@misc{Yi2020VertebraFocused,
  title   = {Vertebra-Focused Landmark Detection for Scoliosis Assessment},
  author  = {Yi, Jingru and Wu, Pengxiang and Huang, Qiaoying and Qu, Hui and Metaxas, Dimitris N.},
  year    = {2020},
  eprint  = {2001.03187},
  archivePrefix = {arXiv}
}
```

### R127. Seg4Reg+: segmentation-regression consistency for Cobb angle
- Full title: Seg4Reg+: Consistency Learning between Spine Segmentation and Cobb Angle Regression
- Authors: Lin Y, Liu L, Ma K, Zheng Y (Tencent Jarvis Lab)
- Year / Venue / Type: 2021 / MICCAI 2021 (venue per citing literature: unverified); arXiv 2208.12462
- DOI / arXiv / URL: arXiv:2208.12462
- Access: preprint
- Passes: 2/3 (ar5iv full text, methods)
- Modality & anatomy: AP radiographs
- Data: AASCE
- Method: PSPNet (ResNet-50) segmentation + regression network; ROIE gate (CAM attention to segmentation), AR module (attention regularisation), triangle consistency learning. Predecessor Seg4Reg won 1st place in AASCE 2019.
- Key results: SMAPE 8.47 (as reported in B-Spine comparison table) or 7.32 (as reported in MMA-Net table) - inconsistent across citing papers, verify
- Code / weights / license: none found
- Useful for us: illustrates that combining segmentation priors with direct angle regression beats landmark-only approaches; note landmark error sensitivity argument.
- Limitations / notes: depends on segmentation quality.
- BibTeX:
```bibtex
@misc{Lin2022Seg4RegPlus,
  title   = {{Seg4Reg+}: Consistency Learning between Spine Segmentation and {Cobb} Angle Regression},
  author  = {Lin, Yi and Liu, Luyan and Ma, Kai and Zheng, Yefeng},
  year    = {2022},
  eprint  = {2208.12462},
  archivePrefix = {arXiv}
}
```

### R128. MMA-Net: multiple morphology-aware network
- Full title: MMA-Net: Multiple Morphology-Aware Network for Automated Cobb Angle Measurement
- Authors: Qiu Z, Yang J, Wang J
- Year / Venue / Type: 2023 / arXiv 2309.13817 (venue unverified) / preprint
- DOI / arXiv / URL: arXiv:2309.13817
- Access: preprint
- Passes: 2/3 full text (methods and results)
- Modality & anatomy: AP radiographs
- Data: AASCE 609 images (481 train / 128 test)
- Method: Res-UNet++ producing spine region, centreline and boundary maps; EfficientNet-b4 regressor on image + maps; losses Dice+BF1 and SMAPE+MAE+CMAE
- Key results: SMAPE 7.28%, MAE 3.18 deg, CMAE 2.26 deg (comparison: KEF 8.62, VF 7.84, Seg4Reg+ 7.32)
- Code / weights / license: not provided
- Useful for us: current-style SOTA on AASCE; useful comparison table of prior methods.
- Limitations / notes: uses AASCE validation split as test, not the original 100-image challenge test.
- BibTeX:
```bibtex
@misc{Qiu2023MMANet,
  title   = {{MMA-Net}: Multiple Morphology-Aware Network for Automated {Cobb} Angle Measurement},
  author  = {Qiu, Zhengxuan and Yang, Jie and Wang, Jiankun},
  year    = {2023},
  eprint  = {2309.13817},
  archivePrefix = {arXiv}
}
```

### R129. LaNet: landmark-aware network for Cobb angle
- Full title: A Landmark-aware Network for Automated Cobb Angle Estimation Using X-ray Images
- Authors: Yang J, Wang J, Meng MQH
- Year / Venue / Type: 2024 / arXiv 2405.19645 (venue unverified) / preprint
- DOI / arXiv / URL: arXiv:2405.19645
- Access: preprint
- Passes: 3/3 full text
- Modality & anatomy: AP radiographs
- Data: AASCE 707 images (481/128/98 train/val/test)
- Method: Feature Robustness Enhancement Module (landmark attention), landmark-aware weighted KL heatmap loss + L2, Cobb calculation via inflection vertebrae from tilt
- Key results: landmark MSE 3.21 mm; test SMAPE 8.99%, CMAE 3.63 deg (val SMAPE 4.51%)
- Code / weights / license: not provided
- Useful for us: explicit Cobb-from-landmarks algorithm (end-vertebra selection) and notes failure modes (implants, severe curves >40 deg).
- Limitations / notes: few severe curves; postoperative images degrade.
- BibTeX:
```bibtex
@misc{Yang2024LaNet,
  title   = {A Landmark-aware Network for Automated {Cobb} Angle Estimation Using {X-ray} Images},
  author  = {Yang, Jie and Wang, Jiankun and Meng, Max Q.-H.},
  year    = {2024},
  eprint  = {2405.19645},
  archivePrefix = {arXiv}
}
```

### R130. B-Spine: B-spline curve representation for spinal curvature
- Full title: B-Spine: Learning B-Spline Curve Representation for Robust and Interpretable Spinal Curvature Estimation
- Authors: Wang H, Song Q, Yin R, et al.
- Year / Venue / Type: 2023 / arXiv 2310.09603 (Elsevier submission; venue unverified) / preprint
- DOI / arXiv / URL: arXiv:2310.09603
- Access: preprint
- Passes: 2/3 full text
- Modality & anatomy: AP radiographs (incl. low-quality images)
- Data: AASCE2019; new CJUH-JLU dataset (584 low-quality radiographs; on request)
- Method: SSformer segmentation + CycleGAN SegRefine; ResNet101 + MLP predicting clamped cubic B-spline parameters; Cobb from curve slopes blended with MLP regression
- Key results: AASCE SMAPE 9.53, MAE MT 3.73 / PT 4.13 / TL 4.81 deg; CJUH-JLU SMAPE 15.55
- Code / weights / license: none
- Useful for us: smooth parametric centreline is a clean way to compute curvature/Cobb and quantify deviation; robustness to low-quality images relevant for our "request better scan" trigger.
- Limitations / notes: data not public.
- BibTeX:
```bibtex
@misc{Wang2023BSpine,
  title   = {{B-Spine}: Learning {B-Spline} Curve Representation for Robust and Interpretable Spinal Curvature Estimation},
  author  = {Wang, Hao and Song, Qiang and Yin, Ruofeng and Ma, Rui and Yu, Yizhou and Chang, Yi},
  year    = {2023},
  eprint  = {2310.09603},
  archivePrefix = {arXiv}
}
```

### R131. CurvNet and the Spinal-AI2024 dataset
- Full title: CurvNet: Latent Contour Representation and Iterative Data Engine for Curvature Angle Estimation
- Authors: Shao Z, Yuan Y, Ma L, Zhu X
- Year / Venue / Type: 2024 / arXiv 2411.12604 (venue unverified) / preprint + dataset
- DOI / arXiv / URL: arXiv:2411.12604 ; code https://github.com/Ernestchenchen/CurvNet ; data https://github.com/Ernestchenchen/Spinal-AI2024
- Access: preprint
- Passes: 3/3 full text
- Modality & anatomy: AP radiographs
- Data: AASCE2019 (609), private Spinal2023 (904), new synthetic Spinal-AI2024 (20,000 generated images via Stable Diffusion 1.5 + pseudo-labels)
- Method: SVD "eigen-spine" latent contour (14 landmarks per segment), ResNet50-FPN detector regressing latent coefficients; iterative data engine
- Key results: SMAPE AASCE 5.05%, Spinal2023 7.13%, Spinal-AI2024 5.34%; PT angle weaker (12.48% SMAPE on AASCE)
- Code / weights / license: code and data on GitHub (licence unverified)
- Useful for us: low-rank shape prior for spine contours is a neat way to express "deviation from typical spine shape"; synthetic data source.
- Limitations / notes: synthetic dataset labelled by authors' own detector (circularity); cervical vertebrae confused as thoracic.
- BibTeX:
```bibtex
@misc{Shao2024CurvNet,
  title   = {{CurvNet}: Latent Contour Representation and Iterative Data Engine for Curvature Angle Estimation},
  author  = {Shao, Zhiwen and Yuan, Yichen and Ma, Lizhuang and Zhu, Xiaojia},
  year    = {2024},
  eprint  = {2411.12604},
  archivePrefix = {arXiv}
}
```

### R132. Cobb angle (seminal definition)
- Full title: Outline for the study of scoliosis (title confirmed via the Wikipedia "Cobb angle" reference list, 2026-10-16)
- Authors: Cobb JR
- Year / Venue / Type: 1948 / The American Academy of Orthopedic Surgeons Instructional Course Lectures, Vol. 5, Ann Arbor MI: Edwards (confirmed via Wikipedia reference). Pages 261-275 are still unverified; the reference gives none. / book chapter (seminal)
- DOI / arXiv / URL: none (pre-DOI)
- Access: not accessible
- Passes: 0/3 content (original not accessible; bibliographic details confirmed via secondary sources: Radiopaedia earlier, Wikipedia reference list 2026-10-16). The 10 deg threshold is confirmed as common usage (Wikipedia severity table: <10 deg "not scoliosis", 10-30 mild). Wikipedia notes supine Cobb angles are ~7-10 deg lower than standing. The ~5 deg inter-observer error needs a primary measurement-error citation (not Cobb 1948).
- Modality & anatomy: radiographs, scoliosis
- Data: n/a
- Method: angle between endplate lines of the most tilted end vertebrae
- Key results: n/a
- Code / weights / license: n/a
- Useful for us: defines the Cobb angle; 10 deg diagnostic threshold and ~5 deg inter-observer error are the clinical tolerance our errors must be compared against.
- Limitations / notes: bibliographic details unverified.
- BibTeX:
```bibtex
@incollection{Cobb1948Scoliosis,
  title     = {Outline for the study of scoliosis},
  author    = {Cobb, John R.},
  booktitle = {Instructional Course Lectures, American Academy of Orthopaedic Surgeons},
  volume    = {5},
  publisher = {J. W. Edwards},
  address   = {Ann Arbor, MI},
  year      = {1948},
  note      = {Pages (commonly cited as 261--275) unverified in this review}
}
```

#### F. Sagittal balance, spinopelvic parameters, spondylolisthesis and X-ray landmark datasets

### R133. Fully automated radiological analysis of spinal disorders on biplanar (EOS) radiographs
- Full title: Fully automated radiological analysis of spinal disorders and deformities: a deep learning approach
- Authors: Galbusera F, Niemeyer F, Wilke HJ, et al.
- Year / Venue / Type: 2019 (online 2019-03-12) / European Spine Journal 28(5):951-960 (CONFIRMED via OpenAlex; PMID 30864061) / journal article
- DOI / arXiv / URL: 10.1007/s00586-019-05944-z
- Access: paywalled (abstract read on Springer)
- Passes: 1/3 abstract only; bibliographic metadata verified via OpenAlex 2026-10-16. Paywalled (OpenAlex: closed, no OA copy), so full text was skipped.
- Modality & anatomy: biplanar (EOS) radiographs, whole spine + pelvis
- Data: 493 spines (AIS, adult deformity, stenosis) with 78 landmarks from 3D reconstructions; 50-patient test
- Method: fully convolutional network with DSNT layer for landmark coordinates; parameters derived from landmarks
- Key results: T4-T12 kyphosis, L1-L5 lordosis, Cobb, PI, SS, PT all strongly correlated; standard errors 2.7 deg (PT) to 11.5 deg (L1-L5 lordosis)
- Code / weights / license: unverified
- Useful for us: the key EOS-AI reference; shows parameter-wise error budgets (lordosis worst) for our alignment module.
- Limitations / notes: accuracy limited for some parameters; single centre.
- BibTeX:
```bibtex
@article{Galbusera2019EOSDeepLearning,
  title   = {Fully automated radiological analysis of spinal disorders and deformities: a deep learning approach},
  author  = {Galbusera, Fabio and Niemeyer, Frank and Wilke, Hans-Joachim and Bassani, Tito and Casaroli, Gloria and Anania, Carla and Costa, Francesco and Brayda-Bruno, Marco and Sconfienza, Luca Maria},
  journal = {European Spine Journal},
  year    = {2019},
  volume  = {28},
  number  = {5},
  pages   = {951--960},
  doi     = {10.1007/s00586-019-05944-z}
}
```

### R134. Landmark detection and 18 alignment parameters on whole-spine lateral radiographs
- Full title: Deep learning approach for automatic landmark detection and alignment analysis in whole-spine lateral radiographs
- Authors: Yeh YC, Weng CH, Huang YJ, et al.
- Year / Venue / Type: 2021 / Scientific Reports 11:7618 / journal article
- DOI / arXiv / URL: 10.1038/s41598-021-87141-x
- Access: open
- Passes: 3/3 full text
- Modality & anatomy: whole-spine lateral radiographs (cervical to femoral heads)
- Data: 2,210 images (scoliosis 1,041, kyphosis 466, implants 703) from Chang Gung Memorial Hospital; 400 test, 90 inter-observer, 1,690 5-fold CV, 120 paediatric training-only
- Method: two-stage coarse-to-fine Cascaded Pyramid Network with DSNT coordinate regression, heatmap regularisation, Wing loss; 45 landmarks; 864x480 input; ensemble of 2
- Key results: 18 parameters (PI, SS, PT, LL, SVA, CL, T1S, cSVA, GTK, PTK, MTK, L4-S1 lordosis, LPA, SSA, GT, TPA, Barrey index, OD-HA); mean errors 0.1 deg (OD-HA) to 6.7 deg (PTK); physician-level reliability for 15/18; femoral head centre errors 2.75/3.39 mm; ~1 s per image
- Code / weights / license: none; data on request
- Useful for us: the most complete list of sagittal parameter definitions with automated errors; target parameter set for our X-ray alignment report.
- Limitations / notes: single centre; excluded abnormal vertebral counts (LSTV) - our system must handle these (see FA08); thoracic level misidentification.
- BibTeX:
```bibtex
@article{Yeh2021WholeSpineLandmarks,
  title   = {Deep learning approach for automatic landmark detection and alignment analysis in whole-spine lateral radiographs},
  author  = {Yeh, Yu-Cheng and Weng, Chi-Hung and Huang, Yu-Jui and Fu, Chen-Ju and Tsai, Tsung-Ting and Yeh, Chao-Yuan and others},
  journal = {Scientific Reports},
  volume  = {11},
  pages   = {7618},
  year    = {2021},
  doi     = {10.1038/s41598-021-87141-x}
}
```

### R135. Pelvic incidence (seminal definition)
- Full title: Pelvic incidence: a fundamental pelvic parameter for three-dimensional regulation of spinal sagittal curves
- Authors: Jean Legaye, G. Duval-Beaupère, J. Hecquet, C. Marty. Note: OpenAlex lists the order as Legaye, Duval-Beaupère, Marty, Hecquet. The conventional citation order (Hecquet before Marty) is kept, but check it against the PDF.
- Year / Venue / Type: 1998 / European Spine Journal 7(2):99-103 / journal article (seminal)
- DOI / arXiv / URL: 10.1007/s005860050038 (CONFIRMED via OpenAlex 2026-10-16; published 1998-05-05) ; PMID 9629932 ; PMC3611230
- Access: green OA copy in PMC (blocked by reCAPTCHA in this session); Springer page not fetchable
- Passes: 0/3 content (bibliographic metadata, volume 7(2):99-103, verified via OpenAlex 2026-10-16; no abstract available there)
- Modality & anatomy: lateral radiographs of spine and pelvis
- Data: unverified
- Method: defines PI = angle between the perpendicular to the sacral plate at its midpoint and the line to the femoral head axis; PI = PT + SS
- Key results: unverified
- Code / weights / license: n/a
- Useful for us: definition of PI, PT, SS used by every spinopelvic AI model (AL13, AL14).
- Limitations / notes: verify bibliographic details before citing.
- BibTeX:
```bibtex
@article{Legaye1998PelvicIncidence,
  title   = {Pelvic incidence: a fundamental pelvic parameter for three-dimensional regulation of spinal sagittal curves},
  author  = {Legaye, J. and Duval-Beaup{\`e}re, G. and Hecquet, J. and Marty, C.},
  journal = {European Spine Journal},
  volume  = {7},
  number  = {2},
  pages   = {99--103},
  year    = {1998},
  doi     = {10.1007/s005860050038}
}
```
- Also relevant to: Uncertainty, image quality, abstention and normative anatomy

### R136. Roussouly classification of normal sagittal alignment
- Full title: Classification of the normal variation in the sagittal alignment of the human lumbar spine and pelvis in the standing position
- Authors: Pierre Roussouly, Sohrab Gollogly, Éric Berthonnaud, Johanes Dimnet
- Year / Venue / Type: 2005 (2005-01-28 per OpenAlex; Feb 1 issue) / Spine 30(3):346-353 (CONFIRMED via OpenAlex 2026-10-16) / journal article (seminal)
- DOI / arXiv / URL: 10.1097/01.brs.0000152379.54463.65 (CONFIRMED via OpenAlex) ; PMID 15682018
- Access: not read
- Passes: 1/3 (OpenAlex metadata + structured abstract reconstructed from its inverted index, 2026-10-16). Full text not read.
- Modality & anatomy: standing lateral radiographs, lumbar spine and pelvis
- Data: prospective; 160 asymptomatic volunteers; standardised standing AP + lateral radiographs measured with custom software (confirmed from abstract)
- Method: four types by sacral slope and lordosis shape (type 1-2 SS < 35 deg, type 3 SS 35-45 deg, type 4 SS > 45 deg) - thresholds from common usage, verify
- Key results: reciprocal relations among sacral slope, PI and lumbar lordosis. Sacral slope determines global lordosis, pelvic tilt, lordosis apex and the number of lordotic vertebrae, giving a four-type classification (abstract). The SS thresholds per type are not in the abstract and remain unverified.
- Code / weights / license: n/a
- Useful for us: normative "shape type" framework - allows reporting deviation relative to a patient's own PI-predicted type rather than a single population mean.
- Limitations / notes: verify before citing.
- BibTeX:
```bibtex
@article{Roussouly2005SagittalClassification,
  title   = {Classification of the normal variation in the sagittal alignment of the human lumbar spine and pelvis in the standing position},
  author  = {Roussouly, Pierre and Gollogly, Sohrab and Berthonnaud, Eric and Dimnet, Johan},
  journal = {Spine},
  volume  = {30},
  number  = {3},
  pages   = {346--353},
  year    = {2005},
  doi     = {10.1097/01.brs.0000152379.54463.65}
}
```
- Also relevant to: Uncertainty, image quality, abstention and normative anatomy

### R137. SRS-Schwab adult spinal deformity classification
- Full title: Scoliosis Research Society-Schwab adult spinal deformity classification: a validation study (OpenAlex lists the main title only)
- Authors: Frank Schwab, Benjamin Ungar, Benjamin Blondel, Jacob M. Buchowski, Jeffrey D. Coe, Donald Deinlein, Christopher J. DeWald, Hossein Mehdian, Christopher I. Shaffrey, Clifford B. Tribus, Virginie Lafage
- Year / Venue / Type: 2012 (issue; online 2011-11-01) / Spine 37(12):1077-1082 (CONFIRMED via OpenAlex 2026-10-16) / journal article
- DOI / arXiv / URL: 10.1097/BRS.0b013e31823e15e2 (CONFIRMED via OpenAlex) ; PMID 22045006
- Access: not read
- Passes: 1/3 (OpenAlex metadata + structured abstract, 2026-10-16). Full text not read.
- Modality & anatomy: full-length standing radiographs, adult spinal deformity
- Data: 9 readers graded 21 pre-marked cases twice, ~1 week apart. Modifier cut-offs were derived from a multicentre adult deformity database (size not in the abstract).
- Method: curve type (T, L, D, N) plus three sagittal modifiers: PI-LL mismatch (0: <10 deg, +: 10-20 deg, ++: >20 deg), PT (0: <20 deg, +: 20-30 deg, ++: >30 deg), SVA (0: <4 cm, +: 4-9.5 cm, ++: >9.5 cm) - thresholds from common usage, verify
- Key results (abstract): inter-rater Fleiss kappa: curve type 0.80/0.87, PI-LL 0.75/0.86, PT 0.97/0.98, SVA 0.96/0.96 (two readings). Intra-rater mean kappa: curve type 0.94, PI-LL 0.88, PT 0.97, SVA 0.97. The modifier thresholds listed under Method are not in the abstract and remain unverified.
- Code / weights / license: n/a
- Useful for us: ready-made thresholds to turn measured PI-LL, PT and SVA into a graded deviation-from-normal statement.
- Limitations / notes: verify before citing.
- BibTeX:
```bibtex
@article{Schwab2012SRSSchwab,
  title   = {Scoliosis Research Society--Schwab adult spinal deformity classification: a validation study},
  author  = {Schwab, Frank and Ungar, Benjamin and Blondel, Benjamin and others},
  journal = {Spine},
  volume  = {37},
  number  = {12},
  pages   = {1077--1082},
  year    = {2012},
  doi     = {10.1097/BRS.0b013e31823e15e2}
}
```

### R138. Meyerding grading of spondylolisthesis
- Full title: Spondylolisthesis (title from prior knowledge; unverified)
- Authors: Meyerding HW
- Year / Venue / Type: 1932 / Surgery, Gynecology & Obstetrics 54:371-377 (unverified) / journal article (seminal)
- DOI / arXiv / URL: none (pre-DOI)
- Access: not accessible
- Passes: 0/3 content (original not accessible). Grade thresholds re-confirmed via Radiopaedia "Meyerding classification" (2026-10-16): I 0-25%, II 26-50%, III 51-75%, IV 76-100%, V >100%; slip measured between posterior cortices / inferior body length; I-II low-grade, III-V high-grade. Journal, volume and pages still unverified (Radiopaedia reference list not rendered). Cite AL20 (CORR 2020) as the verifiable modern source.
- Modality & anatomy: lateral lumbar radiographs
- Data: n/a
- Method: slip grade by percentage of anterior translation of the upper vertebra over the lower endplate: I 0-25%, II 25-50%, III 50-75%, IV 75-100%, V >100% (spondyloptosis)
- Key results: n/a
- Code / weights / license: n/a
- Useful for us: grading rule to apply on top of landmark-derived slip percentage (BUU-LSPINE labels use classes 0-4).
- Limitations / notes: bibliographic details unverified.
- BibTeX:
```bibtex
@article{Meyerding1932Spondylolisthesis,
  title   = {Spondylolisthesis},
  author  = {Meyerding, Henry W.},
  journal = {Surgery, Gynecology \& Obstetrics},
  year    = {1932},
  note    = {Volume and pages unverified in this review}
}
```

### R139. Classification in Brief: the Meyerding classification of spondylolisthesis
- Full title: Classification in Brief: The Meyerding Classification System of Spondylolisthesis
- Authors: Ezekial J. Koslosky, David Gendelberg
- Year / Venue / Type: 2020 / Clinical Orthopaedics and Related Research 478(5):1125-1130 / review
- DOI / arXiv / URL: 10.1097/CORR.0000000000001153 (PMC7170696, PMID 32282463) - confirmed via OpenAlex
- Access: open (PMC); not read directly (PMC blocked)
- Passes: 0/3 content; bibliographic metadata CONFIRMED via OpenAlex 2026-10-16 (Ezekial J. Koslosky, David Gendelberg; CORR 478(5):1125-1130, online 2020-04-10; PMID 32282463). The open copy is PMC only, which is blocked by reCAPTCHA, so content was not read.
- Modality & anatomy: lateral lumbar radiographs
- Data: n/a (review)
- Method: Meyerding grades: I 0-25%, II 25-50%, III 50-75%, IV 75-100%, V >100% of vertebral body width
- Key results: n/a
- Code / weights / license: n/a
- Useful for us: verifiable modern citation for Meyerding thresholds (use alongside AL19).
- Limitations / notes: abstract not read.
- BibTeX:
```bibtex
@article{Koslosky2020Meyerding,
  title   = {Classification in Brief: The {Meyerding} Classification System of Spondylolisthesis},
  author  = {Koslosky, Ezekial and Gendelberg, David},
  journal = {Clinical Orthopaedics and Related Research},
  volume  = {478},
  number  = {5},
  pages   = {1125--1130},
  year    = {2020},
  doi     = {10.1097/CORR.0000000000001153}
}
```

---

## 04. Foundation models, architectures and vision-language

#### A. Spine-specific vision-language models, report generation and VQA (2024-2026)

### R140. Beyond Fluency: spine MRI report generation benchmark
- Full title: Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine MRI Report Generation
- Authors: Bruno Palau, Franziska Vogt, Daria Laslo, Haobo Li, Ender Konukoglu, Maria Monzon, Catherine R. Jutzeler (ETH Zurich / SIB)
- Year / Venue / Type: 2026 (v1 2026-08-07) / arXiv preprint (footnote "(c)2026 IEEE"; no venue named anywhere on the page, so the final venue is still unverified)
- DOI / arXiv / URL: arXiv:2608.07117 — https://arxiv.org/abs/2608.07117
- Access: preprint (open)
- Passes: 3/3 (pass 1-2 earlier from HTML; pass 3 on 2026-10-16 re-read arXiv abs for authors and HTML for assets, heatmap training and metric definitions. The rendered HTML truncates at Sec. 4.3, so the Conclusion and Sec. 4.4 were not visible)
- Modality & anatomy: lumbar spine MRI (sagittal/axial T1w, T2w)
- Data: LSMRI (515 patients, expert free-text reports; Mendeley "lumbar spine MRI" set), SPIDER (218 patients, template-synthesised reports from IVD gradings), LumbarDISC (1,976 patients, 5 stenosis-related conditions x 5 IVD levels; = RSNA 2024 lumbar set, unverified)
- Method: zero-shot benchmark of VLMs (BiomedGPT base/large, ChatGPT-5.0, MAIRA-2, MedGemma 4B/27B, VILA-M3 3B/8B/13B); QLoRA fine-tune of MedGemma-4B (~20.4M trainable params, 4-bit NF4); semi-supervised U-Net++ disc-level anomaly heatmaps (landmarks from SpineNetV2) alpha-blended into the VLM input as a visual "grounding" channel.
- Key results: zero-shot LSMRI T1w BERTScore 91.14 (ChatGPT-5.0) vs 91.59 (MedGemma-27B), BLEU-4 ~0.5-1.1; IVD-level balanced accuracy only 50-57% (high specificity, low sensitivity); heatmap Dice 82.3 +/- 2.0; with overlay MedGemma-27B L1-L2 sensitivity 2.1 -> 22.6 but specificity 100 -> 88.8; paraphrase perturbation drops BERTScore 6.6%, BLEU 14.2% -> lexical metrics do not measure clinical correctness.
- Code / weights / license: code at gitlab.ethz.ch/BMDSlab/publications/low-back/spine-mri-report-generation (licence not stated); no weights.
- Useful for us: strongest evidence that off-the-shelf medical VLMs are near-chance at per-level spine findings -> justifies our "measure first (segmentation/landmarks), then verbalise" design; provides clinical-efficacy evaluation protocol and perturbation test for report metrics.
- Limitations / notes: single central sagittal slice in main experiments; fine-tuned model hallucinated non-existent levels (L6-L7); small data.
- Reusable assets / definitions (pass 3): Clinical-efficacy metrics are per-finding x per-IVD-level (T12-L1..L5-S1) sensitivity, specificity, balanced accuracy, F1 and accuracy against binary presence labels derived from gradings. Models are prompted to list only affected levels in a constrained format. Report text is delimited by [[REPORT_START]]/[[REPORT_END]] tokens. Heatmap model: U-Net++ with 6 output channels (one per IVD level) from 3 central sagittal slices. Loss: channel-balanced MSE plus an off-diagonal co-activation penalty. Targets come from SpineNetV2 landmarks + SPIDER gradings, blended over training from localisation to anomaly heatmaps. Pretraining used 85% LumbarDISC + 30% LSMRI (351 epochs); fine-tuning used SPIDER (501 epochs); AdamW lr 1e-3. The SPIDER report template is in Sup. 6.1 (not read).
- Open questions (pass 3): whether the heatmap model is tested on held-out SPIDER (SPIDER is used for both training and evaluation); templated SPIDER references limit free-text metric validity; heatmap-to-finding extraction accuracy not reported; no data-availability or licence statements for the three datasets in the text.
- BibTeX:
```bibtex
@misc{Palau2026BeyondFluency,
  title         = {Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine {MRI} Report Generation},
  author        = {Palau, Bruno and Vogt, Franziska and Laslo, Daria and Li, Haobo and Konukoglu, Ender and Monzon, Maria and Jutzeler, Catherine R.},
  year          = {2026},
  eprint        = {2608.07117},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV}
}
```

### R141. GateSPINE
- Full title: GateSPINE: Gated Cross-View Fusion for Lumbar Spine MRI Report Generation
- Authors: Hoang Nguyen Van, Cuong Vuong Tuan, Trang Mai Xuan, Bien Tran Van, Nam Tran Van, Thien Van Luong (Phenikaa University and Hospital; National Economics University, Vietnam)
- Year / Venue / Type: 2026 (submitted 2026-09-30) / arXiv preprint
- DOI / arXiv / URL: arXiv:2609.40091 — https://arxiv.org/abs/2609.40091
- Access: preprint (open)
- Passes: 3/3 (abstract earlier; full arXiv HTML read 2026-10-16 for data/method/results, then limitations/availability)
- Modality & anatomy: multi-sequence lumbar MRI (sagittal T1/T2 + axial T2)
- Data: PhenikaaMec (private): 236 patients after exclusions (of 250); sagittal T1, sagittal T2, axial T2; Vietnamese reports translated by LLaMA-3.3-70B; split by month 118/58/60. Lumbar (public Mendeley LSMRI): 515 with reports, split 70/15/15. SPIDER: sagittal T1/T2 only, references are GPT-4 template reports from SPINE (FM-10), split 60/20/20.
- Method: training-free test-time dynamic fusion of sagittal T1+T2 (built on CDDFuse). Two M3D-initialised ViT3D encoders (fused sagittal; axial) on 32x256x256 volumes. Per-channel, per-token sigmoid gate mixes views: g*sag + (1-g)*ax. Pooling to 256 tokens, adapter into MedGemma-4B-IT with LoRA (r=8). Two stages (frozen LLM, then LoRA). Single Quadro RTX 8000.
- Key results: clinical-efficacy micro-F1: PhenikaaMec 71.12 vs 67.49 (SPINE); SPIDER 85.88 vs 82.26 (Dia-LLaMA); Lumbar 69.41 vs 42.51 (SPINE). Recall up to +38 points. BERTScore +0.3 to +1.3. Best ROUGE everywhere; Dia-LLaMA leads BLEU-4/METEOR on PhenikaaMec. Ablations: all three sequences best; gating beats concatenation/dynamic fusion; MedGemma beats Phi-3-mini.
- Code / weights / license: no release or licence stated.
- Useful for us: design pattern for fusing sagittal and axial series in a 3D report generator; clinical-efficacy F1 as the primary report metric; shows a MedGemma-4B decoder trains on one 48 GB GPU.
- Limitations / notes (authors): global representations miss subtle lesions and localisation; errors concentrate in vertebral level and severity; LLM judge and translations not validated by radiologists; SPIDER lacks axial (cross-view gating validated on two cohorts) and its templated references inflate scores; every model scores 0 on osteophytes and disc-height loss (Lumbar); bulge vs herniation confusion.
- BibTeX:
```bibtex
@misc{NguyenVan2026GateSPINE,
  title         = {{GateSPINE}: Gated Cross-View Fusion for Lumbar Spine {MRI} Report Generation},
  author        = {Nguyen Van, Hoang and Vuong Tuan, Cuong and Mai Xuan, Trang and Tran Van, Bien and Tran Van, Nam and Luong, Thien Van},
  year          = {2026},
  eprint        = {2609.40091},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV}
}
```

### R142. SpineBench / SpineMed-450k / SpineGPT (ICLR 2026)
- Full title: SpineBench: A Clinically Salient, Level-Aware Benchmark Powered by the SpineMed-450k Corpus
- Authors: Ming Zhao, Wenhui Dong, Yang Zhang, et al. (26 authors; corresponding Tiansheng Sun, Caifeng Shan)
- Year / Venue / Type: 2026 / ICLR 2026 (conference); arXiv:2510.03160 (v3 Mar 2026)
- DOI / arXiv / URL: arXiv:2510.03160 — https://arxiv.org/abs/2510.03160 ; https://mlanthology.org/iclr/2026/zhao2026iclr-spinebench/
- Access: open
- Passes: 3/3 (pass 1-2 earlier: HTML + venue check; pass 3 on 2026-10-16: HTML re-read for availability, composition, scoring rubric, limitations)
- Modality & anatomy: whole spine; X-ray, CT, MRI + text
- Data: SpineMed-450k instruction corpus, 456,748 items (textbooks ~377k, literature, case reports, question banks, open datasets incl. VerSe and "Spark", ~1,000 de-identified cases from 11 hospitals); 14 spine subconditions; SpineBench test: 487 MCQs + 87 report prompts, validated by 17 orthopaedic surgeons.
- Method: SpineGPT = Qwen2.5-VL-7B-Instruct fine-tuned with a 3-stage curriculum (ms-swift, DeepSpeed, 8x A100); report scored on 5 sections (imaging report, AI diagnosis, treatment, risk/prognosis, reasoning/disclaimer).
- Key results: SpineGPT average 87.44 (close-ended 87.89; report 87.24) vs Gemini-2.5-Pro 89.23, GLM-4.5V 83.26, Qwen2.5-VL-72B 79.88, Qwen2.5-VL-7B 64.74; LLM-judge vs expert Pearson r 0.382-0.949 across 10 dimensions.
- Code / weights / license: The authors promise to release the evaluation framework, training/inference/scoring code and SpineMed-450k annotations as JSON. Raw VerSe/Spark images are not redistributed (metadata pointers instead). The hospital subset is controlled access under a DUA. No GitHub/HF link, software licence or SpineGPT weight-release plan appears in the paper. Europe PMC text was filtered for TDM-permitting licences; textbooks are used under a "transformative use" claim. Base Qwen2.5-VL-7B is Apache-2.0.
- Benchmark composition (pass 3): 487 MCQs by subcondition: tumour/osteomyelitis 96, complications 62, dysplastic/congenital 49, idiopathic scoliosis 47, thoraco-lumbar degenerative 34, general 33, kyphosis/postlaminectomy 31, anatomic approaches 31, adult deformity 26, spondylolisthesis 23, trauma 23, neuromuscular 12, biomechanics 11, cervical degenerative 9. "Level-aware" is never operationally defined. Overall score = sample-weighted sum of text MCQ, multimodal MCQ and report scores. Report rubric: 5 sections x 10 dimensions scored 1-5.
- Inconsistencies found (pass 3): hospital test items 250 (Tab. 2) vs 163 (Tab. 11); some Tab. 6 sums do not match averages; the report-score formula is inconsistent with its stated 0-100 scale. Cite the headline numbers with care.
- Useful for us: the only large spine-specific instruction corpus and level-aware benchmark; template for structured spine report sections; candidate external evaluation for our report module.
- Limitations / notes: mostly text-derived (textbook OCR) data; small hospital share; LLM-generated QA; LLM-as-judge scoring. Authors' future work: >7B models, RL, direct comparison with proprietary models. Few spine trauma/fracture items (23), so it is weak for our fracture module.
- BibTeX:
```bibtex
@inproceedings{Zhao2026SpineBench,
  title     = {{SpineBench}: A Clinically Salient, Level-Aware Benchmark Powered by the {SpineMed-450k} Corpus},
  author    = {Zhao, Ming and Dong, Wenhui and Zhang, Yang and Zheng, Xiang and Zhang, Zhonghao and Zhou, Zi An and Guan, Yunzhi and Xu, Liukun and Peng, Wei and Gong, Zhaoyang and others},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2026},
  eprint    = {2510.03160},
  archivePrefix = {arXiv}
}
```

### R143. SpineBench (ACM MM 2025) — MLLM spinal pathology benchmark
- Full title: SpineBench: Benchmarking Multimodal LLMs for Spinal Pathology Analysis
- Authors: Chenghanyu Zhang, Zekun Li, Peipei Li, et al. (8 authors)
- Year / Venue / Type: 2025 / ACM International Conference on Multimedia (MM '25), Dublin / conference; arXiv:2510.12267
- DOI / arXiv / URL: arXiv:2510.12267 — https://arxiv.org/abs/2510.12267 ; project https://zhangchenghanyu.github.io/SpineBench.github.io/ ; data https://huggingface.co/datasets/Silversorrow/SpineBench
- Access: open
- Passes: 2/3 full text (HTML) + project page
- Modality & anatomy: spine X-ray and MRI (converted to 2D RGB); lumbar levels L1/L2-L5/S1
- Data: 40,263 images from BUU Spine, CSXA, RSNA 2024 Lumbar Spine Degenerative Classification, VinDr-SpineXR; 64,878 QA pairs (diagnosis 40,263; localisation 24,615); eval subset 2,128; 11 disease categories.
- Method: 5-choice MCQ diagnosis with SigLIP2-mined hard negatives + multi-label level localisation; zero-shot evaluation of 12 MLLMs.
- Key results: best overall Gemini-2.5-Pro 20.86% (diagnosis 32.37%, localisation 9.35%); GPT-4o 16.67%; LLaVA-Med v1.5 15.29%; MedGemma-4B 8.73% (below 20% chance on diagnosis).
- Code / weights / license: dataset on Hugging Face; licence not stated (inherits source dataset licences, e.g. RSNA competition terms).
- Useful for us: off-the-shelf MLLMs essentially fail at spine diagnosis/localisation -> strong motivation; a ready-made VQA test set for our system.
- Limitations / notes: 3D flattened to 2D; LLM-generated question phrasing; Table 1 counts inconsistent.
- BibTeX:
```bibtex
@inproceedings{Zhang2025SpineBenchMM,
  title     = {{SpineBench}: Benchmarking Multimodal {LLMs} for Spinal Pathology Analysis},
  author    = {Zhang, Chenghanyu and Li, Zekun and Li, Peipei and others},
  booktitle = {Proceedings of the 33rd ACM International Conference on Multimedia (MM '25)},
  year      = {2025},
  eprint    = {2510.12267},
  archivePrefix = {arXiv}
}
```

### R144. Auto-Rad: lumbar MRI report generation with GIT
- Full title: Auto-Rad: End-to-End Report Generation from Lumber Spine MRI Using Vision–Language Model
- Authors: Mohammed Yeasin, Kazi Ashraf Moinuddin, Felix Havugimana, et al. (5 authors)
- Year / Venue / Type: 2024 / Journal of Clinical Medicine 13(23):7092 / journal
- DOI / arXiv / URL: 10.3390/jcm13237092
- Access: open (MDPI)
- Passes: 2/3 full text
- Modality & anatomy: lumbar MRI, axial composite images
- Data: 515 patients from Mendeley lumbar spine MRI dataset (Sudirman et al.); 1,545 3-channel axial images; 80/20 split; 100 test samples for empirical review; radiologist notes rewritten by GPT-4.
- Method: fine-tuned microsoft/git-base (CLIP ViT-B/16 encoder + 6-layer text decoder), AdamW lr 5e-5, 100 epochs.
- Key results: METEOR 0.37, BERTScore 0.886, ROUGE-L 0.30; but diagnostic completeness only 24.7%, novel (hallucinated) diagnoses 69.8%.
- Code / weights / license: none released.
- Useful for us: negative baseline showing generic captioning VLMs hallucinate spine findings; cite as early lumbar VLM attempt.
- Limitations / notes: no clinician evaluation; axial only; ROUGE values inconsistent in paper.
- BibTeX:
```bibtex
@article{Yeasin2024AutoRad,
  title   = {Auto-Rad: End-to-End Report Generation from Lumber Spine {MRI} Using Vision--Language Model},
  author  = {Yeasin, Mohammed and Moinuddin, Kazi Ashraf and Havugimana, Felix and others},
  journal = {Journal of Clinical Medicine},
  volume  = {13},
  number  = {23},
  pages   = {7092},
  year    = {2024},
  doi     = {10.3390/jcm13237092}
}
```

### R145. Prospective DL-accelerated lumbar MRI + VLM automated reporting
- Full title: Prospective evaluation of artificial intelligence (AI) in lumbar spine magnetic resonance imaging (MRI) workflow: from deep learning (DL)-enhanced accelerated acquisition to simultaneous vision-language model (VLM)-based automated report generation
- Authors: Jiwoo Park, Kyunghwa Han, Ji Seon Oh, et al. (8 authors; Young Han Lee senior)
- Year / Venue / Type: 2026 / European Journal of Radiology 196:112695 / journal (prospective clinical study)
- DOI / arXiv / URL: 10.1016/j.ejrad.2026.112695
- Access: paywalled (abstract only)
- Passes: abstract only, paywalled (skipped in the 2026-10-16 deepening round: no OA copy)
- Modality & anatomy: lumbar MRI
- Data: 70 prospective patients x 2 protocols = 140 scans, two institutions; 4 blinded radiologists; 5 key pathologies.
- Method: DL-reconstructed accelerated protocol vs conventional; commercial VLM report software (vendor unverified) vs radiologist consensus.
- Key results: acquisition time reduced ~80-86% (<2 min) with interchangeable diagnosis; higher SNR/CNR; VLM reports showed substantial-to-almost-perfect agreement for key pathologies (kappa values unverified).
- Code / weights / license: commercial, not available.
- Useful for us: the first prospective evidence of VLM spine reporting in workflow; supports our "request better scan" logic (accelerated scans can be adequate).
- Limitations / notes: small n; commercial black box.
- BibTeX:
```bibtex
@article{Park2026ProspectiveLumbarVLM,
  title   = {Prospective evaluation of artificial intelligence ({AI}) in lumbar spine magnetic resonance imaging ({MRI}) workflow: from deep learning ({DL})-enhanced accelerated acquisition to simultaneous vision-language model ({VLM})-based automated report generation},
  author  = {Park, Jiwoo and Han, Kyunghwa and Oh, Ji Seon and others},
  journal = {European Journal of Radiology},
  volume  = {196},
  pages   = {112695},
  year    = {2026},
  doi     = {10.1016/j.ejrad.2026.112695}
}
```

### R146. AutoSpineAI
- Full title: AutoSpineAI: Lightweight Multimodal CAD Framework for Lumbar Spine MRI Assessments (repo title: "A 3D Vision-Language Framework for Automatic Lumbar Spine Diagnosis and Report Generation")
- Authors: Saied Salem, Afnan Habib, Mukhlis Raza, et al. (9 authors; Mugahed A. Al-antari senior)
- Year / Venue / Type: 2025 / IEEE-EMBS BHI 2025 / conference
- DOI / arXiv / URL: 10.1109/BHI67747.2025.11269503 ; https://github.com/AISSLab2025/AutoSpineAI
- Access: paywalled paper; README read
- Passes: 1/3 (GitHub README only). The IEEE BHI paper is paywalled with no OA copy found, so it was skipped in the 2026-10-16 deepening round.
- Modality & anatomy: 3D lumbar MRI
- Data: not stated in README.
- Method: 3D U-Net-family segmentation of discs/vertebrae/canal -> per-level geometric measurements -> retrieval of exemplar reports from knowledge store -> transformer decoder conditioned on measurement tokens; FastAPI service.
- Key results: not available (unverified).
- Code / weights / license: code on GitHub, licence not stated.
- Useful for us: architecture almost identical to our intended pipeline (segmentation -> measurements -> retrieval-augmented report) — cite as closest prior system.
- Limitations / notes: no numbers verified. A related ResearchGate item "SpineInsight-AI: Lightweight Multimodal CAD System for 3D Lumbar Spine MRI diagnosis and Structural Report Generation" appears to be the same group (unverified).
- BibTeX:
```bibtex
@inproceedings{Salem2025AutoSpineAI,
  title     = {{AutoSpineAI}: Lightweight Multimodal {CAD} Framework for Lumbar Spine {MRI} Assessments},
  author    = {Salem, Saied and Habib, Afnan and Raza, Mukhlis and others},
  booktitle = {IEEE-EMBS International Conference on Biomedical and Health Informatics (BHI)},
  year      = {2025},
  doi       = {10.1109/BHI67747.2025.11269503}
}
```

### R147. SpineAutoCAD (agentic RAG lumbar report generation)
- Full title: SpineAutoCAD: Multimodal CAD System for Lumbar Spine MRI Analysis and Structured Report Generation
- Authors: S. Salem, A. Habib, M. Raza, et al. (6 authors; M. A. Al-Antari senior)
- Year / Venue / Type: 2025 / 9th International Artificial Intelligence and Data Processing Symposium (IDAP 2025), Malatya / conference
- DOI / arXiv / URL: 10.1109/idap68205.2025.11222171
- Access: paywalled (abstract only, via institutional repository page)
- Passes: abstract only, paywalled (skipped in the 2026-10-16 deepening round: no OA copy)
- Modality & anatomy: 3D lumbar MRI (DICOM), sagittal + axial
- Data: unverified (likely Mendeley lumbar MRI / SPIDER)
- Method: mid-sagittal slice extraction -> SegResNet segmentation of vertebrae/IVDs -> 3D cross-projection to find matching axial slices -> anatomical measurements (stenosis grading, alignment) -> LLM report via agentic retrieval-augmented generation (semantic retrieval + knowledge-graph reasoning).
- Key results: Dice 97.79% sagittal, 93.52% axial; report BERT-F1 83.58%.
- Code / weights / license: see AutoSpineAI repo (FM-07); licence not stated.
- Useful for us: concrete measurement-to-report pipeline with sagittal->axial slice linking; same group as FM-07.
- Limitations / notes: no clinical-efficacy metric; small venue.
- BibTeX:
```bibtex
@inproceedings{Salem2025SpineAutoCAD,
  title     = {{SpineAutoCAD}: Multimodal {CAD} System for Lumbar Spine {MRI} Analysis and Structured Report Generation},
  author    = {Salem, S. and Habib, A. and Raza, M. and Aydin, A. A. and Gu, Y. H. and Al-Antari, M. A.},
  booktitle = {9th International Artificial Intelligence and Data Processing Symposium (IDAP)},
  year      = {2025},
  doi       = {10.1109/idap68205.2025.11222171}
}
```

### R148. SpineAgent: multi-agent spine MRI report generation on a DINOv3-based foundation model
- Full title: A multi-agent system for spine MRI report generation from multi-sequence imaging
- Authors: Zhiping Xiao, Junwei Yang, Gongbo Sun, Han Zhang, Hanwen Xu, Yi Yao, Zachary D. Miller, William E. King III, Mohammed M. Kanani, Jalal B. Andre, Sammy Chu, Ming Zhang, Paul E. Kinahan, Nathan M. Cross, Sheng Wang (Univ. Washington, Peking Univ., UW-Madison, NYU)
- Year / Venue / Type: 2026 / arXiv preprint (8 Jun 2026); also Research Square preprint (DOI 10.21203/rs.3.rs-9889807/v1, under review)
- DOI / arXiv / URL: arXiv:2606.08897 — https://arxiv.org/abs/2606.08897
- Access: preprint (arXiv page licence CC BY-NC-SA 4.0)
- Passes: 3/3 (arXiv + Research Square abstracts earlier; full arXiv HTML read twice on 2026-10-16: pass 2 methods/data/results, pass 3 tail for availability/limitations)
- Modality & anatomy: multi-sequence spine MRI (T1w; T2w incl. STIR/Dixon; other sequences = 28.2% of series)
- Data: pretraining at UW Medical Center: 32,047 patients, 50,705 exams, 453,683 series, 13,441,191 slices (4.50M T1w + 4.52M T2w pretraining slices). Diagnosis set: 1,350 patients x 17 conditions, labels extracted from reports by Llama-3.3-70B + Phi-4-14B (subset radiologist-checked). Patient-level 10-fold CV. External: RSNA LumbarDISC (2,697 patients, 8,593 series, 8 institutions, 6 countries).
- Method: separate T1 and T2 ViT encoders pretrained with DINOv3 (4 register tokens; 150 epochs, then 30 epochs with Gram anchoring; 4x A100-80GB; ViT size not stated in the HTML). CLIP-style text alignment with BiomedBERT. A "synthesizer" router fuses T1/T2 encoder layers with learned weights to embed other sequences via continual training. 37 agents: 17 diagnostic, 17 segmentation/slice-localisation, 2 retrieval, and 1 LLaVA-style Medical Report Agent (LLaMA-3.1-8B decoder) that consumes the agents' structured outputs.
- Key results: across 17 conditions, mean +10.8% AUROC / +13.4% AUPRC over the best baseline (DINOv3, ResNet50, BrainMVP, BME-X, BiomedGPT). T1/T2: +8.79% AUROC. Other sequences: +11.1%. Best across 5 manufacturer groups and on RSNA (3 conditions). Retrieval Recall@5 +56.38% over second best. 5 radiologists (resident, fellow, 3 attendings) gave RADPEER scores; only qualitative results reported (fewer false-positive/omitted findings than LLaVA on 15 conditions). No numeric NLG metrics in the main text.
- Code / weights / license: no code, weight or data-release statement found in the HTML. UW data not released.
- Useful for us: the largest spine-MRI foundation model to date and the best architectural template: sequence-specific SSL encoders + task agents + structured tokens to report. Strong evidence that DINOv3-style SSL scales for spine MRI. Uses RSNA LumbarDISC as an external test, so we can compare on the same set.
- Limitations / notes (authors): assistive only; MRI only (no CT/EHR); single exam, no longitudinal modelling; out-of-scope conditions not handled; weak template adherence and severity characterisation. Our notes: report-derived LLM labels; single health system; no public weights.
- BibTeX:
```bibtex
@misc{Xiao2026SpineAgent,
  title         = {A multi-agent system for spine {MRI} report generation from multi-sequence imaging},
  author        = {Xiao, Zhiping and Yang, Junwei and Sun, Gongbo and Zhang, Han and Xu, Hanwen and Yao, Yi and Miller, Zachary D. and King, III, William E. and Kanani, Mohammed M. and Andre, Jalal B. and Chu, Sammy and Zhang, Ming and Kinahan, Paul E. and Cross, Nathan M. and Wang, Sheng},
  year          = {2026},
  eprint        = {2606.08897},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV}
}
```

### R149. SPINE: segmentation-guided 3D VLM for spinal MRI reports (M3D-LaMed fine-tune)
- Full title: SPINE: Segmentation-guided Processing and Integration of Multimodal Spinal MRI for Natural-Language Enhanced Report Generation (conference version title: "3D Vision–Language Models with Segmentation-Guided Multimodal Data for Spinal MRI Report Generation", Springer LNCS chapter DOI 10.1007/978-3-032-07502-4_14)
- Authors: Hoda Helmy, Abdullah Hosseini, Ahmed Ibrahim, Asfand Baig Mirza, Ahmed-Ramadan Sadek, Ahmed Serag (corresponding) (CONFIRMED via OpenAlex)
- Year / Venue / Type: 2026 (online 2026-02-11) / Applied Artificial Intelligence 40(1) (Taylor & Francis; article number not listed) / journal; earlier Springer LNCS chapter (not found in OpenAlex; unverified)
- DOI / arXiv / URL: journal 10.1080/08839514.2026.2626117 (CONFIRMED via OpenAlex) ; chapter 10.1007/978-3-032-07502-4_14 ; weights https://huggingface.co/serag-ai/Best-Fold-SPINE-Axial
- Access: journal open access (gold, CC BY); chapter paywalled
- Passes: 1/3 (model card; OpenAlex record with abstract, 2026-10-16). The journal is gold OA (CC BY), but the tandfonline page could not be fetched by the tool, so full text is still unread.
- Modality & anatomy: lumbar MRI, T1w + T2w + segmentation masks, axial and sagittal
- Data: axial dataset 515 patients and sagittal dataset 190 patients (abstract-confirmed; identity as Mendeley LSMRI / SPIDER per GateSPINE FM-02, which says SPINE produced GPT-4-generated SPIDER reports from gradings)
- Method: fine-tune of M3D-LaMed-Llama-2-7B (3D VLM, see FM-38) with segmentation masks as extra input channels.
- Key results (abstract, no numbers): segmentation maps improved accuracy, coherence and clinical relevance; T1+T2+Seg was most balanced; training on LLM-standardised reports beat human-written reports; GPT-4o standardisation was more fluent and detailed than Grok-3. Numeric results unverified. GateSPINE (FM-02) reports SPINE CE micro-F1 67.49 (PhenikaaMec) and 42.51 (Lumbar) as baselines.
- Code / weights / license: weights on HF, licence not stated (base Llama-2 licence applies).
- Useful for us: demonstrates mask-conditioned 3D VLM for spine; direct baseline.
- Limitations / notes: metrics still unverified (full text not read); LLM-standardised references may inflate scores relative to real reports.
- BibTeX:
```bibtex
@article{Helmy2026SPINE,
  title   = {{SPINE}: Segmentation-guided Processing and Integration of Multimodal Spinal {MRI} for Natural-Language Enhanced Report Generation},
  author  = {Helmy, Hoda and Hosseini, Abdullah and Ibrahim, Ahmed and Mirza, Asfand Baig and Sadek, Ahmed-Ramadan and Serag, Ahmed},
  journal = {Applied Artificial Intelligence},
  volume  = {40},
  number  = {1},
  year    = {2026},
  doi     = {10.1080/08839514.2026.2626117}
}
@incollection{SPINE2025SegGuidedVLM,
  title     = {{3D} Vision--Language Models with Segmentation-Guided Multimodal Data for Spinal {MRI} Report Generation},
  author    = {{authors unverified}},
  publisher = {Springer},
  year      = {2025},
  doi       = {10.1007/978-3-032-07502-4_14}
}
```

### R150. PID-Tversky explainable VLM for lumbar spinal stenosis
- Full title: An Explainable Vision-Language Model Framework with Adaptive PID-Tversky Loss for Lumbar Spinal Stenosis Diagnosis
- Authors: Md. Sajeebul Islam Sk., Md. Mehedi Hasan Shawon, Md. Golam Rabiul Alam
- Year / Venue / Type: 2026 / arXiv preprint (venue unverified)
- DOI / arXiv / URL: arXiv:2604.02502
- Access: preprint
- Passes: 2/3 full text (PDF)
- Modality & anatomy: lumbar MRI (axial), stenosis
- Data: Mendeley LSS MRI dataset (Sudirman et al. 2019), 515 patients / 48,345 images; pseudo-masks from Otsu/Canny/morphology guided by report text.
- Method: LLaVA-Med / BiomedCLIP / SmolVLM backbones + text-query spatial patch cross-attention -> CNN mask decoder + report module; QLoRA; Tversky loss whose beta is adapted per epoch by a PID controller on FN-FP error.
- Key results: 3-grade classification acc 90.69% (LLaVA-Med); Dice 0.9624; report BLEU-4 86.10 (implausibly high -> template-like reports).
- Code / weights / license: none.
- Useful for us: PID-adapted Tversky loss is a cheap trick for FN/FP balance; otherwise weak evidence (pseudo-labels).
- Limitations / notes: no expert masks; metric inconsistencies; no external validation.
- BibTeX:
```bibtex
@misc{IslamSk2026PIDTversky,
  title         = {An Explainable Vision-Language Model Framework with Adaptive {PID}-{Tversky} Loss for Lumbar Spinal Stenosis Diagnosis},
  author        = {Islam Sk., Md. Sajeebul and Shawon, Md. Mehedi Hasan and Alam, Md. Golam Rabiul},
  year          = {2026},
  eprint        = {2604.02502},
  archivePrefix = {arXiv}
}
```

### R151. ChexFract: fracture-description generation on chest X-ray
- Full title: ChexFract: From General to Specialized -- Enhancing Fracture Description Generation
- Authors: Nikolay Nechaev, Evgeniia Przhezdzetskaia, Dmitry Umerenkov, Dmitry V. Dylov (AIRI; Skoltech)
- Year / Venue / Type: 2025 / arXiv preprint (11 Nov 2025)
- DOI / arXiv / URL: arXiv:2511.07983
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv HTML read 2026-10-16 for data/method/results, then availability/limitations)
- Modality & anatomy: chest radiographs; fracture templates for ribs, clavicle, spine, shoulder, sternum, sternal wires, scapula (spine share not reported)
- Data: 18,710 CXR / fracture-description pairs mined by GPT-4o from PadChest, BIMCV-COVID19, CheXpert, OpenI and MIMIC-CXR training splits, rewritten into location templates. Test: MIMIC-CXR test reports (2,921) relabelled by GPT-4o (154 fracture cases vs 77 by the CheXpert labeller; disagreements manually checked). Parser validated on 500 manual reports: 94.2% binary, 89.7% attributes.
- Method: Phi-3.5-Vision-Instruct LLM (3.8B) with Rad-DINO (MAIRA-2) or CheXagent encoder + 2-layer GELU projector. AdamW, 15 epochs, 4x A100-80GB. Variants: original vs templated text, frozen/unfrozen/fine-tuned encoders. 5-seed OR-ensemble.
- Key results (ROC-AUC / F1 / recall): best MAIRA-2-based model 0.713 / 0.629 / 0.584 vs MAIRA-2 baseline 0.518 / 0.085 / 0.045. Best CheXagent-based 0.697 / 0.591 / 0.487 vs baseline 0.604 / 0.376 / 0.246. Templating and encoder fine-tuning help.
- Code / weights / license: HF checkpoints AIRI-Institute/chexfract-maira2 and AIRI-Institute/chexfract-chexagent; licence not stated; no code repo or dataset release stated.
- Useful for us: evidence that specialising general radiology VLMs on a narrow skeletal finding helps; relevant to vertebral fracture mentions on X-ray.
- Limitations / notes: not spine-specific; recall ≤0.58 (screening with human review only); GPT-4o-derived labels; templating may not fit free-form reporting; no prospective validation. Pattern for us: LLM-mined report labels + templated targets for a narrow skeletal finding.
- BibTeX:
```bibtex
@misc{Nechaev2025ChexFract,
  title         = {{ChexFract}: From General to Specialized -- Enhancing Fracture Description Generation},
  author        = {Nechaev, Nikolay and Przhezdzetskaia, Evgeniia and Umerenkov, Dmitry and others},
  year          = {2025},
  eprint        = {2511.07983},
  archivePrefix = {arXiv}
}
```

---

#### B. General-purpose vision backbones and self-supervised learning

### R152. ViT
- Full title: An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
- Authors: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, et al. (12 authors)
- Year / Venue / Type: 2021 / ICLR 2021 / conference (arXiv 22 Oct 2020)
- DOI / arXiv / URL: arXiv:2010.11929
- Access: open
- Passes: 3/3 (abstract; ar5iv full text read 2026-10-16 for variants/data/results, then limitations/future work)
- Modality & anatomy: natural images
- Data: ImageNet-21k / JFT-300M pretraining; ImageNet, CIFAR-100, VTAB transfer
- Method: pure transformer on image patches. ViT-B (86M, 12 layers), ViT-L (307M), ViT-H (632M); patch sizes 16 or 14.
- Key results: ImageNet top-1 ViT-H/14 (JFT-300M) 88.55% at 2.5k TPUv3-core-days vs BiT-L 87.54% (9.9k) and Noisy Student 88.4-88.5% (12.3k). ViT-L/16 on ImageNet-21k 85.30%. VTAB-19 77.63%. On ImageNet-1k alone ViT trails comparable ResNets ("large scale training trumps inductive bias").
- Code / weights / license: google-research/vision_transformer (Apache-2.0).
- Useful for us: canonical backbone citation for all ViT-based encoders (RAD-DINO, DINOv2/3, MedSAM).
- Limitations / notes: data-hungry; overfits small datasets; self-supervised ViT-B/16 was ~4 points behind supervised (79.9%), later closed by DINO/MAE. For us: ViT encoders must be pretrained (DINOv2/v3, RAD-DINO, nnFoundation) for small spine datasets.
- BibTeX:
```bibtex
@inproceedings{Dosovitskiy2021ViT,
  title     = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},
  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2021},
  eprint    = {2010.11929},
  archivePrefix = {arXiv}
}
```

### R153. Swin Transformer
- Full title: Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
- Authors: Ze Liu, Yutong Lin, Yue Cao, et al. (8 authors)
- Year / Venue / Type: 2021 / ICCV 2021 / conference
- DOI / arXiv / URL: arXiv:2103.14030 ; https://github.com/microsoft/Swin-Transformer
- Access: open
- Passes: 2/3 (abstract; ar5iv full text read 2026-10-16 for variants, complexity and results). The limitations section was truncated; ICCV pages not confirmed (CVF page failed to load).
- Modality & anatomy: natural images
- Data: ImageNet-1K/22K, COCO, ADE20K
- Method: hierarchical transformer with shifted-window attention (window M=7). Window MSA costs 4hwC^2 + 2M^2hwC (linear in tokens) vs quadratic global MSA. Variants T/S/B/L: 29M/50M/88M/197M params (4.5/8.7/15.4G FLOPs at 224; L 103.9G at 384).
- Key results (confirmed): ImageNet-1K top-1 Swin-T 81.3, Swin-B 83.5 (85.2 with 22K pretraining; 86.4 at 384), Swin-L 87.3 (22K, 384). COCO test-dev 58.7 box / 51.1 mask AP (Swin-L HTC++). ADE20K val 53.5 mIoU (Swin-L UperNet).
- Code / weights / license: MIT (repo).
- Useful for us: backbone of Swin-UNETR / VoCo / CT-CLIP-style 3D encoders; good for multi-scale dense prediction on spine volumes.
- Limitations / notes: window size tuning needed for anisotropic MRI.
- BibTeX:
```bibtex
@inproceedings{Liu2021Swin,
  title     = {Swin Transformer: Hierarchical Vision Transformer using Shifted Windows},
  author    = {Liu, Ze and Lin, Yutong and Cao, Yue and Hu, Han and Wei, Yixuan and Zhang, Zheng and Lin, Stephen and Guo, Baining},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  year      = {2021},
  eprint    = {2103.14030},
  archivePrefix = {arXiv}
}
```

### R154. ConvNeXt
- Full title: A ConvNet for the 2020s
- Authors: Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, et al. (6 authors)
- Year / Venue / Type: 2022 / CVPR 2022, pp. 11976-11986 (confirmed via CVF open access) / conference
- DOI / arXiv / URL: arXiv:2201.03545 ; https://github.com/facebookresearch/ConvNeXt
- Access: open
- Passes: 2/3 (arXiv abstract; CVF open-access page for pages and abstract, 2026-10-16). Full text not re-read.
- Modality & anatomy: natural images
- Data: ImageNet-1K/22K, COCO, ADE20K
- Method: ResNet modernised with transformer design choices (large kernels, LayerNorm, inverted bottleneck).
- Key results: 87.8% ImageNet top-1.
- Code / weights / license: MIT (repo; unverified on this pass).
- Useful for us: strong CNN backbone; 3D ConvNeXt variants (MedNeXt) and DINOv3 ConvNeXt distilled models make it attractive for edge deployment.
- Limitations / notes: -
- BibTeX:
```bibtex
@inproceedings{Liu2022ConvNeXt,
  title     = {A ConvNet for the 2020s},
  author    = {Liu, Zhuang and Mao, Hanzi and Wu, Chao-Yuan and Feichtenhofer, Christoph and Darrell, Trevor and Xie, Saining},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {11976--11986},
  year      = {2022},
  eprint    = {2201.03545},
  archivePrefix = {arXiv}
}
```

### R155. DINOv2
- Full title: DINOv2: Learning Robust Visual Features without Supervision
- Authors: Maxime Oquab, Timothée Darcet, Théo Moutakanni, et al. (26 authors)
- Year / Venue / Type: 2023 preprint; published TMLR 2024 / journal
- DOI / arXiv / URL: arXiv:2304.07193 ; https://github.com/facebookresearch/dinov2
- Access: open
- Passes: 2/3 (abstract + repository README/licence)
- Modality & anatomy: natural images (curated LVD-142M; size from paper, not verified in this pass)
- Data: automatically curated diverse dataset
- Method: self-distillation (DINO + iBOT) ViT up to 1B params, distilled into smaller ViTs.
- Key results: distilled models beat OpenCLIP on most image- and pixel-level benchmarks.
- Code / weights / license: Apache-2.0 for code and weights (ViT-S/14 21M, B/14 86M, L/14 300M, g/14 1.1B). NOTE: the repo also hosts "XRay-DINO" and Cell-DINO weights under FAIR Noncommercial Research License.
- Useful for us: commercially-usable 2D backbone; base of RAD-DINO; frozen features + linear heads for radiograph tasks.
- Limitations / notes: 2D only; dense features degrade at long training (fixed in DINOv3).
- BibTeX:
```bibtex
@article{Oquab2024DINOv2,
  title   = {{DINOv2}: Learning Robust Visual Features without Supervision},
  author  = {Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Th{\'e}o and others},
  journal = {Transactions on Machine Learning Research},
  year    = {2024},
  eprint  = {2304.07193},
  archivePrefix = {arXiv}
}
```

### R156. DINOv3
- Full title: DINOv3
- Authors: Oriane Siméoni, Huy V. Vo, Maximilian Seitzer, et al. (26 authors)
- Year / Venue / Type: 2025 / arXiv preprint (13 Aug 2025)
- DOI / arXiv / URL: arXiv:2508.10104 ; https://github.com/facebookresearch/dinov3
- Access: open
- Passes: 3/3 (abstract; README model table; LICENSE.md)
- Modality & anatomy: natural images (LVD-1689M), satellite (SAT-493M)
- Data: LVD-1689M curated web images
- Method: SSL scaled to ViT-7B; "Gram anchoring" to prevent dense-feature degradation; post-hoc resolution/size/text alignment; distilled ViT-S/16 (21M), S+/16 (29M), B/16 (86M), L/16 (300M), H+/16 (840M), and ConvNeXt T/S/B/L (29-198M).
- Key results: SOTA dense features vs previous SSL/weakly-supervised models without fine-tuning (abstract, no numbers).
- Code / weights / license: "DINOv3 License" (custom Meta): royalty-free, redistribution and modification allowed, no non-commercial clause, but attribution required, trade-control/military use prohibited; weights behind access request.
- Useful for us: best current general SSL dense features; SpineAgent (FM-09) builds on it; ConvNeXt-T distilled variant is an edge candidate. Licence appears to permit commercial use (verify with counsel).
- Limitations / notes: 2D; large models need access approval.
- BibTeX:
```bibtex
@misc{Simeoni2025DINOv3,
  title         = {{DINOv3}},
  author        = {Sim{\'e}oni, Oriane and Vo, Huy V. and Seitzer, Maximilian and others},
  year          = {2025},
  eprint        = {2508.10104},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV}
}
```

### R157. MAE
- Full title: Masked Autoencoders Are Scalable Vision Learners
- Authors: Kaiming He, Xinlei Chen, Saining Xie, et al. (6 authors)
- Year / Venue / Type: 2022 / CVPR 2022 / conference
- DOI / arXiv / URL: arXiv:2111.06377 ; https://github.com/facebookresearch/mae
- Access: open
- Passes: 2/3 (abstract + repo)
- Modality & anatomy: natural images
- Data: ImageNet-1K
- Method: mask 75% of patches, asymmetric encoder (visible patches only) + light decoder reconstructs pixels.
- Key results: ViT-Huge 87.8% ImageNet-1K (best among IN-1K-only methods); >=3x faster training.
- Code / weights / license: CC-BY-NC 4.0 (non-commercial) for repo.
- Useful for us: MAE is the SSL objective selected by nnFoundation (FM-26) for 3D radiology; cheap to adapt to spine volumes ourselves (reimplement rather than reuse NC weights).
- Limitations / notes: official weights NC.
- BibTeX:
```bibtex
@inproceedings{He2022MAE,
  title     = {Masked Autoencoders Are Scalable Vision Learners},
  author    = {He, Kaiming and Chen, Xinlei and Xie, Saining and Li, Yanghao and Doll{\'a}r, Piotr and Girshick, Ross},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2022},
  eprint    = {2111.06377},
  archivePrefix = {arXiv}
}
```

#### C. Self-supervised / supervised pretraining for 3D medical imaging

### R158. Models Genesis
- Full title: Models Genesis (journal version of "Models Genesis: Generic Autodidactic Models for 3D Medical Image Analysis", MICCAI 2019)
- Authors: Zongwei Zhou, Vatsal Sodha, Jiaxuan Pang, et al. (5 authors; Gotway, Liang)
- Year / Venue / Type: 2021 / Medical Image Analysis vol. 67, 101840 / journal
- DOI / arXiv / URL: 10.1016/j.media.2020.101840 ; arXiv:2004.07882 ; https://github.com/MrGiovanni/ModelsGenesis
- Access: open (preprint)
- Passes: 2/3 (abstract + repo)
- Modality & anatomy: CT (and MRI per repo) — chest CT primarily
- Data: unlabelled CT (LUNA16, per paper; not verified this pass)
- Method: restoration-based SSL (non-linear intensity, local shuffling, in/out-painting) on 3D U-Net.
- Key results: beats scratch and prior 3D pretrained models on 5 target 3D tasks; 3D Models Genesis beats 2D/2.5D ImageNet transfer.
- Code / weights / license: Keras + PyTorch weights; licence file not read (unverified).
- Useful for us: seminal citation for 3D medical SSL; baseline initialisation.
- Limitations / notes: small, CT-only pretraining corpus.
- BibTeX:
```bibtex
@article{Zhou2021ModelsGenesis,
  title   = {Models Genesis},
  author  = {Zhou, Zongwei and Sodha, Vatsal and Pang, Jiaxuan and Gotway, Michael B. and Liang, Jianming},
  journal = {Medical Image Analysis},
  volume  = {67},
  pages   = {101840},
  year    = {2021},
  doi     = {10.1016/j.media.2020.101840}
}
```

### R159. Swin UNETR self-supervised pretraining
- Full title: Self-Supervised Pre-Training of Swin Transformers for 3D Medical Image Analysis
- Authors: Yucheng Tang, Dong Yang, Wenqi Li, et al. (8 authors)
- Year / Venue / Type: 2022 / CVPR 2022 / conference
- DOI / arXiv / URL: arXiv:2111.14791 ; https://monai.io/research/swin-unetr
- Access: open
- Passes: 2/3 full text (abstract + PDF details/limitations)
- Modality & anatomy: CT (chest, head/neck, abdomen/pelvis)
- Data: 5,050 public CTs (LUNA16 888, TCIA Covid19 761, LIDC 475, HNSCC 1,287, TCIA Colon 1,599 — sums to 5,010 as noted)
- Method: Swin UNETR encoder; proxy tasks masked volume inpainting, 3D rotation prediction, contrastive coding.
- Key results: #1 BTCV leaderboard (avg Dice 0.918 table / 0.908 text); MSD avg Dice 78.68% over 10 tasks.
- Code / weights / license: MONAI, Apache-2.0.
- Useful for us: standard 3D SSL baseline; MONAI weights easily loadable for vertebra segmentation fine-tuning.
- Limitations / notes: CT only; authors note poor MRI transfer due to domain gap/channels.
- BibTeX:
```bibtex
@inproceedings{Tang2022SwinUNETRSSL,
  title     = {Self-Supervised Pre-Training of {Swin} Transformers for {3D} Medical Image Analysis},
  author    = {Tang, Yucheng and Yang, Dong and Li, Wenqi and Roth, Holger R. and Landman, Bennett and Xu, Daguang and Nath, Vishwesh and Hatamizadeh, Ali},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {20730--20740},
  year      = {2022},
  eprint    = {2111.14791},
  archivePrefix = {arXiv}
}
```

### R160. VoCo
- Full title: VoCo: A Simple-yet-Effective Volume Contrastive Learning Framework for 3D Medical Image Analysis
- Authors: Linshan Wu, Jiaxin Zhuang, Hao Chen
- Year / Venue / Type: 2024 / CVPR 2024, pp. 22873-22882 / conference
- DOI / arXiv / URL: arXiv:2402.17300 ; https://github.com/Luffy03/VoCo
- Access: open
- Passes: 2/3 (abstract + repo venue)
- Modality & anatomy: CT
- Data: public CT (see FM-23 for scaled version)
- Method: base crops from different regions define region "classes"; predict which region a random sub-volume belongs to via similarity (geometric context prior).
- Key results: superior on 6 downstream tasks (abstract).
- Code / weights / license: Apache-2.0 code.
- Useful for us: positional/contextual SSL is well suited to the repetitive yet ordered vertebral column (level identity).
- Limitations / notes: CT only.
- BibTeX:
```bibtex
@inproceedings{Wu2024VoCo,
  title     = {{VoCo}: A Simple-yet-Effective Volume Contrastive Learning Framework for {3D} Medical Image Analysis},
  author    = {Wu, Linshan and Zhuang, Jiaxin and Chen, Hao},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {22873--22882},
  year      = {2024},
  eprint    = {2402.17300},
  archivePrefix = {arXiv}
}
```

### R161. Large-scale VoCo (PreCT-160K)
- Full title: Large-Scale 3D Medical Image Pre-training with Geometric Context Priors
- Authors: Linshan Wu, Jiaxin Zhuang, Hao Chen
- Year / Venue / Type: 2024 preprint; IEEE TPAMI 2026 (per repo) / journal
- DOI / arXiv / URL: arXiv:2410.09890 ; https://github.com/Luffy03/Large-Scale-Medical
- Access: open
- Passes: 3/3 (abstract; full PDF; repo)
- Modality & anatomy: CT pretraining; downstream includes 13 MRI datasets and VerSe20 vertebrae
- Data: PreCT-160K = 160,167 CT volumes / 42M slices from 30 public datasets (NLST 84,830; CT-RATE 47,149; TotalSegmentator; AbdomenAtlas...); VoComni 20K pseudo-labelled volumes, 20 classes.
- Method: VoCo SSL + omni-supervision on SwinUNETR B/L/H (72M/290M/1.2B) and nnU-Net (31M).
- Key results: BTCV Swin-B 82.79 -> 86.64 DSC; +3.12% avg over 7 seg datasets; VerSe20 63.72 vs 62.01 scratch (but SuPreM 89.54 — VoCo not best for vertebrae); CT-RATE vocab AUC 73.69; 48-task benchmark; bigger models not always better; 10K->160K data gives marginal gains.
- Code / weights / license: Apache-2.0 code; weight licence not stated.
- Useful for us: largest open CT SSL weights; but evidence that generic SSL helps vertebrae little -> supervised pretraining (SuPreM/TotalSegmentator) may be better init for spine CT.
- Limitations / notes: CT only; data quality.
- BibTeX:
```bibtex
@article{Wu2024LargeScaleVoCo,
  title   = {Large-Scale {3D} Medical Image Pre-training with Geometric Context Priors},
  author  = {Wu, Linshan and Zhuang, Jiaxin and Chen, Hao},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year    = {2026},
  note    = {arXiv:2410.09890; TPAMI acceptance per authors' repository},
  eprint  = {2410.09890},
  archivePrefix = {arXiv}
}
```

### R162. MIS-FM / Volume Fusion
- Full title: MIS-FM: 3D Medical Image Segmentation using Foundation Models Pretrained on a Large-Scale Unannotated Dataset
- Authors: Guotai Wang, Jianghao Wu, Xiangde Luo, et al. (6 authors)
- Year / Venue / Type: 2023 / arXiv preprint; journal version "Volume Fusion-based Self-Supervised Pretraining for 3D Medical Image Segmentation", IEEE TIP 34:6041-6052, 2025
- DOI / arXiv / URL: arXiv:2306.16925 ; https://github.com/openmedlab/MIS-FM
- Access: open
- Passes: 2/3 (abstract + repo)
- Modality & anatomy: CT (head-neck, thorax, abdomen)
- Data: 110k unannotated CT volumes
- Method: Volume Fusion pretext (blend foreground patches into background, predict per-voxel fusion coefficient); parallel conv+transformer network (PCT-Net), FMUNet.
- Key results: outperforms scratch and SSL baselines on organ segmentation (no numbers in abstract).
- Code / weights / license: Apache-2.0; weights on Google Drive.
- Useful for us: commercially permissive 3D CT init; segmentation-like pretext suits vertebra segmentation.
- Limitations / notes: CT only.
- BibTeX:
```bibtex
@misc{Wang2023MISFM,
  title         = {{MIS-FM}: {3D} Medical Image Segmentation using Foundation Models Pretrained on a Large-Scale Unannotated Dataset},
  author        = {Wang, Guotai and Wu, Jianghao and Luo, Xiangde and others},
  year          = {2023},
  eprint        = {2306.16925},
  archivePrefix = {arXiv}
}
```

### R163. SuPreM (supervised 3D pretraining, AbdomenAtlas 1.1)
- Full title: How Well Do Supervised 3D Models Transfer to Medical Imaging Tasks?
- Authors: Wenxuan Li, Alan Yuille, Zongwei Zhou
- Year / Venue / Type: 2024 / ICLR 2024 (oral) / conference
- DOI / arXiv / URL: https://github.com/MrGiovanni/SuPreM ; PDF cs.jhu.edu/~zongwei/publication/li2023suprem.pdf (arXiv id unverified)
- Access: open
- Passes: 3/3 (repo README earlier; ICLR 2024 PDF from the author's JHU page read 2026-10-16 for data/method/results, then limitations/licence). arXiv id still not recorded.
- Modality & anatomy: abdominal CT
- Data: AbdomenAtlas 1.1: 9,262 CTs from 88 hospitals in 19 countries; 25 structures per voxel (incl. 2 skeletal) + pseudo-labels for 7 tumour types. Semi-automatic annotation revised by 10 radiologists. Benchmark models pretrained on 2,100 CTs; 21-CT scaling experiment.
- Method: fully supervised multi-organ pretraining; released Swin UNETR (62.19M), U-Net (19.08M), SegResNet (4.70M).
- Key results: the 21-CT supervised model (40 GPU-h) matches a 5,050-CT SSL model (1,152 GPU-h). Fine-tuning with 512 labelled CTs matches SSL with 1,024. TotalSegmentator organs (U-Net) 92.1 vs 88.9 from scratch. Novel classes: the 24 vertebrae average 89.2 (supervised) vs 86.4 (SSL) Dice. Supervised wins in 5/10/20-shot. Per FM-23, SuPreM is best on VerSe20 (89.54).
- Code / weights / license: code on GitHub (code licence not stated in the paper; "patents pending" in README); weights on HF; AbdomenAtlas 1.1 data CC BY-NC-SA 4.0 (non-commercial).
- Useful for us: strongest transfer for vertebrae per VoCo benchmark; small SegResNet good for edge.
- Limitations / notes: abdominal CT only; tumour labels unconfirmed pseudo-labels; baseline checkpoints not retrained identically; validation-size inconsistency (1,310 vs 310); NC data licence. Vertebra-transfer evidence (89.2) strongly supports supervised CT pretraining for our vertebra segmenter.
- BibTeX:
```bibtex
@inproceedings{Li2024SuPreM,
  title     = {How Well Do Supervised {3D} Models Transfer to Medical Imaging Tasks?},
  author    = {Li, Wenxuan and Yuille, Alan and Zhou, Zongwei},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024}
}
```

### R164. nnFoundation
- Full title: nnFoundation: 3D Foundation Models for Radiology
- Authors: Constantin Ulrich Harsy, Tassilo Wald, Karol Gotkowski, Yannick Kirchhoff, Marcel Knopp, Maximilian Rokuss, Elisa Stegmeier, Philipp Schader, Dasha Trofimova, Raphael Stock, et al. (82 authors; DKFZ)
- Year / Venue / Type: 2026 / arXiv preprint (22 Sep 2026)
- DOI / arXiv / URL: arXiv:2609.26924
- Access: preprint (CC BY 4.0)
- Passes: 3/3 (pass 1-2 earlier from HTML; pass 3 on 2026-10-16: HTML re-read for availability, compute, spine coverage, limitations)
- Modality & anatomy: MRI 71.7%, CT 26.6%, PET 1.7%; head, chest, abdomen, pelvis, extremities
- Data: ~2.1M 3D volumes from 125 sources
- Method: MAE pretraining (chosen over DINOv2 and contrastive in controlled benchmark) of nnFoundationCNN (ResEnc-L based) and nnFoundationViT (Primus based); integrated into nnU-Net/nnDetection.
- Key results: 108 downstream tasks; segmentation +3.0 Dice vs CT-FM and +1.9 vs nnU-Net (34 datasets; only FM to beat nnU-Net); classification +8.3 AUROC vs scratch; CT-RATE report F1 43.7 vs 42.8 (CURIA); OOD Dice 74.9 (88.8% retention); +~3 Dice with 10 training cases; 99.16% performance at ~15% compute.
- Code / weights / license: the nnSSL pretraining framework and downstream repos are on GitHub, and the models are integrated into the official nnU-Net/nnDetection repos (code Apache-2.0). No weight licence stated (CC BY 4.0 covers only the article); no HF listing mentioned. Parameter counts not stated. Compute: controlled benchmark ~400 A100 GPU-h per method; dev budget ~25k GPU-h per team; downstream suite >50k GPU-h; final pretraining compute not reported.
- Useful for us: the most important 3D init for a CT+MRI spine segmenter in nnU-Net; MRI-heavy pretraining matches our MRI focus; evidence MAE > DINOv2 for 3D radiology.
- Limitations / notes (pass 3 confirmed): no spine datasets identifiable among downstream tasks (VerSe/SPIDER/CTSpine1K not mentioned), so spine benefit is an open question we can answer. MRI numbers only in the supplement. No full-scale ablations (scale, capacity, modality mix). Retrospective only. No subgroup/fairness audits. PET underrepresented. Robustness to artefacts and long-tail pathology not established. Detection excluded from cross-model ranking.
- BibTeX:
```bibtex
@misc{Harsy2026nnFoundation,
  title         = {{nnFoundation}: {3D} Foundation Models for Radiology},
  author        = {Harsy, Constantin Ulrich and Wald, Tassilo and Gotkowski, Karol and Kirchhoff, Yannick and Knopp, Marcel and Rokuss, Maximilian and Stegmeier, Elisa and Schader, Philipp and Trofimova, Dasha and Stock, Raphael and others},
  year          = {2026},
  eprint        = {2609.26924},
  archivePrefix = {arXiv}
}
```

---

#### D. Medical image foundation models (segmentation, encoders, CT/MRI/X-ray)

### R165. BiomedParse
- Full title: A foundation model for joint segmentation, detection and recognition of biomedical objects across nine modalities (arXiv: "BiomedParse: a biomedical foundation model for image parsing of everything everywhere all at once")
- Authors: Theodore Zhao, Yu Gu, Jianwei Yang, et al. (15 authors; Microsoft)
- Year / Venue / Type: 2025 / Nature Methods 22:166-176 / journal
- DOI / arXiv / URL: 10.1038/s41592-024-02499-w ; arXiv:2405.12971 ; https://huggingface.co/microsoft/BiomedParse
- Access: open (preprint)
- Passes: 2/3 (abstract + model card)
- Modality & anatomy: 9 modalities incl. CT, MRI, X-ray
- Data: >6M image-mask-text triples, 82 object types; GPT-4-harmonised labels; 102,855 test triples
- Method: text-prompted joint segmentation/detection/recognition (segment all objects of a named type without boxes).
- Key results: SOTA on segmentation/detection especially irregular shapes (abstract gives no Dice).
- Code / weights / license: weights CC-BY-NC-SA-4.0, gated, research and development only, not for clinical use.
- Useful for us: text-prompted "segment vertebra L3"-style interface concept; not usable commercially.
- Limitations / notes: 2D; NC licence.
- BibTeX:
```bibtex
@article{Zhao2025BiomedParse,
  title   = {A foundation model for joint segmentation, detection and recognition of biomedical objects across nine modalities},
  author  = {Zhao, Theodore and Gu, Yu and Yang, Jianwei and others},
  journal = {Nature Methods},
  volume  = {22},
  pages   = {166--176},
  year    = {2025},
  doi     = {10.1038/s41592-024-02499-w}
}
```

### R166. RAD-DINO
- Full title: Exploring scalable medical image encoders beyond text supervision
- Authors: Fernando Pérez-García, Harshita Sharma, Sam Bond-Taylor, et al. (Microsoft Health Futures)
- Year / Venue / Type: 2025 / Nature Machine Intelligence / journal (arXiv Jan 2024)
- DOI / arXiv / URL: 10.1038/s42256-024-00965-w ; arXiv:2401.10815 ; https://huggingface.co/microsoft/rad-dino
- Access: open (preprint)
- Passes: 3/3 (abstract; model card data/architecture; model card licence/limitations)
- Modality & anatomy: chest X-ray
- Data: 882,775 CXRs (MIMIC-CXR 368,960; CheXpert 223,648; PadChest 136,787; NIH-CXR 112,120; BRAX 41,260)
- Method: DINOv2 continued SSL from dinov2-base (ViT-B, 86.6M), image-only (no text).
- Key results: matches/exceeds language-supervised encoders on classification, segmentation, report generation; features correlate better with age/sex; scales with data amount/diversity.
- Code / weights / license: MIT licence on HF, but card states research-only, not for clinical practice.
- Useful for us: strongest argument for image-only SSL on our own (unlabelled) spine radiographs; ready-made X-ray encoder for spine X-ray tasks (domain-adjacent).
- Limitations / notes: chest only; trained on 3 countries.
- BibTeX:
```bibtex
@article{PerezGarcia2025RADDINO,
  title   = {Exploring scalable medical image encoders beyond text supervision},
  author  = {P{\'e}rez-Garc{\'i}a, Fernando and Sharma, Harshita and Bond-Taylor, Sam and others},
  journal = {Nature Machine Intelligence},
  year    = {2025},
  doi     = {10.1038/s42256-024-00965-w}
}
```

### R167. MedImageInsight
- Full title: MedImageInsight: An Open-Source Embedding Model for General Domain Medical Imaging
- Authors: Noel C. F. Codella, Ying Jin, Shrey Jain, et al. (31 authors; Microsoft)
- Year / Venue / Type: 2024 / arXiv preprint (9 Oct 2024)
- DOI / arXiv / URL: arXiv:2410.06542
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv HTML read 2026-10-16 for data/method/results, then availability/limitations)
- Modality & anatomy: X-ray, CT, MRI, dermoscopy, OCT, fundus, US, histopathology, mammography
- Data: ~3.79M image-text/label/age samples across 14 domains (~1,000 categorical labels); evaluation ~86k samples. CT: MSD (116,500 pairs), LIDC-IDRI; MRI: UPENN, TCGA; bone age: RSNA BoneAge 12,611 images.
- Method: two-tower Florence-derived model trained with UniCL. DaViT image encoder (~360M) + text encoder (~252M). AdamW lr 1e-5, batch 1024, 40k iterations; 7,680 V100 GPU-hours. Images resized to 512x512 (aspect not preserved). Optional small report decoder (<0.5B total).
- Key results: 3D-MIR CT retrieval tumour-presence AP 95.4 (BiomedCLIP 91.4). MR/CT exam-parameter mAUC 0.977. Bone age MAE 6.19 months (RSNA) / 6.57 (MGB) via KNN vs a cited expert reference of 7.32. MIMIC-CXR reports: CheXbert micro-F1-14 53.6, RadGraph F1 25.5. Independent UW-Madison evaluation (8,842 images): mAUC 91.2 vs RAD-DINO 83.9.
- Code / weights / license: weights described as open-source; the paper does not name a licence or distribution channel (Azure AI Foundry mention unverified). Not for diagnostic use.
- Useful for us: general embedding for retrieval of similar spine cases and bone-related tasks (bone age shows skeletal sensitivity).
- Limitations / notes: 2D encoder (3D only via slice retrieval, four CT organs); aspect-ratio distortion; limited fairness analysis; some recreated splits; report generation only on single frontal CXR.
- BibTeX:
```bibtex
@misc{Codella2024MedImageInsight,
  title         = {{MedImageInsight}: An Open-Source Embedding Model for General Domain Medical Imaging},
  author        = {Codella, Noel C. F. and Jin, Ying and Jain, Shrey and others},
  year          = {2024},
  eprint        = {2410.06542},
  archivePrefix = {arXiv}
}
```

### R168. BiomedCLIP
- Full title: A Multimodal Biomedical Foundation Model Trained from Fifteen Million Image–Text Pairs (arXiv: "BiomedCLIP: a multimodal biomedical foundation model pretrained from fifteen million scientific image-text pairs")
- Authors: Sheng Zhang, Yanbo Xu, Naoto Usuyama, et al. (24 authors)
- Year / Venue / Type: 2024/2025 / NEJM AI 2(1) / journal
- DOI / arXiv / URL: 10.1056/AIoa2400640 ; arXiv:2303.00915 ; https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224
- Access: open (preprint)
- Passes: 2/3 (abstract + model card)
- Modality & anatomy: mixed biomedical figures
- Data: PMC-15M, ~15M figure-caption pairs from 4.4M PubMed Central articles
- Method: CLIP with ViT-B/16 + PubMedBERT (256 tokens).
- Key results: new SOTA across retrieval/classification/VQA; beats BioViL on RSNA pneumonia.
- Code / weights / license: MIT, but card says any deployed use (commercial or otherwise) out of scope.
- Useful for us: zero-shot text-image baseline; used as backbone in spine VLM work (FM-11).
- Limitations / notes: 2D figures, not raw DICOM.
- BibTeX:
```bibtex
@article{Zhang2025BiomedCLIP,
  title   = {A Multimodal Biomedical Foundation Model Trained from Fifteen Million Image--Text Pairs},
  author  = {Zhang, Sheng and Xu, Yanbo and Usuyama, Naoto and others},
  journal = {NEJM AI},
  volume  = {2},
  number  = {1},
  year    = {2025},
  doi     = {10.1056/AIoa2400640}
}
```

### R169. RadFM
- Full title: Towards Generalist Foundation Model for Radiology by Leveraging Web-scale 2D&3D Medical Data
- Authors: Chaoyi Wu, Xiaoman Zhang, Ya Zhang, et al. (5 authors; Yanfeng Wang, Weidi Xie)
- Year / Venue / Type: 2023 / arXiv preprint (journal version unverified)
- DOI / arXiv / URL: arXiv:2308.02463 ; https://github.com/chaoyi-wu/RadFM
- Access: preprint
- Passes: 2/3 (abstract + repo)
- Modality & anatomy: 2D and 3D radiology (CT, MRI, X-ray), >5,000 diseases
- Data: MedMD 16M 2D/3D scans with text; RadMD ~3M radiology pairs; RadBench (modality recognition, diagnosis, VQA, report generation, rationale diagnosis)
- Method: 3D ViT + Perceiver (32 tokens/image) feeding an LLM; 2D images repeated along depth (D=4); interleaved multi-image input.
- Key results: beats OpenFlamingo, MedFlamingo, MedVInT, GPT-4V on RadBench (auto + human eval).
- Code / weights / license: code MIT; weights on HF (licence not stated); Radiopaedia-derived data requires permission.
- Useful for us: native 2D+3D multi-image VLM baseline; Radiopaedia contains many spine cases.
- Limitations / notes: venue unverified.
- BibTeX:
```bibtex
@misc{Wu2023RadFM,
  title         = {Towards Generalist Foundation Model for Radiology by Leveraging Web-scale {2D\&3D} Medical Data},
  author        = {Wu, Chaoyi and Zhang, Xiaoman and Zhang, Ya and Wang, Yanfeng and Xie, Weidi},
  year          = {2023},
  eprint        = {2308.02463},
  archivePrefix = {arXiv}
}
```

### R170. Merlin
- Full title: Merlin: A Computed Tomography Vision-Language Foundation Model and Dataset
- Authors: Louis Blankemeier, Ashwin Kumar, Joseph Paul Cohen, Jiaming Liu, Longchao Liu, Dave Van Veen, Syed Jamal Safdar Gardezi, Hongkun Yu, Magdalini Paschali, Zhihong Chen, et al. (40 authors; Stanford)
- Year / Venue / Type: 2026 (published 2026-03-04) / Nature 652(8112):1318-1328 (confirmed via OpenAlex 2026-10-16) / journal (arXiv Jun 2024)
- DOI / arXiv / URL: 10.1038/s41586-026-10181-8 ; arXiv:2406.06512 ; https://github.com/StanfordMIMI/Merlin
- Access: publisher closed; green OA (arXiv + PMC13082451)
- Passes: 3/3 (abstract; full PDF methods/results/limitations; repo)
- Modality & anatomy: abdominal CT (incl. lumbar spine T12-S1 in field of view)
- Data: 15,331 CTs (>6M images), >1.8M ICD codes, >6M report tokens; internal test 5,137 CTs; external 44,098 CTs (3 sites + 2 public)
- Method: I3D ResNet152 (ImageNet-inflated) + Clinical Longformer; multi-task BCE on EHR phenotypes + InfoNCE on report sections; ~160 GPU-hours on one A6000.
- Key results: zero-shot findings F1 0.741 internal / 0.647 external; phenotype macro-AUROC 0.812 (692 phenotypes); zero-shot vertebral fracture detection on VerSe F1 0.767 (95% CI 0.623-0.867); segmentation with 10% data +4.7% Dice over nnU-Net; 752 tasks total.
- Code / weights / license: code MIT; weights on HF (licence not stated on repo page); dataset release with access terms.
- Useful for us: directly reports zero-shot spine fracture detection; vertebrae among segmentation targets; shows cheap single-GPU 3D CLIP training is feasible.
- Limitations / notes: single centre, 97% portal venous; report generation under-reports positives.
- BibTeX:
```bibtex
@article{Blankemeier2026Merlin,
  title   = {Merlin: A Computed Tomography Vision-Language Foundation Model and Dataset},
  author  = {Blankemeier, Louis and Kumar, Ashwin and Cohen, Joseph Paul and Liu, Jiaming and Liu, Longchao and Van Veen, Dave and Gardezi, Syed Jamal Safdar and Yu, Hongkun and Paschali, Magdalini and Chen, Zhihong and others},
  journal = {Nature},
  volume  = {652},
  number  = {8112},
  pages   = {1318--1328},
  year    = {2026},
  doi     = {10.1038/s41586-026-10181-8}
}
```

### R171. CT-FM
- Full title: Vision Foundation Models for Computed Tomography
- Authors: Suraj Pai, Ibrahim Hadzic, Dennis Bontempi, et al. (8 authors; AIM / Mass General Brigham, unverified)
- Year / Venue / Type: 2025 / arXiv preprint
- DOI / arXiv / URL: arXiv:2501.09001 ; https://github.com/project-lighter/CT-FM
- Access: preprint
- Passes: 2/3 (abstract + repo)
- Modality & anatomy: whole-body CT
- Data: 148,000 CT scans from NCI Imaging Data Commons
- Method: SegResEncoder (77M) trained with modified SimCLR intra-sample contrastive learning, 500 epochs; plugs into SegResNetDS.
- Key results: better than SOTA on whole-body/tumour segmentation, head CT triage, retrieval, semantic understanding; test-retest robust.
- Code / weights / license: code MIT; weights released (licence not stated); IDC data mostly CC-BY.
- Useful for us: permissive, CNN-based (deployable) CT encoder; nnFoundation uses it as main comparator.
- Limitations / notes: CT only.
- BibTeX:
```bibtex
@misc{Pai2025CTFM,
  title         = {Vision Foundation Models for Computed Tomography},
  author        = {Pai, Suraj and Hadzic, Ibrahim and Bontempi, Dennis and others},
  year          = {2025},
  eprint        = {2501.09001},
  archivePrefix = {arXiv}
}
```

### R172. CT-RATE / CT-CLIP / CT-CHAT
- Full title: Generalist Foundation Models from a Multimodal Dataset for 3D Computed Tomography
- Authors: Ibrahim Ethem Hamamci, Sezgin Er, Chenyu Wang, et al. (30 authors; Bjoern Menze senior)
- Year / Venue / Type: 2026 / Nature Biomedical Engineering / journal (arXiv Mar 2024)
- DOI / arXiv / URL: 10.1038/s41551-025-01599-y ; arXiv:2403.17834 ; https://huggingface.co/datasets/ibrahimhamamci/CT-RATE
- Access: open
- Passes: 2/3 (abstract + dataset card)
- Modality & anatomy: non-contrast chest CT (thoracic spine in FOV)
- Data: 25,692 CTs (50,188 reconstructions) from 21,304 patients with reports; 2.7M QA pairs for CT-CHAT
- Method: CT-CLIP (3D contrastive) for multi-abnormality detection and retrieval; CT-CHAT = CT-CLIP encoder + LLM.
- Key results: CT-CLIP beats fully-supervised baselines on all key metrics (numbers not in abstract).
- Code / weights / license: dataset CC-BY-NC-SA (commercial use requires contacting providers); paper CC BY-NC-SA.
- Useful for us: the standard public 3D CT report dataset; benchmark for report generation (nnFoundation, VoCo report F1 on CT-RATE).
- Limitations / notes: chest only, single country (Turkey).
- BibTeX:
```bibtex
@article{Hamamci2026CTRATE,
  title   = {Generalist foundation models from a multimodal dataset for {3D} computed tomography},
  author  = {Hamamci, Ibrahim Ethem and Er, Sezgin and Wang, Chenyu and others},
  journal = {Nature Biomedical Engineering},
  year    = {2026},
  doi     = {10.1038/s41551-025-01599-y}
}
```

### R173. M3D (M3D-Data, M3D-LaMed, M3D-Bench)
- Full title: M3D: Advancing 3D Medical Image Analysis with Multi-Modal Large Language Models
- Authors: Fan Bai, Yuxin Du, Tiejun Huang, et al. (5 authors; Max Q.-H. Meng, Bo Zhao)
- Year / Venue / Type: 2024 / arXiv preprint
- DOI / arXiv / URL: arXiv:2404.00578 ; https://github.com/BAAI-DCAI/M3D
- Access: preprint
- Passes: 2/3 (abstract + repo)
- Modality & anatomy: 3D CT (Radiopaedia-derived), multi-region
- Data: 120K image-text pairs, 662K instruction-response pairs; M3D-Bench 8 tasks (retrieval, report generation, VQA, positioning, segmentation, ...)
- Method: 3D ViT (M3D-CLIP) + LLM (Llama-2-7B or Phi-3-4B) with segmentation via promptable decoder.
- Key results: outperforms existing 3D MLLMs (abstract).
- Code / weights / license: code MIT; data via Radiopaedia non-commercial approval; weight licence not stated (base LLM licences apply).
- Useful for us: the base model used by spine VLM FM-10; 3D VQA + grounding template.
- Limitations / notes: non-commercial data.
- BibTeX:
```bibtex
@misc{Bai2024M3D,
  title         = {{M3D}: Advancing {3D} Medical Image Analysis with Multi-Modal Large Language Models},
  author        = {Bai, Fan and Du, Yuxin and Huang, Tiejun and Meng, Max Q.-H. and Zhao, Bo},
  year          = {2024},
  eprint        = {2404.00578},
  archivePrefix = {arXiv}
}
```

### R174. MAIRA-2
- Full title: MAIRA-2: Grounded Radiology Report Generation
- Authors: Shruthi Bannur, Kenza Bouzid, Daniel C. Castro, Anton Schwaighofer, Anja Thieme, Sam Bond-Taylor, Maximilian Ilse, Fernando Pérez-García, Valentina Salvatelli, Harshita Sharma, et al. (21 authors; Microsoft)
- Year / Venue / Type: 2024 / arXiv preprint
- DOI / arXiv / URL: arXiv:2406.04449
- Access: preprint
- Passes: 3/3 (abstract earlier; full arXiv HTML read 2026-10-16 for data/architecture/RadFact/results, then release/limitations)
- Modality & anatomy: chest X-ray
- Data: 510,848 examples from 226,077 patients (14% grounded). MIMIC-CXR 158,555; PadChest 85,598 (+3,183 PadChest-GR grounded); private USMix 193,652. GR-Bench (USMix subset): 8,580 train / 1,231 test. External test on IU-Xray (3,306).
- Method: frozen RAD-DINO-MAIRA-2 encoder (ViT-B, 87M) + 4-layer MLP adapter + Vicuna-7B v1.5. Inputs: current frontal and lateral images, prior frontal image and prior report, plus Indication/Technique/Comparison. Boxes emitted as coordinate tokens on a 100-step grid. RadFact: Llama3-70B judge (10 in-context examples) computes sentence-level logical precision/recall (entailment both ways), grounding precision/recall and spatial precision/recall.
- Key results: MIMIC-CXR findings: RadFact logical precision/recall 52.9 / 48.2 (MAIRA-1 48.3 / 47.2); RadGraph-F1 34.6 (MedVersa 28.0); ROUGE-L 38.4; CheXbert similarity 50.7; CheXpert macro-F1-14 41.6. RadCliQ difference vs MedVersa not significant. GR-Bench: logical P/R 74.1 / 72.8, grounding P/R 68.8 / 90.6, spatial P/R 33.5 / 34.2.
- Code / weights / license: model released (HF microsoft/maira-2) and an open-source RadFact implementation on GitHub; licence not stated in the paper (unverified; assumed research-only).
- Useful for us: grounded findings (sentence + box) is exactly the output format we want for "deviation from normal" with localisation; RadFact as evaluation metric.
- Limitations / notes: CXR only; poor zero-shot on spine MRI in FM-01. Omissions are the most common error. RadFact ignores severity, penalises partially correct sentences and misses internal inconsistency. Single-expert review. Possible text shortcuts from the prior report. Below clinical-deployment level. RadFact's sentence-level entailment plus grounding scheme is directly reusable for our level-wise spine reports.
- BibTeX:
```bibtex
@misc{Bannur2024MAIRA2,
  title         = {{MAIRA-2}: Grounded Radiology Report Generation},
  author        = {Bannur, Shruthi and Bouzid, Kenza and Castro, Daniel C. and others},
  year          = {2024},
  eprint        = {2406.04449},
  archivePrefix = {arXiv}
}
```

> NOTE for entries FM-40 onward marked "passes: 0/3 (prior knowledge)": the shared web-fetch budget (400 calls/h across all agents) and web-search budget were exhausted mid-review. These entries are seminal/well-known works whose bibliographic metadata is recorded from the reviewer's prior knowledge and has NOT been re-verified online in this session; any number or detail not certain is marked "unverified". Re-verify DOIs/pages before final bibliography.

#### E. Medical multimodal LLMs / generalist VLMs (2D and 3D)

### R175. MedGemma
- Full title: MedGemma Technical Report
- Authors: Andrew Sellergren, Sahar Kazemzadeh, Tiam Jaroensri, Atilla Kiraly, Madeleine Traverse, Timo Kohlberger, Shawn Xu, Fayaz Jamil, Cían Hughes, Charles Lau, et al. (81 authors, Google)
- Year / Venue / Type: 2025 (v1 2025-07-07; v4 2026-04-06) / arXiv preprint (technical report)
- DOI / arXiv / URL: arXiv:2507.05201 ; https://huggingface.co/google/medgemma-4b-it ; goo.gle/medgemma
- Access: open (paper CC BY 4.0)
- Passes: 2/3 (arXiv abs + full HTML v4 read for methods/data/results/limitations + HF model card for licence, 2026-10-16)
- Modality & anatomy: CXR, dermatology, ophthalmology, histopathology, CT and MRI as 2D slices only. 3D volumes were NOT used in training. CT slices are encoded as three preset windows mapped to RGB.
- Data: MedSigLIP enhancement used >33M image-text pairs (~635k non-pathology images + 32.6M histopathology patches), mixed at 2% with the original SigLIP data. Imaging sources: MIMIC-CXR 231,483; EyePACS 199,258; internal derm 51,049; CT-US1 59,979 slices; MRI-US1 47,622 slices; PMC 41,853. Text post-training: MedQA, MedMCQA, PubMedQA, AfriMed-QA and ~200k synthetic questions.
- Method: built on Gemma 3. Variants: MedGemma 4B multimodal, 27B text, 27B multimodal (27B-MM evaluation preliminary, App. F). MedSigLIP image encoder (400M, derived from SigLIP-400M; released at 448x448; internal 896x896). Context 128k.
- Key results: MedQA 64.4 (4B) and 87.7 (27B, test-time scaling). VQA-RAD token F1 49.9 / closed acc 69.1 (4B). SLAKE F1 72.3 / closed acc 87.6. MIMIC-CXR macro-F1 (5 conditions) 88.9 on the Med-Gemini split and 40.5 on the MAIRA split. CXR report RadGraph F1 29.5, rising to 30.3 after fine-tuning (claimed SOTA vs MedVersa 30.0). In a review by 1 unblinded radiologist, 81% of reports led to the same or better clinical decisions. Fine-tuning: pneumothorax 85.9 to 87.8; CRC100k weighted F1 32.8 to 94.5. Independent spine results: MedGemma-4B 8.73% overall on SpineBench-MM (below chance, FM-04); MedGemma-27B had the best zero-shot BERTScore on LSMRI (FM-01); QLoRA fine-tuning of the 4B was feasible (FM-01).
- Code / weights / license: weights on HF under the "Health AI Developer Foundations terms of use" (licence tag health-ai-developer-foundations; gated, must accept). The model card does not state whether commercial use is allowed. CORRECTION: the earlier memory note "commercial use reportedly allowed" is unconfirmed; read the HAI-DEF terms directly before deployment.
- Useful for us: most practical open medical LLM backbone (4B fits a single GPU; QLoRA). It has no native 3D support, so a spine MRI/CT pipeline must feed it 2D slices or our structured measurements. Zero-shot spine skill is poor.
- Limitations / notes: 3D and genomics excluded. Benchmarks near saturation, with possible contamination. 4B variant does poorly on agentic tasks (AgentClinic). Human evaluation used a single unblinded reader. The model card says outputs must not directly guide diagnosis without validation. Tested mainly on single-image, single-turn use.
- BibTeX:
```bibtex
@misc{Sellergren2025MedGemma,
  title         = {{MedGemma} Technical Report},
  author        = {Sellergren, Andrew and Kazemzadeh, Sahar and Jaroensri, Tiam and Kiraly, Atilla and Traverse, Madeleine and Kohlberger, Timo and Xu, Shawn and Jamil, Fayaz and Hughes, C{\'i}an and Lau, Charles and others},
  year          = {2025},
  eprint        = {2507.05201},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI}
}
```

### R176. LLaVA-Med
- Full title: LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day
- Authors: Chunyuan Li, Cliff Wong, Sheng Zhang, Naoto Usuyama, Haotian Liu, Jianwei Yang, Tristan Naumann, Hoifung Poon, Jianfeng Gao (Microsoft)
- Year / Venue / Type: 2023 / NeurIPS 2023 Datasets and Benchmarks Track (spotlight, per the repo README) / conference
- DOI / arXiv / URL: arXiv:2306.00890 (v1 2023-06-01) ; https://github.com/microsoft/LLaVA-Med ; HF microsoft/llava-med-v1.5-mistral-7b
- Access: open
- Passes: 3/3 (arXiv abs; full HTML for data/method/results/limitations; GitHub README for venue/licence, 2026-10-16)
- Modality & anatomy: biomedical figures from PMC. Instruction data covers CXR, CT, MRI, histopathology and gross pathology.
- Data: built from PMC-15M (~15M PubMed Central figure-caption pairs). Stage 1 alignment used 600K pairs. Stage 2 instruction tuning used 60K pairs with GPT-4-generated multi-turn conversations (plus a 10K ablation subset; the 60K-IM variant adds inline figure mentions).
- Method: LLaVA (vision encoder + linear projection + Vicuna/LLaMA 7B; 13B also tested). Vision encoder initialised from CLIP or BiomedCLIP (BiomedCLIP slightly better). Two-stage curriculum: concept alignment (~7 h) then instruction tuning (~8 h), under 15 h total on 8x A100-40GB. v1.5 (May 2024) uses a Mistral-7B base.
- Key results (fine-tuned, open recall / closed accuracy): VQA-RAD 64.75/83.09; SLAKE 87.11/86.78; PathVQA 39.60/91.09. LLaVA scored 50.00/65.07, 78.18/63.22 and 7.74/63.20. LLaVA-Med beats the prior supervised SOTA on some metrics only (e.g. SLAKE open 87.11 vs 84.30). GPT-4-judged chat score was 50.2% vs LLaVA 36.1%. Spine: LLaVA-Med v1.5 scored 15.29% on SpineBench-MM (FM-04); it is the backbone in FM-11.
- Code / weights / license: code under the Microsoft Research License; data CC BY-NC 4.0. Also bound by LLaMA/Vicuna/GPT-4 terms. "Research use only"; use in clinical care or decision-making is expressly prohibited.
- Useful for us: canonical medical VLM baseline and template for the two-stage alignment-then-instruction recipe. Not deployable.
- Limitations / notes: the authors acknowledge hallucination and weak in-depth reasoning. Open-set VQA is weak. Chat evaluation relies on GPT-4 judging (text-only reference). 2D only.
- BibTeX:
```bibtex
@inproceedings{Li2023LLaVAMed,
  title     = {{LLaVA-Med}: Training a Large Language-and-Vision Assistant for Biomedicine in One Day},
  author    = {Li, Chunyuan and Wong, Cliff and Zhang, Sheng and Usuyama, Naoto and Liu, Haotian and Yang, Jianwei and Naumann, Tristan and Poon, Hoifung and Gao, Jianfeng},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track},
  volume    = {36},
  year      = {2023},
  eprint    = {2306.00890},
  archivePrefix = {arXiv}
}
```

### R177. Med-PaLM M
- Full title: Towards Generalist Biomedical AI
- Authors: Tao Tu, Shekoofeh Azizi, Danny Driess, Mike Schaekermann, Mohamed Amin, Pi-Chuan Chang, Andrew Carroll, Chuck Lau, Ryutaro Tanno, Ira Ktena, et al. (32 authors; Vivek Natarajan senior) (Google)
- Year / Venue / Type: 2024 (published 2024-02-22) / NEJM AI 1(3) / journal (arXiv v1 2023-07-26)
- DOI / arXiv / URL: DOI 10.1056/AIoa2300138 (confirmed via OpenAlex) ; arXiv:2307.14334
- Access: journal closed; arXiv preprint open
- Passes: 2/3 (arXiv abs; arXiv HTML methods/results/limitations; OpenAlex journal record, 2026-10-16)
- Modality & anatomy: multi-domain (CXR, dermatology, pathology, mammography, genomics, text)
- Data: MultiMedBench: 14 tasks, 5 task types, 12 datasets, 7 modalities, >1M samples
- Method: PaLM-E (PaLM + ViT) fine-tuned as a generalist with a single set of weights. 12B = PaLM 8B + ViT 4B; 84B = PaLM 62B + ViT 22B; 562B = PaLM 540B + ViT 22B.
- Key results: MIMIC-CXR report generation F1-RadGraph 25.20 / 26.71 / 26.06% and BLEU-4 10.43 / 11.31 / 11.50% (12B / 84B / 562B). Reader study: 246 MIMIC-CXR test images, 4 thoracic radiologists. Model reports were preferred over the reference report in 40.50% of cases (84B), vs 34.05% (12B) and 32.00% (562B). Clinically significant errors per report: 0.25 (84B), 0.28 (12B), 0.29 (562B).
- Code / weights / license: weights not released ("will not be able to open source").
- Useful for us: cite for generalist medical AI and for the side-by-side radiologist preference plus error-count protocol for evaluating reports.
- Limitations / notes: closed. The vision encoder is a bottleneck. The largest model is verbose. Benchmark diversity is limited. Real-world validation is lacking.
- BibTeX:
```bibtex
@article{Tu2024MedPaLMM,
  title   = {Towards Generalist Biomedical {AI}},
  author  = {Tu, Tao and Azizi, Shekoofeh and Driess, Danny and Schaekermann, Mike and Amin, Mohamed and Chang, Pi-Chuan and Carroll, Andrew and Lau, Chuck and Tanno, Ryutaro and Ktena, Ira and others},
  journal = {NEJM AI},
  volume  = {1},
  number  = {3},
  year    = {2024},
  doi     = {10.1056/AIoa2300138},
  eprint  = {2307.14334},
  archivePrefix = {arXiv}
}
```

### R178. Med-Gemini (multimodal: 2D, 3D, genomics)
- Full title: Advancing Multimodal Medical Capabilities of Gemini
- Authors: Lin Yang, Shawn Xu, Andrew Sellergren, Timo Kohlberger, Yuchen Zhou, Ira Ktena, Atilla Kiraly, Faruk Ahmed, Farhad Hormozdiari, Tiam Jaroensri, et al. (47 authors, Google)
- Year / Venue / Type: 2024 (submitted 2024-05-06) / arXiv preprint
- DOI / arXiv / URL: arXiv:2405.03162
- Access: preprint (open)
- Passes: 2/3 (arXiv abs metadata; arXiv HTML v1 read for methods/data/results/limitations, 2026-10-16)
- Modality & anatomy: CXR, head/neck CT (3D), pathology, dermatology, ophthalmology, genomics (polygenic risk)
- Data: public sets (MIMIC-CXR, CheXpert, ChestX-ray14, NLST, PAD-UFES-20, EyePACS, SLAKE, PathVQA, VQA-RAD, PMC-OA, TCGA, UK Biobank) plus private sets (CT-US1 from three US hospital regions, 657,719 3D training volumes; IND1 Indian hospital group CXR; internal histopathology).
- Method: Gemini fine-tuned into Med-Gemini-2D, Med-Gemini-3D and Med-Gemini-Polygenic. Med-Gemini-3D feeds the CT volume through Gemini's video encoder, with slice depth as the time axis.
- Key results: on 92 non-contrast head/neck CTs rated by one US board-certified radiologist, 53% of Med-Gemini-3D reports were clinically acceptable and only 17% were equal to or better than the original report. Med-Gemini-2D CXR reports rated equal or better than the original: MIMIC-CXR normal 57% (prior SOTA 45%), abnormal 43% (42%); IND1 normal 96%, abnormal 65%. Clinically acceptable overall: 72% (MIMIC) and 88% (IND1). The authors call it the first LLM-based end-to-end 3D CT-to-report model.
- Code / weights / license: models not released. Some re-labelled splits announced for release.
- Useful for us: first demonstration of LLM report generation from full 3D CT volumes. Treating slices as video frames is a cheap way to feed spine MRI/CT stacks to a VLM. Shows the gap to radiologists (17%).
- Limitations / notes: missed and hallucinated findings (e.g. subdural haematomas). Out-of-distribution drop (ChestX-ray14 fracture F1 5.5%). Single rater for 3D. Closed.
- BibTeX:
```bibtex
@misc{Yang2024MedGeminiMultimodal,
  title         = {Advancing Multimodal Medical Capabilities of {Gemini}},
  author        = {Yang, Lin and Xu, Shawn and Sellergren, Andrew and Kohlberger, Timo and Zhou, Yuchen and Ktena, Ira and Kiraly, Atilla and Ahmed, Faruk and Hormozdiari, Farhad and Jaroensri, Tiam and others},
  year          = {2024},
  eprint        = {2405.03162},
  archivePrefix = {arXiv}
}
```

### R179. CLIP
- Full title: Learning Transferable Visual Models From Natural Language Supervision
- Authors: Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever (OpenAI)
- Year / Venue / Type: 2021 / ICML 2021, PMLR 139:8748-8763 / conference (arXiv 2021-02-26)
- DOI / arXiv / URL: arXiv:2103.00020 ; https://proceedings.mlr.press/v139/radford21a.html
- Access: open
- Passes: 2/3 (arXiv abs; ar5iv full text for methods/results/limitations; PMLR page for pages/BibTeX, 2026-10-16)
- Modality & anatomy: natural images
- Data: WIT (WebImageText), 400M web image-text pairs; benchmarked on >30 datasets
- Method: contrastive image-text pretraining. Encoders: ResNets (RN50 to RN50x64) and ViTs (B/32, B/16, L/14, and L/14@336px as the best model). Compute: RN50x64 took 18 days on 592 V100s; the largest ViT took 12 days on 256 V100s.
- Key results: zero-shot ImageNet top-1 76.2% (confirmed), matching the original ResNet-50 without using ImageNet training labels.
- Code / weights / license: MIT per the openai/CLIP repository (licence not re-checked this pass)
- Useful for us: foundation of BiomedCLIP, CT-CLIP, Merlin and M3D-CLIP. Basis for contrastive alignment of our measurements/reports with images.
- Limitations / notes: weak on fine-grained, counting/abstract and truly out-of-distribution data (MNIST ~88%). Weak zero-shot on medical PatchCamelyon, which motivates domain-specific CLIPs.
- BibTeX:
```bibtex
@inproceedings{Radford2021CLIP,
  title     = {Learning Transferable Visual Models From Natural Language Supervision},
  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and Krueger, Gretchen and Sutskever, Ilya},
  booktitle = {Proceedings of the 38th International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {139},
  pages     = {8748--8763},
  publisher = {PMLR},
  year      = {2021},
  eprint    = {2103.00020},
  archivePrefix = {arXiv}
}
```

---

#### F. Radiology-specific pretraining datasets and MRI/CT segmentation foundation models, modality-agnostic training

### R180. RadImageNet
- Full title: RadImageNet: An Open Radiologic Deep Learning Research Dataset for Effective Transfer Learning
- Authors: Xueyan Mei, Zelong Liu, Philip M. Robson, Brett Marinelli, Mingqian Huang, Amish Doshi, Adam Jacobi, Chendi Cao, Katherine E. Link, Thomas Yang, Ying Wang, Hayit Greenspan, Timothy Deyer, Zahi A. Fayad, Yang Yang (Mount Sinai)
- Year / Venue / Type: 2022 (published 2022-07-27) / Radiology: Artificial Intelligence 4(5):e210315 / journal
- DOI / arXiv / URL: 10.1148/ryai.210315 ; https://github.com/BMEII-AI/RadImageNet ; https://www.radimagenet.com/
- Access: open (hybrid OA, CC BY 4.0, confirmed via OpenAlex)
- Passes: 2/3 (OpenAlex record + full structured abstract; GitHub README for assets/licence, 2026-10-16)
- Modality & anatomy: CT, MRI, ultrasound. Musculoskeletal, neurologic, oncologic, GI, endocrine, abdominal and pulmonary conditions. Spine is not explicitly mentioned on the repo page (unverified).
- Data: 1.35M annotated key images from 131,872 patients (outpatient facility, 2005-2020); 165 pathology labels (README). Confirmed.
- Method: supervised pretraining from random initialisation of 2D CNNs (ResNet50, DenseNet121, InceptionResNetV2, InceptionV3); Swin weights "to be released".
- Key results (AUC gain vs ImageNet init, P<.001): small datasets thyroid US +9.4%, breast US +4.0%, ACL MRI +4.8%, meniscus MRI +4.5%. Larger datasets: pneumonia CXR +1.9%, COVID-19 CT +6.1%, SARS-CoV-2 CT +1.7%, ICH CT +0.9%. Lesion localisation improved by 64.6% (thyroid US) and 16.4% (breast US).
- Code / weights / license: repo MIT; pretrained weights (TF and PyTorch) are a direct Google Drive download; the dataset is available on request. Dataset terms not stated. Correction: the memory note said weights were "on request"; it is actually the dataset that is on request.
- Useful for us: alternative 2D initialisation for MRI/CT slice classifiers; gains are largest on small datasets, which matches our labelled spine subsets.
- Limitations / notes: 2D key images only; single institution; superseded by SSL foundation models (DINOv2/RAD-DINO).
- BibTeX:
```bibtex
@article{Mei2022RadImageNet,
  title   = {{RadImageNet}: An Open Radiologic Deep Learning Research Dataset for Effective Transfer Learning},
  author  = {Mei, Xueyan and Liu, Zelong and Robson, Philip M. and Marinelli, Brett and Huang, Mingqian and Doshi, Amish and Jacobi, Adam and Cao, Chendi and Link, Katherine E. and Yang, Thomas and Wang, Ying and Greenspan, Hayit and Deyer, Timothy and Fayad, Zahi A. and Yang, Yang},
  journal = {Radiology: Artificial Intelligence},
  volume  = {4},
  number  = {5},
  pages   = {e210315},
  year    = {2022},
  doi     = {10.1148/ryai.210315}
}
```

### R181. BrainSegFounder
- Full title: BrainSegFounder: Towards 3D Foundation Models for Neuroimage Segmentation
- Authors: Joseph Cox, Peng Liu, Skylar E. Stolte, Yunchao Yang, Kang Liu, Kyle B. See, Huiwen Ju, Ruogu Fang (Univ. Florida)
- Year / Venue / Type: 2024 / Medical Image Analysis (journal and year confirmed via the NSF PAR record; volume 97 and article 103301 still unverified) / journal
- DOI / arXiv / URL: arXiv:2406.10395 (v3 2024-11-07) ; https://github.com/lab-smile/BrainSegFounder
- Access: open preprint (also NSF PAR accepted manuscript)
- Passes: 2/3 (arXiv abs; arXiv HTML v3 read for methods/data/results/limitations; NSF PAR for venue, 2026-10-16). OpenAlex lookup rate-limited, so the DOI is not confirmed.
- Modality & anatomy: brain MRI (T1w, T2-FLAIR, plus T1-ce and T2w downstream)
- Data: Stage 1 used UK Biobank, 41,400 participants / 82,800 volumes (T1w + T2-FLAIR). Downstream: BraTS 1,251 subjects (4 sequences, 5-fold CV) and ATLAS v2.0 655 T1 MRIs.
- Method: SwinUNETR encoder (Tiny/Small/Big = 19.1/21.0/26.6M encoder parameters; 62/64/69M total). Stage 1 SSL (masked inpainting + 3D rotation + contrastive, following Tang et al.) on healthy brains with 96^3 crops, 3-6 days on 8-64 A100-80GB. Stage 2 runs SSL on the target dataset, then fine-tuning with a UNet decoder. New MRI channels are added with Kaiming initialisation.
- Key results: BraTS 5-fold mean Dice 0.9115 (Small) vs nnU-Net 0.908, SegResNet 0.907, SwinUNETR 0.897. Stage-1-only reaches 0.9110. T1w-only BraTS: 0.721 vs SwinUNETR 0.678. ATLAS v2.0 Dice 0.712, lesion-wise F1 0.711 (top-3 on the training-set leaderboard). More label-efficient at 5-40% of training data (exact values in the supplement).
- Code / weights / license: code and pretrained weights on GitHub; licence not stated in the paper (unverified).
- Useful for us: template for two-stage SSL (normal anatomy at scale, then target pathology), which matches our "deviation from normal" goal for spine MRI. The modality-restricted result supports handling missing sequences.
- Limitations / notes: brain only. Small margins over nnU-Net (~0.007 Dice), and Stage 2 adds little on BraTS. The Big model is worse than Small. ATLAS comparison is not cross-validated. The paper has internal hyper-parameter inconsistencies between text and tables.
- BibTeX:
```bibtex
@article{Cox2024BrainSegFounder,
  title   = {{BrainSegFounder}: Towards {3D} Foundation Models for Neuroimage Segmentation},
  author  = {Cox, Joseph and Liu, Peng and Stolte, Skylar E. and Yang, Yunchao and Liu, Kang and See, Kyle B. and Ju, Huiwen and Fang, Ruogu},
  journal = {Medical Image Analysis},
  year    = {2024},
  note    = {volume/article number to be confirmed},
  eprint  = {2406.10395},
  archivePrefix = {arXiv}
}
```

### R182. MRSegmentator
- Full title: (journal) Segmenting Whole-Body MRI and CT for Multiorgan Anatomic Structure Delineation ; (preprint) MRSegmentator: Multi-Modality Segmentation of 40 Classes in MRI and CT
- Authors: Hartmut Häntze, Lina Xu, Christian J. Mertens, Felix J. Dorfner, Leonhard Donle, Felix Busch, Avan Kader, Sebastian Ziegelmayer, Nadine Bayerl, Nassir Navab, et al. (32 authors; Keno K. Bressem senior) (Charité Berlin and others)
- Year / Venue / Type: 2025 (published 2025-08-06) / Radiology: Artificial Intelligence 7(6):e240777 / journal (arXiv v1 2024-05-10, v3 2024-11-14)
- DOI / arXiv / URL: 10.1148/ryai.240777 (confirmed via arXiv + OpenAlex) ; arXiv:2405.06463 ; https://github.com/hhaentze/MRSegmentator
- Access: open (hybrid OA, CC BY 4.0)
- Passes: 2/3 (arXiv abstract; OpenAlex journal record; GitHub README for classes/licence, 2026-10-16). Full text was not read. CORRECTION: the memory entry said "journal version unverified"; it is RyAI 2025, and the journal title differs from the preprint title.
- Modality & anatomy: MRI (multiple sequences) + CT; 40 classes. Spine is a SINGLE "spine" class (no per-vertebra labels); sacrum is separate.
- Data: training used 1,200 manually annotated UK Biobank axial MRIs, 221 in-house MRIs and 1,228 TotalSegmentator CTs. Evaluation on NAKO (n=900), AMOS22 (n=60) and TotalSegmentator-MRI test (n=29).
- Method: nnU-Net; human-in-the-loop annotation starting from CT-to-MRI transfer, refined by manual corrections.
- Key results: DSC lungs 0.96, heart 0.94, liver 0.96, kidneys 0.95; small structures lower (portal/splenic veins 0.64, adrenals 0.69). NAKO mean DSC from 0.85 (T2-HASTE) to 0.91 (in-phase). AMOS CT 0.84.
- Code / weights / license: code Apache-2.0; weights licence not stated separately; memory-heavy (split_level option; CPU mode available).
- Useful for us: evidence that a single model handles CT and multiple MRI sequences; CT-to-MRI transfer plus human-in-the-loop is a cheap annotation recipe for spine MRI. Too coarse for vertebra-level work.
- Limitations / notes: spine not level-resolved; small vessels/glands weak.
- BibTeX:
```bibtex
@article{Haentze2025MRSegmentator,
  title   = {Segmenting Whole-Body {MRI} and {CT} for Multiorgan Anatomic Structure Delineation},
  author  = {H{\"a}ntze, Hartmut and Xu, Lina and Mertens, Christian J. and Dorfner, Felix J. and Donle, Leonhard and Busch, Felix and Kader, Avan and Ziegelmayer, Sebastian and Bayerl, Nadine and Navab, Nassir and others},
  journal = {Radiology: Artificial Intelligence},
  volume  = {7},
  number  = {6},
  pages   = {e240777},
  year    = {2025},
  doi     = {10.1148/ryai.240777},
  eprint  = {2405.06463},
  archivePrefix = {arXiv}
}
```

### R183. SynthSeg (contrast-agnostic domain randomisation)
- Full title: SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining
- Authors: Benjamin Billot, Douglas N. Greve, Oula Puonti, Axel Thielscher, Koen Van Leemput, Bruce Fischl, Adrian V. Dalca, Juan Eugenio Iglesias
- Year / Venue / Type: 2023 / Medical Image Analysis 86:102789 / journal (arXiv v1 2021-07-20, v4 2023-02-28)
- DOI / arXiv / URL: 10.1016/j.media.2023.102789 (confirmed in the arXiv DOI field) ; arXiv:2107.09559 ; https://github.com/BBillot/SynthSeg
- Access: open (preprint)
- Passes: 3/3 (arXiv abs; full PDF methods/results; PDF limitations/code, 2026-10-16). Volume/article number 86:102789 is from memory and consistent with the DOI, but was not shown on a fetched page.
- Modality & anatomy: brain MRI (any contrast) and CT; extension to cardiac MR/CT
- Data: no real images used for training. Label maps: 20 manual (T1-39) + 500 automated HCP + 500 automated ADNI. Evaluated on 5,000 scans across six modalities and ten resolutions.
- Method: on-the-fly generative model. Random affine + diffeomorphic deformation of label maps; GMM intensities with uniformly random per-label means/SDs; bias field + gamma; random slice thickness/spacing blur-downsample-resample to 1 mm; random acquisition direction; random removal of extra-cerebral labels; lesion pasting. 3D U-Net with 5 levels and 24 base features, soft Dice loss, 300k steps (~7 days on 1 GPU). Inference with test-time flip averaging and largest-connected-component post-processing.
- Key results: in-domain T1 Dice 0.88 (supervised/nnU-Net 0.91, SAMSEG 0.85). Best mean Dice on all 9 target domains: CT 3 mm 0.76 vs SAMSEG 0.71; FLAIR 5 mm 0.78 vs 0.64. Loses ~3.8 Dice points from 1 mm to 7 mm spacing (SAMSEG ~7.6). Cardiac MR 0.84, CT 0.88.
- Code / weights / license: GitHub + FreeSurfer distribution; licence not stated in the paper (check repo/FreeSurfer terms).
- Useful for us: key technique for one spine segmenter that works on T1/T2/STIR/CT and thick-slice clinical MRI without per-sequence labels, by synthesising images from vertebra/disc/cord label maps (e.g. VerSe/SPIDER labels). The cardiac result shows it transfers beyond the brain.
- Limitations / notes: needs label maps covering all tissues in the field of view (background structures in spine scans!). Thin structures degrade. Much evaluation ground truth is automated.
- BibTeX:
```bibtex
@article{Billot2023SynthSeg,
  title   = {{SynthSeg}: Segmentation of brain {MRI} scans of any contrast and resolution without retraining},
  author  = {Billot, Benjamin and Greve, Douglas N. and Puonti, Oula and Thielscher, Axel and Van Leemput, Koen and Fischl, Bruce and Dalca, Adrian V. and Iglesias, Juan Eugenio},
  journal = {Medical Image Analysis},
  volume  = {86},
  pages   = {102789},
  year    = {2023},
  doi     = {10.1016/j.media.2023.102789},
  eprint  = {2107.09559},
  archivePrefix = {arXiv}
}
```

#### G. Efficient architectures and compression for edge deployment

### R184. MobileNetV2
- Full title: MobileNetV2: Inverted Residuals and Linear Bottlenecks
- Authors: Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, Liang-Chieh Chen
- Year / Venue / Type: 2018 / CVPR 2018, pp. 4510-4520 (confirmed via the CVF open-access page) / conference
- DOI / arXiv / URL: arXiv:1801.04381 (v4 2019-03-21) ; https://openaccess.thecvf.com/content_cvpr_2018/html/Sandler_MobileNetV2_Inverted_Residuals_CVPR_2018_paper.html
- Access: open
- Passes: 2/3 (arXiv abs; full PDF results/limitations; CVF page for pages, 2026-10-16)
- Modality & anatomy: natural images
- Data: ImageNet, COCO, PASCAL VOC 2012
- Method: inverted residual blocks with linear bottlenecks and depthwise separable convolutions; expansion factor 6.
- Key results: ImageNet top-1 72.0% at 300M MAdds / 3.4M params (width 1.0, 224 px). Width 1.4: 74.7% at 585M MAdds / 6.9M params. Pixel-1 single-core TF-Lite latency 75 ms. SSDLite COCO 22.1 mAP (4.3M params, 0.8B MAdds). Mobile DeepLabv3 VOC 75.32% mIoU.
- Code / weights / license: TF/torchvision implementations (licences from memory: Apache-2.0/BSD; not re-checked).
- Useful for us: X-ray classifier/segmenter backbone for mobile/edge (Mobile DeepLabv3 head for radiograph vertebra segmentation).
- Limitations / notes: memory-splitting trade-offs; natural images only.
- BibTeX:
```bibtex
@inproceedings{Sandler2018MobileNetV2,
  title     = {{MobileNetV2}: Inverted Residuals and Linear Bottlenecks},
  author    = {Sandler, Mark and Howard, Andrew and Zhu, Menglong and Zhmoginov, Andrey and Chen, Liang-Chieh},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {4510--4520},
  year      = {2018},
  eprint    = {1801.04381},
  archivePrefix = {arXiv}
}
```

### R185. EfficientNet
- Full title: EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
- Authors: Mingxing Tan, Quoc V. Le
- Year / Venue / Type: 2019 / ICML 2019, PMLR 97:6105-6114 (confirmed via the PMLR page) / conference
- DOI / arXiv / URL: arXiv:1905.11946 (v5 2020-09-11) ; https://proceedings.mlr.press/v97/tan19a.html
- Access: open
- Passes: 2/3 (arXiv abstract with numbers; PMLR record, 2026-10-16). Full text was not re-read.
- Modality & anatomy: natural images
- Data: ImageNet; transfer to CIFAR-100, Flowers and others
- Method: compound scaling of depth/width/resolution from a NAS-designed baseline B0.
- Key results: B7 84.3% ImageNet top-1, 8.4x smaller and 6.1x faster than the best prior ConvNet. Transfer: CIFAR-100 91.7%, Flowers 98.8%, SOTA on 5 of 8 transfer sets (confirmed from the abstract).
- Code / weights / license: Apache-2.0 (TF repo; from memory, not re-checked).
- Useful for us: widely used in RSNA spine Kaggle solutions (2D slice classifiers); scalable family for the accuracy/latency trade-off.
- Limitations / notes: -
- BibTeX:
```bibtex
@inproceedings{Tan2019EfficientNet,
  title     = {{EfficientNet}: Rethinking Model Scaling for Convolutional Neural Networks},
  author    = {Tan, Mingxing and Le, Quoc V.},
  booktitle = {Proceedings of the 36th International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {97},
  pages     = {6105--6114},
  publisher = {PMLR},
  year      = {2019},
  eprint    = {1905.11946},
  archivePrefix = {arXiv}
}
```

### R186. EfficientViT
- Full title: EfficientViT: Multi-Scale Linear Attention for High-Resolution Dense Prediction
- Authors: Han Cai, Junyan Li, Muyan Hu, Chuang Gan, Song Han (MIT)
- Year / Venue / Type: 2023 / ICCV 2023 (venue confirmed by the official repo README) / conference
- DOI / arXiv / URL: arXiv:2205.14756 (v6 2024-02-06) ; https://github.com/mit-han-lab/efficientvit ; EfficientViT-SAM: arXiv:2402.05008 (Zhang, Cai, Han 2024, CVPR 2024 eLVM workshop)
- Access: open
- Passes: 2/3 (arXiv abstract with numbers; GitHub README for licence/families/medical use, 2026-10-16). Full text was not read; ICCV pages not confirmed.
- Modality & anatomy: natural images (segmentation, super-resolution, SAM)
- Data: Cityscapes, ADE20K, ImageNet, COCO
- Method: ReLU linear attention with multi-scale tokens built from hardware-friendly operations; global receptive field without softmax attention or large kernels.
- Key results: Cityscapes GPU latency up to 13.9x lower than SegFormer and 6.2x lower than SegNeXt at no loss of performance. SR up to 6.4x faster than Restormer (+0.11 dB). EfficientViT-SAM: 48.9x A100 TensorRT throughput vs SAM-ViT-H, with slightly better COCO zero-shot instance segmentation.
- Code / weights / license: code Apache-2.0 (weights licence not stated). The repo is no longer maintained (moved to DC-Gen). MedficientSAM (built on EfficientViT-SAM) won the CVPR 2024 "Segment Anything in Medical Images on Laptop" challenge.
- Useful for us: high-resolution dense prediction (vertebra segmentation on radiographs) on edge; EfficientViT-SAM / MedficientSAM as fast promptable segmenters with a medical track record.
- Limitations / notes: unmaintained codebase.
- BibTeX:
```bibtex
@inproceedings{Cai2023EfficientViT,
  title     = {{EfficientViT}: Multi-Scale Linear Attention for High-Resolution Dense Prediction},
  author    = {Cai, Han and Li, Junyan and Hu, Muyan and Gan, Chuang and Han, Song},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  year      = {2023},
  eprint    = {2205.14756},
  archivePrefix = {arXiv}
}
```

### R187. Knowledge distillation
- Full title: Distilling the Knowledge in a Neural Network
- Authors: Geoffrey Hinton, Oriol Vinyals, Jeff Dean
- Year / Venue / Type: 2015 (arXiv 2015-03-09) / arXiv preprint. The commonly cited venue "NIPS 2014 Deep Learning Workshop" is NOT shown on the arXiv record (unverified).
- DOI / arXiv / URL: arXiv:1503.02531
- Access: open
- Passes: 3/3 (arXiv abstract; full PDF read 2026-10-16 for method/experiments, then limitations). The PDF names no venue, so the NIPS 2014 Deep Learning Workshop venue remains unverified.
- Modality & anatomy: general
- Data: MNIST; Google's proprietary speech acoustic model; internal JFT (100M images, 15k labels) for specialist ensembles
- Method: student trained on a weighted sum of cross-entropy to the teacher's softmax at temperature T (softmax(z/T)) and to hard labels at T=1. A much lower weight on the hard term worked best. Soft-target gradients are scaled by T^2. Logit matching is the high-T limit. Also introduces generalist + fast-trainable specialist ensembles for confusable classes.
- Key results: MNIST: teacher 67 errors, small net 146, distilled (T=20) 74. With all 3s omitted from the transfer set, 206 errors, or 109 after bias correction (tuned on test). Speech: baseline frame accuracy 58.9% / WER 10.9%; 10x ensemble 61.1% / 10.7%; distilled single model 60.8% / 10.7% (>80% of the ensemble gain). Soft targets as regulariser: with 3% of data, 57.0% vs 44.5% with hard labels. JFT: 61 specialists improve top-1 from 25.0% to 26.1%.
- Code / weights / license: n/a
- Useful for us: distil a 3D foundation-model teacher (nnFoundation/Merlin/DINOv3) into an edge student. DINOv2/v3 use distillation to produce their small models.
- Limitations / notes: proprietary speech/JFT data (not reproducible); T and loss weights chosen empirically; specialists not distilled back into one model; some results tuned on the test set. For us: soft targets help most when student labelled data are scarce (3%-data result), which fits our label-scarce spine setting.
- BibTeX:
```bibtex
@misc{Hinton2015Distilling,
  title         = {Distilling the Knowledge in a Neural Network},
  author        = {Hinton, Geoffrey and Vinyals, Oriol and Dean, Jeff},
  year          = {2015},
  eprint        = {1503.02531},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML}
}
```

### R188. Integer quantisation
- Full title: Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference
- Authors: Benoit Jacob, Skirmantas Kligys, Bo Chen, Menglong Zhu, Matthew Tang, Andrew Howard, Hartwig Adam, Dmitry Kalenichenko (Google)
- Year / Venue / Type: 2018 / CVPR 2018, pp. 2704-2713 (confirmed via the CVF open-access page) / conference
- DOI / arXiv / URL: arXiv:1712.05877 ; https://openaccess.thecvf.com/content_cvpr_2018/html/Jacob_Quantization_and_Training_CVPR_2018_paper.html
- Access: open
- Passes: 3/3 (arXiv abs; full PDF methods/results; PDF limitations + CVF pages, 2026-10-16)
- Modality & anatomy: general
- Data: ImageNet, COCO, face detection/attributes
- Method: affine quantisation r = S(q - Z) with uint8 weights/activations and int32 bias/accumulators; fixed-point rescaling multiplier. Quantisation-aware training with simulated (fake) quantisation in the forward pass; EMA activation ranges; activation quantisation delayed 50K-2M steps; batch norm folded into weights.
- Key results: ResNet-50 ImageNet 76.4% float vs 74.9% int8. Inception-v3 78.4% vs 75.4% (ReLU6 degrades less than ReLU). Integer MobileNets are ~10% more accurate than float MobileNets at the same 33 ms budget on Snapdragon 835 LITTLE cores. MobileNet-SSD COCO mAP 22.1 to 21.7 with latency 370 to 272 ms (big core). Face detection ~2x faster for ~2% AP.
- Code / weights / license: implemented in TensorFlow Lite.
- Useful for us: INT8 QAT recipe for deploying spine segmenters on CPU/edge (use ReLU6/bounded activations, fold BN). Pairs with QLoRA (4-bit NF4) used in FM-01 on the LLM side.
- Limitations / notes: gains are hardware dependent. 4-bit weights drop sharply (-11 to -14%); 7-bit is close to 8-bit. Concatenation/addition need matched or rescaled quantisation parameters. Evaluated on ARM CPUs only.
- BibTeX:
```bibtex
@inproceedings{Jacob2018Quantization,
  title     = {Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference},
  author    = {Jacob, Benoit and Kligys, Skirmantas and Chen, Bo and Zhu, Menglong and Tang, Matthew and Howard, Andrew and Adam, Hartwig and Kalenichenko, Dmitry},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {2704--2713},
  year      = {2018},
  eprint    = {1712.05877},
  archivePrefix = {arXiv}
}
```

---

## 05. Uncertainty, image quality, abstention and normative anatomy

#### Part A. Knowing when to abstain

### R189. MC dropout as Bayesian approximation
- Full title: Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning
- Authors: Yarin Gal, Zoubin Ghahramani
- Year / Venue / Type: 2016 / ICML 2016 (PMLR 48) / conference
- DOI / arXiv / URL: arXiv:1506.02142; https://arxiv.org/abs/1506.02142
- Access: open (preprint + PMLR)
- Passes: 2/3 (abstract, method sections via ar5iv; experimental tables not extracted)
- Modality & anatomy: general (MNIST, UCI regression, RL)
- Data: MNIST, UCI regression benchmarks
- Method: Dropout before every weight layer interpreted as variational inference in a deep Gaussian process; keep dropout on at test time and average T stochastic forward passes (MC dropout); predictive variance = model (epistemic) uncertainty.
- Key results: reported "considerable improvement in predictive log-likelihood and RMSE" over VI and probabilistic backprop baselines on UCI (exact numbers not re-extracted; see paper tables).
- Code / weights / license: author code linked from paper (Theano/Keras era); trivially implemented in any framework.
- Useful for us: cheapest epistemic-uncertainty baseline for our segmentation/classification heads (no extra training). Cite as origin of MC dropout.
- Limitations / notes: approximation only; quality depends on dropout rate and placement; Jungo & Reyes and Mehrtash et al. show MC dropout is worse calibrated than ensembles in medical segmentation, and heavy dropout degrades segmentation.
- BibTeX:
```bibtex
@inproceedings{Gal2016Dropout,
  title     = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
  author    = {Gal, Yarin and Ghahramani, Zoubin},
  booktitle = {Proceedings of the 33rd International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {48},
  pages     = {1050--1059},
  year      = {2016},
  eprint    = {1506.02142},
  archivePrefix = {arXiv}
}
```

### R190. Deep ensembles
- Full title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles
- Authors: Balaji Lakshminarayanan, Alexander Pritzel, Charles Blundell
- Year / Venue / Type: 2017 / NeurIPS (NIPS) 2017 / conference
- DOI / arXiv / URL: arXiv:1612.01474; https://proceedings.neurips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html
- Access: open
- Passes: 3/3 (ar5iv full text; classification/OOD tables partially truncated in extraction)
- Modality & anatomy: general (toy regression, UCI, MNIST/SVHN, ImageNet)
- Data: UCI regression (Boston, Concrete, Energy, Kin8nm, Naval, Power, Protein, Wine, Year MSD), MNIST, SVHN, ImageNet
- Method: M (default 5) independently randomly initialised networks trained on full data with proper scoring rules (NLL / Brier), optional adversarial training (FGSM, eps = 1% input range); regression heads predict mean+variance (heteroscedastic Gaussian); predictions averaged as uniform mixture. Bagging hurt performance.
- Key results: best NLL on several UCI datasets (e.g. Energy 1.38, Kin8nm -1.20, Naval -5.63, Power 2.79); MC dropout sometimes better RMSE (Energy 1.66 vs 2.09). Higher uncertainty on OOD inputs; scales to ImageNet.
- Code / weights / license: no official code; many reimplementations (e.g. github.com/dougbrion/pytorch-deep-ensembles).
- Useful for us: strongest practical uncertainty baseline in medical segmentation benchmarks (Mehrtash 2020, Jungo 2019, Zenk 2025). nnU-Net's 5-fold cross-validation models give a free 5-member ensemble for our spine segmentation.
- Limitations / notes: M x training and inference cost; diversity relies on random init only.
- BibTeX:
```bibtex
@inproceedings{Lakshminarayanan2017DeepEnsembles,
  title     = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
  author    = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
  booktitle = {Advances in Neural Information Processing Systems 30 (NeurIPS)},
  pages     = {6402--6413},
  year      = {2017},
  eprint    = {1612.01474},
  archivePrefix = {arXiv}
}
```

### R191. Test-time augmentation for aleatoric uncertainty in medical segmentation
- Full title: Aleatoric uncertainty estimation with test-time augmentation for medical image segmentation with convolutional neural networks
- Authors: Guotai Wang, Wenqi Li, Michael Aertsen, et al. (Deprest, Ourselin, Vercauteren)
- Year / Venue / Type: 2019 / Neurocomputing 335:34-45 / journal
- DOI / arXiv / URL: 10.1016/j.neucom.2019.01.103; arXiv:1807.07356; PMCID PMC6783308; PMID 31595105
- Access: open (CC BY author manuscript)
- Passes: 3/3 full text
- Modality & anatomy: MRI; fetal brain (2D) and brain tumour (3D)
- Data: in-house fetal brain T2 SSFSE, 60 fetuses (train 2640 slices/40 pts; val 278/4; test 1180/16); BraTS 2017 (285 studies; 215/20/50 split), whole tumour
- Method: formulates TTA as Monte Carlo sampling over priors on transformation (flips p=0.5, rotation U(0,2pi), scale U(0.8,1.2)) and Gaussian noise N(0,0.05); N=20 (2D) / 40 (3D) samples; majority vote prediction, entropy as uncertainty; compared with test-time dropout (p=0.5); networks FCN, U-Net, P-Net, 3D U-Net, V-Net, W-Net (NiftyNet).
- Key results: TTA improved Dice, e.g. fetal U-Net 91.93 -> 92.88; 3D W-Net 88.76 -> 90.07 (ASSD 1.61 -> 1.13 mm). TTA uncertainty identified errors better than dropout uncertainty, which produced overconfident wrong predictions.
- Code / weights / license: no repo given in paper; implemented in NiftyNet.
- Useful for us: TTA is a cheap, model-agnostic way to get per-voxel and per-vertebra uncertainty on spine MRI/CT; directly reusable recipe (transform priors, N=20-40). Aleatoric uncertainty from TTA relates to image quality, which matches our "request better scan" goal.
- Limitations / notes: only spatial + Gaussian noise transforms; N-fold inference cost; single dataset per dimension; private 2D data.
- BibTeX:
```bibtex
@article{Wang2019TTA,
  title   = {Aleatoric uncertainty estimation with test-time augmentation for medical image segmentation with convolutional neural networks},
  author  = {Wang, Guotai and Li, Wenqi and Aertsen, Michael and Deprest, Jan and Ourselin, S{\'e}bastien and Vercauteren, Tom},
  journal = {Neurocomputing},
  volume  = {335},
  pages   = {34--45},
  year    = {2019},
  doi     = {10.1016/j.neucom.2019.01.103}
}
```

### R192. Evidential deep learning
- Full title: Evidential Deep Learning to Quantify Classification Uncertainty
- Authors: Murat Sensoy, Lance Kaplan, Melih Kandemir
- Year / Venue / Type: 2018 / NeurIPS 2018 / conference
- DOI / arXiv / URL: arXiv:1806.01768; https://proceedings.neurips.cc/paper/2018/hash/a981f2b708044d6fb4a71a1463242520-Abstract.html
- Access: open
- Passes: 2/3 (abstract + method via ar5iv; quantitative tables truncated)
- Modality & anatomy: general (MNIST, CIFAR)
- Data: MNIST (rotated-digit experiment, LeNet), CIFAR-type benchmarks (not fully extracted)
- Method: replace softmax with Dirichlet; non-negative evidence e, alpha = e+1; subjective-logic belief b_k = e_k/S and uncertainty u = K/S; sum-of-squares Bayes risk loss + KL regulariser toward uniform Dirichlet (annealed).
- Key results: uncertainty rises for rotated digits beyond ~50 deg while softmax stays confident; closer to max-entropy on OOD than BNN baselines; more robust to adversarial perturbations (numbers in paper tables; not re-extracted).
- Code / weights / license: community implementations; none verified as official.
- Useful for us: single-pass uncertainty (no sampling) for classification heads such as Pfirrmann grade, stenosis grade, fracture/no-fracture; gives explicit "I don't know" mass u usable for abstention.
- Limitations / notes: later work questions whether evidential uncertainties are faithful (not reviewed here); loss choice heuristic.
- BibTeX:
```bibtex
@inproceedings{Sensoy2018Evidential,
  title     = {Evidential Deep Learning to Quantify Classification Uncertainty},
  author    = {Sensoy, Murat and Kaplan, Lance and Kandemir, Melih},
  booktitle = {Advances in Neural Information Processing Systems 31 (NeurIPS)},
  year      = {2018},
  eprint    = {1806.01768},
  archivePrefix = {arXiv}
}
```

### R193. Aleatoric vs epistemic uncertainty in Bayesian deep learning for vision
- Full title: What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?
- Authors: Alex Kendall, Yarin Gal
- Year / Venue / Type: 2017 / NeurIPS (NIPS) 2017 / conference (venue from proceedings listing; arXiv page carries no journal-ref)
- DOI / arXiv / URL: arXiv:1703.04977
- Access: open
- Passes: 2/3 (abstract + method via ar5iv; result tables not rendered)
- Modality & anatomy: natural images (semantic segmentation, depth regression)
- Data: CamVid (367 train / 233 test, 11 classes), NYUv2, Make3D
- Method: heteroscedastic aleatoric uncertainty via predicted variance ("learned attenuation" loss; for classification, Gaussian noise on logits sampled by MC); epistemic via MC dropout (p=0.2, 50 samples); DenseNet-based dense predictor.
- Key results: 1-3% improvement over non-Bayesian baselines (as stated); aleatoric uncertainty peaks at object boundaries and distant objects, epistemic on unfamiliar content; aleatoric alone cannot detect out-of-data examples.
- Code / weights / license: none official verified.
- Useful for us: conceptual basis for separating "scan is noisy/ambiguous" (aleatoric, suggests better scan) from "model has not seen this" (epistemic, suggests referral) in our abstention logic.
- Limitations / notes: large-data regime argument (epistemic explained away) may not hold for small spine datasets.
- BibTeX:
```bibtex
@inproceedings{Kendall2017Uncertainties,
  title     = {What Uncertainties Do We Need in {B}ayesian Deep Learning for Computer Vision?},
  author    = {Kendall, Alex and Gal, Yarin},
  booktitle = {Advances in Neural Information Processing Systems 30 (NeurIPS)},
  year      = {2017},
  eprint    = {1703.04977},
  archivePrefix = {arXiv}
}
```

### R194. Uncertainty-based referral in medical diagnosis (diabetic retinopathy)
- Full title: Leveraging uncertainty information from deep neural networks for disease detection
- Authors: Christian Leibig, Vaneeda Allken, Murat Seckin Ayhan, et al. (Berens, Wahl)
- Year / Venue / Type: 2017 / Scientific Reports 7:17816 / journal
- DOI / arXiv / URL: 10.1038/s41598-017-17876-z; PMID 29259224; PMC5736701
- Access: open
- Passes: 2/3 (metadata via Crossref/Semantic Scholar plus the abstract; Nature full-text HTML read 2026-10-16 for data, method, referral results and limitations. Table 1 AUCs and the number of MC samples were not in the extracted text.)
- Modality & anatomy: colour fundus photography; retina
- Data: Kaggle DR, 35,126 train (split 80/20 into train/validation) and 53,576 test images, grades 0-4, about 73% with no DR. Messidor, 1,200 images, external test only. Two binary tasks: onset 1 (mild DR or worse) and onset 2 (moderate DR or worse).
- Method: Bayesian CNN (VGG-like, monocular, dropout p = 0.2 after each conv) and the public JFnet (Kaggle winner, p = 0.5 in FC layers) with MC dropout. Prediction = predictive mean; uncertainty = predictive SD (entropy of the mean performed comparably). Cases above an uncertainty threshold are referred. Cost is about 200 ms per image.
- Key results:
  - Referring the 20% most uncertain cases gave >= 90% accuracy on retained cases, against about 87% for random referral.
  - On Kaggle, the NHS (85% sensitivity / 80% specificity) and BDA (80% / 95%) targets were met after referring about 0-30% of cases, depending on task and network.
  - On Messidor both targets were met with no referral.
  - Plain softmax with standard dropout was worse than random referral for mild DR at up to about 30% referral (miscalibration).
  - A GP on penultimate features underperformed MC dropout, and seeded-network ensembling gave only marginal gains.
- Code / weights / license: no release of the authors' BCNN is mentioned. JFnet is at github.com/JeffreyDF/kaggle_diabetic_retinopathy (third-party).
- Useful for us: early clinical demonstration of "refer when uncertain" with accuracy-vs-referral-rate curves; template for our referral-rate analysis.
- Limitations / notes: Crossref lists article number 17816 (DOI suffix 17876). Classification only. Kaggle labels are noisy and about 10% of images are ungradable, with unknown overlap with the uncertain set. Uncertainty did not cleanly flag OOD (ImageNet) images; autoencoder reconstruction error did better. This argues for a separate OOD/IQA gate alongside the uncertainty-based referral.
- BibTeX:
```bibtex
@article{Leibig2017Uncertainty,
  title   = {Leveraging uncertainty information from deep neural networks for disease detection},
  author  = {Leibig, Christian and Allken, Vaneeda and Ay{\c{h}}an, Murat Se{\c{c}}kin and Berens, Philipp and Wahl, Siegfried},
  journal = {Scientific Reports},
  volume  = {7},
  number  = {1},
  pages   = {17816},
  year    = {2017},
  doi     = {10.1038/s41598-017-17876-z}
}
```

### R195. Communicating uncertainty in medical ML (perspective)
- Full title: Second opinion needed: communicating uncertainty in medical machine learning
- Authors: Benjamin Kompa, Jasper Snoek, Andrew L. Beam
- Year / Venue / Type: 2021 / npj Digital Medicine 4:4 (article number confirmed on the Nature page) / perspective
- DOI / arXiv / URL: 10.1038/s41746-020-00367-3; PMID 33402680; PMC7785732
- Access: open
- Passes: 3/3 (abstract; Nature full text read 2026-10-16 section by section, then the abstention section and open problems re-read; see also [C17] in file 06)
- Modality & anatomy: general medical ML
- Data: n/a (review)
- Method: reviews uncertainty quantification and abstention methods; argues models must be able to say "I don't know".
- Key results (full text): four widely cited medical ML models lack abstention and per-sample calibration. Taxonomy: aleatoric, epistemic and dataset shift (covariate and label). Methods reviewed: prediction intervals, conformal inference (marginal coverage only, not shift-robust by default), MC dropout and ensembles (best under shift per Ovadia et al.), Bayesian/VI (VI underestimates), GPs, calibration with proper scoring rules. Routes to abstention: empty conformal set, cost-based selective prediction, bounded selective prediction with a rejection function, SelectiveNet, Deep Gamblers, learning to defer. Abstention should trigger human review, not hide the output. Examples: bootstrap heart-risk SD 7.6% vs 15.3%, with the second patient flagged; situs inversus on MRI as OOD; hospital-to-hospital shift. Recommends reporting calibration and sample-level uncertainty and making uncertainty a required part of clinical integration.
- Code / weights / license: n/a
- Useful for us: citation for the clinical motivation of our "ask for a better scan / defer" behaviour.
- Limitations / notes: no experiments; classification focus; no conditional coverage guarantees; conformal is not shift-robust by default.
- BibTeX:
```bibtex
@article{Kompa2021SecondOpinion,
  title   = {Second opinion needed: communicating uncertainty in medical machine learning},
  author  = {Kompa, Benjamin and Snoek, Jasper and Beam, Andrew L.},
  journal = {npj Digital Medicine},
  volume  = {4},
  pages   = {4},
  year    = {2021},
  doi     = {10.1038/s41746-020-00367-3},
  note    = {Article number unverified}
}
```
- Also relevant to: Reviews, reporting guidelines, validation and deployment

### R196. Uncertainty under dataset shift benchmark (Ovadia)
- Full title: Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift
- Authors: Yaniv Ovadia, Emily Fertig, Jie Ren, Zachary Nado, D. Sculley, Sebastian Nowozin, Joshua V. Dillon, Balaji Lakshminarayanan, Jasper Snoek
- Year / Venue / Type: 2019 / Advances in Neural Information Processing Systems 32 (NeurIPS 2019; venue as listed on arXiv) / conference
- DOI / arXiv / URL: arXiv:1906.02530 (v2, 17 Dec 2019)
- Access: open
- Passes: 3/3 (arXiv abs, then the v2 PDF on 2026-10-16 read for setup and findings, then for ensemble size, code and limitations; added in pass 2 from this file's gaps list)
- Modality & anatomy: general (no medical data): images, text, ad-click, genomics
- Data: MNIST (rotation, translation; NotMNIST OOD); CIFAR-10 with 16 corruptions x 5 intensities (SVHN OOD); ImageNet-C; 20 Newsgroups (LM1B OOD); Criteo (37M, feature reassignment); genomics (appendix)
- Method: compares vanilla softmax, temperature scaling, MC dropout, deep ensembles (M = 10), SVI, last-layer SVI and last-layer dropout. Metrics: accuracy, NLL, Brier (with decomposition), ECE, entropy and confidence histograms, accuracy-vs-confidence curves.
- Key results: uncertainty quality degrades with shift for every method. Good i.i.d. calibration does not transfer to shift. Temperature scaling is fine for small shifts but its ECE grows with shift. Deep ensembles are the most robust, with gains growing with shift, and about 5 members capture most of the benefit. Dropout beats temperature scaling and the last-layer methods, which are sometimes worse than vanilla. SVI is hard to scale. Higher-capacity single models do not match ensembles.
- Code / weights / license: github.com/google-research/google-research, tree/master/uq_benchmark_2019 (code and predictions; URL from the paper)
- Useful for us: the standard citation for evaluating our calibration under scanner and site shift (corrupted MRI and CT as 'shift intensities'), and the justification that a 5-model nnU-Net fold ensemble is enough. Calibrating only on in-distribution validation data is not enough.
- Limitations / notes: classification only, no medical images; compute cost is not part of the ranking; OOD-specific detectors with extra components were excluded.
- BibTeX:
```bibtex
@inproceedings{Ovadia2019DatasetShift,
  title     = {Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift},
  author    = {Ovadia, Yaniv and Fertig, Emily and Ren, Jie and Nado, Zachary and Sculley, D. and Nowozin, Sebastian and Dillon, Joshua V. and Lakshminarayanan, Balaji and Snoek, Jasper},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {32},
  year      = {2019},
  eprint    = {1906.02530},
  archivePrefix = {arXiv}
}
```

### R197. Probabilistic U-Net for ambiguous segmentation (Kohl)
- Full title: A Probabilistic U-Net for Segmentation of Ambiguous Images
- Authors: Simon A. A. Kohl, Bernardino Romera-Paredes, Clemens Meyer, Jeffrey De Fauw, Joseph R. Ledsam, Klaus H. Maier-Hein, S. M. Ali Eslami, Danilo Jimenez Rezende, Olaf Ronneberger
- Year / Venue / Type: 2018 / NeurIPS 2018 per common citation (not stated on the arXiv page or in the extracted PDF; verify) / conference
- DOI / arXiv / URL: arXiv:1806.05034 (v4, 29 Jan 2019)
- Access: open
- Passes: 3/3 (arXiv abs, then the v4 PDF on 2026-10-16 read for architecture, data and results, then for limitations and code; added in pass 2 from this file's gaps list)
- Modality & anatomy: chest CT lung lesions (LIDC-IDRI); Cityscapes with synthetic ambiguity
- Data: LIDC-IDRI, 1,018 CT scans from 1,010 patients, 4 of 12 radiologists' masks per lesion, patient split 722/144/144 (8,882/1,996/1,992 crops of 180x180). Cityscapes with 5 classes randomly flipped (32 modes).
- Method: U-Net plus conditional VAE. The prior net (image) and posterior net (image + mask) output axis-aligned Gaussians (latent dimension 6). The latent sample is concatenated to the last U-Net feature map and passed through 3 1x1 convs. Loss = cross-entropy + beta * KL (beta = 1). Baselines: dropout U-Net, U-Net ensemble, M-heads, Image2Image VAE.
- Key results: generalized energy distance D2_GED (d = 1 - IoU) for 1/4/8/16 samples is 0.811/0.388/0.321/0.287 on LIDC and 0.874/0.337/0.248/0.206 on Cityscapes, significantly better than baselines at 16 samples (Wilcoxon). Mode frequencies on Cityscapes are well calibrated.
- Code / weights / license: https://github.com/SimonKohl/probabilistic_unet (URL from the paper)
- Useful for us: models inter-rater ambiguity, for example disc herniation or stenosis boundaries that radiologists disagree on. D2_GED is the metric if we have multiple annotations, and sample diversity is an aleatoric-uncertainty signal for 'inconclusive'.
- Limitations / notes: needs multiple annotations per image; lesion-centred crops are not clinically end-to-end; the prior is sometimes under-conservative about lesion presence; mode-mixing samples appear. Baseline numbers are only in figures.
- BibTeX:
```bibtex
@inproceedings{Kohl2018ProbUNet,
  title     = {A Probabilistic {U-Net} for Segmentation of Ambiguous Images},
  author    = {Kohl, Simon A. A. and Romera-Paredes, Bernardino and Meyer, Clemens and De Fauw, Jeffrey and Ledsam, Joseph R. and Maier-Hein, Klaus H. and Eslami, S. M. Ali and Rezende, Danilo Jimenez and Ronneberger, Olaf},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {31},
  year      = {2018},
  eprint    = {1806.05034},
  archivePrefix = {arXiv},
  note      = {Venue per common citation; verify}
}
```

### R198. Calibration of modern neural networks / temperature scaling
- Full title: On Calibration of Modern Neural Networks
- Authors: Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger
- Year / Venue / Type: 2017 / ICML 2017 (PMLR 70) / conference
- DOI / arXiv / URL: arXiv:1706.04599
- Access: open
- Passes: 2/3 (abstract, definitions, analysis sections; result tables not re-extracted)
- Modality & anatomy: general (CIFAR-10/100, SVHN, ImageNet, text datasets)
- Data: image and document classification benchmarks
- Method: defines Expected Calibration Error (ECE: M equal-width confidence bins, weighted |acc - conf|) and reliability diagrams; compares histogram binning, isotonic regression, BBQ, matrix/vector scaling and temperature scaling (single scalar T dividing logits, fit by NLL on validation set).
- Key results: modern deep nets are overconfident; depth, width, BatchNorm and reduced weight decay increase miscalibration; NLL can overfit while accuracy improves; temperature scaling is "surprisingly effective" on most datasets.
- Code / weights / license: github.com/gpleiss/temperature_scaling (widely used; unverified license).
- Useful for us: post-hoc calibration of every classification output before thresholding for abstention; ECE/reliability diagrams as standard reporting in our paper.
- Limitations / notes: calibration under distribution shift is not guaranteed by temperature scaling; ECE is binning dependent.
- BibTeX:
```bibtex
@inproceedings{Guo2017Calibration,
  title     = {On Calibration of Modern Neural Networks},
  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {70},
  pages     = {1321--1330},
  year      = {2017},
  eprint    = {1706.04599},
  archivePrefix = {arXiv}
}
```

### R199. Calibration and uncertainty for deep medical image segmentation
- Full title: Confidence Calibration and Predictive Uncertainty Estimation for Deep Medical Image Segmentation
- Authors: Alireza Mehrtash, William M. Wells III, Clare M. Tempany, et al. (Abolmaesumi, Kapur)
- Year / Venue / Type: 2020 / IEEE Transactions on Medical Imaging 39(12):3868-3878 / journal
- DOI / arXiv / URL: 10.1109/TMI.2020.3006437 (verified via OpenAlex: TMI 39(12):3868-3878); arXiv:1911.13273; PMC7704933
- Access: open (arXiv, PMC)
- Passes: 3/3 full text (arXiv v2; re-read arXiv abs + v2 PDF Table II and limitations on 2026-10-16)
- Modality & anatomy: MRI; brain tumour, cardiac ventricles, prostate
- Data: BraTS 2017 (66 train/22 val CBICA; 102 test TCIA); ACDC (40/10/50, ED only); PROSTATEx (16/4/20) + PROMISE12 (35, OOD test)
- Method: 2D U-Net with BN; CE vs soft Dice loss; deep ensembles up to M=50 vs MC dropout (p=0.5, 50 samples); segment-level uncertainty = mean voxel entropy over predicted foreground; metrics NLL, Brier, ECE within bounding box.
- Key results (Table II, within bounding box, single -> 50-ensemble, NLL / ECE%): Brain CE 0.52/8.11 -> 0.29/3.28; Brain Dice 0.62/13.20 -> 0.31/3.71; Heart CE 0.36/5.75 -> 0.23/2.51; Prostate CE 0.40/8.08 -> 0.16/4.12; Prostate Dice 0.74/5.72 -> 0.15/2.02. Heart Dice-loss row is identical to Brain Dice row in the arXiv v2 table (apparent copy error; do not quote). M=5 already cut NLL ~44-66%. Text reports a strong correlation between logit(Dice) and mean segment entropy with 0.77 <= r <= 0.92 across tasks (CORRECTION: earlier entry gave negative signs, which are not in the text; per-task r only in Fig. 3). On PROMISE12 (target domain) poorly segmented cases flagged by high entropy were mostly endorectal-coil scans, i.e. OOD; no numeric OOD metric reported.
- Code / weights / license: none provided (confirmed: paper gives no repository; only public datasets for reproducibility).
- Useful for us: justifies (i) ensemble-based calibration of our segmentation, (ii) per-structure (per-vertebra/per-disc) mean entropy as a predicted-quality score for abstention.
- Limitations / notes (authors' own): 2D networks with fewer filters than original U-Net, limited tuning; MRI only (no CT); entropy metric assumes binary classes and ignores neighbourhood; ignores number of samples; segment-level approach called "an early attempt"; ensembles costly to train; rater disagreement not studied. Also small data; Heart Dice-loss row duplicates Brain row in Table II.
- BibTeX:
```bibtex
@article{Mehrtash2020Calibration,
  title   = {Confidence Calibration and Predictive Uncertainty Estimation for Deep Medical Image Segmentation},
  author  = {Mehrtash, Alireza and Wells, William M. and Tempany, Clare M. and Abolmaesumi, Purang and Kapur, Tina},
  journal = {IEEE Transactions on Medical Imaging},
  volume  = {39},
  number  = {12},
  pages   = {3868--3878},
  year    = {2020},
  doi     = {10.1109/TMI.2020.3006437},
  eprint  = {1911.13273},
  archivePrefix = {arXiv}
}
```

### R200. Reliability of uncertainty estimates in medical segmentation
- Full title: Assessing Reliability and Challenges of Uncertainty Estimations for Medical Image Segmentation
- Authors: Alain Jungo, Mauricio Reyes
- Year / Venue / Type: 2019 / MICCAI 2019, LNCS 11765, pp. 48-56 (chapter DOI below) / conference
- DOI / arXiv / URL: 10.1007/978-3-030-32245-8_6; arXiv:1907.03338
- Access: open (arXiv)
- Passes: 3/3 full text
- Modality & anatomy: brain tumour MRI (BraTS 2018), skin lesion dermoscopy (ISIC 2017)
- Data: BraTS 2018 265 subjects (100/25/160); ISIC 2017 (2000/150/600)
- Method: U-Net; compares softmax entropy, MC dropout (T=20, two placements), aleatoric (learned variance), ensemble of 10 (90% subsets), auxiliary networks (feature-based and separate error-predicting U-Net). Metrics: ECE (10 bins), uncertainty-error overlap (U-E Dice), correction benefit, Dice.
- Key results: well calibrated at dataset level but miscalibrated per subject (~28%/46% under-, 32%/18% overconfident for BraTS/ISIC); ensemble most reliable overall; aleatoric worst U-E (~0.05 vs ~0.43 baseline on BraTS); heavy dropout harms segmentation; subject-level aggregated uncertainty not yet reliable for failure flagging.
- Code / weights / license: https://github.com/alainjungo/reliability-challenges-uncertainty
- Useful for us: evaluation protocol (U-E overlap, subject-level calibration) for our per-vertebra uncertainty maps; warns that dataset-level ECE hides per-case miscalibration, which matters for per-study abstention.
- Limitations / notes: only large structures; uncertainty quality entangled with segmentation accuracy.
- BibTeX:
```bibtex
@inproceedings{Jungo2019Reliability,
  title     = {Assessing Reliability and Challenges of Uncertainty Estimations for Medical Image Segmentation},
  author    = {Jungo, Alain and Reyes, Mauricio},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2019},
  series    = {Lecture Notes in Computer Science},
  volume    = {11765},
  pages     = {48--56},
  publisher = {Springer},
  year      = {2019},
  doi       = {10.1007/978-3-030-32245-8_6},
  eprint    = {1907.03338},
  archivePrefix = {arXiv}
}
```

### R201. Benchmark of failure detection in medical segmentation
- Full title: Comparative benchmarking of failure detection methods in medical image segmentation: Unveiling the role of confidence aggregation
- Authors: Maximilian Zenk, David Zimmerer, Fabian Isensee, et al. (Traub, Norajitra, Jaeger, Maier-Hein)
- Year / Venue / Type: 2025 / Medical Image Analysis 101:103392 / journal
- DOI / arXiv / URL: 10.1016/j.media.2024.103392 (confirmed via DKFZ inrepo record 294922 BibTeX; online 30 Nov 2024); PMID 39657400; arXiv:2406.03323 (v1 5 Jun 2024, v2 24 Jun 2024)
- Access: open (arXiv)
- Passes: 3/3 full text (arXiv html v1; re-read arXiv abs + html v2 on 2026-10-16 to extract dataset table and caveats; per-dataset AURC values exist only in figures, not text)
- Modality & anatomy: MRI and CT; brain tumour (FeTS 2D, BraTS 2019), heart (M&Ms), prostate (MSD + multi-site), COVID lung lesions CT, kidney tumour (KiTS23)
- Data: five public 3D collections with realistic test-time shifts (unseen vendors/institutions, artificial corruptions: affine, bias field, spikes, ghosting). Table 2 (v2), train / test (ID first, then shifted subsets): Brain tumour 2D 939 / 313x5 (ID + 4 corruptions); Brain tumour 235 / 50, 50 (more low-grade); Heart 190 / 60, 190, 100, 100 (unseen vendors); Prostate 26 / 6, 30, 19, 13, 12, 12 (unseen institutions); Covid CT 160 / 39, 50, 20 (unseen institutions); Kidney tumour CT 367 / 122 (no shift, hard ID cases).
- Method: nnU-Net 3D models (25 per dataset: 5 seeds x 5 folds); pixel confidence (predictive entropy, MC dropout, ensembles) with aggregation (mean, non-boundary mean, patch-based, regression forests on radiomics or simple features); pairwise Dice (Roy 2019); image-level quality regression, Mahalanobis, VAE loss. Main metric AURC with risk = 1 - DSC (also NSD).
- Key results: ensemble + pairwise DSC best overall, often near-optimal AURC; MC dropout + pairwise DSC close second; AURC gap to naive mean-entropy baseline > 0.1 on kidney and COVID; Mahalanobis best for OOD detection but not failure detection.
- Code / weights / license: framework announced as public, but arXiv v2 still says "Link will be added upon acceptance"; no repository URL found in the arXiv, DKFZ repository record or web search on 2026-10-16 (unverified; do not cite a URL).
- Useful for us: adopt risk-coverage (AURC) as our headline abstention metric; pairwise Dice between nnU-Net fold models is a strong, free per-case failure score for spine segmentation; corruption types mirror MRI artefacts we want to detect.
- Limitations / notes: reimplementations with limited tuning; scores not calibrated; image-level only. Mean predictive entropy beats random ranking clearly only on Heart and Prostate; prostate training set tiny (21 train / 5 val), weakening trained aggregators; MC dropout used 5 (not 10) samples on Kidney for compute reasons; quality-regression target selection simple; no adversarial training in ensembles. Recommends treating failure detection separately from OOD detection.
- BibTeX:
```bibtex
@article{Zenk2025FailureDetection,
  title   = {Comparative benchmarking of failure detection methods in medical image segmentation: Unveiling the role of confidence aggregation},
  author  = {Zenk, Maximilian and Zimmerer, David and Isensee, Fabian and Traub, Jeremias and Norajitra, Tobias and J{\"a}ger, Paul F. and Maier-Hein, Klaus},
  journal = {Medical Image Analysis},
  volume  = {101},
  pages   = {103392},
  year    = {2025},
  doi     = {10.1016/j.media.2024.103392},
  eprint  = {2406.03323},
  archivePrefix = {arXiv}
}
```

### R202. Reverse classification accuracy (RCA)
- Full title: Reverse Classification Accuracy: Predicting Segmentation Performance in the Absence of Ground Truth
- Authors: Vanya V. Valindria, Ioannis Lavdas, Wenjia Bai, et al. (Kamnitsas, Aboagye, Rockall, Rueckert, Glocker)
- Year / Venue / Type: 2017 / IEEE Transactions on Medical Imaging 36(8):1597-1606 / journal
- DOI / arXiv / URL: 10.1109/TMI.2017.2665165 (verified via OpenAlex); arXiv:1702.03407
- Access: open (arXiv)
- Passes: 3/3 (abstract, then the arXiv PDF on 2026-10-16 read for data, method and Tables I-IV, then for limitations and code)
- Modality & anatomy: whole-body MRI (T1w Dixon and T2w), 15 structures including the spine (as one structure), pelvis and clavicles
- Data: MALIBO study, 35 healthy volunteers, 525 segmented structures; the reference database in the example is 24 images with ground truth; 3-fold CV
- Method: the predicted segmentation of a new image is used as a pseudo-label to train a 'reverse classifier', which is applied to reference images with ground truth; the best reference score predicts the quality of the new segmentation. Segmenters evaluated: random forests, DeepMedic 3D CNN, multi-atlas. Reverse classifiers: single-atlas registration, atlas forests, constrained CNN. Predicted metrics: DSC, Jaccard, precision, recall, RVD, ASD, HD.
- Key results (Table I, DSC prediction over 525 structures): single-atlas RCA is best, with correlation 0.955-0.973, MAE 0.051-0.067 and 3-class accuracy (<0.6 / 0.6-0.8 / >=0.8) 0.81-0.89. Atlas forests: r 0.83-0.88. Constrained CNN: r 0.72-0.77. On degraded random-forest segmentations, single-atlas gave r 0.875, MAE 0.097 and accuracy 0.928, but bladder failures were missed. Jaccard (r 0.90) is predicted well; ASD (r 0.02) and HD (r 0.19) are not.
- Code / weights / license: stated as available at biomedia.doc.ic.ac.uk/software/ (not visited)
- Useful for us: model-agnostic per-case QC for spine segmentations using a small atlas of annotated reference spines.
- Limitations / notes: needs a reference database and per-case training (compute time not reported); assumes the reference set covers the test anatomy. Healthy volunteers only, one protocol. Small structures (adrenal, clavicle) are poor, and distance metrics are unpredictable. The atlas-forest output needs calibration.
- BibTeX:
```bibtex
@article{Valindria2017RCA,
  title   = {Reverse Classification Accuracy: Predicting Segmentation Performance in the Absence of Ground Truth},
  author  = {Valindria, Vanya V. and Lavdas, Ioannis and Bai, Wenjia and Kamnitsas, Konstantinos and Aboagye, Eric O. and Rockall, Andrea G. and Rueckert, Daniel and Glocker, Ben},
  journal = {IEEE Transactions on Medical Imaging},
  volume  = {36},
  number  = {8},
  pages   = {1597--1606},
  year    = {2017},
  doi     = {10.1109/TMI.2017.2665165}
}
```

### R203. Automated segmentation QC at population scale (UK Biobank CMR)
- Full title: Automated quality control in image segmentation: application to the UK Biobank cardiovascular magnetic resonance imaging study
- Authors: Robert Robinson, Vanya V. Valindria, Wenjia Bai, et al. (22 authors, last Ben Glocker)
- Year / Venue / Type: 2019 / Journal of Cardiovascular Magnetic Resonance 21:18 / journal
- DOI / arXiv / URL: 10.1186/s12968-019-0523-x (verified via Crossref); arXiv:1901.09351
- Access: open
- Passes: 3/3 (abstract, then the arXiv PDF on 2026-10-16 read for the experiments and numbers, then for limitations and code)
- Modality & anatomy: cardiac MRI
- Data: 100 Hammersmith short-axis end-diastolic reference atlases. Exp A: 400 random-forest segmentations of the atlases. Exp B: 4,805 manually segmented UKBB scans (the abstract says 4,800), segmented with RF (4,805) and a CNN (Bai et al., 900). Exp C: 7,250 UKBB multi-atlas segmentations with single-rater visual QC scores 0-6 on LV myocardium.
- Method: single-atlas RCA. The 100 references are registered to the test image (centre-of-mass then non-rigid), their labels are warped, and the best DSC, MSD, RMS or HD is taken as the prediction. Good/poor threshold DSC 0.7 (and MSD 2.0 mm), which the authors call adjustable.
- Key results:
  - Exp A: accuracy 99% (TPR 0.98, FPR 0.00), predicted vs real r = 0.95-0.99.
  - Exp B, RF: accuracy 95% at DSC 0.7 (only 443/589 = 75.2% of poor cases caught), 98% at MSD 2 mm; whole-heart DSC MAE 0.035.
  - Exp B, CNN: accuracy 99.8%.
  - Exp C: predictions track manual QC scores, but no coefficient is given.
  - About 20 references are enough for > 90% accuracy.
- Code / weights / license: https://github.com/mlnotebook/RCA (Python; URL from the paper, not visited)
- Useful for us: evidence that automated per-case QC works at scale; the "quality regression" baseline in Zenk 2025 derives from this line of work.
- Limitations / notes: cardiac only. About 11 min per case on 8 cores, so not real-time. Predicted DSC is not 1:1 with real DSC (LV myocardium under-predicted). The reference set must be representative. Exp C has crude single-rater QC. RV myocardium excluded. Experiment labels B and C are swapped between the Methods and Results sections.
- BibTeX:
```bibtex
@article{Robinson2019AutomatedQC,
  title   = {Automated quality control in image segmentation: application to the {UK} {B}iobank cardiovascular magnetic resonance imaging study},
  author  = {Robinson, Robert and Valindria, Vanya V. and Bai, Wenjia and Oktay, Ozan and Kainz, Bernhard and others},
  journal = {Journal of Cardiovascular Magnetic Resonance},
  volume  = {21},
  number  = {1},
  pages   = {18},
  year    = {2019},
  doi     = {10.1186/s12968-019-0523-x}
}
```

### R204. Bayesian QuickNAT: structure-wise uncertainty for QC
- Full title: Bayesian QuickNAT: Model Uncertainty in Deep Whole-Brain Segmentation for Structure-wise Quality Control
- Authors: Abhijit Guha Roy, Sailesh Conjeti, Nassir Navab, Christian Wachinger
- Year / Venue / Type: 2019 / NeuroImage 195:11-22 / journal
- DOI / arXiv / URL: 10.1016/j.neuroimage.2019.03.042 (verified via OpenAlex; the similar DOI 10.1016/j.neuroimage.2018.11.042 is the original QuickNAT paper, so do not confuse them); arXiv:1811.09800 (v1 only)
- Access: open (arXiv)
- Passes: 3/3 (arXiv abstract re-read, then the arXiv PDF twice on 2026-10-16: methods and Table 3 numbers, then QC use cases and limitations)
- Modality & anatomy: brain T1 MRI, whole-brain parcellation
- Data: pre-trained on 581 IXI volumes with FreeSurfer auxiliary labels; fine-tuned on 15 of 30 MALC volumes; 33 structures. Test sets: MALC-15; ADNI-29 (AD and controls, 1.5T/3T); CANDI-13 (paediatric, age 5-15, psychiatric); IBSR-18 (low resolution, poor contrast). Group analyses on ADNI-29 and ABIDE-I (1,112 scans, 20 sites).
- Method: QuickNAT FCN with MC dropout (p = 0.2, N = 15 samples, < 2 min per scan). Four structure-wise metrics: (1) CV_s = SD/mean of structure volume across samples; (2) mean pairwise Dice between MC samples, d^MC_s (the 'pairwise Dice' later benchmarked by Zenk 2025); (3) IoU_s = intersection over union of the structure label across all N samples; (4) U_s = mean voxel entropy within the structure. The label-based metrics need only label maps (~200 KB), not probability maps (~2 GB).
- Key results (Table 3, correlation with Dice; values are U_s / CV_s / d^MC_s / IoU_s): MALC -0.85 / -0.81 / 0.86 / 0.88; ADNI -0.72 / -0.71 / 0.78 / 0.78; CANDI -0.84 / -0.86 / 0.90 / 0.91; IBSR -0.76 / -0.76 / 0.80 / 0.84. IoU_s was best on all four. As a Dice proxy, IoU had a mean absolute error of 2-7% and 80-88% three-class QC accuracy; the worst structure was the inferior lateral ventricle (about 15% off). Uncertainty-weighted regression brought ADNI diagnosis effects closer to manual results, and on ABIDE it recovered ENIGMA-reported associations that unweighted regression missed (except the amygdala).
- Code / weights / license: none mentioned in the arXiv paper
- Useful for us: per-structure (per-vertebra, per-disc) QC score design; origin of the pairwise-Dice failure score.
- Limitations / notes: brain only. The authors' limitations: no gain in accuracy; memory and compute grow with N; weaker for small structures; no real failures (Dice < 0.5) in the test data, so failure was simulated with Rician noise. For spine, IoU_s across fold or MC samples per vertebra is a cheap QC score.
- BibTeX:
```bibtex
@article{Roy2019BayesianQuickNAT,
  title   = {Bayesian {QuickNAT}: Model Uncertainty in Deep Whole-Brain Segmentation for Structure-wise Quality Control},
  author  = {Roy, Abhijit Guha and Conjeti, Sailesh and Navab, Nassir and Wachinger, Christian},
  journal = {NeuroImage},
  volume  = {195},
  pages   = {11--22},
  year    = {2019},
  doi     = {10.1016/j.neuroimage.2019.03.042},
  eprint  = {1811.09800},
  archivePrefix = {arXiv}
}
```

### R205. MOOD challenge
- Full title: MOOD 2020: A Public Benchmark for Out-of-Distribution Detection and Localization on Medical Images
- Authors: David Zimmerer, Peter M. Full, Fabian Isensee, et al. (36 authors incl. K. Maier-Hein)
- Year / Venue / Type: 2022 / IEEE Transactions on Medical Imaging 41(10):2728-2738 / challenge paper
- DOI / arXiv / URL: 10.1109/TMI.2022.3170077; open copy https://openaccess.city.ac.uk/id/eprint/28169/
- Access: open (published version CC BY 4.0 at openaccess.city.ac.uk/id/eprint/28169)
- Passes: 3/3 (bibliographic and abstract; City repository published PDF read 2026-10-16 for data, design and results, then for analysis and limitations)
- Modality & anatomy: brain MRI (HCP, healthy 22-35 y, one 3T scanner/protocol) and abdominal CT (CT colonography, adults 50+, multicentre)
- Data: training: 800 brain MRI, 550 abdominal CT (normal only). Tests: brain 688 sample-level / 542 pixel-level; abdomen 599 / 358. Mostly synthetic anomalies, local (rendered natural images, tumours/lesions, local corruptions) and global (omitted slices, heavy blurring, deformations), plus a few real conditions (rater consensus). Public toy cases: 4 per dataset (sphere anomalies). Preprocessing details withheld.
- Method: sample-level (one score per scan) and pixel-level (score per voxel) tasks, metric average precision (pixel AP over batches of 20), plus FPR at 95% TPR at sample level; consensus ranking across datasets. 65 registered, 11 active, 8 valid submissions per task; top methods FPI (foreign patch interpolation), VQ-VAE + autoregressive prior (Marimont), DAE + segmentation ensemble (Canon), U-Net inpainting (NUDT), deep perceptual AE.
- Key results: best AP: sample-level brain 0.962 (FPI), abdomen 0.876 (NUDT; FPI/Marimont 0.874); pixel-level brain 0.449, abdomen 0.394 (both FPI). Global anomalies easy (some classes at 95% TPR with zero FPs), local and real medical conditions hard; larger, higher-contrast and bright anomalies easier; brain easier than abdomen. Toy-ish set ranking agrees partly (Kendall tau-b 0.357-1.0; winner matched), so toy data is a development proxy but no guarantee. Authors cannot recommend methods for clinical use yet.
- Code / weights / license: challenge http://medicalood.dkfz.de/web/2020/ ; code https://github.com/mic-dkfz/mood (URLs from the paper)
- Useful for us: canonical OOD benchmark to cite; synthetic-anomaly evaluation protocol could be ported to spine CT/MRI.
- Limitations / notes: mostly synthetic anomalies, few real; test details hidden; only 8 submissions; mostly 2D methods; abdominal site count inconsistent (15 vs 18); easiest anomalies may be clinically irrelevant; pixel-level FPR not analysed. For us: global corruptions (missing slices, blur) are exactly the 'request a better scan' cases and are the easy part; real local pathology is not.
- BibTeX:
```bibtex
@article{Zimmerer2022MOOD,
  title   = {{MOOD} 2020: A Public Benchmark for Out-of-Distribution Detection and Localization on Medical Images},
  author  = {Zimmerer, David and Full, Peter M. and Isensee, Fabian and J{\"a}ger, Paul and Adler, Tim and Petersen, Jens and K{\"o}hler, Gregor and Ross, Tobias and Reinke, Annika and Kascenas, Antanas and others},
  journal = {IEEE Transactions on Medical Imaging},
  volume  = {41},
  number  = {10},
  pages   = {2728--2738},
  year    = {2022},
  doi     = {10.1109/TMI.2022.3170077}
}
```

### R206. Maximum softmax probability baseline for misclassification and OOD detection
- Full title: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks
- Authors: Dan Hendrycks, Kevin Gimpel
- Year / Venue / Type: 2017 / ICLR 2017 (confirmed by the 'Published as a conference paper at ICLR 2017' header in arXiv v3) / conference
- DOI / arXiv / URL: arXiv:1610.02136
- Access: open
- Passes: 3/3 (abstract, then the arXiv v3 PDF on 2026-10-16 read for datasets, metrics and tables, then for the abnormality module, limitations and recommendations)
- Modality & anatomy: general (vision, NLP, speech)
- Data: vision (MNIST, CIFAR-10/100; OOD: SUN, Omniglot, notMNIST, CIFAR-10bw, Gaussian and uniform noise); NLP (IMDB, 20 Newsgroups, Reuters, WSJ POS; OOD: product/movie reviews, Twitter, weblogs); speech (TIMIT CTC-LSTM; OOD: Aurora-2 noise, THCHS-30 Chinese)
- Method: maximum softmax probability (MSP) as a score for error and OOD detection, evaluated with AUROC and with AUPR in both directions (Succ/In positive and Err/Out positive) against random-baseline values. Also proposes an 'abnormality module' (frozen reconstruction decoder plus a sigmoid normal-vs-noised discriminator).
- Key results (AUROC %): error detection on MNIST 97, CIFAR-10 93, CIFAR-100 87; OOD for CIFAR-10 vs SUN 95, CIFAR-100 vs SUN 91, MNIST vs notMNIST 85. The abnormality module raised average AUROC on TIMIT from 80 to 97 and on MNIST from 93 to 100. The authors warn that softmax probabilities are not a direct measure of confidence.
- Code / weights / license: github.com/hendrycks/error-detection (URL given in the paper; licence not checked)
- Useful for us: the default baseline every abstention/OOD component of ours must beat; also defines the AUROC/AUPR evaluation convention.
- Limitations / notes: MSP is overconfident far from the data; near-distribution OOD (weblogs) is hard; small architectures only. The authors recommend reporting AUROC, AUPR and the underlying accuracy, and re-running the MSP baseline rather than copying numbers.
- BibTeX:
```bibtex
@inproceedings{Hendrycks2017Baseline,
  title     = {A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks},
  author    = {Hendrycks, Dan and Gimpel, Kevin},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2017},
  eprint    = {1610.02136},
  archivePrefix = {arXiv}
}
```

### R207. Confidence-based OOD detection: CV vs chest X-ray
- Full title: Confidence-based Out-of-Distribution Detection: A Comparative Study and Analysis
- Authors: Christoph Berger, Magdalini Paschali, Ben Glocker, Konstantinos Kamnitsas
- Year / Venue / Type: 2021 / UNSURE workshop at MICCAI 2021 (venue unverified; arXiv lists no journal-ref) / workshop
- DOI / arXiv / URL: arXiv:2107.02568
- Access: open
- Passes: 3/3 (abstract, then the arXiv PDF on 2026-10-16 read for setup and AUROC tables, then for the failure analysis and limitations. The venue is not stated in the PDF.)
- Modality & anatomy: chest X-ray (plus CV benchmark)
- Data: CIFAR10 (ID) vs SVHN (OOD). CheXpert with held-out diseases as OOD: setting 1, ID cardiomegaly vs pneumothorax, OOD fracture (4,300 ID / 7,200 OOD test); setting 2, ID lung opacity vs pleural effusion, OOD fracture and pneumonia (6,000 / 8,100).
- Method: WRN-28x10 (CIFAR) and WRN-100x2 (CheXpert), 3 seeds. Compared MCP (max softmax), MC dropout, deep ensembles, Mahalanobis (single and ensemble), ODIN (full, perturbation-only, temperature-only) and DUQ (unstable, no usable result). Metrics: AUROC, AUCPR, ID accuracy, ECE.
- Key results (AUROC, CIFAR vs SVHN / CheXpert setting 1 / setting 2): MCP 0.939 / 0.678 / 0.458; MC dropout 0.956 / 0.696 / 0.519; ensemble 0.960 / 0.704 / 0.445; Mahalanobis 0.984 / 0.580 / 0.526; ODIN 0.964 / 0.841 / 0.862, where the input perturbation does the work. Mahalanobis, the best on CV, collapses on CXR because ID and OOD classes overlap in feature space (dimensionality is not the cause). ODIN's perturbation makes the model overconfident; T = 5 restored calibration.
- Code / weights / license: no code URL in the paper
- Useful for us: caution that OOD detectors must be validated on radiographs specifically (our spine X-ray branch); supports building an explicit "wrong body part / wrong view" detector rather than relying on confidence alone.
- Limitations / notes: classification only; one medical dataset; 3 seeds; OOD is defined as unseen pathology (semantic shift), not as a wrong body part or acquisition shift. Shows that AUROC alone can hide miscalibration.
- BibTeX:
```bibtex
@inproceedings{Berger2021ConfidenceOOD,
  title     = {Confidence-based Out-of-Distribution Detection: A Comparative Study and Analysis},
  author    = {Berger, Christoph and Paschali, Magdalini and Glocker, Ben and Kamnitsas, Konstantinos},
  booktitle = {Uncertainty for Safe Utilization of Machine Learning in Medical Imaging (UNSURE), MICCAI Workshop},
  year      = {2021},
  eprint    = {2107.02568},
  archivePrefix = {arXiv},
  note      = {Proceedings details unverified}
}
```

### R208. Mahalanobis OOD detection for silent failures of pretrained nnU-Net
- Full title: Detecting When Pre-trained nnU-Net Models Fail Silently for Covid-19 Lung Lesion Segmentation
- Authors: Camila Gonzalez, Karol Gotkowski, Andreas Bucher, et al. (Fischbach, Kaltenborn, Mukhopadhyay)
- Year / Venue / Type: 2021 / MICCAI 2021, LNCS, pp. 304-314 / conference
- DOI / arXiv / URL: 10.1007/978-3-030-87234-2_29 (verified via Crossref/OpenAlex); arXiv:2107.05975
- Access: open (arXiv, green OA)
- Passes: 3/3 (abstract, then the arXiv PDF on 2026-10-16 read for data, method and Table 1, then for limitations and code)
- Modality & anatomy: chest CT; COVID-19 lung lesions
- Data: COVID-19 Lung CT Lesion Segmentation Grand Challenge (multi-institutional; 199 cases split 160 train / 4 validation / 35 ID test). OOD test sets: Mosmed (50), Radiopaedia (20) and in-house Frankfurt (50 RT-PCR-positive patients, annotated by two readers and reviewed by an expert radiologist).
- Method: 3D full-resolution patch-based nnU-Net (patch 28x256x256, 50% overlap). Encoder features (layer not stated) are average-pooled (2,2,2) repeatedly until there are fewer than 1e4 elements, then flattened. Mean and covariance are fitted on training features (scikit-learn). Each patch gets a Mahalanobis distance, which is spread over the patch with centre weighting into a voxel map. The case score is the voxel mean, normalised by the min and 2x the max on the ID validation set. Baselines: max softmax, temperature scaling (T = 10/100/1000), KL from uniform, MC dropout (10 passes). No change to architecture or training.
- Key results (Table 1, at 95% TPR): proposed detection error 0.082, FPR 0.050, ESCE 0.125, Dice of admitted cases 0.744 +/- 0.143. MC dropout: 0.177 / 0.183 / 0.215 / 0.614. Max softmax: 0.334 / 0.583 / 0.319 / 0.582. All OOD cases admitted under the threshold had Dice > 0.6. In Zenk 2025 the Mahalanobis method was best for OOD metrics but not for failure detection.
- Code / weights / license: github.com/MECLabTUDA/Lifelong-nnUNet, branch ood_detection (URL from the paper; repository not visited, licence unverified)
- Useful for us: drop-in, post-hoc OOD score for our nnU-Net-based spine segmenters (e.g. unseen scanner, unusual sequence, wrong body region) to trigger "request better / standard scan".
- Limitations / notes: OOD is not the same as failure. Only one model and one training dataset; some good OOD predictions are still flagged; normalisation relies on a 4-case validation set; one threshold only, with no AUROC. A journal extension (MedIA 2022) is not verified here.
- BibTeX:
```bibtex
@inproceedings{Gonzalez2021SilentFailures,
  title     = {Detecting When Pre-trained {nnU-Net} Models Fail Silently for {Covid-19} Lung Lesion Segmentation},
  author    = {Gonzalez, Camila and Gotkowski, Karol and Bucher, Andreas and Fischbach, Ricarda and Kaltenborn, Isabel and Mukhopadhyay, Anirban},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2021},
  series    = {Lecture Notes in Computer Science},
  pages     = {304--314},
  publisher = {Springer},
  year      = {2021},
  doi       = {10.1007/978-3-030-87234-2_29}
}
```

### R209. MRIQC
- Full title: MRIQC: Advancing the automatic prediction of image quality in MRI from unseen sites
- Authors: Oscar Esteban, Daniel Birman, Marie Schaer, et al. (Koyejo, Poldrack, Gorgolewski)
- Year / Venue / Type: 2017 / PLOS ONE 12(9): e0184661 / journal
- DOI / arXiv / URL: 10.1371/journal.pone.0184661; bioRxiv 10.1101/111294; PMC5612458
- Access: open
- Passes: 3/3 (abstract plus the bioRxiv summary; PLOS ONE full text read 2026-10-16 for data, labels, harmonisation, results and limitations. The full Table 2 IQM list was not captured.)
- Modality & anatomy: brain T1w MRI
- Data: training on ABIDE, 1,102 T1w scans (1,101 usable) from 17 sites; held-out test on OpenfMRI DS030, 265 scans from 2 centres (BMC, CCN). Two raters labelled exclude / doubtful / accept from about 20 s animated coronal GIFs. ABIDE 337/352/412, DS030 75/145/45. 'Doubtful' was merged with 'accept'. Inter-rater kappa 0.39 for three levels, 0.51 for binary.
- Method: 64 features from 14 IQMs (noise and noise-model fit, information-theoretic measures such as EFC, artefact measures such as INU and QI2 motion leakage, tissue/overlap/sharpness measures such as CJV and rPVE). Site harmonisation: per-site median/IQR normalisation, iterative removal of 14 site-predictive features (extra trees), and winnow selection against a random feature (50 features kept). Linear SVC, RBF SVC and random forest were compared. Nested leave-one-site-out CV (inner random search over 50 models; 10-fold CV was more optimistic); the final model came from a 512-configuration grid search.
- Key results: random forest, leave-one-site-out, AUC 0.73 +/- 0.15 and accuracy 76.15% +/- 13.38% (SVC-lin 0.68, SVC-rbf 0.64). On held-out DS030: AUC 0.707 and accuracy 76% (permutation p = 0.001), against 72% for an 'all accept' classifier. Recall for 'exclude' was only 0.28; on a ghost-free subset, AUC 0.83, accuracy 87% and recall 0.46. QI2 was the most important feature.
- Code / weights / license: the paper gives https://github.com/poldracklab/mriqc under BSD 3-clause (as stated in the 2017 paper; the project now lives at github.com/nipreps/mriqc, current licence not re-checked). Also available on PyPI, Docker, BIDS-App and the OpenNeuro service.
- Useful for us: reference design for a no-reference IQA module (handcrafted IQMs + classifier); several IQMs (SNR, CNR, EFC, ghosting) transfer to spine MRI. Shows cross-site generalisation is the main difficulty.
- Limitations / notes: brain T1w only; modest accuracy and weak cross-site generalisation. The ghosting artefact in the test set was unseen in training, which illustrates that a new artefact type defeats the classifier. Label noise is high (kappa 0.39-0.51), raters used FreeSurfer cues, ABIDE images were resampled, and artefacts are not localised. It needs skull stripping and registration, which is not available for spine. For us: report rater agreement for our 'inadequate scan' labels and test on unseen sites and artefact types.
- BibTeX:
```bibtex
@article{Esteban2017MRIQC,
  title   = {{MRIQC}: Advancing the automatic prediction of image quality in {MRI} from unseen sites},
  author  = {Esteban, Oscar and Birman, Daniel and Schaer, Marie and Koyejo, Oluwasanmi O. and Poldrack, Russell A. and Gorgolewski, Krzysztof J.},
  journal = {PLOS ONE},
  volume  = {12},
  number  = {9},
  pages   = {e0184661},
  year    = {2017},
  doi     = {10.1371/journal.pone.0184661}
}
```

### R210. CNN detection of cardiac MR motion artefacts (k-space augmentation)
- Full title: Automatic CNN-based detection of cardiac MR motion artefacts using k-space data augmentation and curriculum learning
- Authors: Ilkay Oksuz, Bram Ruijsink, Esther Puyol-Anton, et al. (... Rueckert, Schnabel, King)
- Year / Venue / Type: 2019 / Medical Image Analysis 55:136-147 / journal
- DOI / arXiv / URL: 10.1016/j.media.2019.04.009 (verified via Crossref); arXiv:1810.12185
- Access: open (arXiv)
- Passes: 3/3 (abstract, then the arXiv PDF on 2026-10-16 read for data, method and Tables 1-3, then for limitations and code)
- Modality & anatomy: cardiac cine MRI
- Data: UK Biobank short-axis cine bSSFP from 3,510 subjects (50 frames; 1.8x1.8x8 mm). 3,360 good vs 150 artefact cases (57 mistriggering, 46 breathing, 42 arrhythmia, 5 mixed), labelled by visual inspection and validated by a cardiologist. Data available by UK Biobank application only.
- Method: a 3D CNN (C3D-like, 80x80x50 input) compared with an LRCN (CNN + LSTM over frames). Synthetic artefacts in Cartesian k-space: mistriggering replaces 1 in z phase-encode lines with lines from other cardiac phases; breathing applies sinusoidal translation (4 cycles over 256 PE steps) before k-space generation. 10 severity levels drive a 'baby-step' curriculum from easy (most corrupted) to hard. This was compared with anti-curriculum, random ordering and cost-sensitive weighting. SGD, Keras, 10-fold CV.
- Key results (Table 3, in vivo, 10-fold CV; BA / precision / recall / AUC):
  - LRCN + mixed augmentation: 0.742 / 0.751 / 0.733 / 0.828
  - LRCN without augmentation: AUC 0.603
  - 3D CNN + mixed augmentation: AUC 0.735
  - cost-sensitive weighting: AUC about 0.61, which is poor

  The headline AUC of 0.89 is with curriculum learning, shown only in Fig. 9. Curriculum beat random and anti-curriculum ordering (DeLong p < 0.05). On synthetic tests, LRCN accuracy was 0.963 (mistriggering) and 0.961 (breathing), against NIQE at 0.922 and 0.897. Inference time is inconsistent: the abstract says < 1 ms, the text < 1 s per sequence.
- Code / weights / license: no code or model release mentioned
- Useful for us: k-space motion simulation is directly reusable to synthesise motion-corrupted spine MRI (sagittal T2) for training our "image inadequate, please rescan" classifier where real bad scans are rare.
- Limitations / notes: cardiac cine, mid-ventricular short-axis only, binary labels, only 150 real artefacts, no prospective or on-scanner test. The paper's 'balanced accuracy' is defined non-standardly as the mean of precision and recall, so do not compare it with the standard BA.
- BibTeX:
```bibtex
@article{Oksuz2019MotionArtefacts,
  title   = {Automatic {CNN}-based detection of cardiac {MR} motion artefacts using k-space data augmentation and curriculum learning},
  author  = {Oksuz, Ilkay and Ruijsink, Bram and Puyol-Ant{\'o}n, Esther and Clough, James R. and Cruz, Gastao and Bustin, Aurelien and Prieto, Claudia and Botnar, Rene and Rueckert, Daniel and Schnabel, Julia A. and King, Andrew P.},
  journal = {Medical Image Analysis},
  volume  = {55},
  pages   = {136--147},
  year    = {2019},
  doi     = {10.1016/j.media.2019.04.009}
}
```

### R211. Reference-free CNN detection of MRI motion artefacts (Kuestner)
- Full title: Automated reference-free detection of motion artifacts in magnetic resonance images
- Authors: Thomas Kuestner (corresponding), Annika Liebgott, Lukas Mauch, Petros Martirosian, Fabian Bamberg, Konstantin Nikolaou, Bin Yang, Fritz Schick, Sergios Gatidis
- Year / Venue / Type: 2018 (online 20 Sep 2017) / MAGMA (Magnetic Resonance Materials in Physics, Biology and Medicine) 31(2):243-256 / journal
- DOI / arXiv / URL: 10.1007/s10334-017-0650-z (OpenAlex; also the Tuebingen repository record hdl.handle.net/10900/94953); PMID 28932991
- Access: closed (OpenAlex); no file in the Tuebingen repository
- Passes: metadata only (OpenAlex has no abstract and the Springer/SpringerMedicine pages were blocked on 2026-10-16; added from this file's gaps list so it can be cited after the abstract is read)
- Modality & anatomy: MRI; OpenAlex keywords mention T1-weighted imaging and head MRI (other body regions not verified)
- Data: unverified
- Method: CNN-based reference-free motion artefact detection producing probability maps (from record keywords only; details unverified)
- Key results: unverified (do not cite numbers)
- Code / weights / license: unverified
- Useful for us: the MRI-specific counterpart to [A5-02] for a 'motion-corrupted, please rescan' detector, and highly cited (about 100 citations per OpenAlex).
- Limitations / notes: read the abstract and full text before citing anything beyond the bibliographic data.
- BibTeX:
```bibtex
@article{Kuestner2018MotionArtifacts,
  title   = {Automated reference-free detection of motion artifacts in magnetic resonance images},
  author  = {K{\"u}stner, Thomas and Liebgott, Annika and Mauch, Lukas and Martirosian, Petros and Bamberg, Fabian and Nikolaou, Konstantin and Yang, Bin and Schick, Fritz and Gatidis, Sergios},
  journal = {Magnetic Resonance Materials in Physics, Biology and Medicine},
  volume  = {31},
  number  = {2},
  pages   = {243--256},
  year    = {2018},
  doi     = {10.1007/s10334-017-0650-z}
}
```

### R212. Selective classification for deep networks (SGR)
- Full title: Selective Classification for Deep Neural Networks
- Authors: Yonatan Geifman, Ran El-Yaniv
- Year / Venue / Type: 2017 / NeurIPS 2017 / conference
- DOI / arXiv / URL: arXiv:1705.08500; https://papers.nips.cc/paper_files/paper/2017/file/4a8423d5e91fda00bb7e46540e2b0cf1-Paper.pdf
- Access: open
- Passes: 3/3 (ar5iv full text)
- Modality & anatomy: natural images
- Data: CIFAR-10, CIFAR-100 (VGG-16), ImageNet (VGG-16, ResNet-50)
- Method: selective classifier (f, g) with coverage and selective risk; confidence-rate functions softmax response (SR) and MC dropout; Selection with Guaranteed Risk (SGR) chooses a threshold via binary search with a binomial-tail bound so selective risk <= r* with probability 1 - delta.
- Key results: 2% top-5 ImageNet error guaranteed with probability 99.9% at almost 60% coverage; SR ~ MC dropout on CIFAR, SR better on ImageNet.
- Code / weights / license: unverified.
- Useful for us: formal recipe to set our abstention threshold with a statistical guarantee on error among accepted studies; risk-coverage framing used in Zenk 2025.
- Limitations / notes: classifier fixed; guarantee is i.i.d. only (not under scanner shift).
- BibTeX:
```bibtex
@inproceedings{Geifman2017Selective,
  title     = {Selective Classification for Deep Neural Networks},
  author    = {Geifman, Yonatan and El-Yaniv, Ran},
  booktitle = {Advances in Neural Information Processing Systems 30 (NeurIPS)},
  year      = {2017},
  eprint    = {1705.08500},
  archivePrefix = {arXiv}
}
```

### R213. Learning to defer to an expert (consistent surrogate)
- Full title: Consistent Estimators for Learning to Defer to an Expert
- Authors: Hussein Mozannar, David Sontag
- Year / Venue / Type: 2020 / ICML 2020 / conference
- DOI / arXiv / URL: arXiv:2006.01862; https://icml.cc/virtual/2020/poster/6448
- Access: open
- Passes: 2/3 (abstract + method via ar5iv; experiment section truncated)
- Modality & anatomy: general incl. chest X-ray with synthetic experts
- Data: CIFAR-10/100 (synthetic + CIFAR-10H human experts), hate-speech detection, chest X-ray classification
- Method: joint classifier + rejector via reduction to cost-sensitive learning; consistent convex surrogate L_CE generalising cross-entropy (extra "defer" output).
- Key results: theoretical consistency; empirically effective on tasks (numbers not extracted).
- Code / weights / license: github.com/clinicalml/learn-to-defer (unverified)
- Useful for us: if we have radiologist reads, train the "defer" decision jointly rather than thresholding uncertainty post hoc.
- Limitations / notes: needs samples of expert decisions.
- BibTeX:
```bibtex
@inproceedings{Mozannar2020Defer,
  title     = {Consistent Estimators for Learning to Defer to an Expert},
  author    = {Mozannar, Hussein and Sontag, David},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {119},
  year      = {2020},
  eprint    = {2006.01862},
  archivePrefix = {arXiv}
}
```

### R214. CoDoC: complementarity-driven deferral to clinicians
- Full title: Enhancing the reliability and accuracy of AI-enabled diagnosis via complementarity-driven deferral to clinicians
- Authors: Krishnamurthy (Dj) Dvijotham, Jim Winkens, Melih Barsbey, Sumedh Ghaisas, Robert Stanforth, Nick Pawlowski, et al. (30 authors; last Alan Karthikesalingam; mostly Google DeepMind and Google Research)
- Year / Venue / Type: 2023 / Nature Medicine 29(7):1814-1820 / journal
- DOI / arXiv / URL: 10.1038/s41591-023-02437-x
- Access: paywalled (exclusive licence to Springer Nature); abstract and back matter read on the Springer link page
- Passes: 1/3 (abstract plus data/code availability read on link.springer.com, 2026-10-16; methods and full results not accessible)
- Modality & anatomy: screening mammography (breast cancer) and chest X-ray TB triage (confirmed in the abstract)
- Data: OPTIMAM (UK; on request), Northwestern Medicine and St Clair Hospital mammography (US; licensed), US Mammography Dataset 2 (on request), and Stop TB Partnership and icddr,b TB datasets (licensed). Sizes were not on the page. Released: per-case AI score, clinician opinion and label for the tuning, validation and test splits.
- Method: CoDoC takes the predictive AI's confidence score, the clinician's opinion and the ground truth on a tuning set, and learns when to defer to the clinical workflow versus using the AI. The threshold-learning details (kernel density estimation is referenced) were not accessible.
- Key results (abstract): UK breast screening, against double reading with arbitration, 25% fewer false positives at the same false-negative rate and 66% less clinician workload. TB triage: 5-15% fewer false positives at the same FNR for 3 of 5 commercial AI systems, against AI alone or the workflow alone. Gains held across modality, setting and AI system.
- Code / weights / license: https://github.com/deepmind/codoc (open-source implementation per the paper; licence not checked)
- Useful for us: high-profile clinical deferral system to cite next to our abstention module.
- Limitations / notes: most data are licensed or non-public; industry-funded (Google authors); needs paired clinician decisions on a tuning set, which we will not have for direct-to-user scans. Methods detail is still to be read from the full text.
- BibTeX:
```bibtex
@article{Dvijotham2023CoDoC,
  title   = {Enhancing the reliability and accuracy of {AI}-enabled diagnosis via complementarity-driven deferral to clinicians},
  author  = {Dvijotham, Krishnamurthy and Winkens, Jim and Barsbey, Melih and Ghaisas, Sumedh and Stanforth, Robert and others},
  journal = {Nature Medicine},
  volume  = {29},
  number  = {7},
  pages   = {1814--1820},
  year    = {2023},
  doi     = {10.1038/s41591-023-02437-x}
}
```

### R215. Gentle introduction to conformal prediction
- Full title: A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification
- Authors: Anastasios N. Angelopoulos, Stephen Bates
- Year / Venue / Type: 2021 (v6 2022) / arXiv tutorial (later published in Foundations and Trends in ML, 2023; unverified) / preprint
- DOI / arXiv / URL: arXiv:2107.07511
- Access: open
- Passes: 3/3 (abstract and structure; arXiv abs re-read for v6 dated 2022-12-07; v6 PDF read on 2026-10-16 for the algorithm, theorems, score functions, shift and calibration-size guidance. The FnT publication is still unverified.)
- Modality & anatomy: general, with medical examples
- Data: examples incl. ImageNet; code notebooks
- Method: split conformal prediction. Score s(x, y) (e.g. 1 - softmax of the true class); q-hat = the ceil((n+1)(1-alpha))/n empirical quantile of the calibration scores; set C(x) = {y : s(x, y) <= q-hat}. Score functions: APS, CQR, uncertainty-scalar intervals f(x) +/- q-hat * sigma(x), conformalized Bayes. Conditional-coverage diagnostics: feature-stratified coverage (FSC) and size-stratified coverage (SSC). Weighted conformal under known covariate shift; drift weighting; outlier detection with type-1 error control; conformal risk control; Learn-then-Test for selective classification.
- Key results: 1 - alpha <= P(Y in C(X)) <= 1 - alpha + 1/(n+1) for any score and distribution. Coverage conditional on the calibration set is Beta(n + 1 - l, l) with l = floor((n+1) alpha). The authors suggest n = 1000 is enough for most uses. Table 1 (delta = 0.1, alpha = 0.1) gives the n needed for slack epsilon: 22 for 0.1, 102 for 0.05, 2,491 for 0.01. Medical examples: polyp segmentation FNR control, and a hypothetical MRI age-mix shift.
- Code / weights / license: notebooks linked by icon only, so the repository URL github.com/aangelopoulos/conformal-prediction is not confirmed in the text. MAPIE is named as a library.
- Useful for us: wrap our grading classifiers (e.g. stenosis, Pfirrmann) to output prediction sets; set size > 1 = inconclusive -> trigger human read / better scan.
- Limitations / notes: coverage is marginal, not conditional, so report FSC by scanner, sex and age and SSC. Exchangeability breaks under scanner shift; weighted conformal needs the likelihood ratio and reduces the effective n. For us, about 100-1000 calibration studies per modality are needed for tight coverage.
- BibTeX:
```bibtex
@article{Angelopoulos2021GentleCP,
  title   = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
  author  = {Angelopoulos, Anastasios N. and Bates, Stephen},
  journal = {arXiv preprint arXiv:2107.07511},
  year    = {2021}
}
```

### R216. Conformal risk control
- Full title: Conformal Risk Control
- Authors: Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, et al. (Lei, Schuster)
- Year / Venue / Type: 2022 (v4 2025) / arXiv; published at ICLR 2024 (unverified) / preprint
- DOI / arXiv / URL: arXiv:2208.02814
- Access: open
- Passes: 3/3 (arXiv abs re-read, then the v4 PDF on 2026-10-16 read for the algorithm, theorems and experiments, then for limitations. The venue is still unverified because the OpenAlex lookup was rate-limited.)
- Modality & anatomy: general CV/NLP (abstract mentions false negative rate control)
- Data: polyp segmentation (PraNet; pooled Kvasir, Hyper-Kvasir, CVC-ColonDB, CVC-ClinicDB, ETIS-Larib; n = 1000 calibration / 781 test); MS COCO multilabel (TResNet, 4000/1000); hierarchical ImageNet (ResNet152, 30000/20000); Natural Questions (DPR, 2500/1110)
- Method: choose lambda-hat as the smallest lambda with (n/(n+1)) * R_hat_n(lambda) + B/(n+1) <= alpha, where B bounds the loss. Guarantee: E[L_{n+1}(lambda-hat)] <= alpha. The lower bound is alpha - 2B/(n+1) for i.i.d. losses without jumps. Assumptions: exchangeable losses, non-increasing and right-continuous in lambda, bounded by B. Extensions: distribution shift, quantile risk, multiple and adversarial risks, U-statistics.
- Key results (mean over 1000 splits): polyp pixel FNR at alpha 0.1 gave 0.0987 (SD 0.0114); COCO FNR 0.0996 (alpha 0.1); ImageNet graph distance 0.0499 (alpha 0.05); QA F1 loss 0.2996 (alpha 0.3).
- Code / weights / license: https://github.com/aangelopoulos/conformal-risk (URL from the paper; licence not checked)
- Useful for us: calibrate segmentation thresholds of e.g. spinal canal / fracture masks to a guaranteed false-negative rate per study.
- Limitations / notes: needs exchangeability, so a scanner or site shift breaks the guarantee unless weighted. Non-monotone losses are not controlled (Prop. 1), and monotonising helps only when the risk is near-monotone. Weighted CRC under an estimated covariate shift and CVaR control are open problems. The guarantee is marginal (on average over studies), not per study. The polyp experiment is a direct template for a per-pixel FNR guarantee on spinal canal or fracture masks.
- BibTeX:
```bibtex
@article{Angelopoulos2022CRC,
  title   = {Conformal Risk Control},
  author  = {Angelopoulos, Anastasios N. and Bates, Stephen and Fisch, Adam and Lei, Lihua and Schuster, Tal},
  journal = {arXiv preprint arXiv:2208.02814},
  year    = {2022}
}
```

### R217. Fair conformal predictors for medical imaging
- Full title: Fair Conformal Predictors for Applications in Medical Imaging
- Authors: Charles Lu, Andreanne Lemay, Ken Chang, et al. (Hoebel, Kalpathy-Cramer)
- Year / Venue / Type: 2022 / AAAI 2022 (inferred from repo name "AAAI22"; unverified) / conference
- DOI / arXiv / URL: arXiv:2109.04392
- Access: open
- Passes: 3/3 (ar5iv full text)
- Modality & anatomy: dermatology photographs (skin lesions); clinical use cases framed for radiology
- Data: Fitzpatrick17k, 16,577 images, 114 conditions grouped into non-neoplastic/benign/malignant; skin type as group attribute
- Method: ResNet-18; naive softmax thresholding vs APS, RAPS and group-conditional GAPS/GRAPS; interviews with 4 clinicians; "rule-out" and "rule-in" use cases.
- Key results: coverage disparity at alpha=0.1: APS/RAPS 0.026, GAPS 0.024, GRAPS 0.022; but set-size disparity grows (3.5 -> 9.7). Clinicians preferred semantic confidence labels and hiding low-confidence predictions.
- Code / weights / license: repo referenced as AAAI22 (URL unverified)
- Useful for us: group-conditional conformal to equalise coverage across scanners/sites/age-sex groups; clinician-facing presentation insights for our reports.
- Limitations / notes: single dataset; 4 clinicians; larger sets.
- BibTeX:
```bibtex
@inproceedings{Lu2022FairConformal,
  title     = {Fair Conformal Predictors for Applications in Medical Imaging},
  author    = {Lu, Charles and Lemay, Andr{\'e}anne and Chang, Ken and Hoebel, Katharina and Kalpathy-Cramer, Jayashree},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  year      = {2022},
  eprint    = {2109.04392},
  archivePrefix = {arXiv},
  note      = {Venue details unverified}
}
```

### R218. Conformal semantic segmentation with risk control (Mossina)
- Full title: Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty
- Authors: Luca Mossina, Joseba Dalmau, Leo Andeol (IRT Saint Exupery; Institut de Mathematiques de Toulouse / SNCF)
- Year / Venue / Type: 2024 / CVPR 2024 Workshops (SAIAD), pp. 3574-3584 (CVF open access; 'SAIAD' from the CVF URL path) / workshop
- DOI / arXiv / URL: arXiv:2405.05145; https://openaccess.thecvf.com/content/CVPR2024W/SAIAD/html/Mossina_Conformal_Semantic_Image_Segmentation_Post-hoc_Quantification_of_Predictive_Uncertainty_CVPRW_2024_paper.html ; HAL hal-04565173
- Access: open
- Passes: 3/3 (CVF PDF read 2026-10-16 for method and results, then for limitations and code; search listings for the venue; added in pass 2 from this file's gaps list)
- Modality & anatomy: natural and aerial images (no medical data)
- Data: Cityscapes (PSPNet), ADE20K (SegFormer), LoveDA (PSPNet); MMSegmentation pretrained weights; 10 shuffled calibration/test splits
- Method: post-hoc conformal risk control (as in [A7-02]) on multi-label masks. A pixel keeps every class with softmax >= 1 - lambda (the top-1 class is always kept). Losses: binary with coverage threshold tau, miscoverage (1 - fraction of true-label pixels covered), and weighted miscoverage. lambda-hat is chosen with the finite-sample correction by dichotomic search. 'Varisco' heatmaps show the per-pixel number of classes in the set.
- Key results: empirical risk tracks nominal alpha. Cityscapes miscoverage: alpha 0.01 gives risk 0.006 with an average of 1.23 classes per pixel; alpha 0.005 gives risk 0.001 with 2.00. ADE20K at alpha 0.01: risk 0.008 with 15.3 classes per pixel, which is uninformative. LoveDA binary loss (tau 0.9, alpha 0.01): risk 0.010, 5.76 classes per pixel.
- Code / weights / license: https://github.com/deel-ai-papers/conformal-segmentation (URL from the paper)
- Useful for us: a ready recipe for per-pixel prediction sets on multi-class spine segmentation (vertebra, disc, canal, foramen) with a marginal coverage guarantee. Varisco maps can show where labels are ambiguous (e.g. adjacent vertebral levels), and a mask that becomes near-full at the target alpha is itself a signal to abstain.
- Limitations / notes: marginal guarantee only, not per image; needs exchangeable calibration data; strict alpha gives uninformative masks; heatmaps reflect softmax spread, not error; LAC sets only; no medical validation.
- BibTeX:
```bibtex
@inproceedings{Mossina2024ConformalSeg,
  title     = {Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty},
  author    = {Mossina, Luca and Dalmau, Joseba and And{\'e}ol, L{\'e}o},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  pages     = {3574--3584},
  year      = {2024},
  eprint    = {2405.05145},
  archivePrefix = {arXiv}
}
```

#### Part B. Deviation from normal anatomy

### R219. Autoencoders for unsupervised anomaly segmentation in brain MRI (comparative study)
- Full title: Autoencoders for unsupervised anomaly segmentation in brain MR images: A comparative study
- Authors: Christoph Baur, Stefan Denner, Benedikt Wiestler, et al. (Navab, Albarqouni)
- Year / Venue / Type: 2021 / Medical Image Analysis 69:101952 / journal (review + benchmark)
- DOI / arXiv / URL: 10.1016/j.media.2020.101952; arXiv:2004.03271
- Access: open (arXiv)
- Passes: 2/3 (abstract + methods/data via ar5iv; result tables did not render)
- Modality & anatomy: brain MRI (FLAIR)
- Data: in-house 3T: 138 healthy (110 train/28 val), 48 MS, 26 glioma; MSLUB (30 MS); MSSEG2015 (domain shift test)
- Method: unified architecture comparing AE (dense/spatial), context AE, constrained AE, VAE, context VAE, constrained AAE, GMVAE, AnoVAEGAN, f-AnoGAN, restoration (VAE/GMVAE), Bayesian AE/VAE (dropout), gradient-based context VAE; residual-based anomaly maps.
- Key results: metrics AUPRC (primary), best-possible Dice, patient-wise Dice; studies number of healthy training subjects needed and domain shift (numbers not extracted).
- Code / weights / license: https://github.com/StefanDenn3r/unsupervised_anomaly_detection_brain_mri
- Useful for us: canonical review/benchmark for "normative appearance" modelling; evaluation conventions (AUPRC, best Dice) to adopt for spine anomaly maps.
- Limitations / notes: brain only, 2D slices.
- BibTeX:
```bibtex
@article{Baur2021Autoencoders,
  title   = {Autoencoders for unsupervised anomaly segmentation in brain {MR} images: A comparative study},
  author  = {Baur, Christoph and Denner, Stefan and Wiestler, Benedikt and Navab, Nassir and Albarqouni, Shadi},
  journal = {Medical Image Analysis},
  volume  = {69},
  pages   = {101952},
  year    = {2021},
  doi     = {10.1016/j.media.2020.101952}
}
```

### R220. AnoGAN
- Full title: Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery
- Authors: Thomas Schlegl, Philipp Seeboeck, Sebastian M. Waldstein, et al. (Schmidt-Erfurth, Langs)
- Year / Venue / Type: 2017 / IPMI 2017, LNCS (Springer) pp. 146-157 / conference
- DOI / arXiv / URL: 10.1007/978-3-319-59050-9_12 (verified via OpenAlex); arXiv:1703.05921
- Access: open (arXiv)
- Passes: 3/3 (abstract and metadata; arXiv PDF read 2026-10-16 for data, method and results, then for comparisons and limitations)
- Modality & anatomy: retinal OCT
- Data: training: 270 healthy SD-OCT volumes (49 B-scans each), 1,000,000 random 64x64 patches; test: 10 healthy + 10 fluid cases, 8,192 patches (image positive if any fluid pixel)
- Method: DCGAN (5x5 filters, 512-256-128-64 channels, 20 epochs) trained on healthy patches; test image mapped to latent space by 500 backprop steps; anomaly score A(x) = 0.9 * residual R(x) + 0.1 * discrimination D(x) (feature-matching on intermediate discriminator features; lambda = 0.1 tuned on a face dataset)
- Key results: image-level AUC: AnoGAN 0.89 (precision 0.883, sensitivity 0.728, specificity 0.893 at Youden), GAN_R 0.88, adversarial conv AE 0.73, raw discriminator output 0.72; residual alone does most of the work; additional findings looked like hyperreflective foci (not quantified)
- Code / weights / license: no official release stated; implementation adapted from github.com/bamos/dcgan-completion.tensorflow
- Useful for us: origin of "train on normals, flag deviation" generative anomaly detection; cite as historical baseline.
- Limitations / notes: only fluid evaluated; 10+10 test cases; lambda tuned on faces; slow latent optimisation (500 steps; addressed by f-AnoGAN); patch-level; authors call the gain over residual-only 'slight'.
- BibTeX:
```bibtex
@inproceedings{Schlegl2017AnoGAN,
  title     = {Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery},
  author    = {Schlegl, Thomas and Seeb{\"o}ck, Philipp and Waldstein, Sebastian M. and Schmidt-Erfurth, Ursula and Langs, Georg},
  booktitle = {Information Processing in Medical Imaging (IPMI 2017)},
  series    = {Lecture Notes in Computer Science},
  volume    = {10265},
  pages     = {146--157},
  publisher = {Springer},
  year      = {2017},
  doi       = {10.1007/978-3-319-59050-9_12}
}
```

### R221. f-AnoGAN
- Full title: f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks
- Authors: Thomas Schlegl, Philipp Seeboeck, Sebastian M. Waldstein, et al. (Langs, Schmidt-Erfurth)
- Year / Venue / Type: 2019 / Medical Image Analysis 54:30-44 / journal
- DOI / arXiv / URL: 10.1016/j.media.2019.01.010 (verified via OpenAlex); PMID 30831356
- Access: paywalled (closed per OpenAlex; no repository copy; no abstract in OpenAlex). Skipped in round 3 as truly paywalled.
- Passes: metadata only (OpenAlex re-checked 2026-10-16: closed access, no abstract)
- Modality & anatomy: retinal OCT
- Data: unverified
- Method: WGAN + learned encoder (izi_f training) for fast latent mapping; anomaly score from image + feature residuals (method description from Baur 2021 and Lagogiannis 2023 which both benchmark f-AnoGAN).
- Key results: unverified here; in Lagogiannis 2023 benchmark f-AnoGAN is only slightly above random for BraTS-T1 segmentation.
- Code / weights / license: github.com/tSchlegl/f-AnoGAN (link appears in OpenAlex affiliation metadata; not visited, licence unverified)
- Useful for us: standard generative anomaly baseline included in both major benchmarks.
- Limitations / notes: GAN training instability; poor localisation.
- BibTeX:
```bibtex
@article{Schlegl2019fAnoGAN,
  title   = {f-{AnoGAN}: Fast unsupervised anomaly detection with generative adversarial networks},
  author  = {Schlegl, Thomas and Seeb{\"o}ck, Philipp and Waldstein, Sebastian M. and Langs, Georg and Schmidt-Erfurth, Ursula},
  journal = {Medical Image Analysis},
  volume  = {54},
  pages   = {30--44},
  year    = {2019},
  doi     = {10.1016/j.media.2019.01.010}
}
```

### R222. AnoDDPM
- Full title: AnoDDPM: Anomaly Detection With Denoising Diffusion Probabilistic Models Using Simplex Noise
- Authors: Julian Wyatt, Adam Leach, Sebastian M. Schmon, Chris G. Willcocks
- Year / Venue / Type: 2022 / CVPR 2022 Workshops (NTIRE), pp. 650-656 / workshop
- DOI / arXiv / URL: https://openaccess.thecvf.com/content/CVPR2022W/NTIRE/html/Wyatt_AnoDDPM_Anomaly_Detection_With_Denoising_Diffusion_Probabilistic_Models_Using_Simplex_CVPRW_2022_paper.html ; DOI unverified
- Access: open
- Passes: 3/3 (CVF abstract page, then the CVF PDF read 2026-10-16 for data, settings and Table 1, then for limitations and code)
- Modality & anatomy: brain MRI T1w
- Data: training on NFBS repository, 125 healthy T1w (100 train / 25 test), random axial 2D slices (index 40-100), full skull; test on 22 T1w tumour scans (Centre for Clinical Brain Sciences, Edinburgh), 4 tumour slices each, bias-field corrected
- Method: partial diffusion: noise to lambda = 250 of T = 1000 (linear schedule) then denoise, so reconstruction 'heals' anomalies; multi-scale simplex noise (start frequency 2^-6, 6 octaves, decay 0.8) instead of Gaussian; Dhariwal-Nichol U-Net (128 base channels); anomaly map = squared error thresholded at 0.5. Baselines: context encoder, f-AnoGAN, Gaussian AnoDDPM.
- Key results: Table 1 (Dice / IoU / precision / recall / AUC): AnoDDPM simplex 0.383 / 0.269 / 0.373 / 0.468 / 0.863; f-AnoGAN 0.128 / 0.093 / 0.362 / 0.080 / 0.789; Gaussian AnoDDPM 0.009 / 0.004 / 0.006 / 0.032 / 0.601 (near random); context encoder 0.252 / 0.162 / 0.258 / 0.279 / 0.707. The abstract's +25.5% Dice, +17.6% IoU, +7.4% AUC are absolute differences vs f-AnoGAN.
- Code / weights / license: https://github.com/JulianWyatt/AnoDDPM (MIT licence, as stated in the paper; repository not visited; note the earlier entry had 'Julian-Wyatt')
- Useful for us: diffusion "heal and compare" is the most natural way to produce a pseudo-healthy spine image and a voxelwise deviation map; simplex noise trick relevant for large lesions (e.g. collapsed vertebrae).
- Limitations / notes: tiny test set (22 scans x 4 slices), 2D only; lambda grid-searched on the same data; slightly degraded samples with simplex noise; tumours near gyri/sulci harder; hallucinated structures (e.g. ventricles); stochastic, no averaging; no timing reported (cost scales with lambda). Gaussian noise fails, so the noise type is critical for large lesions.
- BibTeX:
```bibtex
@inproceedings{Wyatt2022AnoDDPM,
  title     = {{AnoDDPM}: Anomaly Detection With Denoising Diffusion Probabilistic Models Using Simplex Noise},
  author    = {Wyatt, Julian and Leach, Adam and Schmon, Sebastian M. and Willcocks, Chris G.},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  pages     = {650--656},
  year      = {2022}
}
```

### R223. Latent diffusion for fast brain anomaly detection
- Full title: Fast Unsupervised Brain Anomaly Detection and Segmentation with Diffusion Models
- Authors: Walter H. L. Pinaya, Mark S. Graham, Robert Gray, et al. (... Ourselin, Cardoso)
- Year / Venue / Type: 2022 / MICCAI 2022 (venue unverified; arXiv lists no journal-ref) / conference
- DOI / arXiv / URL: arXiv:2206.03461
- Access: open
- Passes: 3/3 (ar5iv full text)
- Modality & anatomy: brain MRI (FLAIR) and head CT
- Data: train 15,000 UK Biobank FLAIR (lowest lesion load); test MSLUB, BraTS, WMH challenge, UKB WMH; CT train 200 CROMIS, test CROMIS (21), KCH, CHRONIC; synthetic MedNIST sprites
- Method: VQ-VAE latent (f=4/8) + DDPM on healthy latents; per-step KL at t in [400,600] -> mask (97.5th percentile of healthy); masked "healing" from t=500; residual masked -> anomaly map; DDIM 50 steps for speed.
- Key results: best-Dice MRI (DDPM): UKB 0.232, MSLUB 0.247, BraTS 0.398, WMH 0.298 (transformer ensemble higher on some); CT DDPM f=8: 0.284/0.473/0.297; DDIM f=8 ~12 s per 100 slices vs ~4,900 s for transformer ensemble.
- Code / weights / license: not stated in paper text (MONAI generative models later; unverified)
- Useful for us: practical speed/accuracy recipe for 3D-ish spine anomaly maps; healthy-threshold calibration via percentile of healthy validation data is directly reusable for "deviation from normal".
- Limitations / notes: 2D slices; modest Dice.
- BibTeX:
```bibtex
@inproceedings{Pinaya2022FastDiffusion,
  title     = {Fast Unsupervised Brain Anomaly Detection and Segmentation with Diffusion Models},
  author    = {Pinaya, Walter H. L. and Graham, Mark S. and Gray, Robert and Da Costa, Pedro F. and Tudosiu, Petru-Daniel and Wright, Paul and Mah, Yee H. and MacKinnon, Andrew D. and Teo, James T. and Jager, Rolf and Werring, David and Rees, Geraint and Nachev, Parashkev and Ourselin, Sebastien and Cardoso, M. Jorge},
  booktitle = {Medical Image Computing and Computer Assisted Intervention -- MICCAI 2022},
  year      = {2022},
  eprint    = {2206.03461},
  archivePrefix = {arXiv},
  note      = {Proceedings details unverified}
}
```

### R224. Benchmark of unsupervised pathology detection
- Full title: Unsupervised Pathology Detection: A Deep Dive Into the State of the Art
- Authors: Ioannis Lagogiannis, Felix Meissen, Georgios Kaissis, Daniel Rueckert
- Year / Venue / Type: 2023 (2024 issue) / IEEE Transactions on Medical Imaging / journal
- DOI / arXiv / URL: 10.1109/TMI.2023.3298093; arXiv:2303.00609
- Access: open (arXiv, CC BY-NC-SA 4.0)
- Passes: 3/3 (ar5iv full text)
- Modality & anatomy: brain MRI, chest X-ray, retinal fundus
- Data: CamCAN 652 healthy (train); ATLAS 220 stroke; BraTS 2020 371; CheXpert (4,267 train / 720 test used); DDR fundus
- Method: 13 methods: reconstruction (VAE, r-VAE, f-AnoGAN, H-TAE-S), feature modelling (FAE, PaDiM, CFLOW-AD, RD), attention (ExpVAE, AMCons), self-supervised (PII, DAE, CutPaste); metrics AUROC, AP (image), AP pixel, best Dice; 3 seeds.
- Key results: feature-modelling methods dominate: BraTS-T2 FAE APi 0.87; ATLAS RD best Dice 0.22; DDR RD Dice 0.19; CheXpert FAE best (effusion AUROC 0.77). SSL pre-training small gains. Performance far from clinically useful.
- Code / weights / license: https://github.com/iolag/UPD_study/
- Useful for us: includes chest X-ray: shows anomaly detection on radiographs is hard and confounded by positioning/corruption (relevant to spine X-ray). Feature-modelling (RD/FAE) are strong cheap baselines for our normative-appearance module.
- Limitations / notes: no unified architecture; conflict of interest for FAE; age-dependent normality not modelled (which normative modelling addresses).
- BibTeX:
```bibtex
@article{Lagogiannis2023UPD,
  title   = {Unsupervised Pathology Detection: A Deep Dive Into the State of the Art},
  author  = {Lagogiannis, Ioannis and Meissen, Felix and Kaissis, Georgios and Rueckert, Daniel},
  journal = {IEEE Transactions on Medical Imaging},
  year    = {2023},
  doi     = {10.1109/TMI.2023.3298093},
  eprint  = {2303.00609},
  archivePrefix = {arXiv}
}
```

### R225. Normative modelling to parse heterogeneity in clinical cohorts
- Full title: Understanding Heterogeneity in Clinical Cohorts Using Normative Models: Beyond Case-Control Studies
- Authors: Andre F. Marquand, Iead Rezek, Jan K. Buitelaar, Christian F. Beckmann
- Year / Venue / Type: 2016 / Biological Psychiatry 80(7):552-561 / journal
- DOI / arXiv / URL: 10.1016/j.biopsych.2015.12.023 (verified via OpenAlex and Europe PMC); PMID 26927419; PMCID PMC5023321
- Access: open (CC BY; full text via Europe PMC)
- Passes: 3/3 (abstract via OpenAlex, re-checked on Europe PMC; full-text XML PMC5023321 read for methods/results and then discussion/limitations, 2026-10-16; Supplement with kernel details not read)
- Modality & anatomy: task fMRI (reward-related brain activity) + behaviour
- Data: Human Connectome Project, healthy cohort N = 491 (288 female; mean age 27, range 22-36); no diagnosed ADHD cases, ADHD hyperactivity/inattention measured with Adult Self-Report scales (means 2.37 / 3.03). Excluded high-motion subjects.
- Method: GP regression fitted separately per brainordinate, predicting reward-vs-baseline fMRI contrast (HCP gambling task) from delay-discounting AUC at $200 and $40,000 (kernel only in Supplement); 10-fold CV respecting family structure. Per-subject normative probability map: Z = (y - y_hat) / sqrt(predictive variance + normative data variance). Subject summary = 90% trimmed mean of top 1% of NPM Z-scores (block maxima), then an extreme value distribution fitted to give subject-level outlier probabilities (family not named in main text); absolute deviation = total abnormality, signed deviation for symptom correlations.
- Key results: delay discounting itself did not correlate with hyperactivity or inattention (all p > .2); 22 participants had deviating regions (FDR p < .05); negative deviance correlated with hyperactivity in the most extreme subgroups: top 1% (n=5) r=.91 p=.03, top 5% (n=25) r=.53 p=.007, top 10% (n=50) r=.31 p=.03, top 15% (n=74) r=.36 p=.002, top 20% (n=99) r=.22 p=.03; positive deviance not (p > .4); inattention not (p > .2); no region deviated in more than 3 participants (individualised abnormality patterns).
- Code / weights / license: none stated in the paper; the group's later PCNtoolkit (see [B2-02]) implements the approach (link not verified here)
- Useful for us: the conceptual template for "quantify deviation from normal anatomy": model measurement y (e.g. vertebral height, canal AP diameter, lordosis) as a function of age, sex, level, body size, and report per-patient Z-scores / centiles rather than binary abnormal flags.
- Limitations / notes: brain/psychiatry domain; authors note GP scales poorly to very large N (Bayesian polynomial regression scaled well at small accuracy cost), temporal stability of abnormality indices untested, spatial correlations not modelled; head-motion sensitivity checked (conclusions held). For us: the Z = residual / sqrt(predictive + noise variance) definition and the extreme-value summary over many measurements (e.g. all vertebral levels) transfer directly.
- BibTeX:
```bibtex
@article{Marquand2016Normative,
  title   = {Understanding Heterogeneity in Clinical Cohorts Using Normative Models: Beyond Case-Control Studies},
  author  = {Marquand, Andre F. and Rezek, Iead and Buitelaar, Jan K. and Beckmann, Christian F.},
  journal = {Biological Psychiatry},
  volume  = {80},
  number  = {7},
  pages   = {552--561},
  year    = {2016},
  doi     = {10.1016/j.biopsych.2015.12.023}
}
```

### R226. Normative modelling framework / PCNtoolkit protocol
- Full title: The normative modeling framework for computational psychiatry
- Authors: Saige Rutherford, Seyed Mostafa Kia, Thomas Wolfers, et al. (Fraza, Zabihi, ..., Marquand)
- Year / Venue / Type: 2022 / Nature Protocols 17(7):1711-1734 / protocol
- DOI / arXiv / URL: 10.1038/s41596-022-00696-5 (verified via Crossref)
- Access: paywalled (open preprint on bioRxiv exists per common knowledge; unverified)
- Passes: metadata only (abstract not in Crossref record)
- Modality & anatomy: brain MRI (cortical thickness, subcortical volumes)
- Data: unverified (large multi-site reference cohorts)
- Method: step-by-step protocol for fitting normative models (e.g. hierarchical Bayesian regression / warped Bayesian linear regression with site effects) and deriving per-subject deviation Z-scores; transfer of pretrained models to new sites (method details from general knowledge of PCNtoolkit; unverified in fetched text).
- Key results: unverified
- Code / weights / license: PCNtoolkit (Python; URL unverified)
- Useful for us: practical recipe and software for site-adjusted normative models; the same machinery can model spinal measurements vs age/sex/level/scanner.
- Limitations / notes: retrieve full text before quoting specific steps.
- BibTeX:
```bibtex
@article{Rutherford2022NormativeProtocol,
  title   = {The normative modeling framework for computational psychiatry},
  author  = {Rutherford, Saige and Kia, Seyed Mostafa and Wolfers, Thomas and Fraza, Charlotte and Zabihi, Mariam and others},
  journal = {Nature Protocols},
  volume  = {17},
  number  = {7},
  pages   = {1711--1734},
  year    = {2022},
  doi     = {10.1038/s41596-022-00696-5}
}
```

### R227. Brain charts for the human lifespan
- Full title: Brain charts for the human lifespan
- Authors: Richard A. I. Bethlehem, Jakob Seidlitz, Simon R. White, et al.
- Year / Venue / Type: 2022 / Nature 604:525-533 / journal
- DOI / arXiv / URL: 10.1038/s41586-022-04554-y (verified via OpenAlex); PMID 35388223
- Access: open (CC BY 4.0, confirmed on the Nature page)
- Passes: 3/3 (metadata, then the Nature full text read 2026-10-16 for data and methods, then for validation, clinical results and limitations. The code/tool URLs were missing from the extracted page.)
- Modality & anatomy: brain MRI morphometry across lifespan
- Data: 123,984 MRI scans from 101,457 participants in more than 100 primary studies, aged 115 days post-conception to 100 years. Controls form the reference; clinical cases are scored separately.
- Method: sex-stratified GAMLSS with a generalized gamma outcome (mu, sigma and nu modelled), fractional-polynomial age terms (powers -2 to 3), study/site random intercepts, and processing-software version as a fixed effect. Phenotypes: GMV, WMV, sGMV, ventricular CSF, total cerebrum volume, surface area, mean cortical thickness, and 34 regional volumes. New studies are scored out of sample by ML estimation of study-specific offsets, which needs N > 100 scans per study for stable centiles.
- Key results:
  - Developmental peaks: GMV at 5.9 y (95% CI 5.8-6.1), WMV at 28.7 y (28.1-29.2), sGMV at 14.4 y, TCV at 12.5 y, cortical thickness at 1.7 y.
  - Alzheimer's disease showed the largest deviation (female GMV median centile 14%, d = 0.88).
  - Centile scores were about 11.8 percentage points more heritable than raw phenotypes.
  - Longitudinal centile stability: median IQR < 0.05 over 9,306 scans from 41 studies.
  - Validated with bootstrap, jack-knife, leave-one-study-out and test-retest analyses.
- Code / weights / license: the paper states that code, model parameters and an interactive tool are available, but the URLs were not present in the extracted text (unverified).
- Useful for us: flagship example of centile/growth charts for imaging-derived phenotypes; template for "spine charts" (vertebral body height, disc height, canal diameter by age/sex/level) and for reporting a patient centile.
- Limitations / notes: data are biased toward European and North American and European-ancestry participants; fetal, neonatal and 30-40-year-old ages are under-represented; ascertainment and diagnostic heterogeneity; binary sex; robustness to poor-quality scans shown only for global phenotypes. The authors state the charts are NOT yet suitable for individual diagnosis, a caveat we must echo for spine centiles. For us: the GAMLSS recipe (generalized gamma, fractional polynomials, site random effect, out-of-sample offset with N > 100 per site) transfers directly to vertebral and disc measurements.
- BibTeX:
```bibtex
@article{Bethlehem2022BrainCharts,
  title   = {Brain charts for the human lifespan},
  author  = {Bethlehem, Richard A. I. and Seidlitz, Jakob and White, Simon R. and Vogel, Jacob W. and Anderson, Karen M. and others},
  journal = {Nature},
  volume  = {604},
  pages   = {525--533},
  year    = {2022},
  doi     = {10.1038/s41586-022-04554-y}
}
```

### R228. Mental disorders as deviations from normative functioning (normative modelling review)
- Full title: Conceptualizing mental disorders as deviations from normative functioning
- Authors: Andre F. Marquand, Seyed Mostafa Kia, Mariam Zabihi, et al. (Wolfers, Buitelaar, Beckmann)
- Year / Venue / Type: 2019 / Molecular Psychiatry 24(10):1415-1424 / review
- DOI / arXiv / URL: 10.1038/s41380-019-0441-1 (verified via OpenAlex); PMID 31201374; PMC6756106
- Access: open (hybrid OA, CC BY per OpenAlex; PDF at nature.com/articles/s41380-019-0441-1.pdf; also Radboud hdl 2066/208606)
- Passes: 1/3 (abstract; OA status confirmed via OpenAlex on 2026-10-16, but the Nature HTML/PDF and Radboud handle fetches failed, so the full text is still unread)
- Modality & anatomy: neuroimaging (general)
- Data: n/a (review)
- Method: non-technical overview of normative modelling (reference ranges analogous to paediatric growth charts), conceptual framework linking approaches, survey of applications.
- Key results: argues for individual-level deviation maps over group averages ("precision psychiatry").
- Code / weights / license: n/a
- Useful for us: citable framing for our design choice to report each patient's measurements as centiles/Z-scores against age-sex-matched normative spine data.
- Limitations / notes: psychiatry focus.
- BibTeX:
```bibtex
@article{Marquand2019Conceptualizing,
  title   = {Conceptualizing mental disorders as deviations from normative functioning},
  author  = {Marquand, Andre F. and Kia, Seyed Mostafa and Zabihi, Mariam and Wolfers, Thomas and Buitelaar, Jan K. and Beckmann, Christian F.},
  journal = {Molecular Psychiatry},
  volume  = {24},
  number  = {10},
  pages   = {1415--1424},
  year    = {2019},
  doi     = {10.1038/s41380-019-0441-1}
}
```

### R229. Statistical shape models for 3D segmentation (review)
- Full title: Statistical shape models for 3D medical image segmentation: A review
- Authors: Tobias Heimann, Hans-Peter Meinzer
- Year / Venue / Type: 2009 / Medical Image Analysis 13(4):543-563 / review
- DOI / arXiv / URL: 10.1016/j.media.2009.05.004 (verified via Crossref and OpenAlex); PMID 19525140
- Access: paywalled (closed per OpenAlex, no repository copy, no abstract in index). Skipped in round 3 as truly paywalled.
- Passes: metadata only (re-checked OpenAlex 2026-10-16; method line below is from general knowledge, not from the source)
- Modality & anatomy: general 3D CT/MRI
- Data: n/a (review)
- Method: reviews construction of point distribution models (correspondence, alignment, PCA modes), local appearance models and search algorithms (content from general knowledge; not re-read in this session).
- Key results: n/a
- Code / weights / license: n/a
- Useful for us: standard citation for SSM methodology; PCA mode coefficients (in SD units) of a vertebra/spine SSM are a natural "deviation from normal shape" score.
- Limitations / notes: pre-deep-learning; verify specific claims against full text.
- BibTeX:
```bibtex
@article{Heimann2009SSMReview,
  title   = {Statistical shape models for {3D} medical image segmentation: A review},
  author  = {Heimann, Tobias and Meinzer, Hans-Peter},
  journal = {Medical Image Analysis},
  volume  = {13},
  number  = {4},
  pages   = {543--563},
  year    = {2009},
  doi     = {10.1016/j.media.2009.05.004}
}
```

### R230. Multi-vertebrae shape+pose statistical model of the lumbar spine
- Full title: Lumbar Spine Segmentation Using a Statistical Multi-Vertebrae Anatomical Shape+Pose Model
- Authors: Abtin Rasoulian, Robert N. Rohling, Purang Abolmaesumi
- Year / Venue / Type: 2013 / IEEE Transactions on Medical Imaging 32(10):1890-1900 / journal
- DOI / arXiv / URL: 10.1109/TMI.2013.2268424 (verified via OpenAlex); PMID 23771318
- Access: paywalled (closed per OpenAlex, no repository copy). Skipped in round 3 as truly paywalled.
- Passes: 1/3 (abstract re-read via the OpenAlex inverted index on 2026-10-16; all details above confirmed: 32 subjects, lumbar CT, mean error < 2 mm, facet-injection motivation)
- Modality & anatomy: CT; lumbar vertebrae L1-L5
- Data: lumbar CT of 32 subjects
- Method: statistical multi-object model jointly capturing vertebral shape variation and inter-vertebral pose; registration-based segmentation with reduced parameter count.
- Key results: mean segmentation error < 2 mm (sufficient for facet-joint injection guidance).
- Code / weights / license: unverified
- Useful for us: shape+pose decomposition lets us separate "abnormal vertebral shape" (e.g. wedge deformity) from "abnormal alignment" (e.g. spondylolisthesis, scoliosis) when scoring deviation from normal.
- Limitations / notes: small training population (32); lumbar only; CT only.
- BibTeX:
```bibtex
@article{Rasoulian2013ShapePose,
  title   = {Lumbar Spine Segmentation Using a Statistical Multi-Vertebrae Anatomical Shape+Pose Model},
  author  = {Rasoulian, Abtin and Rohling, Robert N. and Abolmaesumi, Purang},
  journal = {IEEE Transactions on Medical Imaging},
  volume  = {32},
  number  = {10},
  pages   = {1890--1900},
  year    = {2013},
  doi     = {10.1109/TMI.2013.2268424}
}
```

### R231. Sagittal alignment norms in 300 asymptomatic adults (Vialle)
- Full title: Radiographic Analysis of the Sagittal Alignment and Balance of the Spine in Asymptomatic Subjects
- Authors: Raphael Vialle, N. Levassor, L. Rillardon, et al. (Templier, Skalli, Guigui)
- Year / Venue / Type: 2005 / Journal of Bone and Joint Surgery (Am) 87(2):260-267 / journal
- DOI / arXiv / URL: 10.2106/JBJS.D.02043 (verified via OpenAlex)
- Access: paywalled (abstract via OpenAlex inverted index)
- Passes: 1/3 (abstract re-read against the Europe PMC record, PMID 15687145, 2026-10-16; every number below confirmed; JBJS full text paywalled, not read)
- Modality & anatomy: standing sagittal radiographs of head, spine and pelvis (prospective); whole spine + pelvis
- Data: 300 asymptomatic volunteers
- Method: digitised radiographs, software measurement of lumbar lordosis, thoracic kyphosis, T9 sagittal offset, sacral slope, PI, PT, intervertebral angles, wedging.
- Key results (means +/- SD; verified against Europe PMC abstract): max lumbar lordosis 60 +/- 10 deg; sacral slope 41 +/- 8.4 deg; pelvic tilt 13 +/- 6 deg; pelvic incidence 55 +/- 10.6 deg; T9 sagittal offset 10.3 +/- 3.1 deg. Correlations: SS-PI r = 0.8; max LL-SS r = 0.86; PI-PT r = 0.66; max LL with PI, PT and max thoracic kyphosis (multivariate) r = 0.9; PI with T9 offset, SS, PT, max LL and TK (multivariate) r = 0.98. (Previous entry text 'r = 0.66-0.98 (PI with SS, LL, PT)' was a loose paraphrase: 0.9 and 0.98 are multivariate fits, not pairwise.) Ages, p values and thoracic kyphosis mean are not in the abstract.
- Code / weights / license: n/a
- Useful for us: ready-to-use adult reference means/SDs for converting automated spinopelvic measurements into Z-scores.
- Limitations / notes: European (French author group; population origin not stated in abstract); no age stratification in abstract; software not named in abstract; per-level intervertebral angles and wedging (T9-S1) are only in the paywalled full text.
- BibTeX:
```bibtex
@article{Vialle2005Sagittal,
  title   = {Radiographic Analysis of the Sagittal Alignment and Balance of the Spine in Asymptomatic Subjects},
  author  = {Vialle, Rapha{\"e}l and Levassor, Nicolas and Rillardon, Ludovic and Templier, Alexandre and Skalli, Wafa and Guigui, Pierre},
  journal = {The Journal of Bone and Joint Surgery. American Volume},
  volume  = {87},
  number  = {2},
  pages   = {260--267},
  year    = {2005},
  doi     = {10.2106/JBJS.D.02043}
}
```

### R232. Normative 3D spine shape values (Le Huec & Hasegawa)
- Full title: Normative values for the spine shape parameters using 3D standing analysis from a database of 268 asymptomatic Caucasian and Japanese subjects
- Authors: Jean Charles Le Huec, Kazuhiro Hasegawa
- Year / Venue / Type: 2016 / European Spine Journal 25(11):3630-3637 / journal
- DOI / arXiv / URL: 10.1007/s00586-016-4485-5 (verified via OpenAlex); PMID 26951168
- Access: paywalled (closed per OpenAlex); abstract readable on the Springer link page
- Passes: 1/3 (abstract read on link.springer.com, 2026-10-16; full text paywalled)
- Modality & anatomy: 3D standing analysis (imaging system not named in the abstract; EOS likely but unverified); whole spine and pelvis
- Data: 268 asymptomatic subjects: 137 Caucasian and 131 Japanese (sex/age breakdown not in the abstract)
- Method: 3D standing spinopelvic measurements; between-population comparison; linear regression of LL, PT and SS on PI
- Key results: PI, PT and SS comparable between Japanese and Caucasian groups. Regression equations (comparable in both populations): LL(L1-S1) = 0.54 x PI + 27.6; PT = 0.44 x PI - 11.4; SS = 0.54 x PI + 11.90. No means/SDs or r values in the abstract.
- Code / weights / license: n/a
- Useful for us: multi-ethnic normative reference for spinopelvic parameters; ethnicity as a covariate in our normative model.
- Limitations / notes: means, SDs and goodness of fit only in the paywalled full text; a 2017 Letter to the Editor about this paper exists (springermedicine record), not read. For us: the LL-from-PI equation gives a PI-adjusted expected lordosis, so (measured LL - predicted LL) is a deviation score; we need the residual SD from the full text to convert it to a Z-score.
- BibTeX:
```bibtex
@article{LeHuec2016Normative,
  title   = {Normative values for the spine shape parameters using {3D} standing analysis from a database of 268 asymptomatic {C}aucasian and {J}apanese subjects},
  author  = {Le Huec, Jean Charles and Hasegawa, Kazuhiro},
  journal = {European Spine Journal},
  volume  = {25},
  number  = {11},
  pages   = {3630--3637},
  year    = {2016},
  doi     = {10.1007/s00586-016-4485-5}
}
```

### R233. Normal vertebral shape range and fracture classification (Eastell)
- Full title: Classification of vertebral fractures
- Authors: Richard Eastell, Sandra L. Cedel, Heinz W. Wahner, et al. (Riggs, Melton)
- Year / Venue / Type: 1991 / Journal of Bone and Mineral Research 6(3):207-215 / journal
- DOI / arXiv / URL: 10.1002/jbmr.5650060302 (verified via OpenAlex); PMID 2035348
- Access: paywalled (abstract via OpenAlex)
- Passes: 1/3 (abstract re-read on the OUP JBMR abstract page, 2026-10-16; all numbers below confirmed; full text paywalled PDF, not read)
- Modality & anatomy: lateral spine radiographs, T4-L5 vertebral morphometry
- Data: 52 healthy women (normal range); 195 community postmenopausal women (Rochester, MN, age 47-94); 74 referred women
- Method: level-specific normal ranges of vertebral height ratios (mean +/- 3 SD) from healthy women; deformities classified by type (wedge, biconcave, compression) and grade (1, 2).
- Key results (verified): normal range = mean +/- 3 SD of level-specific shape from 52 healthy women, T4-L5. Community sample (195 postmenopausal women, age-stratified random sample, Rochester MN, age 47-94): 40 (21%) had fractures, mean 2 per affected woman, compression and wedge similar in number, grade 2 as common as grade 1. Referral sample (74 women with suspected osteoporosis): 62 (84%) with fractures, mean 3.3 per woman, wedge most common, grade 2 more common than grade 1. Type/grade distributions differed between groups (P < 0.01). Lumbar spine BMD vs mean fracture grade r = -0.33 (P < 0.05), vs fracture number r = -0.57 (P < 0.001), no relation with fracture type.
- Code / weights / license: n/a
- Useful for us: the classic example of level-specific normative height ratios with SD-based thresholds, which our CT/MRI/X-ray morphometry can reproduce automatically (anterior/middle/posterior height ratios -> Z-score per level).
- Limitations / notes: small normal sample (52), women only; abstract numbers now verified (OUP page); the per-level normal ratios themselves are only in the paywalled full text.
- BibTeX:
```bibtex
@article{Eastell1991Classification,
  title   = {Classification of vertebral fractures},
  author  = {Eastell, Richard and Cedel, Sandra L. and Wahner, Heinz W. and Riggs, B. Lawrence and Melton, L. Joseph},
  journal = {Journal of Bone and Mineral Research},
  volume  = {6},
  number  = {3},
  pages   = {207--215},
  year    = {1991},
  doi     = {10.1002/jbmr.5650060302}
}
```

### R234. Age changes in lumbar vertebrae and discs (Twomey & Taylor)
- Full title: Age Changes in Lumbar Vertebrae and Intervertebral Discs
- Authors: Lance T. Twomey, James R. Taylor
- Year / Venue / Type: 1987 / Clinical Orthopaedics and Related Research 224:97-104 / journal
- DOI / arXiv / URL: 10.1097/00003086-198711000-00013 (verified via Crossref)
- Access: paywalled (abstract via OpenAlex)
- Passes: 1/3 (abstract)
- Modality & anatomy: cadaveric lumbar spines (anatomical measurement, radiographs/sections)
- Data: 204 cadaveric lumbar spines, age 1 day to 97 years
- Method: measurements of vertebral and disc heights, endplate concavity, trabecular architecture across age.
- Key results: stature loss with age is due to vertebral (not disc) height loss; endplates become more concave and bone density falls, earlier/more in females; discs become more convex and disc height loss is unusual in normal ageing (only a minority of lower lumbar discs in elderly beyond Rolander grade 2).
- Code / weights / license: n/a
- Useful for us: key prior for our normative model: disc height should NOT be assumed to decline with normal age, so disc narrowing is a meaningful deviation; vertebral concavity increases with age (age-adjust vertebral height ratios).
- Limitations / notes: cadaveric; selection bias; old methods.
- BibTeX:
```bibtex
@article{Twomey1987AgeChanges,
  title   = {Age Changes in Lumbar Vertebrae and Intervertebral Discs},
  author  = {Twomey, Lance T. and Taylor, James R.},
  journal = {Clinical Orthopaedics and Related Research},
  volume  = {224},
  pages   = {97--104},
  year    = {1987},
  doi     = {10.1097/00003086-198711000-00013}
}
```

### R235. Radiographic reference values for lumbar disc height and vertebral concavity by age and sex
- Full title: Radiographic Changes in the Lumbar Intervertebral Discs and Lumbar Vertebrae With Age
- Authors: Zengwu Shao, Gerhard Rompe, Marcus Schiltenwolf
- Year / Venue / Type: 2002 / Spine 27(3):263-268 / journal
- DOI / arXiv / URL: 10.1097/00007632-200202010-00013 (verified via Crossref); PMID 11805689
- Access: paywalled (abstract via OpenAlex)
- Passes: 1/3 (abstract via OpenAlex inverted index, re-read 2026-10-16. Title confirmed exactly as above by OpenAlex/Crossref metadata, PMID 11805689. The Heidelberg catalogue title variant flagged earlier is not supported. Europe PMC was still rate-limited and PubMed/LWW were blocked, so the numbers have only been cross-checked against the inverted index. The index paraphrase says concavity changes were 'greater in men than in women', which conflicts with the per-sex percentages below; resolve from the full text before quoting.)
- Modality & anatomy: lateral lumbar radiographs; T12-S1
- Data: 607 women (20-87 y) and 633 men (20-92 y)
- Method: new disc height measurement protocol (precision 3.9%); concavity index = central / anterior vertebral height; osteophyte prevalence.
- Key results (inverted index, re-read twice; numbers consistent across both reads): disc heights increased with age between 20 and 69 y by 4.6-6.9% (men) and 4.7-8.4% (women) (the per-decade or per-level basis of these ranges is not clear from the index); concavity index decreased linearly with age (0.9-1.5% men, 1.6-3.2% women); osteophyte prevalence by age/sex was tabulated, but the 'more common in men' direction is not confirmed in the 2026-10-16 re-read. Still verify against full text.
- Code / weights / license: n/a
- Useful for us: large age- and sex-stratified X-ray reference database for disc height and vertebral concavity; corroborates Twomey that normal ageing does not reduce disc height; concavity index definition reusable.
- Limitations / notes: single-centre German population; radiographic projection effects.
- BibTeX:
```bibtex
@article{Shao2002Radiographic,
  title   = {Radiographic Changes in the Lumbar Intervertebral Discs and Lumbar Vertebrae With Age},
  author  = {Shao, Zengwu and Rompe, Gerhard and Schiltenwolf, Marcus},
  journal = {Spine},
  volume  = {27},
  number  = {3},
  pages   = {263--268},
  year    = {2002},
  doi     = {10.1097/00007632-200202010-00013}
}
```

### R236. Population reference range for lumbar spinal canal size (CT)
- Full title: Population reference range for developmental lumbar spinal canal size
- Authors: James F. Griffith, Junbin Huang, Sheung-Wai Law, et al. (Xiao, Leung, Wang, Shi)
- Year / Venue / Type: 2016 / Quantitative Imaging in Medicine and Surgery 6(6):671-679 / journal
- DOI / arXiv / URL: 10.21037/qims.2016.12.17 (verified via Crossref)
- Access: open (CC BY-NC-ND 4.0, full text HTML at qims.amegroups.org/article/view/13035/13440)
- Passes: 2/3 (abstract via OpenAlex; full-text HTML read 2026-10-16 for methods, text-reported results and caveats; per-level Tables 2-4 and Figs S1-S3 are images, values not extracted)
- Modality & anatomy: abdominopelvic CT; lumbar canal L1-L5
- Data: 1,080 ambulatory patients undergoing abdominopelvic CT (540 M / 540 F; 90 per sex per 10-year band, age 21-80; mean age ~50.5 y; SD 17 from abstract, recruitment years 2014-2015 not re-confirmed), Hong Kong, >99% ethnically Chinese. Exclusions: non-Chinese names, dwarfism or scoliosis, prior lumbar surgery, childhood chronic inflammatory conditions, major lumbar abnormality (fracture, dysraphism). Ethics CRE-2013.058.
- Method: 64-slice MDCT (GE LightSpeed VCT), 0.6 mm bone-window reconstructions; axial slice at mid-pedicle level L1-L5. Canal CSA by semi-automated seed-growing segmentation with manual correction (software unnamed); AP depth = posterior vertebral body margin to neural arch at spinous-process base; width = inner pedicle to inner pedicle; vertebral body CSA by thresholding + manual edit. Single operator; intra-operator ICC 0.85-0.96 (20 subjects); computerised vs manual agreement 0.80-0.95. Height/weight recorded; level- and sex-specific reference ranges.
- Key results (full text): canal CSA smallest at L3 in both sexes (~9% smaller than L1, ~23% smaller than L5); smallest-vs-largest quartile difference ~34% CSA, ~24% depth, ~22% width; 'smallest 25%' thresholds CSA < 212 mm2 (M) / < 213 mm2 (F) (level not explicit in text) and AP depth < 13 mm (M) / < 14 mm (F) at L2; canal CSA larger in males at all levels except L2, but after height/weight adjustment larger in females at L1-L3; canal width larger in males at all levels even after adjustment; no detectable change of canal CSA with age; weak positive correlation with height; vertebral body CSA increases with age (about twice as fast in females); canal CSA ~1/5 of vertebral body CSA, ratio consistently larger in females. Males taller (168.1 +/- 6.8 vs 157.0 +/- 5.9 cm).
- Code / weights / license: n/a
- Useful for us: directly usable normative table for canal CSA/AP depth by level and sex from CT; supports normalising canal size by vertebral body size (body-size-independent deviation score) for developmental stenosis.
- Limitations / notes: single Chinese population (authors say each population needs its own range); patients undergoing abdominopelvic CT, 'clearly not healthy' (argued valid for developmental size); 'smallest 25%' cut-off admitted arbitrary, no accepted definition of abnormal developmental size; single operator, reliability on 20 subjects; bony canal on CT not MRI (MRI soft-tissue canal differs). Open: per-level tables need manual transcription from the PDF before use as a normative prior.
- BibTeX:
```bibtex
@article{Griffith2016LumbarCanal,
  title   = {Population reference range for developmental lumbar spinal canal size},
  author  = {Griffith, James F. and Huang, Junbin and Law, Sheung-Wai and Xiao, Fan and Leung, Jason C. S. and Wang, Defeng and Shi, Lin},
  journal = {Quantitative Imaging in Medicine and Surgery},
  volume  = {6},
  number  = {6},
  pages   = {671--679},
  year    = {2016},
  doi     = {10.21037/qims.2016.12.17}
}
```

### R237. Population reference range for cervical spinal canal size (CT)
- Full title: Developmental cervical spinal canal size: population reference range
- Authors: James F. Griffith, Jeremiah C. H. Lee
- Year / Venue / Type: 2024 / Quantitative Imaging in Medicine and Surgery 14(4):3044-3059 / journal
- DOI / arXiv / URL: 10.21037/qims-22-1395 (verified via Crossref/OpenAlex)
- Access: open (CC BY-NC-ND 4.0; HTML full text at qims.amegroups.org/article/view/122776/html)
- Passes: 3/3 (abstract, then the full-text HTML read 2026-10-16 for methods and the per-level Table 1 values, then the discussion and limitations; quartile cut-offs are only in Figs 2-8 and were not extracted)
- Modality & anatomy: neck CT; cervical canal C3-C7
- Data: 522 ambulatory patients undergoing routine neck CT (256 M / 266 F), mean age 55 +/- 18 y (20-89), at least 30 per sex in each of 7 age bands. Hong Kong, prospective. Patients with non-Chinese names were excluded. CT indications: cancer 60%, trauma 11%, nerve palsy 8%, thyroid 6%, vascular 5%. Excluded: scoliosis, prior cervical surgery, childhood chronic inflammatory illness, fracture, dysraphism, OPLL. Ethics CRE-2016.527.
- Method: 64-slice MDCT, 0.6 mm reconstructions, true axial plane, C3-C7 (2,610 levels). Manual segmentation in ITK-SNAP 3.6.0 by one of two operators. Measured canal CSA, AP diameter, width and AP/width ratio, plus vertebral body CSA, AP and width, and the body/canal AP ratio. Inter-rater ICC 0.924 (CSA) and 0.976 (lengths). SPSS 26.
- Key results: canal mean +/- SD, male / female:

  | Level | CSA (mm2) | AP (mm) | Width (mm) |
  |---|---|---|---|
  | C3 | 259.6+/-38.6 / 242.1+/-34 | 13.83+/-1.33 / 13.35+/-1.28 | 23.66+/-1.63 / 22.56+/-1.56 |
  | C4 | 261.4+/-39.6 / 241.6+/-33.9 | 13.35+/-1.33 / 12.92+/-1.18 | 26.03+/-2.06 / 24.47+/-1.75 |
  | C5 | 276.0+/-41.5 / 252.6+/-38.4 | 13.75+/-1.34 / 13.15+/-1.28 | 27.39+/-2.2 / 25.72+/-1.99 |
  | C6 | 282.1+/-44.5 / 254.0+/-36.2 | 14.16+/-1.43 / 13.50+/-1.39 | 26.94+/-2.31 / 25.60+/-1.89 |
  | C7 | 263.0+/-38.3 / 237.9+/-33.4 | 14.21+/-1.42 / 13.37+/-1.29 | 25.52+/-2.26 / 24.42+/-2.05 |

  - AP/width ratio is about 0.50-0.59 and smallest at C5.
  - Vertebral body CSA rises from C3 to C7 (M 327.3 to 489.0, F 270.6 to 405.1 mm2).
  - All canal measures are larger in males (p < 0.0001), but canal CSA relative to vertebral body is larger in females.
  - Correlation with height is weak (canal CSA r = 0.25 M / 0.36 F).
  - Canal CSA vs age: r = -0.23 M / -0.33 F. Vertebral body CSA vs age: r = 0.43 / 0.46.
  - Variation in C5 CSA between smallest and largest is about 164-168%.
  - The smallest 25% is proposed as a 'developmentally small canal'; the cut-offs are in the figures only.
- Code / weights / license: n/a
- Useful for us: cervical counterpart of [B4-09] for canal-size deviation scores.
- Limitations / notes (the authors' own): CT, not MRI (MRI values are about 8% smaller); hospital population; foramina not measured; no cord size; no CT-MRI validation; the 25% cut-off is arbitrary.

  Internal inconsistencies in the paper:
  - The abstract says canal AP increases with age, but the results show a slight decrease.
  - Weight is said to have no influence, but female weight vs CSA has r = 0.23 (P < 0.001).
  - CSA variation is given as 166% in one place and 164-168% in another.
  - The significance threshold is printed as 'P < 0.5' (typo).

  For us: Table 1 gives directly usable means and SDs for per-level Z-scores of cervical canal size on CT.
- BibTeX:
```bibtex
@article{Griffith2024CervicalCanal,
  title   = {Developmental cervical spinal canal size: population reference range},
  author  = {Griffith, James F. and Lee, Jeremiah C. H.},
  journal = {Quantitative Imaging in Medicine and Surgery},
  volume  = {14},
  number  = {4},
  pages   = {3044--3059},
  year    = {2024},
  doi     = {10.21037/qims-22-1395}
}
```

### R238. Age-based normative sagittal alignment from full-body radiographs (Iyer)
- Full title: Variations in Sagittal Alignment Parameters Based on Age: A Prospective Study of Asymptomatic Volunteers Using Full-Body Radiographs
- Authors: Sravisht Iyer, Lawrence G. Lenke, Venu M. Nemani, et al. (Albert, Sides, Metz, Cunningham, Kim)
- Year / Venue / Type: 2016 / Spine 41(23):1826-1836 / journal
- DOI / arXiv / URL: 10.1097/BRS.0000000000001642 (verified via Crossref and Weill Cornell VIVO record); PMID 27111763; published 1 Dec 2016
- Access: paywalled (abstract via OpenAlex)
- Passes: 1/3 (abstract re-read against the Weill Cornell VIVO record, 2026-10-16; all numbers confirmed; full text paywalled, not read)
- Modality & anatomy: standing full-body radiographs (EOS-type); occiput to feet
- Data: 115 asymptomatic adults (prospective cross-sectional), mean age 50.1 (22-78), mean BMI 28; NDI 3.4 +/- 4.4, ODI 1.7 +/- 4.9; level of evidence 4
- Method: measured CL (C2-C7), O-C2, TK (T2-T12), T2-T5, TL, LL (L1-S1), SS, PT, PI, PI-LL, knee flexion, global sagittal angle, T1-pelvic angle, C2/C7/basion SVAs; age-group comparison and Pearson correlations.
- Key results (abstract verified): correlations with age: global sagittal angle r = 0.56, C7 SVA r = 0.46, T1PA r = 0.44, knee flexion r = 0.42 (all P < 0.001); cervical lordosis r = -0.34 (P = 0.001) and listed among parameters that increased with age; lumbar lordosis r = +0.212 (P = 0.039) and described as decreasing with age. The signs are consistent with the text only if lordosis is recorded as a negative angle (more negative = more lordotic), so CL increases and LL decreases with age; this convention is our inference, confirm in full text before quoting signs.
- Code / weights / license: n/a
- Useful for us: supports age-dependent normative expectations for global alignment (SVA, T1PA increase with age even in asymptomatic people), so our deviation scores must be age-adjusted to avoid over-calling malalignment in the elderly.
- Limitations / notes: small n; single centre (US).
- BibTeX:
```bibtex
@article{Iyer2016SagittalAge,
  title   = {Variations in Sagittal Alignment Parameters Based on Age: A Prospective Study of Asymptomatic Volunteers Using Full-Body Radiographs},
  author  = {Iyer, Sravisht and Lenke, Lawrence G. and Nemani, Venu M. and Albert, Todd J. and Sides, Brenda A. and Metz, Lionel N. and Cunningham, Matthew E. and Kim, Han Jo},
  journal = {Spine},
  volume  = {41},
  number  = {23},
  pages   = {1826--1836},
  year    = {2016},
  doi     = {10.1097/BRS.0000000000001642}
}
```

### R239. Whole-axial-skeleton standing alignment relative to the gravity line (Hasegawa)
- Full title: Standing sagittal alignment of the whole axial skeleton with reference to the gravity line in humans
- Authors: Kazuhiro Hasegawa (corresponding), Masashi Okamoto, Shun Hatsushikano, Haruka Shimoda, Masatoshi Ono, Takao Homma, Kei Watanabe
- Year / Venue / Type: 2017 / Journal of Anatomy 230(5):619-630 / journal
- DOI / arXiv / URL: 10.1111/joa.12586 (OpenAlex); PMID 28127750; PMC5382592
- Access: open (hybrid OA, CC BY per OpenAlex)
- Passes: 1/3 (abstract via the OpenAlex inverted index, 2026-10-16; the Wiley full text and PDF could not be fetched and PMC is CAPTCHA-blocked; added in pass 2 from this file's gaps list)
- Modality & anatomy: EOS slot-scanning biplanar radiography with a force plate (gravity line through the centre of pressure); head to feet
- Data: 136 healthy Japanese adults (40 men, 96 women), mean age 39.7, range 20-69
- Method: positions of skeletal landmarks measured relative to the force-plate gravity line (GL); comparison across age decades
- Key results (inverted-index reconstruction; magnitudes consistent, DIRECTIONS NOT VERIFIED): acoustic meati 0.0 cm from the GL; thoracic kyphosis apex (T7) 5.0 cm posterior; lumbar lordosis apex (L4) 0.6 cm anterior; hip axis 1.4 cm; knee 2.4 cm; ankle 4.8 cm from the GL. With age the trunk stoops, compensated by increased cervical lordosis, pelvic tilt and knee/ankle flexion; cervical lordosis and PT keep the gaze horizontal.
- Code / weights / license: n/a
- Useful for us: whole-body normative reference that links global balance to gravity. It supports age-adjusted norms (with Iyer [B4-11]) and shows that compensations (PT, CL, knee flexion) must be read together, not as isolated abnormalities.
- Limitations / notes: needs a force plate and EOS; mostly women; Japanese only; ages 20-69. Directions and spinopelvic means must be verified in the full text before quoting.
- BibTeX:
```bibtex
@article{Hasegawa2017GravityLine,
  title   = {Standing sagittal alignment of the whole axial skeleton with reference to the gravity line in humans},
  author  = {Hasegawa, Kazuhiro and Okamoto, Masashi and Hatsushikano, Shun and Shimoda, Haruka and Ono, Masatoshi and Homma, Takao and Watanabe, Kei},
  journal = {Journal of Anatomy},
  volume  = {230},
  number  = {5},
  pages   = {619--630},
  year    = {2017},
  doi     = {10.1111/joa.12586}
}
```

## 06. Reviews, reporting guidelines, validation and deployment

#### B. Reporting and evaluation guidelines

### R240. CLAIM 2024 update
- Full title: Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update
- Authors: Tejani AS, Klontzas ME, Gatti AA, et al. (with Mongan JT, Moy L, Park SH, Kahn CE Jr; CLAIM 2024 Update Panel)
- Year / Venue / Type: 2024 / Radiology: Artificial Intelligence 6(4):e240300 / reporting guideline
- DOI / arXiv / URL: 10.1148/ryai.240300 ; https://pubs.rsna.org/doi/10.1148/ryai.240300
- Access: open (RSNA landing page and checklist .docx supplement)
- Passes: 3/3 (publisher page read twice for metadata and key features; third read of the RSNA full text on 2026-10-16 extracting all 44 items one by one)
- Modality & anatomy: all medical imaging AI
- Data: not applicable. Delphi panel of 72 members, two survey rounds
- Method: modified Delphi update of CLAIM 2020
- Key results: 44 items. Each item answered Yes / No / Not applicable, with page/line numbers. "Reference standard" replaces "ground truth". The panel discourages "validation" in favour of "internal testing" and "external testing". Former item 11 (data dictionary) removed. New item 13 covers the image acquisition protocol. Radiomics/pathomics explicitly out of scope.
- Item-by-item (CLAIM 2024, from the RSNA full text; our planned response in brackets):
  - Title/Abstract: 1 identify as AI study and name technique [title: deep learning]; 2 structured abstract incl. design, data, partitions, statistics, results, data/code availability.
  - Introduction: 3 background, current practice, intended role of the AI; 4 aims/objectives/hypotheses, ideally a priori.
  - Study design: 5 prospective vs retrospective [retrospective, public datasets]; 6 goal, intended use (triage/diagnosis), prediction target [decision support + abstention/rescan request].
  - Data: 7 data sources incl. public/synthetic and fit to target population; 8 inclusion/exclusion and case selection (consecutive/random/convenience); 9 preprocessing steps, software, settings; 10 selection of data subsets (crops, slices, report segments); 11 de-identification and privacy compliance; 12 missing data handling and imputation bias; 13 image acquisition protocol with reproducible parameters (NEW in 2024) [tabulate MRI sequences/CT kernels/X-ray views per dataset].
  - Reference standard: 14 definition and annotator guidelines ("reference standard" replaces "ground truth"); 15 rationale and its errors/biases; 16 annotators: number, qualifications, training; 17 test-set annotation method, tools and versions, any NLP label extraction; 18 inter-/intrarater variability and disagreement resolution.
  - Data partitions: 19 train/tuning/test split, proportions, justification ("tuning" preferred over "validation"); 20 partition level (patient-level or higher) to prevent leakage.
  - Testing data: 21 intended test sample size and how determined.
  - Model: 22 architecture in reproducible detail or code; 23 libraries, frameworks, versions, hardware; 24 parameter initialisation and transfer-learning source.
  - Training: 25 augmentation, convergence monitoring, stopping, hyperparameters, loss; 26 final-model selection; 27 ensemble components and combination [nnU-Net 5-fold ensemble].
  - Evaluation: 28 metrics and their fit to the clinical question, comparison with prior models; 29 statistical uncertainty (SD/CI), tests, software versions; 30 robustness/sensitivity analysis; 31 explainability methods and their validation; 32 internal testing performance vs training; 33 external testing data and differences, or justification if none; 34 trial registration if applicable.
  - Results: 35 numbers included/excluded with flowchart; 36 demographics and clinical characteristics per partition, bias sources; 37 performance vs reference standard on all partitions and subgroups with uncertainty; 38 diagnostic accuracy with CIs, calibration, class-imbalance handling [calibration plots + risk-coverage]; 39 failure analysis incl. confusion matrix and error examples.
  - Discussion: 40 limitations (methods, bias, uncertainty, generalisability); 41 implications for practice, intended use, translation barriers.
  - Other: 42 pointer to full protocol/technical details; 43 access to software, trained models, data and conditions; 44 funding, funder role, author independence.
  - Changes vs 2020 confirmed: NA answer option added for every item, page/line numbers for Yes and explanations for No/NA encouraged; 2020 item 11 (data elements / data dictionary) deleted; item 13 new; terminology changed in items 14, 19, 32, 33; radiomics/pathomics out of scope. Mapping of other items to 2020 numbering not given in the text.
- Code / weights / license: checklist .docx supplement (ryai240300_CLAIMchecklist.docx)
- Useful for us: the primary reporting checklist for the arXiv paper. Attach a completed CLAIM 2024 checklist as a supplement, and use its vocabulary ("reference standard", "internal/external testing") in the text.
- Limitations / notes: Klontzas (Diagn Interv Radiol 2025, doi 10.4274/dir.2024.242849) notes that many papers claiming CLAIM adherence lacked a completed checklist, citing Koçak et al. 2024.
- BibTeX:
```bibtex
@article{Tejani2024CLAIM,
  title   = {Checklist for Artificial Intelligence in Medical Imaging ({CLAIM}): 2024 Update},
  author  = {Tejani, Ali S. and Klontzas, Michail E. and Gatti, Anthony A. and Mongan, John T. and Moy, Linda and Park, Seong Ho and Kahn, Jr., Charles E.},
  journal = {Radiology: Artificial Intelligence},
  volume  = {6},
  number  = {4},
  pages   = {e240300},
  year    = {2024},
  doi     = {10.1148/ryai.240300}
}
```

### R241. CLAIM 2020 (original)
- Full title: Checklist for Artificial Intelligence in Medical Imaging (CLAIM): A Guide for Authors and Reviewers
- Authors: Mongan J, Moy L, Kahn CE Jr
- Year / Venue / Type: 2020 / Radiology: Artificial Intelligence 2(2):e200029 / editorial and reporting guideline
- DOI / arXiv / URL: 10.1148/ryai.2020200029
- Access: open
- Passes: 2/3 (landing page read; full checklist items not read item by item)
- Modality & anatomy: all medical imaging AI
- Data: not applicable
- Method: expert adaptation of STARD, in EQUATOR format
- Key results: 42 items covering title/abstract, introduction, methods (study design, data, ground truth, partitions, model, training, evaluation), results, discussion and other information (registration, code, funding).
- Code / weights / license: not applicable
- Useful for us: cite as the original CLAIM when citing the 2024 update. It shows why the terminology changed.
- Limitations / notes: superseded by G01.
- BibTeX:
```bibtex
@article{Mongan2020CLAIM,
  title   = {Checklist for Artificial Intelligence in Medical Imaging ({CLAIM}): A Guide for Authors and Reviewers},
  author  = {Mongan, John and Moy, Linda and Kahn, Jr., Charles E.},
  journal = {Radiology: Artificial Intelligence},
  volume  = {2},
  number  = {2},
  pages   = {e200029},
  year    = {2020},
  doi     = {10.1148/ryai.2020200029}
}
```

### R242. TRIPOD+AI
- Full title: TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods
- Authors: Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, Ghassemi M, Liu X, Reitsma JB, van Smeden M, Boulesteix AL, Camaradou JC, Celi LA, Denaxas S, Denniston AK, Glocker B, Golub RM, Harvey H, Heinze G, Hoffman MM, Kengne AP, Lam E, Lee N, Loder EW, Maier-Hein L, Mateen BA, McCradden MD, Oakden-Rayner L, Ordish J, Parnell R, Rose S, Singh K, Wynants L, Logullo P (34 authors, per BMJ page)
- Year / Venue / Type: 2024 / BMJ 385:e078378 / reporting guideline
- DOI / arXiv / URL: 10.1136/bmj-2023-078378 ; published 16 Apr 2024; green OA copy https://discovery.ucl.ac.uk/id/eprint/10191161
- Access: open (CC BY 4.0)
- Passes: 3/3 (BMJ full text summarised; BMJ page re-read 2026-10-16 for authors, Delphi numbers and section structure; UCL Discovery published PDF read for Table 2 item-by-item and Table 3 abstract items)
- Modality & anatomy: any clinical prediction model, including image-based ones
- Data: Delphi round 1 (19 Apr-13 May 2021): 292 invited, 170 completed (8 partial), 22 countries; round 2 (16 Dec 2021-17 Jan 2022): 395 invited, 200 completed (15 partial), 27 countries; consensus meeting 5 Jul 2022 with 28 participants (one non-voting)
- Method: Delphi plus consensus meeting; supersedes TRIPOD 2015
- Key results: 27 main items expanded to 52 subitems, plus a 13-item TRIPOD+AI for Abstracts checklist. Fairness is embedded throughout, including performance in key subgroups such as sociodemographic groups. New open-science item (18: funding, conflicts, protocol, registration, data and code sharing) and new patient and public involvement item (19).
- Item-by-item (Table 2; D = development, E = evaluation, D;E = both): 1 title (develop/evaluate, population, outcome); 2 abstract per TRIPOD+AI for Abstracts; 3a context, purpose, existing models; 3b target population, place in care pathway, intended users; 3c known health inequalities; 4 objectives; 5a data sources and representativeness; 5b dates; 6a setting, centres; 6b eligibility; 6c treatments; 7 preprocessing and quality checks incl. across sociodemographic groups; 8a outcome definition and consistency across groups; 8b outcome-assessor qualifications/demographics; 8c blinding of outcome assessment; 9a choice of initial predictors (D); 9b predictor definitions, timing, blinding; 9c predictor-assessor qualifications; 10 sample size rationale; 11 missing data; 12a data use and partitioning (D); 12b predictor handling (D); 12c model type, building steps, hyperparameter tuning, internal validation (D); 12d heterogeneity across clusters; 12e performance measures, plots, comparisons; 12f model updating (E); 12g how predictions were computed for evaluation (E); 13 class imbalance and recalibration; 14 fairness approaches; 15 output type and threshold setting (D); 16 development vs evaluation data differences; 17 ethics; 18a-f funding, conflicts, protocol, registration, data availability, code availability; 19 patient and public involvement; 20a participant flow; 20b characteristics incl. by demographic group; 20c predictor/outcome distributions vs development data (E); 21 participants and events per analysis; 22 full model details for third-party use (D); 23a performance with CIs incl. key subgroups; 23b heterogeneity across clusters; 24 model updating results (E); 25 interpretation incl. fairness; 26 limitations; 27a handling poor-quality or unavailable input data in implementation (D); 27b user interaction and expertise needed (D); 27c next steps for applicability/generalisability.
- TRIPOD+AI for Abstracts (13 items; 7 and 10 development only): 1 identification; 2 context/rationale; 3 objectives; 4 data sources; 5 eligibility and setting; 6 outcome and horizon; 7 model type, building steps, internal validation; 8 performance measures; 9 participants and events; 10 predictors in final model; 11 performance with CIs; 12 interpretation; 13 registration.
- Code / weights / license: not applicable
- Useful for us (item 27a is a direct reporting hook for our 'request a better scan' abstention behaviour; items 7, 14, 23a for subgroup/fairness reporting across sex, age, scanner vendor): relevant to any output framed as a prediction or risk estimate (e.g. a deviation-from-normal score). Use its subgroup-performance and open-science items.
- Limitations / notes: written for prediction models; CLAIM is the better fit for the image-analysis parts.
- BibTeX:
```bibtex
@article{Collins2024TRIPODAI,
  title   = {{TRIPOD+AI} statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods},
  author  = {Collins, Gary S. and Moons, Karel G. M. and Dhiman, Paula and others},
  journal = {BMJ},
  volume  = {385},
  pages   = {e078378},
  year    = {2024},
  doi     = {10.1136/bmj-2023-078378}
}
```

### R243. STARD-AI
- Full title: The STARD-AI reporting guideline for diagnostic accuracy studies using artificial intelligence
- Authors: Sounderajah V, Guni A, Liu X, et al. (STARD-AI Steering Committee)
- Year / Venue / Type: 2025 / Nature Medicine 31(10):3283-3289 / reporting guideline
- DOI / arXiv / URL: 10.1038/s41591-025-03953-8 ; PMID 40954311
- Access: open (White Rose repository record); publisher version may be paywalled
- Passes: 2/3 (EQUATOR record and White Rose record; full checklist not read)
- Modality & anatomy: diagnostic accuracy studies using AI
- Data: modified Delphi with more than 240 international stakeholders, then a consensus meeting
- Method: extension of STARD 2015
- Key results: 18 new or modified items on top of STARD 2015, covering dataset practices, the AI index test and its evaluation, and algorithmic bias and fairness.
- Code / weights / license: not applicable
- Useful for us: if we report sensitivity and specificity for findings such as fracture, stenosis or listhesis, STARD-AI is the matching checklist. Use it alongside CLAIM.
- Limitations / notes: protocol published earlier: Sounderajah et al., BMJ Open 2021 (PMC8240576).
- BibTeX:
```bibtex
@article{Sounderajah2025STARDAI,
  title   = {The {STARD-AI} reporting guideline for diagnostic accuracy studies using artificial intelligence},
  author  = {Sounderajah, Viknesh and Guni, Ahmad and Liu, Xiaoxuan and others},
  journal = {Nature Medicine},
  volume  = {31},
  number  = {10},
  pages   = {3283--3289},
  year    = {2025},
  doi     = {10.1038/s41591-025-03953-8}
}
```

### R244. DECIDE-AI
- Full title: Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI
- Authors: Vasey B, Nagendran M, Campbell B, et al. (DECIDE-AI expert group)
- Year / Venue / Type: 2022 / Nature Medicine 28(5):924-933 (also BMJ 2022;377:e070904) / reporting guideline
- DOI / arXiv / URL: 10.1038/s41591-022-01772-9 ; PMID 35585198
- Access: open (Oxford-hosted PDF)
- Passes: 3/3 full text (EQUATOR record, then PDF for item details and limitations)
- Modality & anatomy: any AI clinical decision support at early live clinical evaluation
- Data: two-round Delphi (123 then 138 participants), consensus meeting (16), qualitative evaluation (16)
- Method: modified Delphi
- Key results: 17 AI-specific items (28 subitems) and 10 generic items. Covers the AI system and its version, implementation and workflow, safety and errors (definition, rate, cause, correctability), human factors and usability, and human-AI agreement and reasons for overriding the AI.
- Code / weights / license: not applicable
- Useful for us: the right frame for any small user study of the browser prototype (usability, error analysis, how users react to "please re-scan" prompts).
- Limitations / notes: aimed at live clinical evaluation; a research prototype covers only part of it.
- BibTeX:
```bibtex
@article{Vasey2022DECIDEAI,
  title   = {Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: {DECIDE-AI}},
  author  = {Vasey, Baptiste and Nagendran, Myura and Campbell, Bruce and others},
  journal = {Nature Medicine},
  volume  = {28},
  number  = {5},
  pages   = {924--933},
  year    = {2022},
  doi     = {10.1038/s41591-022-01772-9}
}
```

### R245. CONSORT-AI
- Full title: Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension
- Authors: Liu X, Cruz Rivera S, Moher D, et al. (SPIRIT-AI and CONSORT-AI Working Group)
- Year / Venue / Type: 2020 / Nature Medicine 26(9):1364-1374 / reporting guideline
- DOI / arXiv / URL: 10.1038/s41591-020-1034-x
- Access: open
- Passes: 2/3 (abstract and development details read)
- Modality & anatomy: randomised trials of AI interventions
- Data: 29 candidate items; Delphi of 103; consensus meeting of 31; pilot with 34
- Method: Delphi extension of CONSORT 2010
- Key results: 14 new items: description of the AI intervention and required skills, setting, handling of inputs and outputs, human-AI interaction, and analysis of error cases.
- Code / weights / license: not applicable
- Useful for us: cite in the discussion as the standard any future prospective trial would need to meet; its "input data quality / handling of poor-quality input" item supports our ask-for-a-better-scan feature.
- Limitations / notes: trials only; not directly applicable to a retrospective study.
- BibTeX:
```bibtex
@article{Liu2020CONSORTAI,
  title   = {Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the {CONSORT-AI} extension},
  author  = {Liu, Xiaoxuan and Cruz Rivera, Samantha and Moher, David and Calvert, Melanie J. and Denniston, Alastair K.},
  journal = {Nature Medicine},
  volume  = {26},
  number  = {9},
  pages   = {1364--1374},
  year    = {2020},
  doi     = {10.1038/s41591-020-1034-x}
}
```

### R246. SPIRIT-AI
- Full title: Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension
- Authors: Cruz Rivera S, Liu X, Chan AW, et al.
- Year / Venue / Type: 2020 / BMJ 370:m3210 (published at the same time in Nature Medicine, citation for that version unverified here) / reporting guideline
- DOI / arXiv / URL: 10.1136/bmj.m3210
- Access: open
- Passes: 3/3 (abstract and development summary; BMJ full text read 2026-10-16 for the item list, then for the process and limitations; the Nature Medicine co-publication citation is still unverified)
- Modality & anatomy: trial protocols for AI interventions
- Data: steering group of 15; Delphi with 169 invited, 103 responses in round 1 and 91 in round 2; consensus meeting of 31 stakeholders (80% inclusion threshold); pilot with 34 participants
- Method: Delphi extension of SPIRIT 2013
- Key results: 15 items: 12 extensions and 3 elaborations.
  - Elaborations: 1(i) AI and model type in the title/abstract; 1(ii) intended use and disease context; 10(i) participant eligibility.
  - Extensions: 6a(i) place in the clinical pathway and intended users; 6a(ii) prior validation evidence; 9 integration requirements; 10(ii) input-data eligibility; 11a(i) software version; 11a(ii) input acquisition and pre-processing; 11a(iii) how poor-quality or unavailable input data are assessed and handled; 11a(iv) human-AI interaction and required expertise; 11a(v) the AI output; 11a(vi) how outputs feed decisions; 22 error-analysis plan; 29 access to the AI or its code.
- Code / weights / license: not applicable
- Useful for us: cite with CONSORT-AI when we describe the evaluation road map.
- Limitations / notes: protocol guideline only. Only 7 AI trials existed at development; continuously evolving systems and 'AI as therapy' are excluded; minimum reporting, not methods. Item 11a(iii) directly matches our 'poor input, request a better scan' behaviour (as does TRIPOD+AI 27a).
- BibTeX:
```bibtex
@article{CruzRivera2020SPIRITAI,
  title   = {Guidelines for clinical trial protocols for interventions involving artificial intelligence: the {SPIRIT-AI} extension},
  author  = {Cruz Rivera, Samantha and Liu, Xiaoxuan and Chan, An-Wen and Denniston, Alastair K. and Calvert, Melanie J.},
  journal = {BMJ},
  volume  = {370},
  pages   = {m3210},
  year    = {2020},
  doi     = {10.1136/bmj.m3210}
}
```

### R247. Metrics Reloaded
- Full title: Metrics reloaded: recommendations for image analysis validation
- Authors: Maier-Hein L, Reinke A, Godau P, et al.
- Year / Venue / Type: 2024 / Nature Methods 21(2):195-212 / consensus recommendation
- DOI / arXiv / URL: 10.1038/s41592-023-02151-z ; arXiv:2206.01653
- Access: open (CC licence)
- Passes: 3/3 (repository record and abstract; Nature Methods full text re-read 2026-10-16 for fingerprint items, per-category recommendations, calibration guidance and scope limits; supplementary metric cheat sheets not read)
- Modality & anatomy: biomedical image analysis in general
- Data: multistage Delphi 2020-2022 (kickoff Dec 2020, ~2.5 years): 73 consortium experts, 156 contributors in total (84 named in acknowledgements); 5 international workshops, 9 surveys, expert meetings and crowdsourced feedback; consensus threshold > 75% agreement, median final-round agreement 93%
- Method: "problem fingerprint" (domain interest, target structures, dataset properties, algorithm output) drives metric selection, with pitfall warnings
- Key results: covers image-level classification (ImLC), object detection (ObD), semantic segmentation (SemS) and instance segmentation (InS). Fingerprint: FP1 problem category; FP2 domain interest (boundary importance, volume, centre/centreline, localisation granularity, class-confusion severity, error-penalty type, annotation-imprecision compensation, double-assignment penalty, decision rule, calibration assessment FP2.7); FP3 target structure (size relative to grid, size variability, shape); FP4 dataset (prevalence, reference noise, granularity, hierarchy); FP5 algorithm output (continuous scores). Recommendations: ImLC = expected cost if confusions have unequal severity else accuracy/balanced accuracy/MCC, optional per-class F-beta, always a multi-threshold metric (AUROC default, AP when imbalance high), calibration metric if requested; SemS = overlap metric (DSC or IoU default; F-beta for FP/FN preference; clDice for tubular structures) plus boundary metric (NSD default when annotation imprecision should be tolerated), computed per image then aggregated (HD95 not named as default in the text); ObD = localisation criterion (e.g. mask IoU) + assignment strategy + F-beta, plus AP or FROC when continuous scores exist, no TN-based metrics; InS = ObD metrics (or panoptic quality) plus per-instance SemS metrics. Calibration: some members favour proper scoring rules (Brier) over stand-alone calibration metrics; calibrated scores are not true posteriors. Implemented in the MONAI-integrated library; online tool described.
- Code / weights / license: https://github.com/Project-MONAI/MetricsReloaded/ (URL confirmed in the paper text; repository itself not visited); online tool URL not given in the text
- Useful for us: choose segmentation metrics for vertebra masks (e.g. a Dice-type overlap plus a boundary metric such as NSD/HD95) and detection/classification metrics for findings, and justify the choice with the fingerprint.
- Limitations / notes (confirmed in full text): scope limited to categorical reference data; fuzzy/multi-observer reference out of scope; regression and reconstruction not covered (expansion planned), so angle/height measurements (Cobb, lordosis, PI) need separate agreement statistics (MAE, Bland-Altman, ICC); only reference-based metrics, with robustness, reliability and subgroup analysis discussed but not part of core recommendations. For us: vertebra masks = SemS (DSC + NSD), vertebra labelling = InS/ObD with matching, findings = ImLC with AUROC + calibration via Brier.
- BibTeX:
```bibtex
@article{MaierHein2024MetricsReloaded,
  title   = {Metrics reloaded: recommendations for image analysis validation},
  author  = {Maier-Hein, Lena and Reinke, Annika and Godau, Patrick and others},
  journal = {Nature Methods},
  volume  = {21},
  number  = {2},
  pages   = {195--212},
  year    = {2024},
  doi     = {10.1038/s41592-023-02151-z}
}
```

### R248. Metric-related pitfalls
- Full title: Understanding metric-related pitfalls in image analysis validation
- Authors: Reinke A, Tizabi MD, Baumgartner M, et al. (78 authors on arXiv; last author Maier-Hein L)
- Year / Venue / Type: 2024 / Nature Methods 21(2):182-194 / consensus review
- DOI / arXiv / URL: 10.1038/s41592-023-02150-0 ; arXiv:2302.01790 (v4, 23 Feb 2024)
- Access: open (accepted manuscript on Edinburgh repository)
- Passes: 3/3 (abstract and repository record; arXiv v4 PDF read 2026-10-16 for the taxonomy and examples, then for the Delphi evidence and limitations. The Nature page itself was not fetchable.)
- Modality & anatomy: biomedical image analysis
- Data: multi-stage Delphi with 62 experts plus crowdsourced feedback; review of 138 challenges (2018-2022) and a literature search
- Method: domain-agnostic taxonomy of metric pitfalls
- Key results: 37 pitfall sources in a domain-agnostic taxonomy:
  - [P1] inadequate problem category, e.g. voxel metrics such as DSC used where object detection matters.
  - [P2] poor metric selection: domain interest (P2.1); target structure properties such as small, complex, disconnected, size-variable or touching structures (P2.2); dataset properties such as class imbalance, small test sets, imperfect reference and empty references (P2.3); algorithm output (P2.4).
  - [P3] poor application: implementation (P3.1), aggregation (P3.2, e.g. pooling hides small-structure errors and ignores many images per patient), ranking (P3.3), reporting (P3.4), interpretation (P3.5).

  Examples: one pixel shifts DSC heavily for small structures; HD is outlier-sensitive (use HD95); empty references give NaN sensitivity, PPV and F1; accuracy and balanced accuracy can hide FPs where MCC does not. 24% of challenge metric choices relied on common practice without justification. Only 68% of the pitfalls were already in the literature, and only 27% of those were illustrated.
- Code / weights / license: not applicable
- Useful for us: companion to G08; cite when we explain why we do not rely on Dice alone for small structures such as pedicles or discs.
- Limitations / notes: scope is classification, semantic and instance segmentation, and detection only; reference-based metrics only; some pitfalls may be missing. For spine: pedicles and small discs suffer from P2.2, many slices or levels per patient need P3.2 per-patient aggregation, and normal studies with no fracture are empty references (P2.3). The earlier preprint "Common limitations of image processing metrics: A picture story" (G10) covers the same ground with figures.
- BibTeX:
```bibtex
@article{Reinke2024Pitfalls,
  title   = {Understanding metric-related pitfalls in image analysis validation},
  author  = {Reinke, Annika and Tizabi, Minu D. and Baumgartner, Michael and others},
  journal = {Nature Methods},
  volume  = {21},
  number  = {2},
  pages   = {182--194},
  year    = {2024},
  doi     = {10.1038/s41592-023-02150-0}
}
```

### R249. MI-CLAIM
- Full title: Minimum information about clinical artificial intelligence modeling: the MI-CLAIM checklist
- Authors: Norgeot B, Quer G, Beaulieu-Jones BK, et al.
- Year / Venue / Type: 2020 / Nature Medicine 26(9):1320-1324 / reporting checklist
- DOI / arXiv / URL: 10.1038/s41591-020-1041-y ; PMID 32908275
- Access: paywalled (abstract only)
- Passes: 1/3 (publisher landing page; round 3 on 2026-10-16: the paper is paywalled. The GitHub README only links the checklist file MI_CLAIM_checklist_repo.docx (not parsed) and has no licence file. The MI-CLAIM-GEN arXiv abstract (2403.02558, 18 authors incl. Norgeot) does not enumerate the original items.)
- Modality & anatomy: clinical AI modelling in general
- Data: not applicable
- Method: minimum-information checklist
- Key results: per the 2025 MI-CLAIM-GEN follow-up (Miao et al., Nature Medicine 2025), the original has six parts, including study design, data and optimisation, performance evaluation, model examination, and reproducibility with tiered transparency for code and data sharing. Item-level content of the 2020 paper unverified here.
- Code / weights / license: github.com/beaunorgeot/MI-CLAIM (checklist .docx; no licence file in the repository)
- Useful for us: use its reproducibility tiers to state what we release (code, weights, synthetic or public data).
- Limitations / notes: the generative-AI update MI-CLAIM-GEN (arXiv:2403.02558) is relevant if we use an LLM to write reports.
- BibTeX:
```bibtex
@article{Norgeot2020MICLAIM,
  title   = {Minimum information about clinical artificial intelligence modeling: the {MI-CLAIM} checklist},
  author  = {Norgeot, Beau and Quer, Giorgio and Beaulieu-Jones, Brett K. and others},
  journal = {Nature Medicine},
  volume  = {26},
  number  = {9},
  pages   = {1320--1324},
  year    = {2020},
  doi     = {10.1038/s41591-020-1041-y}
}
```

### R250. Model cards
- Full title: Model Cards for Model Reporting
- Authors: Mitchell M, Wu S, Zaldivar A, et al.
- Year / Venue / Type: 2019 / Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19), pp. 220-229 (pages unverified) / conference paper
- DOI / arXiv / URL: 10.1145/3287560.3287596 ; arXiv:1810.03993
- Access: open (arXiv)
- Passes: 2/3 (ar5iv full text; examples skimmed)
- Modality & anatomy: general ML
- Data: examples are a smile detector and a toxicity classifier
- Method: structured documentation
- Key results: nine sections: Model Details, Intended Use, Factors, Metrics, Evaluation Data, Training Data, Quantitative Analyses, Ethical Considerations, Caveats and Recommendations. Performance should be reported across demographic and intersectional groups.
- Code / weights / license: not applicable
- Useful for us: publish a model card with the browser app, stating intended use (research only, not for diagnosis), out-of-scope inputs and subgroup performance.
- Limitations / notes: no medical-specific fields; add scanner, protocol and population fields ourselves.
- BibTeX:
```bibtex
@inproceedings{Mitchell2019ModelCards,
  title     = {Model Cards for Model Reporting},
  author    = {Mitchell, Margaret and Wu, Simone and Zaldivar, Andrew and Barnes, Parker and Vasserman, Lucy and Hutchinson, Ben and Spitzer, Elena and Raji, Inioluwa Deborah and Gebru, Timnit},
  booktitle = {Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19)},
  year      = {2019},
  doi       = {10.1145/3287560.3287596}
}
```

### R251. Datasheets for datasets
- Full title: Datasheets for Datasets
- Authors: Gebru T, Morgenstern J, Vecchione B, et al.
- Year / Venue / Type: 2021 / Communications of the ACM 64(12):86-92 / article (preprint arXiv:1803.09010, 2018)
- DOI / arXiv / URL: 10.1145/3458723 (DOI from the PDF file name 3458723.pdf and search result; not shown on the Microsoft Research page) ; arXiv:1803.09010
- Access: open
- Passes: 3/3 (Microsoft Research record; arXiv v8 (1 Dec 2021) PDF read 2026-10-16 for the sections and questions, then for the development process and limitations; the CACM citation is not printed in arXiv, so volume and pages remain from the earlier record)
- Modality & anatomy: general ML datasets
- Data: not applicable
- Method: question-based documentation
- Key results: 7 sections, about 57 questions by my count: Motivation (4), Composition (16, incl. noise and redundancy, confidential data, subpopulations, identifiability), Collection Process (12, incl. ethical review and consent), Preprocessing/cleaning/labelling (4, incl. raw data kept, software), Uses (6, incl. tasks it should NOT be used for), Distribution (7, licence and IP), Maintenance (8, errata, updates, retention). Refined through example datasheets, product-team pilots at two companies, public comment and legal review. Legal and ethical questions were moved into the lifecycle stages.
- Code / weights / license: not applicable
- Useful for us: write a datasheet for any spine dataset we assemble or relabel, especially the "deviation from normal" reference set.
- Limitations / notes: needs adapting to each organisation; a poor fit for dynamic datasets (version the datasheet); does not by itself solve bias; takes time. Inspired model cards, data cards and factsheets.
- BibTeX:
```bibtex
@article{Gebru2021Datasheets,
  title   = {Datasheets for Datasets},
  author  = {Gebru, Timnit and Morgenstern, Jamie and Vecchione, Briana and Vaughan, Jennifer Wortman and Wallach, Hanna and Daum{\'e} III, Hal and Crawford, Kate},
  journal = {Communications of the ACM},
  volume  = {64},
  number  = {12},
  pages   = {86--92},
  year    = {2021},
  doi     = {10.1145/3458723}
}
```

### R252. Common limitations of image processing metrics (picture story)
- Full title: Common Limitations of Image Processing Metrics: A Picture Story
- Authors: Reinke A, Tizabi MD, Sudre CH, et al.
- Year / Venue / Type: 2021 (living document, revised to v8) / arXiv preprint / consensus preprint
- DOI / arXiv / URL: arXiv:2104.05642
- Access: preprint (open)
- Passes: 2/3 (ar5iv full text read for structure and pitfall list; final section on cross-topic analyses not fully read)
- Modality & anatomy: biomedical image analysis
- Data: Delphi consensus with experts from more than 60 institutions
- Method: illustrated catalogue of metric pitfalls
- Key results: three kinds of pitfall: ignoring metric properties (class imbalance, small structures), ignoring dataset properties (non-independent test cases), ignoring the domain interest. For segmentation: small structures relative to pixel size, varying structure sizes, noisy reference annotations, empty reference masks, resolution dependence. For detection: localisation criteria, assignment strategies, AP vs FROC.
- Code / weights / license: not applicable
- Useful for us: practical figure-level guidance for vertebra/disc segmentation and lesion detection metrics. Patient-level (not slice-level) aggregation to avoid non-independent test cases.
- Limitations / notes: superseded in journal form by G08 and G09, but still cited as the "picture story".
- BibTeX:
```bibtex
@article{Reinke2021PictureStory,
  title   = {Common Limitations of Image Processing Metrics: A Picture Story},
  author  = {Reinke, Annika and Tizabi, Minu D. and Sudre, Carole H. and others},
  journal = {arXiv preprint arXiv:2104.05642},
  year    = {2021}
}
```

---

#### C. Generalisation, dataset shift, shortcut learning and fairness

### R253. Zech 2018 - variable generalisation (pneumonia CXR)
- Full title: Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study (preprint title: "Confounding variables can degrade generalization performance of radiological deep learning models")
- Authors: Zech JR, Badgeley MA, Liu M, et al.
- Year / Venue / Type: 2018 / PLOS Medicine 15(11):e1002683 / journal article
- DOI / arXiv / URL: 10.1371/journal.pmed.1002683 ; arXiv:1807.00431
- Access: open
- Passes: 2/3 (arXiv abstract and PMC search record; PMC full text blocked by CAPTCHA, AUC values not re-checked)
- Modality & anatomy: chest radiograph
- Data: 158,323 CXRs: NIH (112,120 / 30,805 patients), Mount Sinai (42,396 / 12,904), Indiana (3,807 / 3,683)
- Method: CNN pneumonia classifier, trained and tested within and across hospital systems
- Key results: in 3 of 5 natural comparisons, external performance was significantly lower than internal. CNNs could identify the hospital system and department with very high accuracy and used it to calibrate predictions.
- Code / weights / license: unverified
- Useful for us: the classic citation for site-specific confounding. Motivates multi-site external testing and site-held-out splits for spine data.
- Limitations / notes: exact AUCs not recorded here because the full text could not be opened.
- BibTeX:
```bibtex
@article{Zech2018Variable,
  title   = {Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study},
  author  = {Zech, John R. and Badgeley, Marcus A. and Liu, Manway and Costa, Anthony B. and Titano, Joseph J. and Oermann, Eric Karl},
  journal = {PLOS Medicine},
  volume  = {15},
  number  = {11},
  pages   = {e1002683},
  year    = {2018},
  doi     = {10.1371/journal.pmed.1002683}
}
```

### R254. DeGrave 2021 - shortcuts over signal
- Full title: AI for radiographic COVID-19 detection selects shortcuts over signal
- Authors: DeGrave AJ, Janizek JD, Lee SI
- Year / Venue / Type: 2021 / Nature Machine Intelligence 3(7):610-619 / journal article
- DOI / arXiv / URL: 10.1038/s42256-021-00338-7
- Access: open (publisher full text readable)
- Passes: 3/3 full text
- Modality & anatomy: chest radiograph
- Data: Dataset I (GitHub-COVID 408 positives + ChestX-ray14 112,120 negatives); Dataset II (BIMCV-COVID-19+ 1,596 + PadChest 96,270); Dataset III (BIMCV +/- 3,086, same hospitals and period)
- Method: DenseNet-121 (plus 9 other architectures); expected-gradients saliency; CycleGAN-style counterfactual images; region-swap experiments vs 1,000 random-patch controls
- Key results: models trained on Dataset I lost about half their performance on Dataset II. Laterality markers, text, borders and patient positioning drove predictions (swapping markers shifted log odds by -5.63 / +13.85; moving the shoulder region shifted it by 6.57, P = 0.005). A less confounded dataset 1/20th the size generalised better (P = 0.016). Augmentation, cropping and simpler models did not fix it.
- Code / weights / license: unverified
- Useful for us: spine radiographs carry the same shortcuts (laterality markers, rulers, implants, positioning aids, scanner text). Supports saliency audits and same-source positive/negative sampling.
- Limitations / notes: authors note dataset III still holds some shortcuts, and saliency audits are labour-intensive.
- BibTeX:
```bibtex
@article{DeGrave2021Shortcuts,
  title   = {{AI} for radiographic {COVID-19} detection selects shortcuts over signal},
  author  = {DeGrave, Alex J. and Janizek, Joseph D. and Lee, Su-In},
  journal = {Nature Machine Intelligence},
  volume  = {3},
  number  = {7},
  pages   = {610--619},
  year    = {2021},
  doi     = {10.1038/s42256-021-00338-7}
}
```

### R255. Oakden-Rayner 2020 - hidden stratification
- Full title: Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging
- Authors: Oakden-Rayner L, Dunnmon J, Carneiro G, Ré C
- Year / Venue / Type: 2019 preprint; published at ACM Conference on Health, Inference, and Learning (CHIL) 2020 (venue and proceedings DOI unverified in this review) / conference paper
- DOI / arXiv / URL: arXiv:1909.12475
- Access: preprint (open)
- Passes: 3/3 (arXiv abstract; arXiv PDF read 2026-10-16 for datasets, methods and results, then for limitations and recommendations. The venue is not stated in the PDF.)
- Modality & anatomy: radiographs (chest, musculoskeletal upper limb, pelvis/hip)
- Data: CXR14 (112,120 frontal CXRs, 30,805 patients); MURA (13,942 train / 714 test); Royal Adelaide Hospital pelvic radiographs (hip fracture)
- Method: schema completion (radiologist subclass labels), error auditing (review of FPs and FNs) and k-means on pre-softmax features (k = 2-5, clusters > 100 points)
- Key results:
  - Hip fracture: AUC 0.994 and sensitivity 0.981 overall, but sensitivity 0.900 for subtle fractures (n = 38) and 0.911 for cervical (n = 81).
  - MURA: AUC 0.91 overall; hardware 0.98; degenerative joint disease 0.76.
  - CXR14 pneumothorax: AUC 0.87 overall; with chest drain 0.94, without 0.77; PPV 0.90 vs 0.60. About 80% of test pneumothoraces had a drain.
  - Clustering separated drain prevalence (0.17 vs 0.84 between clusters) but not the MURA subsets.
  - Relative drops computed from these numbers are about 16-18%. The wording of the headline '20%' claim ('over' vs 'up to') differed between the abstract read earlier and the PDF extraction, so check it before quoting.
- Code / weights / license: none mentioned
- Useful for us: report per-finding and per-subtype results (e.g. fracture with/without hardware, osteoporotic vs traumatic), not only pooled AUC.
- Limitations / notes: schema completion needs expertise and time; auditing can miss rare strata; clustering is weak; small subsets; single-radiologist subclass labels. The published CHIL version was not opened. For spine, report subsets such as with/without hardware, subtle vs obvious fractures and degenerative vs not, mirroring MURA hardware and DJD.
- BibTeX:
```bibtex
@article{OakdenRayner2019Hidden,
  title   = {Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging},
  author  = {Oakden-Rayner, Luke and Dunnmon, Jared and Carneiro, Gustavo and R{\'e}, Christopher},
  journal = {arXiv preprint arXiv:1909.12475},
  year    = {2019}
}
```

### R256. Seyyed-Kalantari 2021 - underdiagnosis bias
- Full title: Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations
- Authors: Seyyed-Kalantari L, Zhang H, McDermott MBA, et al.
- Year / Venue / Type: 2021 / Nature Medicine 27:2176-2182 / journal article
- DOI / arXiv / URL: 10.1038/s41591-021-01595-0
- Access: open (publisher page readable)
- Passes: 3/3 full text
- Modality & anatomy: chest radiograph
- Data: MIMIC-CXR (371,858 images / 65,079 patients), CheXpert (223,648 / 64,740), ChestX-ray14 (112,120 / 30,805), combined (707,626 / 129,819)
- Method: DenseNet-121; underdiagnosis = false-positive rate of the "no finding" label per subgroup (sex, age, race/ethnicity, insurance) and intersections
- Key results: female, under-20, Black, Hispanic and Medicaid patients were underdiagnosed more often; intersectional groups (e.g. Hispanic female) fared worse. Pattern held across datasets.
- Code / weights / license: unverified
- Useful for us: our "normal / no significant finding" output carries this exact risk. Report false "normal" rates by sex and age band at minimum.
- Limitations / notes: NLP-derived labels, self-reported race, insurance as SES proxy, small subgroups.
- BibTeX:
```bibtex
@article{SeyyedKalantari2021Underdiagnosis,
  title   = {Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations},
  author  = {Seyyed-Kalantari, Laleh and Zhang, Haoran and McDermott, Matthew B. A. and Chen, Irene Y. and Ghassemi, Marzyeh},
  journal = {Nature Medicine},
  volume  = {27},
  pages   = {2176--2182},
  year    = {2021},
  doi     = {10.1038/s41591-021-01595-0}
}
```

### R257. Gichoya 2022 - AI recognition of patient race
- Full title: AI recognition of patient race in medical imaging: a modelling study
- Authors: Gichoya JW, Banerjee I, Bhimireddy AR, et al.
- Year / Venue / Type: 2022 / The Lancet Digital Health 4(6):e406-e414 / journal article (preprint "Reading Race", arXiv:2107.10356)
- DOI / arXiv / URL: 10.1016/S2589-7500(22)00063-2 ; arXiv:2107.10356
- Access: open (CC BY)
- Passes: 2/3 (OpenAlex abstract and arXiv abstract; Lancet full text fetch failed)
- Modality & anatomy: CXR, chest CT, cervical spine radiographs (Emory), mammography, hand radiographs
- Data: Emory CXR, Emory Chest CT, Emory Cervical Spine, Emory Mammogram; MIMIC-CXR, CheXpert, NLST, RSNA PE CT, Digital Hand Atlas
- Method: standard deep learning classifiers for self-reported race; proxy-variable regression; image corruption and frequency-filter experiments
- Key results: race AUC 0.91-0.99 on x-ray, 0.87-0.96 on chest CT, 0.81 on mammography. Not explained by BMI (AUC 0.55), disease distribution (0.61) or breast density (0.61). Persisted under cropping, noise and filtering. Cervical-spine-specific AUC not recorded (full text not opened).
- Code / weights / license: unverified
- Useful for us: directly includes spine radiographs. Cite to justify subgroup auditing even when demographic variables are not model inputs.
- Limitations / notes: mechanism of race detection unknown.
- BibTeX:
```bibtex
@article{Gichoya2022Race,
  title   = {{AI} recognition of patient race in medical imaging: a modelling study},
  author  = {Gichoya, Judy Wawira and Banerjee, Imon and Bhimireddy, Ananth Reddy and others},
  journal = {The Lancet Digital Health},
  volume  = {4},
  number  = {6},
  pages   = {e406--e414},
  year    = {2022},
  doi     = {10.1016/S2589-7500(22)00063-2}
}
```

### R258. Geirhos 2020 - shortcut learning
- Full title: Shortcut learning in deep neural networks
- Authors: Geirhos R, Jacobsen JH, Michaelis C, et al.
- Year / Venue / Type: 2020 / Nature Machine Intelligence 2:665-673 (volume and pages unverified) / perspective
- DOI / arXiv / URL: 10.1038/s42256-020-00257-z ; arXiv:2004.07780
- Access: open (arXiv)
- Passes: 3/3 (arXiv abstract; arXiv v5 PDF (21 Nov 2023) read 2026-10-16 for the taxonomy and examples, then for the conclusions and limitations; volume and pages still unverified)
- Modality & anatomy: general deep learning
- Data: not applicable
- Method: perspective, with a small toy experiment (MLP/CNN on synthetic star/moon images). Taxonomy of decision rules: all rules, then training solutions (incl. overfitting), then i.i.d. test solutions (incl. shortcuts, which fail o.o.d.), then the intended solution (generalises o.o.d.).
- Key results: shortcuts are decision rules that do well on standard benchmarks but fail under harder, real-world conditions. They arise from the dataset, the decision rule and generalisation biases. Medical example: a pneumonia CNN learning a hospital-specific metal token, which fails at new hospitals (Zech). Recommendations: (1) connect the dots, since shortcuts are ubiquitous; (2) interpret results carefully; (3) make o.o.d. generalisation tests the rule; (4) understand what makes a solution easy to learn (architecture, data, loss, optimisation).
- Code / weights / license: not applicable
- Useful for us: the general definition of shortcut learning to cite with C01/C02.
- Limitations / notes: computer-vision-biased examples; a perspective, not a systematic study; good o.o.d. test design is an open problem; the intended solution is hard to formalise. For spine: watch for shortcuts such as implants, scanner text and institution-specific positioning.
- BibTeX:
```bibtex
@article{Geirhos2020Shortcut,
  title   = {Shortcut learning in deep neural networks},
  author  = {Geirhos, Robert and Jacobsen, J{\"o}rn-Henrik and Michaelis, Claudio and Zemel, Richard and Brendel, Wieland and Bethge, Matthias and Wichmann, Felix A.},
  journal = {Nature Machine Intelligence},
  year    = {2020},
  doi     = {10.1038/s42256-020-00257-z}
}
```

### R259. Larrazabal 2020 - gender imbalance
- Full title: Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis
- Authors: Larrazabal AJ, Nieto N, Peterson V, Milone DH, Ferrante E
- Year / Venue / Type: 2020 / PNAS 117(23):12592-12594 / brief report
- DOI / arXiv / URL: 10.1073/pnas.1919012117
- Access: open (CC BY)
- Passes: 3/3 (abstract; author-repository PDF (sinc.unl.edu.ar) read 2026-10-16 for data, design and findings, then for code, limitations and conclusions; volume and pages taken from the earlier record)
- Modality & anatomy: chest radiograph
- Data: NIH ChestX-ray14: 112,120 images from 30,805 patients, 56.5% male. CheXpert: 224,316 images from 65,240 patients, about 60% male, uncertain labels set to negative. Splits of 48,568 (NIH) and 27,147 (CheXpert) images, pathology-matched by sex.
- Method: DenseNet-121 (14 sigmoid outputs, ImageNet init), plus ResNet and Inception-v3; training sets of 0, 25, 50, 75 and 100% female, tested on male and female folds; 20 random splits; AUC with Mann-Whitney U tests
- Key results: training on one sex and testing on the other gives a consistent AUC drop for the under-represented sex. At a 25/75 mix, the minority sex's average AUC is significantly below the balanced model. A 50/50 model matched same-sex training for both sexes, the best overall. Exact AUC values were not in the extracted text.
- Code / weights / license: https://github.com/N-Nieto/GenderBias_CheXNet (code, splits, extra results; per the paper)
- Useful for us: check the sex balance of public spine datasets and report per-sex results.
- Limitations / notes: CXR only; 2 datasets and 3 CNNs; NLP-derived labels; the term 'gender' is used though anatomical sex is what is imaged. The authors call for balanced datasets and for regulators to address sex in evaluation. For us: check and report the sex balance of the spine training data and per-sex performance.
- BibTeX:
```bibtex
@article{Larrazabal2020Gender,
  title   = {Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis},
  author  = {Larrazabal, Agostina J. and Nieto, Nicol{\'a}s and Peterson, Victoria and Milone, Diego H. and Ferrante, Enzo},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {117},
  number  = {23},
  pages   = {12592--12594},
  year    = {2020},
  doi     = {10.1073/pnas.1919012117}
}
```

### R260. Glocker 2023 - algorithmic encoding of protected characteristics
- Full title: Algorithmic encoding of protected characteristics in chest X-ray disease detection models
- Authors: Glocker B, Jones C, Bernhardt M, Winzeck S
- Year / Venue / Type: 2023 / eBioMedicine 89:104467 / journal article
- DOI / arXiv / URL: 10.1016/j.ebiom.2023.104467 ; arXiv:2110.14755 (v4, 21 Jul 2022; arXiv title 'Algorithmic encoding of protected characteristics in image-based models for disease detection')
- Access: open (CC BY)
- Passes: 3/3 (abstract; arXiv v4 PDF read 2026-10-16 for data, methods and numbers, then for limitations and conclusions. The published eBioMedicine version was not readable, ScienceDirect being robots-blocked, so numbers may differ slightly from the journal version.)
- Modality & anatomy: chest radiograph
- Data: CheXpert: 42,884 patients, 127,118 scans (76,205 / 12,673 / 38,240), about 78% White, 15% Asian, 7% Black. MIMIC-CXR: 43,209 patients, 183,207 scans, about 77% White, 4% Asian, 19% Black. Black patients are younger on average.
- Method: DenseNet-121 multi-label (14 findings; ResNet-34 supplementary); tasks 'no finding' and 'pleural effusion'; threshold at overall FPR 0.20. Methods: race-balanced test-set resampling controlling for age and prevalence; SPLIT (frozen backbone plus a new race or sex head, as in 'reading race'); multitask disease + sex + race model; PCA/t-SNE/logit inspection with KS tests.
- Key results: overall AUC: no finding 0.87 (CheXpert) / 0.85 (MIMIC); effusion 0.87 / 0.90. CheXpert 'no finding', Black patients: FPR 0.23 -> 0.20 after resampling, so the disparity largely disappears. 'Pleural effusion', Black patients: lower AUC and Youden J persist after resampling. SPLIT race AUC about 0.78-0.80, and still 0.67-0.75 from a randomly initialised backbone; sex > 0.90. So SPLIT is necessary but not sufficient to show attribute use. No strong evidence that race is used for predictions, but subtle use cannot be excluded.
- Code / weights / license: https://github.com/biomedia-mira/chexploration (Apache 2.0, per the paper)
- Useful for us: methods for subgroup analysis that account for prevalence differences.
- Limitations / notes: two datasets, two labels, two attributes; resampling depends on the chosen controls; label bias is not addressed; causes not established. For us: report subgroup TPR/FPR on prevalence- and age-matched resampled test sets (sex, age band, scanner).
- BibTeX:
```bibtex
@article{Glocker2023Encoding,
  title   = {Algorithmic encoding of protected characteristics in chest X-ray disease detection models},
  author  = {Glocker, Ben and Jones, Charles and Bernhardt, M{\'e}lanie and Winzeck, Stefan},
  journal = {eBioMedicine},
  volume  = {89},
  pages   = {104467},
  year    = {2023},
  doi     = {10.1016/j.ebiom.2023.104467}
}
```

### R261. Castro 2020 - causality matters
- Full title: Causality matters in medical imaging
- Authors: Castro DC, Walker I, Glocker B
- Year / Venue / Type: 2020 / Nature Communications 11:3673 / perspective
- DOI / arXiv / URL: 10.1038/s41467-020-17478-w ; arXiv:1912.08142
- Access: open (CC BY)
- Passes: 2/3 (abstract; ar5iv full text read 2026-10-16 for the causal framework, shift taxonomy and examples. The extracted text was truncated before the recommendations and closing sections.)
- Modality & anatomy: general medical imaging
- Data: not applicable
- Method: causal framework. Tasks are causal (X->Y, e.g. manual contours from MRI) or anticausal (Y->X, e.g. biopsy-proven melanoma). Implications: SSL is theoretically futile for causal tasks such as segmentation but may help anticausal tasks; augmentation helps both (invariance refines P(X|Y), equivariance informs P(X,Y)).
- Key results: dataset-shift taxonomy with mitigations:
  - population P(Z): reweighting, needs support coverage
  - annotation P(Y|X): hard to correct
  - prevalence P(Y): prior or Bayes adjustment, instance weights
  - manifestation P(Z|Y): uncorrectable without strong assumptions
  - acquisition P(X|Z): registration, intensity normalisation, domain adaptation

  Selection bias can be random, image-based (QC acts as selection, causing population or acquisition shift), target-based (prevalence) or joint (spurious associations). A metadata checklist table (annotation method, cohort, acquisition, selection) supports inferring the causal structure.
- Code / weights / license: not applicable
- Useful for us: vocabulary for describing acquisition shift (MRI field strength, CT kernel, X-ray vendor) in the paper.
- Limitations / notes: conceptual, with illustrative examples (prostate MRI, skin lesions, brain tumour 3T to 1.5T). For us: our vertebra/disc segmentation is causal (labels drawn from images), so unlabelled data is unlikely to help fundamentally. Radiologist grading is a causal task with annotation-shift risk across graders. Image-based QC at dataset curation induces selection bias, which matters for our abstention module.
- BibTeX:
```bibtex
@article{Castro2020Causality,
  title   = {Causality matters in medical imaging},
  author  = {Castro, Daniel C. and Walker, Ian and Glocker, Ben},
  journal = {Nature Communications},
  volume  = {11},
  pages   = {3673},
  year    = {2020},
  doi     = {10.1038/s41467-020-17478-w}
}
```

### R262. Finlayson 2021 - clinician and dataset shift
- Full title: The Clinician and Dataset Shift in Artificial Intelligence
- Authors: Finlayson SG, Subbaswamy A, Singh K, et al.
- Year / Venue / Type: 2021 / New England Journal of Medicine 385(3):283-286 / correspondence
- DOI / arXiv / URL: 10.1056/NEJMc2104626
- Access: paywalled (accepted version in PMC8665481)
- Passes: abstract only, paywalled
- Modality & anatomy: general clinical AI
- Data: not applicable
- Method: commentary
- Key results: describes how to recognise and mitigate common sources of dataset shift (changes in technology, population, and behaviour).
- Code / weights / license: not applicable
- Useful for us: short clinician-facing citation for why the app must detect out-of-distribution input.
- Limitations / notes: list of shift sources not verified item by item.
- BibTeX:
```bibtex
@article{Finlayson2021DatasetShift,
  title   = {The Clinician and Dataset Shift in Artificial Intelligence},
  author  = {Finlayson, Samuel G. and Subbaswamy, Adarsh and Singh, Karandeep and others},
  journal = {New England Journal of Medicine},
  volume  = {385},
  number  = {3},
  pages   = {283--286},
  year    = {2021},
  doi     = {10.1056/NEJMc2104626}
}
```

### R263. Koh 2021 - WILDS benchmark
- Full title: WILDS: A Benchmark of in-the-Wild Distribution Shifts
- Authors: Koh PW, Sagawa S, Marklund H, et al.
- Year / Venue / Type: 2021 / ICML 2021, PMLR 139 (confirmed from the PDF header) / benchmark
- DOI / arXiv / URL: arXiv:2012.07421
- Access: preprint (open)
- Passes: 3/3 (abstract; arXiv PDF read 2026-10-16 for datasets and the ERM gap table, then for methods, limitations and code)
- Modality & anatomy: includes histopathology across hospitals (Camelyon17-WILDS) among 10 datasets
- Data: 10 datasets. Domain generalisation: iWildCam, Camelyon17 (5 hospitals, 455,954 96x96 lymph-node patches; staining shift; single OOD test hospital), RxRx1, OGB-MolPCBA, GlobalWheat. Subpopulation shift: CivilComments. Hybrid: FMoW, PovertyMap, Amazon, Py150.
- Method: benchmark plus the WILDS Python package; baselines ERM, CORAL, IRM, Group DRO; model selection on an OOD validation set
- Key results: ERM in-distribution vs OOD gap on every dataset, e.g. Camelyon17 average accuracy 93.2 vs 70.3 (gap 22.9), iWildCam macro-F1 47.0 vs 31.0, CivilComments worst-group 92.2 vs 56.0, Amazon 10th-percentile 71.9 vs 53.8. CORAL, IRM and Group DRO did not consistently beat ERM (except Group DRO on CivilComments, 70.0).
- Code / weights / license: https://wilds.stanford.edu (code, leaderboards; open-source package)
- Useful for us: cite for "hospital as domain" evaluation protocol.
- Limitations / notes: no spine data; classification and regression only (no segmentation or detection); few OOD domains (one test hospital for Camelyon17); ID comparisons differ by dataset; gaps slightly underestimated.
- BibTeX:
```bibtex
@article{Koh2020WILDS,
  title   = {{WILDS}: A Benchmark of in-the-Wild Distribution Shifts},
  author  = {Koh, Pang Wei and Sagawa, Shiori and Marklund, Henrik and others},
  journal = {arXiv preprint arXiv:2012.07421},
  year    = {2020}
}
```

### R264. Yu 2022 - external validation systematic review
- Full title: External Validation of Deep Learning Algorithms for Radiologic Diagnosis: A Systematic Review
- Authors: Yu AC, Mohajer B, Eng J
- Year / Venue / Type: 2022 / Radiology: Artificial Intelligence 4(3):e210064 / systematic review
- DOI / arXiv / URL: 10.1148/ryai.210064
- Access: open (PMC9152694)
- Passes: 3/3 (abstract; RSNA full text read 2026-10-16 for methods and results, then for limitations and recommendations. The Table E2 body-part breakdown was not seen.)
- Modality & anatomy: radiology, all modalities
- Data: PubMed search on 1 May 2021 covering 1 Jan 2015 to 1 Apr 2021, English only. 6,018 screened, 83 studies with 86 algorithms (patient-level DL diagnostic classification with external data from another institution; segmentation and triage excluded). Chest 48%, brain 16%, bone 12%, abdomen 8%, breast 6%; about 3/4 radiography or CT.
- Method: systematic review comparing internal vs external performance
- Key results: median external minus development difference -0.046 (range -0.60 to +0.13). 70/86 (81%) were lower externally; 42 (49%) dropped by >= 0.05 ('modest') and 21 (24%) by >= 0.10 ('substantial'). No characteristic (body part, modality, conspicuity, labelling, institutional diversity, size, prevalence) was associated with the drop. External sets were smaller than development sets (P < .001). Only 11/86 cited a reporting guideline.
- Code / weights / license: not applicable
- Useful for us: number to quote when arguing for external testing and for expecting lower performance on users' uploads.
- Limitations / notes: PubMed only; no pooling because of heterogeneity; no formal risk of bias; likely publication bias. Recommendations: include external data, describe populations, use interpretability to detect leakage, follow CLAIM.
- BibTeX:
```bibtex
@article{Yu2022ExternalValidation,
  title   = {External Validation of Deep Learning Algorithms for Radiologic Diagnosis: A Systematic Review},
  author  = {Yu, Alice C. and Mohajer, Bahram and Eng, John},
  journal = {Radiology: Artificial Intelligence},
  volume  = {4},
  number  = {3},
  pages   = {e210064},
  year    = {2022},
  doi     = {10.1148/ryai.210064}
}
```

### R265. Kim 2019 - design characteristics of AI imaging studies
- Full title: Design Characteristics of Studies Reporting the Performance of Artificial Intelligence Algorithms for Diagnostic Analysis of Medical Images: Results from Recently Published Papers
- Authors: Kim DW, Jang HY, Kim KW, Shin Y, Park SH
- Year / Venue / Type: 2019 / Korean Journal of Radiology 20(3):405-410 (pages confirmed on kjronline.org; online 19 Feb 2019) / systematic review
- DOI / arXiv / URL: 10.3348/kjr.2019.0025
- Access: open
- Passes: 3/3 (abstract; KJR full text read 2026-10-16 for methods and results, then for limitations and conclusions; Tables 1-2 are images, not extracted)
- Modality & anatomy: medical imaging, all
- Data: PubMed MEDLINE and Embase, 1 Jan to 17 Aug 2018; 2,748 articles, 516 eligible original studies of AI diagnostic image analysis
- Method: design audit on 4 features: external validation (and newly collected validation data), diagnostic cohort vs case-control design, multiple institutions, prospective collection
- Key results: 31/516 (6%) performed external validation; none of the 31 had all three of cohort design, multi-institution and prospective data; no difference between medical and non-medical journals (Fisher's exact test). Nearly all were proof-of-concept feasibility studies.
- Code / weights / license: not applicable
- Useful for us: baseline evidence of weak validation in the field.
- Limitations / notes: only major design features were assessed; a 2018 snapshot; diagnostic performance only, not outcomes; transparency issues noted but not analysed.
- BibTeX:
```bibtex
@article{Kim2019DesignCharacteristics,
  title   = {Design Characteristics of Studies Reporting the Performance of Artificial Intelligence Algorithms for Diagnostic Analysis of Medical Images: Results from Recently Published Papers},
  author  = {Kim, Dong Wook and Jang, Hye Young and Kim, Kyung Won and Shin, Youngbin and Park, Seong Ho},
  journal = {Korean Journal of Radiology},
  volume  = {20},
  number  = {3},
  pages   = {405--410},
  year    = {2019},
  doi     = {10.3348/kjr.2019.0025}
}
```

### R266. Nagendran 2020 - AI versus clinicians
- Full title: Artificial intelligence versus clinicians: systematic review of design, reporting standards, and claims of deep learning studies
- Authors: Nagendran M, Chen Y, Lovejoy CA, et al.
- Year / Venue / Type: 2020 / BMJ 368:m689 / systematic review
- DOI / arXiv / URL: 10.1136/bmj.m689
- Access: open (CC BY-NC)
- Passes: 1/3 (abstract; round 3 retry on 2026-10-16 failed because the BMJ full-text fetch errored although the article is OA)
- Modality & anatomy: medical imaging, all
- Data: 10 trial records and 81 non-randomised studies (2010 - June 2019)
- Method: systematic review against CONSORT, TRIPOD and PROBAST
- Key results: 9/81 prospective; 58/81 high risk of bias; data unavailable in 95% and code in 93%; 61/81 claimed AI at least comparable to clinicians but only 31 (38%) called for prospective work.
- Code / weights / license: not applicable
- Useful for us: argues for releasing code and weights and avoiding "matches radiologists" claims.
- Limitations / notes: none.
- BibTeX:
```bibtex
@article{Nagendran2020AIvsClinicians,
  title   = {Artificial intelligence versus clinicians: systematic review of design, reporting standards, and claims of deep learning studies},
  author  = {Nagendran, Myura and Chen, Yang and Lovejoy, Christopher A. and others},
  journal = {BMJ},
  volume  = {368},
  pages   = {m689},
  year    = {2020},
  doi     = {10.1136/bmj.m689}
}
```

### R267. Roberts 2021 - COVID-19 ML pitfalls
- Full title: Common pitfalls and recommendations for using machine learning to detect and prognosticate for COVID-19 using chest radiographs and CT scans
- Authors: Roberts M, Driggs D, Thorpe M, et al.
- Year / Venue / Type: 2021 / Nature Machine Intelligence 3(3):199-217 / systematic review
- DOI / arXiv / URL: 10.1038/s42256-021-00307-0
- Access: open (CC BY)
- Passes: 3/3 (abstract; Nature MI full text read 2026-10-16 for methods and pitfalls, then for recommendations and limitations)
- Modality & anatomy: CXR, CT
- Data: 1 Jan to 3 Oct 2020; arXiv plus the Living Evidence on COVID-19 database (EMBASE, MEDLINE, bioRxiv, medRxiv); PROSPERO CRD42020188887. 2,212 records, 2,150 after deduplication, 415 after title/abstract screening, 320 after full text, 62 after quality screen (37 DL, 23 traditional ML, 2 hybrid).
- Method: systematic review with quality screening by CLAIM (DL; papers failing at least 3 mandatory items excluded), RQS (traditional ML; < 6 excluded) and PROBAST
- Key results: 215/254 DL papers failed the quality screen (51% missed at least 3 mandatory CLAIM items; most often model selection 61%, pre-processing 58%, training details 49%). Of the 62 included: 55 high risk of bias in at least one PROBAST domain; 48 internal validation only (13 external); 16 used a paediatric pneumonia set as controls; 'Frankenstein' datasets produced duplicated train/test data; only 13 shared code. None of the models were judged to be of potential clinical use.
- Code / weights / license: not applicable
- Useful for us: list of pitfalls to avoid (duplicate data across public sets, patient leakage between splits).
- Limitations / notes: COVID-specific; CLAIM and RQS are not comparable; PROBAST sample-size rules may not suit DL; search cutoff Oct 2020. Recommendations relevant to us: avoid Frankenstein public-data mixes (check duplicates across spine datasets), use patient-level splits, report calibration, decision curves and CIs, set operating points on development data, and follow CLAIM/TRIPOD.
- BibTeX:
```bibtex
@article{Roberts2021Pitfalls,
  title   = {Common pitfalls and recommendations for using machine learning to detect and prognosticate for {COVID-19} using chest radiographs and {CT} scans},
  author  = {Roberts, Michael and Driggs, Derek and Thorpe, Matthew and others},
  journal = {Nature Machine Intelligence},
  volume  = {3},
  number  = {3},
  pages   = {199--217},
  year    = {2021},
  doi     = {10.1038/s42256-021-00307-0}
}
```

### R268. Varoquaux and Cheplygina 2022 - methodological failures
- Full title: Machine learning for medical imaging: methodological failures and recommendations for the future
- Authors: Varoquaux G, Cheplygina V
- Year / Venue / Type: 2022 / npj Digital Medicine 5:48 / perspective-review
- DOI / arXiv / URL: 10.1038/s41746-022-00592-y ; preprint arXiv:2103.10292 (titled 'How I failed machine learning in medical imaging - shortcomings and recommendations')
- Access: open (CC BY)
- Passes: 2/3 (abstract; arXiv preprint full text read 2026-10-16. The preprint asks readers to cite the npj version, whose numbers may differ; the published version was not read.)
- Modality & anatomy: medical imaging, all
- Data: not applicable
- Method: evidence review on dataset bias, evaluation variance and research incentives
- Key results: (preprint):
  - A meta-analysis of 478 Alzheimer's/MCI studies found accuracy did not improve with sample size.
  - In 4 Kaggle challenges, the public-to-private leaderboard shift often exceeded the top-10% improvement, and only nerve segmentation showed real gains.
  - Leakage examples: feature selection before CV, repeated measures across splits, 'overfitting by observer'.
  - Only 6% of segmentation challenges and 15% of 410 ACM papers used significance tests, and 97% of those reported p < 0.05.
  - 179 classifiers on 121 datasets: the top methods were not significantly different.
  - Recommends test sets of at least several hundred, ideally thousands, of samples.
- Code / weights / license: not applicable
- Useful for us: justify confidence intervals on all metrics and caution about leaderboard comparisons.
- Limitations / notes: numbers come from the preprint, so check them against the npj version before quoting. Recommendations: multi-source data, leakage control, adequate test size, strong baselines, multiple metrics including calibration, variance analysis, registered reports, negative results.
- BibTeX:
```bibtex
@article{Varoquaux2022Failures,
  title   = {Machine learning for medical imaging: methodological failures and recommendations for the future},
  author  = {Varoquaux, Ga{\"e}l and Cheplygina, Veronika},
  journal = {npj Digital Medicine},
  volume  = {5},
  pages   = {48},
  year    = {2022},
  doi     = {10.1038/s41746-022-00592-y}
}
```

#### A. Reviews and meta-analyses of AI in spine imaging

### R269. Galbusera 2019 - AI and ML in spine research
- Full title: Artificial intelligence and machine learning in spine research
- Authors: Galbusera F, Casaroli G, Bassani T
- Year / Venue / Type: 2019 / JOR Spine 2(1):e1044 / narrative review
- DOI / arXiv / URL: 10.1002/jsp2.1044 ; PMID 31463458
- Access: open (CC BY-NC-ND)
- Passes: 1/3 (abstract via OpenAlex; round 3 retry on 2026-10-16 failed because the Wiley full text is blocked for fetching although the article is OA)
- Modality & anatomy: spine; radiographs, CT, MRI
- Data: not applicable (narrative review)
- Method: narrative review of AI/ML techniques and spine applications
- Key results: maps applications: vertebra and disc localisation, segmentation, computer-aided diagnosis, outcome and complication prediction, decision support, content-based image retrieval, biomechanics and motion analysis. Discusses accountability, bias, privacy and security.
- Code / weights / license: not applicable
- Useful for us: early field map to cite in the introduction; taxonomy of spine imaging tasks.
- Limitations / notes: pre-dates most deep-learning spine work (2019).
- BibTeX:
```bibtex
@article{Galbusera2019AISpine,
  title   = {Artificial intelligence and machine learning in spine research},
  author  = {Galbusera, Fabio and Casaroli, Gloria and Bassani, Tito},
  journal = {JOR Spine},
  volume  = {2},
  number  = {1},
  pages   = {e1044},
  year    = {2019},
  doi     = {10.1002/jsp2.1044}
}
```

### R270. D'Antoni 2021 - AI and computer vision in low back pain (systematic review)
- Full title: Artificial Intelligence and Computer Vision in Low Back Pain: A Systematic Review
- Authors: D'Antoni F, Russo F, Ambrosio L, et al.
- Year / Venue / Type: 2021 / International Journal of Environmental Research and Public Health 18(20):10909 / systematic review
- DOI / arXiv / URL: 10.3390/ijerph182010909
- Access: open (CC BY)
- Passes: 3/3 (abstract via OpenAlex; MDPI full text read 2026-10-16 for search, breakdown and best metrics, then for quality assessment and limitations)
- Modality & anatomy: lumbar spine; mainly MRI, also CT and radiographs
- Data: PubMed only, searched 18 Mar 2021; 558 records, 200 after title/abstract screening, 76 included (two independent reviewers). Excluded cervical, thoracic, trauma, osteoporotic and metastatic topics.
- Method: systematic review; quality assessed with customised QUADAS-2-based criteria (details in Supplementary Tables S1-S2)
- Key results: tasks: feature extraction 8 papers (all classical ML); segmentation 61 (38 digital image processing, 23 neural networks; DL modalities MRI 13, CT 5, X-ray 4, US 1; DL structures vertebrae 16, discs 11, canal 7, muscles 5). Best Dice: vertebrae >98.6% (DIP, CT, 41 subjects) and 94.2% (DL GAN, CT); discs 91.7% (DIP, 3D MRI), 89.4% (DL, SpineWeb MRI); paraspinal muscles >91.3% (DL); spinal canal 87% (DL). Identification accuracy up to 98.9% (DL, MRI, 1,318 subjects). Regression MAE: Cobb 3.42 deg; lumbar lordosis 8.06 deg. Datasets named: SpineWeb, Microsoft Research spine CT, LUMINOUS (US), MyoSegmentum (MRI).
- Code / weights / license: not applicable
- Useful for us: benchmark ranges to quote for lumbar segmentation; confirms that segmentation is largely solved and diagnosis/grading is the open problem.
- Limitations / notes: PubMed only, English only; heterogeneous metrics; the quality section rates 68 studies vs 76 included (internal inconsistency); many tiny studies. The authors conclude DL works well for segmentation and identification, while DIP remains competitive with less data, and AI cannot replace clinicians.
- BibTeX:
```bibtex
@article{DAntoni2021LBP,
  title   = {Artificial Intelligence and Computer Vision in Low Back Pain: A Systematic Review},
  author  = {D'Antoni, Federico and Russo, Fabrizio and Ambrosio, Luca and others},
  journal = {International Journal of Environmental Research and Public Health},
  volume  = {18},
  number  = {20},
  pages   = {10909},
  year    = {2021},
  doi     = {10.3390/ijerph182010909}
}
```

### R271. Hornung 2022 - AI in spine care
- Full title: Artificial intelligence in spine care: current applications and future utility
- Authors: Hornung AL, Hornung CM, Mallow GM, et al.
- Year / Venue / Type: 2022 / European Spine Journal 31(8):2057-2081 / review
- DOI / arXiv / URL: 10.1007/s00586-022-07176-0 ; PMID 35347425
- Access: paywalled (abstract not retrievable this session)
- Passes: metadata only (abstract not available in the index; Springer page fetch failed)
- Modality & anatomy: spine care broadly, including imaging
- Data: unverified
- Method: review
- Key results: unverified. Index keywords include machine learning, spinal surgery, osteoporosis screening and adolescent idiopathic scoliosis.
- Code / weights / license: not applicable
- Useful for us: a recent European Spine Journal review to cite for clinical applications; read in full before citing specifics.
- Limitations / notes: abstract and content to be verified.
- BibTeX:
```bibtex
@article{Hornung2022AISpineCare,
  title   = {Artificial intelligence in spine care: current applications and future utility},
  author  = {Hornung, Alexander L. and Hornung, Christopher M. and Mallow, G. Michael and others},
  journal = {European Spine Journal},
  volume  = {31},
  number  = {8},
  pages   = {2057--2081},
  year    = {2022},
  doi     = {10.1007/s00586-022-07176-0}
}
```

### R272. Vrtovec and Ibragimov 2022 - spinopelvic measurement with deep learning
- Full title: Spinopelvic measurements of sagittal balance with deep learning: systematic review and critical evaluation
- Authors: Tomaz Vrtovec (University of Ljubljana, corresponding), Bulat Ibragimov (University of Copenhagen and Ljubljana)
- Year / Venue / Type: 2022 / European Spine Journal 31(8):2031-2045 / systematic review
- DOI / arXiv / URL: 10.1007/s00586-022-07155-5 ; PMID 35278146 ; published online 12 Mar 2022 (bibliographic details re-confirmed via OpenAlex, 2026-10-16)
- Access: closed access. OpenAlex lists a submitted version in the University of Copenhagen repository without an OA URL. OpenAlex has no abstract.
- Passes: metadata only
- Modality & anatomy: sagittal radiographs, spine and pelvis
- Data: unverified
- Method: systematic review and critical evaluation
- Key results: unverified (abstract not retrieved; fetch budget ran out).
- Code / weights / license: not applicable
- Useful for us: directly relevant to "deviation from normal" measurements (pelvic incidence, sacral slope, pelvic tilt, lumbar lordosis). Read in full for error ranges.
- Limitations / notes: content to be verified.
- BibTeX:
```bibtex
@article{Vrtovec2022Spinopelvic,
  title   = {Spinopelvic measurements of sagittal balance with deep learning: systematic review and critical evaluation},
  author  = {Vrtovec, Toma{\v z} and Ibragimov, Bulat},
  journal = {European Spine Journal},
  volume  = {31},
  number  = {8},
  pages   = {2031--2045},
  year    = {2022},
  doi     = {10.1007/s00586-022-07155-5}
}
```

### R273. Joshi 2019 - AI for adult spinal deformity
- Full title: Artificial Intelligence for Adult Spinal Deformity
- Authors: Rushikesh S. Joshi, Alexander F. Haddad, Darryl Lau, Christopher P. Ames (corresponding)
- Year / Venue / Type: 2019 / Neurospine 16(4):686-694 / narrative review
- DOI / arXiv / URL: 10.14245/ns.1938414.207
- Access: open (CC BY-NC)
- Passes: 3/3 (abstract; Neurospine full text read 2026-10-16 for the applications and their numbers, then for limitations and future directions)
- Modality & anatomy: adult spinal deformity; clinical and radiographic alignment data
- Data: not applicable
- Method: review of ML for outcome prediction and patient classification
- Key results: tabulates ASD ML studies, almost all tree ensembles or regression on clinical and radiographic variables:
  - early major complications: AUC 0.89 (n = 557)
  - proximal junctional failure: AUC 0.89 (n = 510)
  - pseudarthrosis: AUC 0.94 (n = 336)
  - major complications, readmission and reoperation: AUC 0.67-0.92 (n = 1,612)
  - MCID in ODI: AUC 0.94-0.96
  - SRS-22 item prediction: AUC 0.57-0.87
  - 2-year cost: R2 29-35%

  Unsupervised clustering of 570 patients gave 3 patient clusters and 4 surgical clusters with different risk-benefit profiles. One study reporting 100% test accuracy had only 33 test patients. The review does not cover image-based or automated alignment measurement.
- Code / weights / license: not applicable
- Useful for us: context for why spinopelvic deviation measurements matter clinically (they feed ASD surgical planning).
- Limitations / notes: outcome prediction only, with no imaging AI; small samples and overfitting risk; scarce prospective databases; class imbalance; interpretability. Future directions: multicentre prospective databases, EMR integration, and the ISSG ASD risk calculator.
- BibTeX:
```bibtex
@article{Joshi2019ASD,
  title   = {Artificial Intelligence for Adult Spinal Deformity},
  author  = {Joshi, Rushikesh S. and Haddad, Alexander F. and Lau, Darryl and Ames, Christopher P.},
  journal = {Neurospine},
  volume  = {16},
  number  = {4},
  pages   = {686--694},
  year    = {2019},
  doi     = {10.14245/ns.1938414.207}
}
```

### R274. Litjens 2017 - survey of deep learning in medical image analysis
- Full title: A survey on deep learning in medical image analysis
- Authors: Litjens G, Kooi T, Ehteshami Bejnordi B, et al.
- Year / Venue / Type: 2017 / Medical Image Analysis 42:60-88 / survey
- DOI / arXiv / URL: 10.1016/j.media.2017.07.005 ; arXiv:1702.05747
- Access: open (bronze; arXiv)
- Passes: 1/3 (metadata and arXiv abstract; round 3 on 2026-10-16: the arXiv v2 PDF extraction confirmed 'over 300 contributions', papers up to 1 Feb 2017, and the task and anatomy taxonomy (incl. a musculoskeletal section), but the text was cut at the breast section, so the MSK section and Discussion were not read)
- Modality & anatomy: all; includes a musculoskeletal section (per the full paper; not re-read)
- Data: more than 300 papers
- Method: survey across classification, detection, segmentation, registration and other tasks
- Key results: field map up to early 2017 with open challenges.
- Code / weights / license: not applicable
- Useful for us: classic general citation for deep learning in medical imaging, placed before spine-specific reviews.
- Limitations / notes: pre-transformer era.
- BibTeX:
```bibtex
@article{Litjens2017Survey,
  title   = {A survey on deep learning in medical image analysis},
  author  = {Litjens, Geert and Kooi, Thijs and Ehteshami Bejnordi, Babak and Setio, Arnaud Arindra Adiyoso and Ciompi, Francesco and Ghafoorian, Mohsen and van der Laak, Jeroen A. W. M. and van Ginneken, Bram and S{\'a}nchez, Clara I.},
  journal = {Medical Image Analysis},
  volume  = {42},
  pages   = {60--88},
  year    = {2017},
  doi     = {10.1016/j.media.2017.07.005}
}
```

### R275. Wang 2024 - ML/DL for diagnosis of lumbar spinal stenosis (systematic review and meta-analysis)
- Full title: Machine Learning and Deep Learning for Diagnosis of Lumbar Spinal Stenosis: Systematic Review and Meta-Analysis
- Authors: Tianyi Wang, Ruiyuan Chen, Ning Fan, Lei Zang, Shuo Yuan, Peng Du, Qichao Wu, Aobo Wang, Jian Li, Xiaochuan Kong, Wenyi Zhu
- Year / Venue / Type: 2024 (published 23 Dec 2024) / Journal of Medical Internet Research 26:e54676 / systematic review and meta-analysis
- DOI / arXiv / URL: 10.2196/54676 (from JMIR BibTeX export); https://www.jmir.org/2024/1/e54676 ; PMC11704645
- Access: open (JMIR)
- Passes: 1/3 (JMIR BibTeX export with abstract, 2026-10-16; full text not read because the fetch budget ran out and Europe PMC/PMC were rate-limited or CAPTCHA-blocked)
- Modality & anatomy: lumbar spine; imaging modalities of included studies not confirmed (abstract-level only)
- Data: 12 included studies, 15,044 patients
- Method: systematic review + diagnostic-accuracy meta-analysis of traditional ML and DL models for lumbar spinal stenosis; risk of bias assessed (tool not confirmed at abstract level)
- Key results: risk of bias high in 4, unclear in 3, low in 5 studies; pooled sensitivity 0.84 (95% CI 0.82-0.86), specificity 0.87 (0.84-0.90), DOR 36 (26-49), LR+ 6.6 (5.1-8.4), LR- 0.18 (0.16-0.21), summary AUC 0.92 (0.89-0.94).
- Code / weights / license: not applicable
- Useful for us: the up-to-date pooled benchmark for AI stenosis diagnosis to position our MRI stenosis-grading results; its call for objective reference standards, external validation and complete reporting matches our CLAIM/TRIPOD+AI plan.
- Limitations / notes: authors conclude no model is yet reliable enough for routine clinical use; call for better sensitivity/specificity balance, objective reference standards, multimodal approaches, larger datasets, external validation. Subgroup results (MRI vs CT, DL vs ML, central vs foraminal) not yet extracted; pass 2 should read the full text.
- BibTeX:
```bibtex
@article{Wang2024LSSMeta,
  title   = {Machine Learning and Deep Learning for Diagnosis of Lumbar Spinal Stenosis: Systematic Review and Meta-Analysis},
  author  = {Wang, Tianyi and Chen, Ruiyuan and Fan, Ning and Zang, Lei and Yuan, Shuo and Du, Peng and Wu, Qichao and Wang, Aobo and Li, Jian and Kong, Xiaochuan and Zhu, Wenyi},
  journal = {Journal of Medical Internet Research},
  volume  = {26},
  pages   = {e54676},
  year    = {2024},
  doi     = {10.2196/54676}
}
```

### R276. Ghareh Mohammadi & Sebro 2026 - AI opportunistic CT screening for osteoporosis and spine fractures (systematic review and meta-analysis)
- Full title: Artificial Intelligence for Opportunistic Screening for Osteoporosis and Spine Fractures Using Computed Tomography: A Systematic Review and Meta-Analysis
- Authors: Farid Ghareh Mohammadi, Ronnie Sebro (as listed on the CiteDrive record; completeness of author list unverified)
- Year / Venue / Type: 2026 / Journal of Computer Assisted Tomography (inferred from e-ISSN 1532-3145, Wolters Kluwer; journal name not shown on the record), volume/issue/pages not yet available / systematic review and meta-analysis
- DOI / arXiv / URL: 10.1097/rct.0000000000001899
- Access: likely paywalled (Wolters Kluwer); abstract read via CiteDrive discovery page
- Passes: 1/3 (abstract via CiteDrive record, 2026-10-16; publisher page not read)
- Modality & anatomy: CT (opportunistic); abdomen / lumbar spine most studied
- Data: 31 of 1,258 screened studies (26 osteoporosis screening, 5 fracture screening); English-language, 2011-2025; PubMed, Web of Science, Scopus, Google Scholar; DXA reference standard
- Method: PRISMA; QUADAS-2; random-effects meta-analysis of AUC
- Key results: osteoporosis screening, abdomen/L-spine pooled AUC 0.931 (95% CI 0.926-0.936), I2 = 47.24%; ML in 21/26 studies (SVM most common, 13/21), DL in 4/26 (custom CNNs 3/4). Fracture screening, abdomen/L-spine pooled AUC 0.863 (95% CI 0.73-0.936), I2 = 64.8%; only 1/5 used DL. No pooled sensitivity/specificity in the abstract.
- Code / weights / license: not applicable
- Useful for us: shows the opportunistic-CT literature is dominated by classical ML and has very few DL fracture studies, which positions a DL spine CT pipeline that also reports bone status; DXA as reference standard is the norm to adopt if we add a BMD output.
- Limitations / notes: small fracture subset (5 studies) with wide CI; bibliographic details (volume/pages) to be completed when the issue is published; full text not read.
- BibTeX:
```bibtex
@article{GharehMohammadi2026OpportunisticCT,
  title   = {Artificial Intelligence for Opportunistic Screening for Osteoporosis and Spine Fractures Using Computed Tomography: A Systematic Review and Meta-Analysis},
  author  = {Ghareh Mohammadi, Farid and Sebro, Ronnie},
  journal = {Journal of Computer Assisted Tomography},
  year    = {2026},
  doi     = {10.1097/rct.0000000000001899},
  note    = {Journal inferred from ISSN 1532-3145; volume and pages not yet verified}
}
```

### R277. Zhu 2025 - deep learning for automated Cobb angle measurement on X-rays (systematic review and meta-analysis)
- Full title: Deep learning in Cobb angle automated measurement on X-rays: a systematic review and meta-analysis
- Authors: Yuanpeng Zhu, Xiangjie Yin, Zefu Chen, Haoran Zhang, Kexin Xu, Jianguo Zhang, Nan Wu
- Year / Venue / Type: 2025 / Spine Deformity 13:19-27 / systematic review and meta-analysis (PROSPERO CRD42023403057; PRISMA)
- DOI / arXiv / URL: 10.1007/s43390-024-00954-4 (Springer page); PMC11729091
- Access: open (CC BY 4.0)
- Passes: 3/3 (Springer abstract, then the Springer full text read twice on 2026-10-16: methods/results, then discussion/limitations; forest-plot per-study values not extracted)
- Modality & anatomy: radiographs; whole spine (scoliosis, Cobb angle)
- Data: PubMed, Embase, Web of Science, IEEE Xplore, Cochrane and arXiv to Sep 2023, English only. Inclusion: non-operated patients with vertebral deformity, CMAE reported, validated against clinical experts, Cobb angle on AP radiographs only (not CT/MRI). 50 studies (55 models, 2016-2023; 35/55 from China; only 3 prospective, 1 multicentre) in the systematic review, 17 in the meta-analysis. Data: 21 models used the AASCE 2019 challenge set (707 AP X-rays: 609 train / 98 test), 24 private, 5 both, 2 other public, 3 unspecified. Search count reported as 3022 in the abstract but 3032 in the results.
- Method: pooled circular mean absolute error (CMAE) of deep-learning Cobb angle algorithms vs manual reference; risk of bias with revised QUADAS-2
- Key results: random-effects pooled CMAE 2.99 deg (95% CI 2.61-3.38), I2 = 94% (p < 0.01). Segmentation-based CMAE 2.40 (1.85-2.95, I2 89%, 6 models) vs landmark-based 3.31 (2.89-3.72, I2 93%, 11 models); subgroup p < 0.01, but the Results section calls this only a 'trend'. Leave-one-out sensitivity analysis was stable. Funnel plot asymmetric but Egger p = 0.283. QUADAS-2 low risk: patient selection 82.35%, index test 47.06%, reference standard 35.29% (47.06% unclear), flow/timing 52.94%. The reported 'unclear' figure for the index test (47.18%) does not match 7/17.
- Code / weights / license: not applicable
- Useful for us: benchmark target for our X-ray Cobb angle module (pooled ~3 deg CMAE). The paper gives no quantitative inter-observer comparison, so cite a primary reliability study for the ~5 deg manual variability. AASCE 2019 is the shared public test set to report on; supports a segmentation-based rather than landmark-only design; CMAE is the metric to report alongside Bland-Altman/ICC.
- Limitations / notes: very high heterogeneity. Authors' limitations: end-vertebra selection accuracy rarely assessed, no standard evaluation framework, heterogeneous designs, no large-scale validation, AP view only. Their recommendations are two-stage models, combining segmentation and landmarks, multi-view (AP + lateral) modelling, weighing efficiency and integration, and following reporting guidelines.
- BibTeX:
```bibtex
@article{Zhu2025CobbMeta,
  title   = {Deep learning in Cobb angle automated measurement on X-rays: a systematic review and meta-analysis},
  author  = {Zhu, Yuanpeng and Yin, Xiangjie and Chen, Zefu and Zhang, Haoran and Xu, Kexin and Zhang, Jianguo and Wu, Nan},
  journal = {Spine Deformity},
  volume  = {13},
  pages   = {19--27},
  year    = {2025},
  doi     = {10.1007/s43390-024-00954-4}
}
```

### R278. Beculic 2024 - ML/DL for thoracolumbar vertebral fracture diagnosis (systematic review and meta-analysis)
- Full title: Sensitivity and specificity of machine learning and deep learning algorithms in the diagnosis of thoracolumbar injuries resulting in vertebral fractures: A systematic review and meta-analysis
- Authors: Hakija Beculic, Emir Begagic (corresponding), Amina Dzidic-Krivic, Ragib Pugonja, Namira Softic, Binasa Basic, Simon Adewale Balogun, Adem Nuhovic, Emir Softic, Adnana Ljevakovic, Haso Sefo, Sabina Segalo, Rasim Skomorac, Mirza Pojskic
- Year / Venue / Type: 2024 / Brain and Spine 4:102809 / systematic review and meta-analysis (PRISMA)
- DOI / arXiv / URL: 10.1016/j.bas.2024.102809 (confirmed via OpenAlex record pmid:38681175); PMID 38681175; PMCID PMC11052896; DOAJ record doaj.org/article/4e79b40490824803bbcb5f84d1b7fd97
- Access: open (gold OA, CC BY-NC-ND per OpenAlex)
- Passes: 1/3 (abstract via the BVS/LILACS MEDLINE record, DOAJ metadata, and OpenAlex for DOI/OA, 2026-10-16; full text not read because ScienceDirect is robots-blocked and PMC is CAPTCHA-blocked)
- Modality & anatomy: thoracolumbar spine; imaging modalities of included studies not confirmed at abstract level
- Data: PubMed and Scopus; 793 records; 17 studies in the systematic review, 11 in the meta-analysis, 14,524 participants; 29.41% of studies from China; 2 ML (11.76%) vs 15 DL (88.24%)
- Method: diagnostic-accuracy meta-analysis (pooled sensitivity/specificity)
- Key results: pooled sensitivity 0.91 (95% CI 0.86-0.95), specificity 0.90 (0.86-0.93), false-positive rate 0.097 (0.068-0.137).
- Code / weights / license: not applicable
- Useful for us: pooled reference point for trauma (thoracolumbar injury) fracture detection, complementing osteoporotic-fracture reviews; DL dominates the literature.
- Limitations / notes: only two databases; small meta-analysis (11 studies); authors call for methodological standardisation before clinical use.
- BibTeX:
```bibtex
@article{Beculic2024ThoracolumbarMeta,
  title   = {Sensitivity and specificity of machine learning and deep learning algorithms in the diagnosis of thoracolumbar injuries resulting in vertebral fractures: A systematic review and meta-analysis},
  author  = {Be{\v{c}}uli{\'c}, Hakija and Begagi{\'c}, Emir and D{\v{z}}idi{\'c}-Krivi{\'c}, Amina and Pugonja, Ragib and Softi{\'c}, Namira and Ba{\v{s}}i{\'c}, Binasa and Balogun, Simon and Nuhovi{\'c}, Adem and Softi{\'c}, Emir and Ljevakovi{\'c}, Adnana and Sefo, Haso and {\v{S}}egalo, Sabina and Skomorac, Rasim and Pojski{\'c}, Mirza},
  journal = {Brain and Spine},
  volume  = {4},
  pages   = {102809},
  year    = {2024},
  doi     = {10.1016/j.bas.2024.102809}
}
```

### R279. Li 2024 - machine learning for diagnosis of vertebral fractures (systematic review and meta-analysis)
- Full title: Machine learning value in the diagnosis of vertebral fractures: A systematic review and meta-analysis
- Authors: Yue Li, Zhuang Liang, Yingchun Li, Yang Cao, Hui Zhang, Bo Dong (corresponding)
- Year / Venue / Type: 2024 / European Journal of Radiology 181:111714 / systematic review and meta-analysis
- DOI / arXiv / URL: 10.1016/j.ejrad.2024.111714 (OpenAlex)
- Access: open (hybrid OA, CC BY-NC-ND per OpenAlex). The ejradiology.com PDF could not be fetched.
- Passes: 1/3 (abstract read twice, 2026-10-16: the Epistemonikos record, then OpenAlex metadata and inverted index; the numbers agree)
- Modality & anatomy: CT, X-ray, MRI and clinical features; vertebral fractures
- Data: PubMed, Embase, Cochrane Library and Web of Science searched to 31 Dec 2023; 81 included studies
- Method: QUADAS-2; bivariate mixed-effects model; five tasks; subgroups by model type (ML vs DL) and modality
- Key results: pooled sensitivity/specificity by task:
  - vertebral fracture detection 0.91/0.95, best SROC subgroups DL 0.98 and CT 0.98
  - osteoporotic vertebral fracture 0.93/0.96, best DL 0.99 and X-ray 0.99
  - benign vs malignant 0.92/0.93, best DL 0.96 and MRI 0.97
  - acute vs chronic 0.92/0.93, best ML 0.96 and CT 0.97
  - fracture prediction 0.76/0.87, best ML 0.80 and clinical features 0.86

  CIs are not in the abstract.
- Code / weights / license: not applicable
- Useful for us: the broadest pooled benchmark for spine fracture AI across CT, X-ray and MRI. It also covers acute vs chronic and benign vs malignant tasks, which map onto our MRI/CT findings.
- Limitations / notes: abstract-level only. The authors call for further validation. CIs, heterogeneity and the external-validation share still need the full text.
- BibTeX:
```bibtex
@article{Li2024VFMeta,
  title   = {Machine learning value in the diagnosis of vertebral fractures: A systematic review and meta-analysis},
  author  = {Li, Yue and Liang, Zhuang and Li, Yingchun and Cao, Yang and Zhang, Hui and Dong, Bo},
  journal = {European Journal of Radiology},
  volume  = {181},
  pages   = {111714},
  year    = {2024},
  doi     = {10.1016/j.ejrad.2024.111714}
}
```

---

#### D. Regulation, evidence for commercial products, ethics of patient-facing AI

### R280. van Leeuwen 2021 - 100 commercial radiology AI products
- Full title: Artificial intelligence in radiology: 100 commercially available products and their scientific evidence
- Authors: van Leeuwen KG, Schalekamp S, Rutten MJCM, et al.
- Year / Venue / Type: 2021 / European Radiology 31(6):3797-3804 / review
- DOI / arXiv / URL: 10.1007/s00330-021-07892-z
- Access: open (CC BY)
- Passes: 3/3 (abstract; Springer full text read 2026-10-16 for methods and breakdowns, then for limitations and recommendations)
- Modality & anatomy: radiology, all (includes musculoskeletal and spine products)
- Data: 100 CE-marked radiology AI products (CE by April 2020; status as of Sep 2020) from RSNA/ECR exhibitor lists, marketplaces and news, verified with vendors. PubMed search 1 Jan 2015 to 18 May 2020 (791 hits, 175 included) plus 62 from manual search, giving 237 papers.
- Method: product overview (AIforRadiology.com) plus literature search, graded with a hierarchical efficacy model (Fryback and Thornbury)
- Key results: subspecialties: neuro 38, chest 31, breast 12, MSK 11 (no separate spine count). Modalities: CT 37, MR 25, X-ray 22. Quantification was the most common task (33). CE class I 32%, IIa 53%. 51/100 FDA-cleared. 64/100 products had no peer-reviewed evidence. Of 237 papers: level 1 27%, level 2 (diagnostic accuracy) 65%, level >= 3 covering 18 products; 116/237 vendor-independent; 192/237 retrospective; 30% multicentre, 15% multinational, 25% multi-vendor.
- Code / weights / license: not applicable
- Useful for us: evidence that CE-marked or cleared spine AI often lacks independent evidence; supports our open-evaluation stance.
- Limitations / notes: 2020 snapshot; incomplete vendor data; PubMed and manual search only. The authors suggest public CE-mark validation data (EUDAMED) and say level-2 accuracy may suffice for measurement tasks, which is relevant to our spinal measurements.
- BibTeX:
```bibtex
@article{vanLeeuwen2021Products,
  title   = {Artificial intelligence in radiology: 100 commercially available products and their scientific evidence},
  author  = {van Leeuwen, Kicky G. and Schalekamp, Steven and Rutten, Matthieu J. C. M. and van Ginneken, Bram and de Rooij, Maarten},
  journal = {European Radiology},
  volume  = {31},
  number  = {6},
  pages   = {3797--3804},
  year    = {2021},
  doi     = {10.1007/s00330-021-07892-z}
}
```

### R281. Wu 2021 - how FDA-cleared medical AI devices are evaluated
- Full title: How medical AI devices are evaluated: limitations and recommendations from an analysis of FDA approvals
- Authors: Wu E, Wu K, Daneshjou R, et al.
- Year / Venue / Type: 2021 / Nature Medicine 27(4):582-584 / comment
- DOI / arXiv / URL: 10.1038/s41591-021-01312-x
- Access: paywalled (preview only)
- Passes: abstract only, paywalled (preview read)
- Modality & anatomy: all FDA-cleared AI devices (130 analysed)
- Data: database of 130 FDA-approved AI devices
- Method: audit of FDA summaries; case study
- Key results: evaluation practices can mask vulnerabilities once devices meet patients. Detailed counts (retrospective vs prospective; single vs multi-site) not readable in the preview; the widely cited figure that most were retrospective-only is unverified here.
- Code / weights / license: database and code reported as public (URL not recorded)
- Useful for us: cite when contrasting regulatory evidence with multi-site testing.
- Limitations / notes: verify counts before quoting.
- BibTeX:
```bibtex
@article{Wu2021FDAEvaluation,
  title   = {How medical {AI} devices are evaluated: limitations and recommendations from an analysis of {FDA} approvals},
  author  = {Wu, Eric and Wu, Kevin and Daneshjou, Roxana and Ouyang, David and Ho, Daniel E. and Zou, James},
  journal = {Nature Medicine},
  volume  = {27},
  number  = {4},
  pages   = {582--584},
  year    = {2021},
  doi     = {10.1038/s41591-021-01312-x}
}
```

### R282. FDA list of AI-enabled medical devices (incl. FDA-cleared spine AI)
- Full title: Artificial Intelligence-Enabled Medical Devices (List of AI-Enabled Medical Devices)
- Authors: US Food and Drug Administration, Digital Health Center of Excellence
- Year / Venue / Type: continuously updated (page modified 2026) / regulatory database web page
- DOI / arXiv / URL: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices
- Access: open
- Passes: 2/3 (page read twice: compilation notes, then spine rows in both halves of the visible table)
- Modality & anatomy: all; spine-related rows extracted
- Data: devices identified by AI terms in their authorisation summaries; FDA says the list is not comprehensive
- Method: regulatory listing, reverse-chronological
- Key results: spine-related rows visible on 2026-10-16 (most recent part of the table only): Spine Auto-Seg (Agada Medical, K253628, 2026-06-29, Radiology); DeepXray Spina (Alpha Intelligence Manifolds, K253192, 2026-06-10, Radiology; spine indication inferred from name only); UNiD Spine Analyzer (Medicrea/Medtronic, K261289, 2026-05-15, Radiology); CoLumbo C-Spine (Smart Soft Healthcare, K254015, 2026-04-01, Radiology); Stealth AXiS Spine (Medtronic Navigation, K253381, 2026-02-12, Neurology); SafeOp 3 (Alphatec Spine, K252842, 2026-01-11, Neurology); xvision Spine (Augmedics, K251639, 2025-10-03); SpineAR SNAP (Surgical Theater, K252054, 2025-09-29). Older spine clearances are in the downloadable full list, not read here. FDA plans to tag devices that use foundation models or LLMs.
- Code / weights / license: public domain (US government)
- Useful for us: cite for the commercial landscape of spine AI (radiology triage/segmentation for CoLumbo-type MRI reports, surgical planning for UNiD). Check each 510(k) summary for its evidence base before citing performance.
- Limitations / notes: the page shows only recent entries; the evidence behind each clearance not reviewed here.
- BibTeX:
```bibtex
@misc{FDA2026AIDeviceList,
  title        = {Artificial Intelligence-Enabled Medical Devices},
  author       = {{U.S. Food and Drug Administration}},
  howpublished = {\url{https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices}},
  note         = {Accessed 2026-10-16},
  year         = {2026}
}
```

### R283. FDA draft guidance - AI-enabled device software functions
- Full title: Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations (Draft Guidance)
- Authors: US FDA (CDRH, with CBER, CDER and the Office of Combination Products)
- Year / Venue / Type: January 2025 (the PDF is dated 7 Jan 2025; the landing page said 6 Jan) / FDA draft guidance, docket FDA-2024-D-4488 / regulatory guidance
- DOI / arXiv / URL: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing ; PDF fda.gov/media/184856/download
- Access: open
- Passes: 2/3 (guidance landing page; PDF read 2026-10-16 through Section X and the appendix list. Sections XI-XIII (performance monitoring, cybersecurity, public summary) were cut off in extraction.)
- Modality & anatomy: all AI-enabled devices
- Data: not applicable
- Method: total product life-cycle approach to documentation for marketing submissions
- Key results: draft, not for implementation (90-day comment period). Covers 510(k), De Novo, PMA, HDE and BLA submissions for AI-DSFs with a total-product-lifecycle approach.
  - Device description: inputs, outputs, users, workflow, degree of automation, operating points.
  - Labelling: AI use, architecture, development and performance data incl. subgroup performance and CIs, known limitations; a model card is suggested (examples in Appendices E-F).
  - Risk management per ISO 14971.
  - Data management: sites and time periods, reference-standard uncertainty and reader variability, independent annotations, test data sequestered and generally from different sites, representativeness (e.g. at least 3 geographically diverse US sites; justify non-US data), demographic breakdowns.
  - Model description: architecture, loss, calibration, thresholds.
  - Validation: performance plus human factors/usability; post-hoc changes based on test data need FDA concurrence.
  - PCCP encouraged; monitor data drift.
- Code / weights / license: public domain
- Useful for us: frames what would be needed to move from research prototype to device; supports our model card and subgroup reporting.
- Limitations / notes: still draft at the last check; sections XI-XIII not read. The PCCP final guidance is logged as [D09]. For us: separate-site test data, subgroup CIs and model-card style labelling are the minimum we should mirror.
- BibTeX:
```bibtex
@misc{FDA2025AIEnabledDraft,
  title        = {Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations. Draft Guidance for Industry and Food and Drug Administration Staff},
  author       = {{U.S. Food and Drug Administration}},
  howpublished = {\url{https://www.fda.gov/media/184856/download}},
  note         = {Docket FDA-2024-D-4488, issued January 2025},
  year         = {2025}
}
```

### R284. EU AI Act - Article 6 high-risk classification
- Full title: Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence (Artificial Intelligence Act); Article 6, Classification rules for high-risk AI systems
- Authors: European Parliament and Council of the European Union
- Year / Venue / Type: 2024 (adopted 13 June 2024, per the EUR-Lex title and metadata) / Official Journal of the European Union / legislation (the OJ L issue reference is still not seen)
- DOI / arXiv / URL: https://eur-lex.europa.eu/eli/reg/2024/1689/oj ; article text read at https://artificialintelligenceact.eu/article/6/
- Access: open
- Passes: 2/3 (Article 6 text via a third-party mirror; round 3 on 2026-10-16: EUR-Lex record read for the title and date, and the Article 2 text read on the same mirror for the research exemptions)
- Modality & anatomy: not applicable
- Data: not applicable
- Method: legislation
- Key results: an AI system is high-risk if it is a safety component of, or itself, a product under Annex I harmonisation legislation (which includes the Medical Device Regulation) that requires third-party conformity assessment. Article 6(3) allows a derogation for Annex III systems that do not materially influence decisions; profiling is always high-risk. The mirror page states Annex III obligations apply from 2 December 2027 and Annex I obligations from 2 August 2028 (this reflects a later amendment to the original timeline; verify against the consolidated text before citing).
- Code / weights / license: not applicable
- Useful for us: an image-analysis tool giving diagnostic output would be a medical device under MDR (class IIa or higher under Rule 11, unverified here) and hence high-risk under the AI Act. Our prototype must be framed as research-only, not placed on the market.
- Limitations / notes: Article 2 (mirror text): 2(6) excludes AI systems or models, including their output, developed and put into service solely for scientific research and development; 2(8) excludes research, testing and development before placing on the market or putting into service, but NOT testing in real-world conditions, and other Union law still applies. The mirror marks paragraphs 2 and 7 as amended. This supports framing our prototype as research-only, but a public demo used on real patients' scans could count as real-world testing; check before any public release. MDR (EU) 2017/745 Rule 11 is still not opened.
- BibTeX:
```bibtex
@misc{EU2024AIAct,
  title        = {Regulation ({EU}) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence ({Artificial Intelligence Act})},
  author       = {{European Parliament and Council of the European Union}},
  howpublished = {Official Journal of the European Union, \url{https://eur-lex.europa.eu/eli/reg/2024/1689/oj}},
  year         = {2024}
}
```

### R285. Gilbert 2023 - LLM chatbots require approval as medical devices
- Full title: Large language model AI chatbots require approval as medical devices
- Authors: Gilbert S, Harvey H, Melvin T, et al.
- Year / Venue / Type: 2023 / Nature Medicine 29(10):2396-2398 / comment
- DOI / arXiv / URL: 10.1038/s41591-023-02412-6
- Access: paywalled (no abstract available)
- Passes: metadata only, paywalled
- Modality & anatomy: patient- and clinician-facing LLM tools
- Data: not applicable
- Method: regulatory commentary
- Key results: argues that LLM chatbots used for diagnosis or medical advice fall within medical device law (EU MDR, US FDA) and need approval (content summarised from title; argument details unverified).
- Code / weights / license: not applicable
- Useful for us: if the prototype writes natural-language reports for patients, this frames the regulatory risk of direct-to-patient interpretation; supports the "research prototype, not for diagnosis" disclaimer.
- Limitations / notes: read full text before quoting.
- BibTeX:
```bibtex
@article{Gilbert2023LLMDevices,
  title   = {Large language model {AI} chatbots require approval as medical devices},
  author  = {Gilbert, Stephen and Harvey, Hugh and Melvin, Tom and Vollebregt, Erik and Wicks, Paul},
  journal = {Nature Medicine},
  volume  = {29},
  number  = {10},
  pages   = {2396--2398},
  year    = {2023},
  doi     = {10.1038/s41591-023-02412-6}
}
```

### R286. Good Machine Learning Practice (GMLP) guiding principles - FDA, Health Canada, MHRA (2021); IMDRF N88 (2025)
- Full title: Good Machine Learning Practice for Medical Device Development: Guiding Principles
- Authors: US FDA, Health Canada, UK MHRA (joint); later adopted and extended by IMDRF as final document N88 (January 2025)
- Year / Venue / Type: first published 27 Oct 2021 (GOV.UK page last updated 5 Oct 2026); IMDRF final document January 2025 / regulator guiding principles
- DOI / arXiv / URL: https://www.gov.uk/government/publications/good-machine-learning-practice-for-medical-device-development-guiding-principles ; FDA page https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles (current as of 19 Dec 2025)
- Access: open
- Passes: 2/3 (2026-10-16: FDA page read for status and the IMDRF link, then the GOV.UK page for all 10 principles; IMDRF N88 not read)
- Modality & anatomy: all ML-enabled medical devices
- Data: not applicable
- Method: 10 principles agreed by the three regulators
- Key results: the 10 principles:
  1. Multidisciplinary expertise is leveraged throughout the total product life cycle.
  2. Good software engineering and security practices are implemented.
  3. Clinical study participants and data sets are representative of the intended patient population.
  4. Training data sets are independent of test sets (accounting for patient, source and site overlap).
  5. Selected reference datasets are based upon best available methods.
  6. Model design is tailored to the available data and reflects the intended use of the device.
  7. Focus is placed on the performance of the human-AI team.
  8. Testing demonstrates device performance during clinically relevant conditions, including subgroups.
  9. Users are provided clear, essential information (intended use, subgroup performance, data, limitations, updates).
  10. Deployed models are monitored for performance and retraining risks are managed.
- Code / weights / license: Crown copyright / US public domain texts
- Useful for us: a short regulatory checklist to cite in the paper's deployment section. Principle 4 matches patient-level splits. Principles 3 and 8 match subgroup testing by sex, age and scanner vendor. Principle 7 supports evaluating the reader plus AI and the abstention/referral behaviour. Principle 9 supports model cards.
- Limitations / notes: these are principles, not binding requirements. The IMDRF N88 wording may differ from the 2021 text, so read it before quoting the 2025 version.
- BibTeX:
```bibtex
@misc{FDA2021GMLP,
  title        = {Good Machine Learning Practice for Medical Device Development: Guiding Principles},
  author       = {{U.S. Food and Drug Administration} and {Health Canada} and {Medicines and Healthcare products Regulatory Agency}},
  howpublished = {\url{https://www.gov.uk/government/publications/good-machine-learning-practice-for-medical-device-development-guiding-principles}},
  year         = {2021},
  note         = {Published 27 October 2021}
}
```

### R287. FDA final guidance - Predetermined Change Control Plans (PCCP) for AI-enabled device software functions
- Full title: Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions
- Authors: US FDA, CDRH (with Digital Health Center of Excellence and OPEQ input)
- Year / Venue / Type: final guidance issued 4 Dec 2024 / FDA guidance / regulatory guidance
- DOI / arXiv / URL: fda.gov/media/187905/download. This document appears to be the FDA webinar material on the guidance (webinar 14 Jan 2025), not the guidance PDF itself. The docket number was not seen.
- Access: open
- Passes: 1/3 (FDA webinar document read 2026-10-16; guidance PDF itself not read)
- Modality & anatomy: all AI-enabled device software functions (AI-DSFs)
- Data: not applicable
- Method: an optional standalone PCCP section in a 510(k), De Novo or PMA submission, with three components:
  - Description of modifications: specific and limited in number; each states whether it is implemented manually or automatically, and globally or locally.
  - Modification protocol: data management, retraining, performance evaluation and update procedures, with predefined acceptance criteria and a traceability table.
  - Impact assessment: benefits and risks of each modification and of all of them together, compared against the unmodified device.
- Key results:
  - In scope: modifications that would otherwise need a new submission and that stay within the intended use. Examples are quantitative performance changes (retraining on new data from the same population and input type), input/compatibility changes (new sources of the same signal), and limited use/performance changes (for example a subpopulation).
  - Continuously learning or automatic updates are covered, but FDA strongly encourages a Pre-Submission first.
  - Labelling must say the device has an authorised PCCP and must be updated with performance, data and version history as changes are made.
  - Only one authorised PCCP version applies at a time.
- Code / weights / license: public domain
- Useful for us: the regulatory frame for retraining our spine models on new scanners or sites after release. The 'new sources of the same input signal' modification type fits new MRI vendors.
- Limitations / notes: read through the webinar material only. The guidance text and Appendix A example questions still need to be read before quoting.
- BibTeX:
```bibtex
@misc{FDA2024PCCP,
  title        = {Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions. Guidance for Industry and Food and Drug Administration Staff},
  author       = {{U.S. Food and Drug Administration}},
  year         = {2024},
  note         = {Final guidance issued 4 December 2024}
}
```

---

#### E. Privacy-preserving, on-device and in-browser inference; federated learning

### R288. TensorFlow.js
- Full title: TensorFlow.js: Machine Learning for the Web and Beyond
- Authors: Smilkov D, Thorat N, Assogba Y, et al.
- Year / Venue / Type: 2019 / Proceedings of the 2nd SysML Conference, Palo Alto (confirmed from the PDF header) / systems paper
- DOI / arXiv / URL: arXiv:1901.05350
- Access: preprint (open)
- Passes: 3/3 (abstract; arXiv PDF read 2026-10-16 for backends, design and benchmarks, then for limitations)
- Modality & anatomy: not medical
- Data: not applicable
- Method: JavaScript ML library. Backends: WebGL (fragment shaders), plain-JS CPU fallback, and Node.js bindings to the TF C API (CPU with AVX, CUDA); WASM and WebGPU only listed as future work. Keras-compatible Layers API, Ops API, eager autodiff, tf.tidy/dispose memory management, and a converter that packs weights in 4 MB shards with optional 4x quantisation.
- Key results: MobileNet v1 (224x224) inference: plain JS 3426 ms; WebGL on Intel Iris Pro 49 ms (71x); WebGL on a GTX 1080 5 ms; Node CPU 87 ms; Node CUDA 3 ms. WebGL is 3-10x slower than CUDA (no shared memory or work groups). WebGL support: 99% of desktops, 98% of iOS, 52% of Android devices.
- Code / weights / license: github.com/tensorflow/tfjs (Apache-2.0, per project; not re-checked)
- Useful for us: cite as one option for client-side inference; images never leave the user's machine.
- Limitations / notes: iOS WebGL is fp16 (epsilon underflow); browser inconsistencies (Safari WebGL 1 only at the time); WebGL memory is not garbage-collected; single-threaded JS blocks the UI. These constraints matter for 3D spine volumes in-browser and favour WebGPU and ONNX Runtime Web. The repository licence is not stated in the paper.
- BibTeX:
```bibtex
@article{Smilkov2019TFjs,
  title   = {{TensorFlow.js}: Machine Learning for the Web and Beyond},
  author  = {Smilkov, Daniel and Thorat, Nikhil and Assogba, Yannick and others},
  journal = {arXiv preprint arXiv:1901.05350},
  year    = {2019}
}
```

### R289. Sheller 2020 - federated learning across 10 institutions
- Full title: Federated learning in medicine: facilitating multi-institutional collaborations without sharing patient data
- Authors: Sheller MJ, Edwards B, Reina GA, et al.
- Year / Venue / Type: 2020 / Scientific Reports 10:12598 / journal article
- DOI / arXiv / URL: 10.1038/s41598-020-69250-1
- Access: open (CC BY)
- Passes: 3/3 (abstract; Sci Rep full text read 2026-10-16 for data, methods and results, then for limitations and code)
- Modality & anatomy: brain MRI (T2-FLAIR), glioma vs healthy tissue binary segmentation
- Data: BraTS 2017 training data split back into its 10 source institutions (210 patients: 88, 22, 34, 12, 8, 4, 8, 14, 15, 5); test sets BTEST (116), WashU (18) and MDACC (29), the last two from non-BraTS institutions
- Method: 2D U-Net (TensorFlow, 32 feature maps). Compared FL (federated averaging), institutional incremental learning (IIL), cyclic IIL (CIIL) and centralised data sharing (CDS), plus leave-one-institution-out tests.
- Key results: FL was within 1% Dice of CDS (about 99% of its quality) on all test sets. FL needed about 2.26x the epochs and was the most stable of the private methods. IIL and CIIL suffered catastrophic forgetting. CDS models dropped about 11% and 5% Dice on the outside institutions.
- Code / weights / license: https://github.com/IntelAI/unet/tree/master/2D (commit eaeac1f; per the paper)
- Useful for us: future-work path for training on hospital spine data without moving images.
- Limitations / notes: brain segmentation only; no FL-specific tuning; parameter leakage and malicious participants not addressed; small datasets. The correction is that the data are BraTS 2017 and the model is 2D.
- BibTeX:
```bibtex
@article{Sheller2020Federated,
  title   = {Federated learning in medicine: facilitating multi-institutional collaborations without sharing patient data},
  author  = {Sheller, Micah J. and Edwards, Brandon and Reina, G. Anthony and others},
  journal = {Scientific Reports},
  volume  = {10},
  pages   = {12598},
  year    = {2020},
  doi     = {10.1038/s41598-020-69250-1}
}
```

### R290. Kaissis 2020 - secure, privacy-preserving and federated ML in imaging
- Full title: Secure, privacy-preserving and federated machine learning in medical imaging
- Authors: Kaissis GA, Makowski MR, Rückert D, Braren RF
- Year / Venue / Type: 2020 / Nature Machine Intelligence 2(6):305-311 / review
- DOI / arXiv / URL: 10.1038/s42256-020-0186-1
- Access: open (publisher PDF)
- Passes: 1/3 (abstract)
- Modality & anatomy: medical imaging, general
- Data: not applicable
- Method: review of federated learning, differential privacy, secure aggregation, homomorphic encryption, and attack vectors
- Key results: privacy-preserving methods can link personal data use with clinical routine if the tools themselves are secured; discusses model inversion and membership inference threats.
- Code / weights / license: not applicable
- Useful for us: frame our in-browser design (no upload) within privacy-preserving ML; note that distributing model weights to browsers exposes them to model-extraction and inversion attacks.
- Limitations / notes: none.
- BibTeX:
```bibtex
@article{Kaissis2020Secure,
  title   = {Secure, privacy-preserving and federated machine learning in medical imaging},
  author  = {Kaissis, Georgios A. and Makowski, Marcus R. and R{\"u}ckert, Daniel and Braren, Rickmer F.},
  journal = {Nature Machine Intelligence},
  volume  = {2},
  number  = {6},
  pages   = {305--311},
  year    = {2020},
  doi     = {10.1038/s42256-020-0186-1}
}
```

### R291. Rieke 2020 - future of digital health with federated learning
- Full title: The future of digital health with federated learning
- Authors: Rieke N, Hancox J, Li W, Milletari F, Roth H, Albarqouni S, Bakas S, Galtier MN, Landman B, Maier-Hein K, Ourselin S, Sheller M, Summers RM, Trask A, Xu D, Baust M, Cardoso MJ
- Year / Venue / Type: 2020 / npj Digital Medicine 3:119 / perspective
- DOI / arXiv / URL: 10.1038/s41746-020-00323-1 ; arXiv:2003.08119 (v2, 15 Jan 2021)
- Access: open (CC BY)
- Passes: 3/3 (abstract; arXiv v2 full text read 2026-10-16 for definitions and benefits, then for challenges and conclusions; the Nature page was not fetchable)
- Modality & anatomy: digital health, general
- Data: not applicable
- Method: perspective on federated learning
- Key results: FL defined as minimising a weighted sum of local losses without centralising data. Topologies: client-server, peer-to-peer, hybrid/hierarchical, cyclic. Benefits are listed per stakeholder (clinicians, patients, hospitals, researchers, providers, manufacturers). Challenges: privacy (model inversion and gradient leakage; differential privacy and encryption trade off accuracy), non-IID data (FedAvg can fail; FedProx), traceability and accountability (logging, contribution measurement), architecture and governance. Examples: MELLODDY, HealthChain, TFDA, the German Cancer Consortium's JIP.
- Code / weights / license: not applicable
- Useful for us: standard citation for federated learning in the future-work section.
- Limitations / notes: perspective. Researchers cannot inspect training images or failure cases in FL, which conflicts with error analysis (CLAIM item 39).
- BibTeX:
```bibtex
@article{Rieke2020FederatedFuture,
  title   = {The future of digital health with federated learning},
  author  = {Rieke, Nicola and Hancox, Jonny and Li, Wenqi and others},
  journal = {npj Digital Medicine},
  volume  = {3},
  pages   = {119},
  year    = {2020},
  doi     = {10.1038/s41746-020-00323-1}
}
```

### R292. Dayan 2021 - EXAM federated model across 20 sites
- Full title: Federated learning for predicting clinical outcomes in patients with COVID-19
- Authors: Dayan I, Roth HR, Zhong A, et al.
- Year / Venue / Type: 2021 / Nature Medicine 27(10):1735-1743 / journal article
- DOI / arXiv / URL: 10.1038/s41591-021-01506-3 ; PMID 34526699
- Access: open
- Passes: 3/3 full text (OpenAlex metadata, then publisher page for results and limitations)
- Modality & anatomy: chest radiograph plus EMR
- Data: 20 institutes worldwide; 16,148 cases
- Method: federated learning (NVIDIA Clara/FLARE ecosystem; framework name not re-verified) of the EXAM model combining CXR and EMR features
- Key results: average AUC > 0.92 for 24 h and 72 h oxygen-need outcomes; 16% gain in average AUC across sites and 38% gain in generalisability vs single-site models.
- Code / weights / license: unverified
- Useful for us: evidence that federation improves generalisation, and its failure analysis (low-quality input with motion artefacts, out-of-distribution young patients) mirrors our "ask for a better scan" logic.
- Limitations / notes: research use only; external validation at three Massachusetts hospitals; label proxy issues; non-IID data and batch norm issues.
- BibTeX:
```bibtex
@article{Dayan2021EXAM,
  title   = {Federated learning for predicting clinical outcomes in patients with {COVID-19}},
  author  = {Dayan, Ittai and Roth, Holger R. and Zhong, Aoxiao and others},
  journal = {Nature Medicine},
  volume  = {27},
  number  = {10},
  pages   = {1735--1743},
  year    = {2021},
  doi     = {10.1038/s41591-021-01506-3}
}
```

### R293. ONNX Runtime Web (software documentation)
- Full title: ONNX Runtime Web tutorial / documentation ("Get started with ONNX Runtime Web")
- Authors: ONNX Runtime developers (Microsoft)
- Year / Venue / Type: accessed 2026-10-16 / software documentation
- DOI / arXiv / URL: https://onnxruntime.ai/docs/tutorials/web/
- Access: open
- Passes: 1/3 (documentation page)
- Modality & anatomy: not applicable
- Data: not applicable
- Method: JavaScript runtime for ONNX models; package `onnxruntime-web`
- Key results: execution providers: `wasm` (CPU, supports all ONNX operators), `webgl`, `webgpu`, `webnn` (GPU or CPU); WebGL/WebGPU/WebNN support only a subset of operators. ORT format reduces binary size, start-up time and peak memory; custom operator-reduced builds are possible. Large models are better served server-side.
- Code / weights / license: github.com/microsoft/onnxruntime (MIT, per project; not re-checked)
- Useful for us: our main candidate runtime for in-browser inference. Plan to export models to ONNX, check operator coverage for the WebGPU provider, and fall back to WASM.
- Limitations / notes: documentation, not peer-reviewed; cite with access date.
- BibTeX:
```bibtex
@misc{ONNXRuntimeWeb2026,
  title        = {{ONNX Runtime Web}: Get started with {ONNX Runtime Web}},
  author       = {{ONNX Runtime developers}},
  howpublished = {\url{https://onnxruntime.ai/docs/tutorials/web/}},
  note         = {Accessed 2026-10-16},
  year         = {2026}
}
```

### R294. WebGPU W3C specification
- Full title: WebGPU
- Authors: Ninomiya K, Jones B, Blandy J (editors)
- Year / Venue / Type: 2026 (version dated 15 September 2026) / W3C Candidate Recommendation Draft / standard
- DOI / arXiv / URL: https://www.w3.org/TR/webgpu/
- Access: open
- Passes: 1/3 (spec front matter and structure)
- Modality & anatomy: not applicable
- Data: not applicable
- Method: browser API for GPU rendering and computation; compute pipelines with WGSL shaders
- Key results: provides general-purpose GPU compute in the browser, which ONNX Runtime Web and TF.js use for acceleration.
- Code / weights / license: W3C
- Useful for us: cite for GPU-accelerated in-browser 3D inference of MRI/CT volumes.
- Limitations / notes: browser support varies; status text still cites a 2025 CR date (possibly stale).
- BibTeX:
```bibtex
@misc{W3C2026WebGPU,
  title        = {{WebGPU}},
  author       = {Ninomiya, Kai and Jones, Brandon and Blandy, Jim},
  howpublished = {W3C Candidate Recommendation Draft, \url{https://www.w3.org/TR/webgpu/}},
  note         = {Version of 15 September 2026, accessed 2026-10-16},
  year         = {2026}
}
```

### R295. Brainchop - in-browser MRI segmentation
- Full title: Brainchop: In-browser MRI volumetric segmentation and rendering
- Authors: Masoud M, Hu F, Plis S
- Year / Venue / Type: 2023 / Journal of Open Source Software 8(83):5098 / software paper; companion preprint arXiv:2310.16162 (Masoud, Reddy, Hu, Plis, Oct 2023, 'Brainchop: Next Generation Web-Based Neuroimaging Application'; the preprint does not state a venue, so the ISBI 2024 claim is unverified)
- DOI / arXiv / URL: 10.21105/joss.05098 ; arXiv:2310.16162 ; github.com/neuroneural/brainchop
- Access: open
- Passes: 2/3 (GitHub README; arXiv 2310.16162v1 full PDF read for methods, numbers and limitations, 2026-10-16; JOSS paper itself not opened)
- Modality & anatomy: brain MRI (3D)
- Data: models trained in PyTorch on Human Connectome Project (HCP) T1 MRI with FreeSurfer labels; tasks are brain mask, GM/WM, 50-region and 104-structure atlases. Telemetry: 1,336 user sessions, May 2022 to May 2023 (per arXiv 2310.16162)
- Method: lightweight MeshNet (dilated-convolution) models, 5,598 to 96,078 parameters, run in the browser with TensorFlow.js (WebGL); full-volume or sub-volume (patch) inference, cropping to the brain, and layer-by-layer inference as a failsafe for GPU memory; visualisation with NiiVue
- Key results: MeshNet GWM macro Dice 0.96, equal to a U-Net, with model size 0.022 MB (full volume) / 0.89 MB (sub-volume) vs 288 MB for the U-Net. Inference about 9.9-14 s for GWM, about 13.7 s for the 104-structure atlas, about 39.8 s in failsafe mode. Telemetry success rate about 82% (full volume 81.08%, sub-volume 87.3%); cropping +18.12%, patching +6.23%, texture size 32768 +18.13% success (arXiv 2310.16162).
- Code / weights / license: MIT
- Useful for us: the closest precedent for a browser-only medical volume analysis tool. Reuse ideas: NiiVue viewer, small MeshNet-style models, client-side NIfTI handling.
- Limitations / notes: brain only. Failures are mostly GPU-memory related: shader compile 174/19, program link 33/5 and texture creation 10/0 (full/sub-volume), plus WebGL context loss; mitigated with layer-by-layer inference. Telemetry success is self-reported by the authors, with no external validation. The preprint states no licence; MIT is from the README. Lesson for us: budget for client GPU memory and add a failsafe path.
- BibTeX:
```bibtex
@article{Masoud2023Brainchop,
  title   = {Brainchop: In-browser {MRI} volumetric segmentation and rendering},
  author  = {Masoud, Mohamed and Hu, Farfalla and Plis, Sergey},
  journal = {Journal of Open Source Software},
  volume  = {8},
  number  = {83},
  pages   = {5098},
  year    = {2023},
  doi     = {10.21105/joss.05098}
}
```

### R296. Pati 2022 - Federated Tumor Segmentation (FeTS) at scale
- Full title: Federated learning enables big data for rare cancer boundary detection
- Authors: Pati S, Baid U, Edwards B, et al.
- Year / Venue / Type: 2022 / Nature Communications (volume 13, article number unverified) / journal article
- DOI / arXiv / URL: 10.1038/s41467-022-33407-5 ; PMID 36470898 ; arXiv:2204.10836 (v2, 25 Apr 2022)
- Access: open (CC BY)
- Passes: 3/3 (arXiv abstract, then the v2 PDF read 2026-10-16 for methods and results, then for tools and caveats. The published Nature Communications version was not read and its article number is still unverified.)
- Modality & anatomy: brain MRI (glioblastoma boundary segmentation)
- Data: 71 sites on 6 continents (incl. the public-initial-model node); 6,314 patients, 25,256 MRI scans (T1, T1Gd, T2, FLAIR); 49 training sites plus 6 out-of-sample sites (590 cases); public initial model trained on 231 cases from 16 sites. Labels from a fusion of DeepMedic, DeepScan and nnU-Net with manual refinement.
- Method: 3D ResUNet (30 base filters); OpenFL federated averaging (1 local epoch per round, 73 rounds, aggregator in a trusted execution environment); BraTS harmonised preprocessing via CaPTk, BrainMaGe, GaNDLF; 80/20 local validation
- Key results: relative Dice gain of the final FL model over the public initial model: local validation ET +27%, TC +33%, WT +16%; out-of-sample ET +15%, TC +27%, WT +16% (all p < 1e-5). The abstract's '33% / 23%' differs from the 16% WT gain in the results (unreconciled). OpenVINO 8-bit optimisation gave a 4.48x speed-up with a small Dice cost.
- Code / weights / license: github.com/FETS-AI/Front-End ; github.com/intel/openfl ; CaPTk, BrainMaGe, GaNDLF, LabelFusion (CBICA/FETS-AI GitHub; URLs from the paper). The consensus model release was planned.
- Useful for us: cite with E02 and E05 as proof that federated imaging works at large scale.
- Limitations / notes: glioblastoma only; out-of-sample sites chosen by availability; abstract and results figures differ; Intel authors disclosed an interest in OpenFL; single model, no ensembles. Shows that 8-bit quantisation of a 3D U-Net is viable, which is relevant to in-browser inference.
- BibTeX:
```bibtex
@article{Pati2022FeTS,
  title   = {Federated learning enables big data for rare cancer boundary detection},
  author  = {Pati, Sarthak and Baid, Ujjwal and Edwards, Brandon and others},
  journal = {Nature Communications},
  year    = {2022},
  doi     = {10.1038/s41467-022-33407-5}
}
```

---
