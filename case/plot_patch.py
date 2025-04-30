

import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# --------------------------------
# 1. Load coordinates
# --------------------------------
coords = np.load("coords.npy")   # interior points

# --------------------------------
# 2. Load patch points
# --------------------------------
patch_files = sorted(glob.glob("patch_*.npy"))

# patch 이름 파싱
patch_names = [os.path.splitext(os.path.basename(pf))[0].replace("patch_", "") for pf in patch_files]
patch_points = [np.load(pf) for pf in patch_files]

# --------------------------------
# 3. Plot
# --------------------------------
plt.figure(figsize=(10, 8))

# interior points
plt.scatter(coords[:, 0], coords[:, 1], s=1, color="lightgray", label="interior")

# each patch
cmap = plt.get_cmap("tab10", len(patch_points))

for i, (name, pts) in enumerate(zip(patch_names, patch_points)):
    plt.scatter(pts[:, 0], pts[:, 1], s=5, color=cmap(i), label=name)
    # 중심점(centroid) 위치에 patch 이름 라벨링
    cx, cy = pts.mean(axis=0)
    plt.text(cx, cy, name, fontsize=9, ha="center", va="center")

plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Domain with Boundary Patches (Labelled)")
plt.legend(markerscale=2, fontsize=8, loc="best")
plt.tight_layout()
plt.savefig('plot_patch.png')
