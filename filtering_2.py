import numpy as np
from numpy.fft import fft, ifft
from math import pi, fabs, floor
from matplotlib import pyplot as plt

N = 100
n = np.array([_ for _ in range(N)])
x = np.cos((6*pi*n) / N) + np.random.random(N)
h = np.zeros(N)
M = 8
for i in range(M):
	h[i] = 1 / M
y = np.zeros(N)
for n in range(N):
	for m in range(N):
		y[n] += x[m] * h[(n-m) % N]

y_ = ifft(fft(x) * fft(h)).real

plt.subplot(3, 1, 1)
plt.plot(x)
plt.subplot(3, 1, 2)
plt.plot(y)
plt.subplot(3, 1, 3)
plt.plot(y_)
plt.show()