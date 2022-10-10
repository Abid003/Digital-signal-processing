import numpy as np
from numpy import linalg as la

def solve_system(A,b):
    det = (A[0][0]* A[1][1] - A[0][1])
