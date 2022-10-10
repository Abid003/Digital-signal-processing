import numpy as np
from matplotlib import pyplot as plt
from math import pi

w1 = 2 * pi / 10
w2 = 2 * pi / 20
w3 = 2 * pi / 30
w4 = 2 * pi / 40

n = np.array([_ for _ in range(-20, 21)])

x1 = np.sin(w1 * n)
x2 = np.sin(w2 * n)
x3 = np.sin(w3 * n)
x4 = np.sin(w4 * n)

plt.subplot(2, 2, 1)
plt.stem(n, x1)
plt.subplot(2, 2, 2)
plt.stem(n, x2)
plt.subplot(2, 2, 3)
plt.stem(n, x3)
plt.subplot(2, 2, 4)
plt.stem(n, x4)
plt.show()