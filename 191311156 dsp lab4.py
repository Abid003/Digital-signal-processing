import numpy as np
from matplotlib import pyplot as plt
def signal():
    a = 3
    N = 10
    x = np.zeros(N)
    for n in range(N):
        if n < 5:
            x[n] = -a
            a = a - 1
        
    return np.array(x)
x = signal()
plt.subplot(4, 1, 1)
plt.stem(x)
e = np.zeros(10)
for n in range(10):
    e[n] = .5*(x[n]+x[-n] )
plt.subplot(4, 1, 2)
plt.stem(e)
o = np.zeros(10)
for n in range(10):
    o[n] = .5*(x[n]-x[-n] )
plt.subplot(4, 1, 2)
plt.stem(o)
plt.show()