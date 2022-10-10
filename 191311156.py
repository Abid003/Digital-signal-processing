#task 2

import numpy as np
from numpy import linalg as la

def solve_system(A,b):
    adj = np.array([A[1][1], -A])
    

A = np.array([6,2],[7,6])
b = np.array([1,7],[5,4])
x =solve_system(A,b)
print(x)


