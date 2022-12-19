import numpy as np

# 定义系数矩阵 A 和常数向量 b
A = np.array([[3, 2, 1], [1, 1, 1]])
b = np.array([100, 100])

# 使用 linalg.lstsq 求解线性方程组
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=1e-10)

# 输出结果
print("大马数量: ", int(x[0]))
print("中马数量: ", int(x[1]))
print("小马数量: ", int(x[2]))
