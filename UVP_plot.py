import numpy as np
import matplotlib.pyplot as plt
import os

# ----------------------------
# 1. 파일 설정
# ----------------------------
case_dir = 'extractFields'
time_dir = '30.5'
data_path = os.path.join(case_dir, time_dir, 'U_p_points.dat')
output_dir = 'plots'
os.makedirs(output_dir, exist_ok=True)

# ----------------------------
# 2. 데이터 불러오기
# ----------------------------
data = np.loadtxt(data_path)

x, y, z = data[:, 0], data[:, 1], data[:, 2]
u, v, w = data[:, 3], data[:, 4], data[:, 5]
p = data[:, 6]

# ----------------------------
# 3. z = -0.5 필터링
# ----------------------------
z_target = 0
selected = np.isclose(z, z_target, atol=1e-6)

x_sel, y_sel = x[selected], y[selected]
u_sel, v_sel, p_sel = u[selected], v[selected], p[selected]

# ----------------------------
# 4. U plot (x-velocity)
# ----------------------------
plt.figure(figsize=(8,6))
plt.scatter(x_sel, y_sel, c=u_sel, cmap='jet', s=1)
plt.colorbar(label='U (x-velocity)')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'U field at t={time_dir}, z={z_target}')
plt.axis('equal')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'u_field_{time_dir.replace(".","p")}_z{str(z_target).replace(".","p")}.png'))
plt.close()

# ----------------------------
# 5. V plot (y-velocity)
# ----------------------------
plt.figure(figsize=(8,6))
plt.scatter(x_sel, y_sel, c=v_sel, cmap='jet', s=1)
plt.colorbar(label='V (y-velocity)')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'V field at t={time_dir}, z={z_target}')
plt.axis('equal')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'v_field_{time_dir.replace(".","p")}_z{str(z_target).replace(".","p")}.png'))
plt.close()

# ----------------------------
# 6. P plot (pressure)
# ----------------------------
plt.figure(figsize=(8,6))
plt.scatter(x_sel, y_sel, c=p_sel, cmap='jet', s=1)
plt.colorbar(label='P (pressure)')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Pressure field at t={time_dir}, z={z_target}')
plt.axis('equal')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'p_field_{time_dir.replace(".","p")}_z{str(z_target).replace(".","p")}.png'))
plt.close()
