#!/usr/bin/env pvpython
import sys
import numpy as np
import os
from paraview.simple import OpenFOAMReader
from paraview.servermanager import Fetch
from paraview.numpy_support import vtk_to_numpy


def read_patch_names(boundary_file):
    patch_names = []
    reading_patches = False
    with open(boundary_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(("//", "/*", "*")):
                continue  # skip comments
            if line == "(":
                reading_patches = True
                continue
            if line == ")":
                break
            if reading_patches:
                if "{" not in line:
                    patch_names.append(line)
    return patch_names

# 1. 케이스 입력
if len(sys.argv) < 2:
    print("Usage: pvpython extract_patches.py open.foam")
    sys.exit(1)
case_foam = sys.argv[1]
case_dir = os.path.dirname(case_foam)

# 2. boundary 파일에서 patch 이름 읽기
boundary_file = os.path.join(case_dir, "constant/polyMesh/boundary")
patch_names = read_patch_names(boundary_file)
print("Detected patches:", patch_names)

# 3. OpenFOAMReader
reader = OpenFOAMReader(FileName=case_foam)
reader.PointArrays = []
reader.CellArrays  = []
reader.MeshRegions = ['internalMesh'] + patch_names
reader.UpdatePipeline()

# 4. Fetch
mb = Fetch(reader)

# 5. Save interior mesh points
internal = mb.GetBlock(0)
pts_all = vtk_to_numpy(internal.GetPoints().GetData())[:, :2]
np.save("coords.npy", pts_all)

# 6. Save patch points
for i, name in enumerate(patch_names, start=1):
    block = mb.GetBlock(i)
    if block is not None:
        pts = vtk_to_numpy(block.GetPoints().GetData())[:, :2]
        np.save(f"patch_{name}.npy", pts)
    else:
        print(f"Warning: Block {i} ({name}) is empty.")

print(f"Saved coords.npy and {len(patch_names)} patch_*.npy files.")
