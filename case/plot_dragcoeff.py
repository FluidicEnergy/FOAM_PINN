import numpy as np
import matplotlib.pyplot as plt

# 파일 경로
data_file = "postProcessing/forces/0/coefficient.dat"

# 헤더 건너뛰고 데이터 로딩
data = np.loadtxt(data_file, comments='#')

# 각 열 추출
time = data[:, 0]
Cd = data[:, 1]
Cl = data[:, 4]
Cm = data[:, 7]

# 그래프 생성
plt.figure()
plt.plot(time, Cd, label="Cd")
plt.plot(time, Cl, label="Cl")
plt.plot(time, Cm, label="Cm")
plt.xlabel("Time")
plt.ylabel("Coefficient Value")
plt.title("Force and Moment Coefficients")
plt.legend()
plt.grid(True)
plt.ylim(-1.1, 1.5)
plt.tight_layout()
plt.savefig("drag.png")
