"""Batch augmentation on CPU tensors.

Built to make the model robust to what people actually upload: screenshots and
phone photos of scans at unknown scale, cropped fields of view, overlays and
text, blur, compression-like low resolution, and mirrored orientation.
"""
from __future__ import annotations

import math

import torch
import torch.nn.functional as F


def affine(img, lab, p_flip=0.5, rot=15, scale=(0.7, 1.35), shift=0.12):
    b = img.shape[0]
    ang = (torch.rand(b) * 2 - 1) * math.radians(rot)
    s = torch.empty(b).uniform_(*scale)
    flip = torch.where(torch.rand(b) < p_flip, -1.0, 1.0)
    tx, ty = (torch.rand(b) * 2 - 1) * shift, (torch.rand(b) * 2 - 1) * shift
    cos, sin = torch.cos(ang) / s, torch.sin(ang) / s
    theta = torch.stack([torch.stack([cos * flip, -sin, tx], 1), torch.stack([sin * flip, cos, ty], 1)], 1)
    grid = F.affine_grid(theta, img.shape, align_corners=False)
    img = F.grid_sample(img, grid, mode="bilinear", padding_mode="zeros", align_corners=False)
    lab = F.grid_sample(lab[:, None].float(), grid, mode="nearest", padding_mode="zeros", align_corners=False)
    return img, lab[:, 0].long()


def intensity(img):
    b = img.shape[0]
    g = torch.exp(torch.empty(b, 1, 1, 1).uniform_(-0.5, 0.5))
    img = img.clamp(0, 1) ** g
    img = img * torch.empty(b, 1, 1, 1).uniform_(0.7, 1.3) + torch.empty(b, 1, 1, 1).uniform_(-0.15, 0.15)
    # blur
    k = torch.tensor([1, 4, 6, 4, 1.0])
    k = (k[:, None] * k[None]) / 256
    blur = F.conv2d(F.pad(img, (2, 2, 2, 2), mode="replicate"), k[None, None])
    m = (torch.rand(b, 1, 1, 1) < 0.3).float()
    img = m * blur + (1 - m) * img
    # low resolution
    m = (torch.rand(b) < 0.25)
    if m.any():
        f = float(torch.empty(1).uniform_(0.3, 0.7))
        small = F.interpolate(img[m], scale_factor=f, mode="bilinear", align_corners=False)
        img[m] = F.interpolate(small, size=img.shape[-2:], mode="bilinear", align_corners=False)
    # noise
    img = img + torch.randn_like(img) * torch.empty(b, 1, 1, 1).uniform_(0, 0.06)
    return img


def overlays(img, p=0.4):
    """Bright text-like boxes and lines in random places (scanner annotations, UI)."""
    b, _, h, w = img.shape
    for i in range(b):
        if torch.rand(1) > p:
            continue
        for _ in range(int(torch.randint(1, 6, (1,)))):
            y, x = int(torch.randint(0, h - 8, (1,))), int(torch.randint(0, w - 30, (1,)))
            hh, ww = int(torch.randint(2, 8, (1,))), int(torch.randint(5, 40, (1,)))
            img[i, :, y:y + hh, x:x + ww] = torch.rand(1) * 0.3 + 0.7
    return img


def renormalize(img):
    """Re-apply percentile normalisation after augmentation, as the browser does."""
    flat = img.flatten(1)
    lo = torch.quantile(flat, 0.005, dim=1)[:, None, None, None]
    hi = torch.quantile(flat, 0.995, dim=1)[:, None, None, None]
    return ((img - lo) / (hi - lo).clamp_min(1e-3)).clamp(0, 1)


def augment(img, lab):
    img, lab = affine(img, lab)
    img = overlays(intensity(img))
    return renormalize(img), lab
