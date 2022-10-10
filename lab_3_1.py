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
plt.subplot(4, 1, 1)
plt.stem(x)

y = np.zeros(11)
for n in range(11):
    y[n] = x[(n - 3) % 11]
plt.subplot(4, 1, 2)
plt.stem(y)

for n in range(11):
    y[n] = x[(n + 3) % 11]
plt.subplot(4, 1, 3)
plt.stem(y)

for n in range(11):
    y[n] = x[-n % 11]
plt.subplot(4, 1, 4)
plt.stem(y)

plt.show()