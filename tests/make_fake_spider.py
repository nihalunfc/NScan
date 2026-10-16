"""Write a tiny SPIDER-shaped dataset of phantoms (images/, masks/, radiological_gradings.csv)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "train"))
import numpy as np, SimpleITK as sitk, csv
from synthetic import phantom
from common import CANAL, DISC_OFFSET

out = pathlib.Path(sys.argv[1]); n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
(out / "images").mkdir(parents=True, exist_ok=True); (out / "masks").mkdir(exist_ok=True)
rng = np.random.default_rng(3)
rows = []
for p in range(1, n + 1):
    img2, inst2, truth = phantom(rng, size=200, disc_scale={1: 0.5} if p % 2 else {})
    lab = np.zeros(inst2.shape, np.int16)
    v = (inst2 >= 1) & (inst2 <= 25); lab[v] = inst2[v]
    lab[inst2 == CANAL] = 100
    d = inst2 > DISC_OFFSET; lab[d] = inst2[d] - DISC_OFFSET + 200
    L = 11
    vol = np.stack([img2 * (1 - abs(k - L // 2) / L) for k in range(L)])      # (L, rows=S top-first, cols=P)
    msk = np.stack([lab if abs(k - L // 2) <= 2 else np.where(lab == 100, 0, lab) for k in range(L)])
    for seq in ["t1", "t2"]:
        for arr, folder in [((vol * 1000).astype(np.int16), "images"), (msk, "masks")]:
            # sagittal acquisition: array (z=L, y=S, x=P); y runs inferior so flip rows
            im = sitk.GetImageFromArray(arr[:, ::-1, :].copy())
            im.SetSpacing((0.7, 0.7, 3.5))
            # columns: x->P (0,1,0), y->S (0,0,1), z->L (1,0,0) in LPS
            im.SetDirection((0, 0, 1, 1, 0, 0, 0, 1, 0))
            sitk.WriteImage(im, str(out / folder / f"{p}_{seq}.mha"))
    for k in range(5):
        rows.append([p, k + 1, 0, 0, 0, 0, int(p % 2 and k == 1), int(p % 2 and k == 1), 0, 4 if (p % 2 and k == 1) else 2])
with open(out / "radiological_gradings.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Patient", "IVD label", "Modic", "UP endplate", "LOW endplate", "Spondylolisthesis",
                                   "Disc herniation", "Disc narrowing", "Disc bulging", "Pfirrman grade"]); w.writerows(rows)
print("wrote", out)
