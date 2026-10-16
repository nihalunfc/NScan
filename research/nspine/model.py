"""NSpine reference implementation (see docs/ARCHITECTURE.md).

A runnable skeleton of the large model: modality-conditioned residual-encoder
U-Net, level tokeniser, level transformer and task heads. Sizes default to the
research configuration; tests use a tiny config so it runs on CPU.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import torch
import torch.nn as nn
import torch.nn.functional as F

MODALITIES = ["ct", "mri_t1", "mri_t2", "mri_stir", "xray"]
LEVELS = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9",
          "T10", "T11", "T12", "L1", "L2", "L3", "L4", "L5", "L6", "S1"]   # L6 = transitional


@dataclass
class Config:
    dims: int = 3                                  # 3 for CT/MRI volumes, 2 for radiographs
    widths: tuple = (32, 64, 128, 256, 320, 320)   # ResEnc-L-like
    blocks: tuple = (1, 3, 4, 6, 6, 6)
    n_seg: int = 20                                # anatomy classes
    d_model: int = 384
    n_layers: int = 8
    n_heads: int = 8
    heads: dict = field(default_factory=lambda: {
        "pfirrmann": 5, "modic": 4, "canal_stenosis": 3, "subarticular_stenosis": 3,
        "foraminal_stenosis": 3, "herniation": 4, "spondylolisthesis": 5, "genant": 4, "endplate": 2})
    n_landmarks: int = 4                           # vertebral corners per level


def conv(dims, *a, **k):
    return (nn.Conv3d if dims == 3 else nn.Conv2d)(*a, **k)


def norm(dims, c):
    return (nn.InstanceNorm3d if dims == 3 else nn.InstanceNorm2d)(c, affine=True)


class FiLM(nn.Module):
    """Modality/sequence conditioning: per-channel scale and shift from a learned embedding."""

    def __init__(self, c, n_cond=len(MODALITIES)):
        super().__init__()
        self.emb = nn.Embedding(n_cond, 2 * c)
        nn.init.zeros_(self.emb.weight)

    def forward(self, x, cond):
        g, b = self.emb(cond).chunk(2, -1)
        shape = (x.shape[0], -1) + (1,) * (x.dim() - 2)
        return x * (1 + g.view(shape)) + b.view(shape)


class ResBlock(nn.Module):
    def __init__(self, dims, cin, cout, stride=1):
        super().__init__()
        self.c1, self.n1 = conv(dims, cin, cout, 3, stride, 1, bias=False), norm(dims, cout)
        self.c2, self.n2 = conv(dims, cout, cout, 3, 1, 1, bias=False), norm(dims, cout)
        self.film = FiLM(cout)
        self.skip = conv(dims, cin, cout, 1, stride, bias=False) if (cin != cout or stride != 1) else nn.Identity()

    def forward(self, x, cond):
        h = F.leaky_relu(self.n1(self.c1(x)), 0.01)
        h = self.film(self.n2(self.c2(h)), cond)
        return F.leaky_relu(h + self.skip(x), 0.01)


class ResEncUNet(nn.Module):
    def __init__(self, cfg: Config, in_ch=1):
        super().__init__()
        d, w = cfg.dims, cfg.widths
        self.stem = conv(d, in_ch, w[0], 3, 1, 1)
        self.stages = nn.ModuleList()
        cin = w[0]
        for i, (c, n) in enumerate(zip(w, cfg.blocks)):
            self.stages.append(nn.ModuleList([ResBlock(d, cin if j == 0 else c, c, 2 if (i > 0 and j == 0) else 1)
                                              for j in range(n)]))
            cin = c
        up = nn.ConvTranspose3d if d == 3 else nn.ConvTranspose2d
        self.ups = nn.ModuleList([up(w[i], w[i - 1], 2, 2) for i in range(len(w) - 1, 0, -1)])
        self.decs = nn.ModuleList([ResBlock(d, 2 * w[i - 1], w[i - 1]) for i in range(len(w) - 1, 0, -1)])
        self.seg = conv(d, w[0], cfg.n_seg, 1)
        self.centroid = conv(d, w[0], 1, 1)        # vertebra-centroid heatmap
        self.feat_dims = list(w)

    def forward(self, x, cond):
        x = self.stem(x)
        skips = []
        for st in self.stages:
            for b in st:
                x = b(x, cond)
            skips.append(x)
        feats = list(skips)
        x = skips.pop()
        for up, dec in zip(self.ups, self.decs):
            x = dec(torch.cat([up(x), skips.pop()], 1), cond)
        return {"seg": self.seg(x), "centroid": self.centroid(x), "features": feats, "decoder": x}


class LevelTokenizer(nn.Module):
    """One token per (level, series): ROI-pooled multi-scale features + level and modality embeddings."""

    def __init__(self, cfg: Config, feat_dims):
        super().__init__()
        self.dims = cfg.dims
        self.proj = nn.Linear(sum(feat_dims[-3:]), cfg.d_model)
        self.level_emb = nn.Embedding(len(LEVELS), cfg.d_model)
        self.mod_emb = nn.Embedding(len(MODALITIES), cfg.d_model)

    def forward(self, feats, boxes, level_ids, cond):
        """boxes: (B, L, 2*dims) normalised [0,1] min/max corners per level; level_ids: (B, L)."""
        pooled = []
        for f in feats[-3:]:
            pooled.append(self._roi_mean(f, boxes))
        tok = self.proj(torch.cat(pooled, -1))
        return tok + self.level_emb(level_ids) + self.mod_emb(cond)[:, None]

    def _roi_mean(self, f, boxes):
        # differentiable box-average via a soft mask on the feature grid (fine for coarse maps)
        B, C = f.shape[:2]
        grids = torch.meshgrid(*[torch.linspace(0, 1, s, device=f.device) for s in f.shape[2:]], indexing="ij")
        out = []
        for b in range(B):
            m = torch.ones(boxes.shape[1], *f.shape[2:], device=f.device)
            for k, g in enumerate(grids):
                lo, hi = boxes[b, :, k], boxes[b, :, k + self.dims]
                shape = (-1,) + (1,) * self.dims
                m = m * torch.sigmoid((g - lo.view(shape)) * 50) * torch.sigmoid((hi.view(shape) - g) * 50)
            w = m / m.flatten(1).sum(1).clamp_min(1e-6).view((-1,) + (1,) * self.dims)
            out.append(torch.einsum("c...,l...->lc", f[b], w))
        return torch.stack(out)


class LevelTransformer(nn.Module):
    def __init__(self, cfg: Config):
        super().__init__()
        layer = nn.TransformerEncoderLayer(cfg.d_model, cfg.n_heads, 4 * cfg.d_model, dropout=0.1,
                                           batch_first=True, norm_first=True)
        self.enc = nn.TransformerEncoder(layer, cfg.n_layers)
        self.heads = nn.ModuleDict({k: nn.Linear(cfg.d_model, n) for k, n in cfg.heads.items()})
        self.landmarks = nn.Linear(cfg.d_model, cfg.n_landmarks * cfg.dims)
        self.anomaly_dec = nn.Sequential(nn.Linear(cfg.d_model, cfg.d_model // 4), nn.GELU(),
                                         nn.Linear(cfg.d_model // 4, cfg.d_model))

    def forward(self, tokens, pad_mask=None):
        h = self.enc(tokens, src_key_padding_mask=pad_mask)
        out = {k: head(h) for k, head in self.heads.items()}
        out["landmarks"] = self.landmarks(h)
        # feature-reconstruction anomaly score: trained on unremarkable levels only
        out["anomaly"] = (self.anomaly_dec(tokens.detach()) - tokens.detach()).pow(2).mean(-1)
        return out


class NSpine(nn.Module):
    def __init__(self, cfg: Config = Config()):
        super().__init__()
        self.cfg = cfg
        self.backbone = ResEncUNet(cfg)
        self.tokenizer = LevelTokenizer(cfg, self.backbone.feat_dims)
        self.levels = LevelTransformer(cfg)
        self.gate = nn.Sequential(nn.AdaptiveAvgPool3d(1) if cfg.dims == 3 else nn.AdaptiveAvgPool2d(1), nn.Flatten(),
                                  nn.Linear(cfg.widths[-1], 3))   # [quality score, OOD logit, plane ok]

    def forward(self, image, modality, boxes, level_ids, pad_mask=None):
        dense = self.backbone(image, modality)
        tokens = self.tokenizer(dense["features"], boxes, level_ids, modality)
        out = self.levels(tokens, pad_mask)
        out.update(seg=dense["seg"], centroid=dense["centroid"], gate=self.gate(dense["features"][-1]))
        return out
