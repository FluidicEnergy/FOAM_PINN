"""
Extract OpenFOAM mesh + boundary patches via ParaView, then scatter‐plot with matplotlib.

Requires:
  pip install pyvtkparaview numpy matplotlib

Usage:
  1) Replace CASE_FOAM with your “.foam” file path
  2) Adjust mesh_region_names if needed (reader.MeshRegions)
  3) Run with: python plot_foam_patches.py
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# ParaView Python modules
from paraview.simple import OpenFOAMReader, UpdatePipeline
from paraview.servermanager import Fetch
from paraview.numpy_support import vtk_to_numpy

# -----------------------------------
# 1. Load the OpenFOAM case in ParaView
# -----------------------------------
CASE_FOAM = "open.foam"
reader = OpenFOAMReader(FileName=CASE_FOAM)
reader.PointArrays = []        # no fields, we only need geometry
reader.CellArrays  = []
# by default, reader.MeshRegions contains ["internalMesh","patch1","patch2",...]
UpdatePipeline(reader)

# -----------------------------------
# 2. Fetch the multiblock dataset
# -----------------------------------
mb = Fetch(reader)    # vtkMultiBlockDataSet

# -----------------------------------
# 3. Grab the “internal mesh” as the background domain
# -----------------------------------
# assume block 0 is internalMesh
internal_ds = mb.GetBlock(0)                # vtkUnstructuredGrid
pts_all = vtk_to_numpy(internal_ds.GetPoints().GetData())[:, :2]  # (x,y)

# -----------------------------------
# 4. Extract each patch block
# -----------------------------------
patch_coords = {}
mesh_regions = reader.MeshRegions  # list of names in same order as blocks
for idx, name in enumerate(mesh_regions[1:], start=1):
    block = mb.GetBlock(idx)
    coords = vtk_to_numpy(block.GetPoints().GetData())[:, :2]
    patch_coords[name] = coords

# -----------------------------------
# 5. Plot with matplotlib
# -----------------------------------
plt.figure(figsize=(8,6))

# 5.1 interior points
plt.scatter(pts_all[:,0], pts_all[:,1],
            s=1, color="lightgray", label="internalMesh")

# 5.2 boundary patches
cmap = plt.get_cmap("tab10", len(patch_coords))
for i, (patch, pts) in enumerate(patch_coords.items()):
    plt.scatter(pts[:,0], pts[:,1],
                s=5, color=cmap(i), label=patch)
    cx, cy = pts.mean(axis=0)
    plt.text(cx, cy, patch, fontsize=8, ha="center", va="center")

plt.axis("equal")
plt.xlabel("x"); plt.ylabel("y")
plt.title("OpenFOAM Domain & Boundary Patches (via ParaView)")
plt.legend(markerscale=2, fontsize=8, loc="best")
plt.tight_layout()
plt.show()
