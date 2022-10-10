import numpy as np
from math import pi
from matplotlib import pyplot as plt

N = 100
n = np.array([_ for _ in range(N)])
x = np.cos((2 * pi * n * 4) / N) + np.random.random(N) #frequency is 4 Hz
F = np.array([np.exp((-1j*2*pi*n*k) / N) for k in range(N)])
f = F.dot(x)

f0 = 7
h = np.zeros(N)
for k in range(N):
    if k <= f0:
        h[k] = 1

f_ = f * h
F_ = F.conjugate().T
x_ = (1 / N) * F_.dot(f_)

plt.subplot(4, 1, 1)
plt.plot(x)
plt.subplot(4, 1, 2)
plt.stem(np.abs(f))
plt.subplot(4, 1, 3)
plt.plot(x_.real)
plt.subplot(4, 1, 4)
plt.stem(np.abs(f_))
plt.show()