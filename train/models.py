"""Small models that run in the browser (ONNX Runtime Web, WASM/WebGPU).

These are the phase-one deployable models. The research-scale architecture for
large-GPU training is described in docs/ARCHITECTURE.md.
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from common import BINARY_TASKS, N_PFIRRMANN


class Block(nn.Module):
    def __init__(self, cin, cout, drop=0.0):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(cin, cout, 3, padding=1, bias=False), nn.BatchNorm2d(cout), nn.LeakyReLU(0.01, inplace=True),
            nn.Dropout2d(drop) if drop else nn.Identity(),
            nn.Conv2d(cout, cout, 3, padding=1, bias=False), nn.BatchNorm2d(cout), nn.LeakyReLU(0.01, inplace=True),
        )
        self.skip = nn.Conv2d(cin, cout, 1, bias=False) if cin != cout else nn.Identity()

    def forward(self, x):
        return self.net(x) + self.skip(x)


class UNet(nn.Module):
    """Residual 2D U-Net, 5 levels. base=16 -> about 2M parameters (8 MB fp32)."""

    def __init__(self, n_classes=4, base=16, drop=0.1):
        super().__init__()
        ch = [base, base * 2, base * 4, base * 8, base * 16]
        self.enc = nn.ModuleList()
        cin = 1
        for i, c in enumerate(ch):
            self.enc.append(Block(cin, c, drop if i >= 3 else 0.0))
            cin = c
        self.up = nn.ModuleList()
        self.dec = nn.ModuleList()
        for i in range(len(ch) - 1, 0, -1):
            self.up.append(nn.ConvTranspose2d(ch[i], ch[i - 1], 2, stride=2))
            self.dec.append(Block(ch[i - 1] * 2, ch[i - 1]))
        self.head = nn.Conv2d(ch[0], n_classes, 1)

    def forward(self, x):
        skips = []
        for i, e in enumerate(self.enc):
            x = e(x)
            if i < len(self.enc) - 1:
                skips.append(x)
                x = F.max_pool2d(x, 2)
        for up, dec in zip(self.up, self.dec):
            x = up(x)
            x = dec(torch.cat([x, skips.pop()], 1))
        return self.head(x)


class DiscGrader(nn.Module):
    """Per-disc multi-task classifier on 64x64 rotated crops.

    Output: N_PFIRRMANN logits for Pfirrmann grade 1-5, then one logit per BINARY_TASKS item.
    """

    def __init__(self, width=32):
        super().__init__()
        w = width
        self.features = nn.Sequential(
            Block(1, w), nn.MaxPool2d(2),          # 32
            Block(w, w * 2), nn.MaxPool2d(2),      # 16
            Block(w * 2, w * 4), nn.MaxPool2d(2),  # 8
            Block(w * 4, w * 8, 0.1),
            nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Dropout(0.3),
        )
        self.head = nn.Linear(w * 8, N_PFIRRMANN + len(BINARY_TASKS))

    def forward(self, x):
        return self.head(self.features(x))
