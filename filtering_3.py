import numpy as np
from numpy.fft import fft, ifft, fftshift
from math import pi, fabs, floor
from matplotlib import pyplot as plt

N = 100
H = np.zeros(N)
D0 = 20
for k in range(N):
	H[k] = 1 / (1 + fabs(floor(N/2)-k) / D0) ** 4
n = np.array([_ for _ in range(N)])
x = np.log(n+1) + np.random.random(N)
X = fftshift(fft(x))
H_hp = 1 - H
y = ifft(fftshift(X * H_hp)).real

plt.subplot(2, 1, 1)
plt.plot(x)
plt.subplot(2, 1, 2)
plt.plot(y)
plt.show()