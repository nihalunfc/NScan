import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "research"))
import torch
from nspine.model import NSpine, Config


def test_forward_tiny_3d_and_2d():
    for dims, shape in [(3, (2, 1, 32, 64, 64)), (2, (2, 1, 64, 64))]:
        cfg = Config(dims=dims, widths=(8, 16, 24, 32), blocks=(1, 1, 1, 1), d_model=32, n_layers=2, n_heads=4, n_seg=5)
        m = NSpine(cfg)
        x = torch.randn(*shape)
        L = 6
        lo = torch.rand(2, L, dims) * 0.5
        boxes = torch.cat([lo, lo + 0.3], -1)
        out = m(x, torch.tensor([1, 2]), boxes, torch.arange(L).repeat(2, 1))
        assert out["seg"].shape == (2, 5) + shape[2:]
        assert out["pfirrmann"].shape == (2, L, 5)
        assert out["landmarks"].shape == (2, L, 4 * dims)
        out["pfirrmann"].sum().backward()
