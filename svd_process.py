import numpy as np
import cv2
from sympy import symbols, Matrix

sample = np.array([[1,5,7],[3,0,-2],[-1,2,1]])

def left_singular(matrix):
    length, width = matrix.shape
    x = symbols('x')
    identity = np.identity(length, dtype=int)
    print(identity)
    for i in range(0,length):
        for j in range(0,width):
            if (identity[i][j] == 1):
                identity[i][j] = x
    print(identity)
    print(matrix)

left_singular(sample)