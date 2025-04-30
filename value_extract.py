import numpy as np
import matplotlib.pyplot as plt
import os
import glob

def read_vector_field(filepath):
    """OpenFOAM U 파일에서 (u,v,w) 읽기"""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip() == "(":
            start_idx = i + 1
            break

    vectors = []
    for line in lines[start_idx:]:
        line = line.strip()
        if line == ");":
            break
        vec = line.replace('(', '').replace(')', '').split()
        vectors.append([float(v) for v in vec])

    return np.array(vectors)

def read_scalar_field(filepath):
    """OpenFOAM p 파일에서 scalar 읽기"""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip() == "(":
            start_idx = i + 1
            break

    scalars = []
    for line in lines[start_idx:]:
        line = line.strip()
        if line == ");":
            break
        scalars.append(float(line))

    return np.array(scalars)

# -------------------------------------------------
# 실행
# -------------------------------------------------
case_dir = 'cir-cyl'
result_times = ['0.5', '15.5', '30.5']
output_dir = "plots"

os.makedirs(output_dir, exist_ok=True)  # 결과 저장 폴더

for time in result_times:
    u_file = os.path.join(case_dir, time, 'U')
    p_file = os.path.join(case_dir, time, 'p')

    U = read_vector_field(u_file)
    p = read_scalar_field(p_file)

    # --- Velocity Plot ---
    plt.figure(figsize=(8,6))
    plt.quiver(np.arange(len(U)), np.zeros(len(U)), U[:,0], U[:,1], angles='xy', scale_units='xy', scale=1)
    plt.title(f"Velocity field at t={time}")
    plt.xlabel('Index')
    plt.ylabel('Velocity')
    plt.grid()
    plt.tight_layout()
    save_path = os.path.join(output_dir, f'velocity_{time.replace(".","p")}.png')
    plt.savefig(save_path)
    plt.close()

    # --- Pressure Plot ---
    plt.figure(figsize=(8,6))
    plt.plot(np.arange(len(p)), p, 'o-')
    plt.title(f"Pressure field at t={time}")
    plt.xlabel('Index')
    plt.ylabel('Pressure')
    plt.grid()
    plt.tight_layout()
    save_path = os.path.join(output_dir, f'pressure_{time.replace(".","p")}.png')
    plt.savefig(save_path)
    plt.close()
