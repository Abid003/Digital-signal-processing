import numpy as np
from matplotlib import pyplot as plt

def signal():
    a = 3
    N = 11
    x = np.zeros(N)
    for n in range(N):
        if n < 5:
            x[n] = a
            a = a + 1
        else:
            x[n] = a
            a = a - 1
    return np.array(x)

x = signal()
n = [i for i in range(-15, 16)]
y = np.zeros(31)

for n_ in range(31):
    y[n_] = x[(n[n_] - 3) % 11]
    
n = [i for i in range(-15, 16)]
z = np.zeros(31)

for n_ in range(31):
    z[n_] = x[(n[n_] + 3) % 11]

n = [i for i in range(-15, 16)]
m = np.zeros(31)

for n_ in range(31):
    m[n_] = x[(-n[n_]) % 11]

plt.subplot(4, 1, 1)
plt.stem(x)
plt.subplot(4, 1, 2)
plt.stem(n, y)
plt.subplot(4, 1, 3)
plt.stem(n, y)
plt.subplot(4, 1, 4)
plt.stem(n, m)
plt.show()