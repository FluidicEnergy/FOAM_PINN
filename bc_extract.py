import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# ----------------------------------------
# 1. 데이터 폴더 설정
# ----------------------------------------
data_dir = "./0"  # patch_points.dat 파일들이 저장된 폴더

# patch_*.dat 파일들 찾기
patch_files = sorted(glob.glob(os.path.join(data_dir, "*_points.dat")))

# ----------------------------------------
# 2. Plot 시작
# ----------------------------------------
plt.figure(figsize=(10, 8))

# 컬러맵 설정
cmap = plt.get_cmap('tab10', len(patch_files))

# 각 patch 별로 plotting
for i, filepath in enumerate(patch_files):
    patch_name = os.path.basename(filepath).replace("_points.dat", "")
    pts = np.loadtxt(filepath)[:, :2]  # (x, y)만 사용

    plt.scatter(pts[:, 0], pts[:, 1], s=5, color=cmap(i), label=patch_name)

    # 중심점 계산해서 patch 이름 라벨링
    cx, cy = pts.mean(axis=0)
    plt.text(cx, cy, patch_name, fontsize=9, ha='center', va='center')

# ----------------------------------------
# 3. Plot 옵션
# ----------------------------------------
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Patch-wise Scattering Plot')
plt.legend(markerscale=2, fontsize=8)
plt.tight_layout()
plt.savefig('bc_plot.png')
