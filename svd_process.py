import numpy as np
import cv2
from sympy import symbols, Matrix


def left_singular(matrix):
    width, height = matrix.shape
    matrix_t = matrix.T
    print(matrix_t)
    multiply = np.arange(width * width).reshape(width, width)
    for i in range(len(matrix)):
        for j in range(len(matrix_t[0])):
            for k in range(len(matrix_t)):
                multiply[i][j] += matrix[i][k] * matrix_t[k][j]
    identity = np.identity(len(multiply), dtype=int)
    print(multiply)


