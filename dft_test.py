import functools
import matplotlib.pyplot as plt
import cmath
import random

import numpy as np


# ステップ
s = 0.1
# 横軸(0~2πまで)
x = np.arange(0, 2 * cmath.pi, s)
y1 = np.sin(x)
plt.plot(x, y1)


# 振幅
a = 2
# 位相
b = cmath.pi
# 周波数
o = 2
# sin波
y2 = a * np.sin(o * x + b)
plt.plot(x, y2)

y = y1+y2
plt.plot(x, y)

X = x.reshape(1, -1)
O = np.array([1, 2]).reshape(-1, 1)
B = np.array([0, cmath.pi]).reshape(-1, 1)
A = np.array([1, 2]).reshape(-1, 1)
y = np.sum(A * np.sin(O * X + B), axis=0)
plt.plot(x, y)


def dft(f):
    n = len(f)
    A = np.arange(n)
    M = cmath.e**(-1j * A.reshape(1, -1) * A.reshape(-1, 1) * 2 * cmath.pi / n)
    return np.sum(f * M, axis=1)

fy = dft(y)
plt.plot(fy.real)

plt.show()
