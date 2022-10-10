from re import X
import numpy as np
from matplotlib import pyplot as plt
import math

def signal():
    x = [i for i in range(32)]
    for n in range(32):
        if -15 <= n and n < 0:
           x[n] =  (1.0 / n) * (3 + 2j)
        elif 0 < n and n <= 15:
            x[n] = (-1.0/n) * (5 + 6j)
    return x

x = signal()
x = np.array(x)
plt.stem(np.abs(x))
plt.show()

