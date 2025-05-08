import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import deepxde as dde
import jax
import jax.numpy as jnp
from flax import linen as nn


dde.backend.load_backend("jax")

class GeometryBuilder:
    def __init__(self, patch_dir, time_domain=(0.0, 3.0), atol=1e-4):
        self.patch_dir = patch_dir
        self.time_domain = time_domain
        self.atol = atol
        self.patch_dict = self._load_patches()
        self.xmin, self.ymin, self.xmax, self.ymax = self._get_bounds()
        print("[Loaded patches]:", list(self.patch_dict.keys()))

    def _load_patches(self):
        patch_files = sorted(glob.glob(os.path.join(self.patch_dir, "*_points.dat")))
        patch_dict = {}
        for f in patch_files:
            name = os.path.basename(f).replace("_points.dat", "")
            pts = np.loadtxt(f)
            if pts.ndim == 1:
                pts = pts.reshape(1, -1)
            patch_dict[name] = pts[:, :2]
        return patch_dict

    def _get_bounds(self):
        all_pts = np.vstack(list(self.patch_dict.values()))
        xmin, ymin = np.min(all_pts, axis=0)
        xmax, ymax = np.max(all_pts, axis=0)
        return xmin, ymin, xmax, ymax

    def get_patch_domain(self, patch_name):
        if patch_name not in self.patch_dict:
            raise ValueError(f"Patch '{patch_name}' not found.")
        return self.patch_dict[patch_name]

    def get_outer_geometry(self):
        return dde.geometry.Rectangle([self.xmin, self.ymin], [self.xmax, self.ymax])

    def get_time_geometry(self):
        geom = self.get_outer_geometry()
        timedomain = dde.geometry.TimeDomain(*self.time_domain)
        return dde.geometry.GeometryXTime(geom, timedomain)

    def define_inner_geometry_by_patch(self, patch_name):
        if patch_name not in self.patch_dict:
            raise ValueError(f"Patch '{patch_name}' not found.")
        patch_pts = self.patch_dict[patch_name]
        return dde.geometry.geometry_2d.Polygon(patch_pts)

    def define_csg_domain(self, shape1, shape2, mode="difference"):
        if mode == "difference":
            return dde.geometry.csg.CSGDifference(shape1, shape2)
        elif mode == "union":
            return dde.geometry.csg.CSGUnion(shape1, shape2)
        elif mode == "intersection":
            return dde.geometry.csg.CSGIntersection(shape1, shape2)
        else:
            raise ValueError(f"Unsupported CSG mode: {mode}")

    def make_boundary_func_by_patch(self, patch_name):
        if patch_name not in self.patch_dict:
            raise ValueError(f"Patch '{patch_name}' not found.")
        pts = self.patch_dict[patch_name]

        def boundary_fn(x, on_boundary):
            dists = np.linalg.norm(x[:, :2, None] - pts.T, axis=1)
            close = np.any(dists < self.atol, axis=1)
            return np.logical_and(close, on_boundary)

        return boundary_fn

    def get_patch_points(self, patch_name, num_points):
        domain = self.get_patch_domain(patch_name)
        indices = np.random.choice(domain.shape[0], size=min(num_points, domain.shape[0]), replace=False)
        return domain[indices]

gb = GeometryBuilder("extractPatchPoints/0")
patch_dict =gb.patch_dict


up_geom = gb.define_inner_geometry_by_patch("up")
down_geom = gb.define_inner_geometry_by_patch("down")
left_geom = gb.define_inner_geometry_by_patch("left")
right_geom = gb.define_inner_geometry_by_patch("right")
outer_geom = gb.get_outer_geometry()
cylinder_geom = gb.define_inner_geometry_by_patch("cylinder")
inner_geom = gb.define_csg_domain(outer_geom, cylinder_geom, mode="difference")


cylinder_points = cylinder_geom.random_boundary_points(6000)
inner_points = inner_geom.random_points(10000)
up_points = up_geom.random_boundary_points(6000)

# patch visualization 
plt.figure(figsize=(10, 8))
cmap = plt.get_cmap("tab10", len(patch_dict))

for i, (name, pts) in enumerate(patch_dict.items()):
    plt.scatter(pts[:, 0], pts[:, 1], s=5, color=cmap(i), label=name)
    cx, cy = pts.mean(axis=0)
    plt.text(cx, cy, name, fontsize=9, ha='center', va='center')

plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.title("Boundary Patches (from GeometryBuilder)")
plt.legend(markerscale=2, fontsize=8)
plt.tight_layout()
plt.savefig("boundary_plot.png")
plt.close()

plt.scatter(up_points[:, 0], up_points[:, 1], s=1, color='blue')
plt.scatter(cylinder_points[:, 0], cylinder_points[:, 1], s=2, color='red')
plt.axis("equal")
plt.savefig("datapoinst.png")
plt.close()

print("Geometric data points generation successful")
