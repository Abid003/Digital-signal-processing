import numpy as np
from numpy import linalg as la

def solve_system(A, b):
    det = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    if det == 0:
        return 'not possible'
    adj = np.array([[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]])
    A_inv = (1.0 / det) * adj

    return (A_inv.dot(b), A_inv)

A = np.array([[4, 5], [1, 6]])
b = np.array([4, 2])
x = solve_system(A, b)
A_inv = x[1]
print(A.dot(A_inv))
print(A.dot(x[0]))