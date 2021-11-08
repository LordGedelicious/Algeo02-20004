import re
from mpmath.matrices.eigen import eig
import numpy as np
import cv2
from numpy.core.fromnumeric import shape
from sympy import symbols, Matrix
from sympy.core.symbol import Symbol
import sympy
from sympy.matrices.dense import zeros
from sympy.solvers import solve

sample = np.array([[3,-2,0],[-2,3,0],[0,0,5]])

def left_singular(matrix):
    length, width = matrix.shape
    identity = Matrix.eye(length)
    x = symbols('x')
    print(identity)
    for i in range(0,length):
        for j in range(0,width):
            if (identity[i,j] == 1):
                identity[i,j] = x
    print(identity)
    result = identity - matrix
    print(matrix)
    print(result)
    print(result.det())
    eigenvalues = sympy.solve(result.det(),x)
    print(eigenvalues)
    eigenvalues_np = np.array(eigenvalues).astype(np.int64)
    eigenvalues_np[::-1].sort()
    print(eigenvalues_np)
    eigenvalues = sympy.Matrix(eigenvalues_np)
    print(eigenvalues)
    print(sympy.shape(eigenvalues))
    zeroMatrix = zeros(length,1)
    print(zeroMatrix)
    for i in range(0,sympy.shape(eigenvalues)[0]): #ini baru bisa manggil eigen value pertama
        for j in range(0,length):
            for k in range(0,width):
                if (identity[j,k] == x):
                    identity[j,k] = eigenvalues[i,0]
        subtractToEigen = identity - matrix
        print(subtractToEigen)
        newsubtractToEigen = subtractToEigen.col_insert(length,zeroMatrix)
        print(newsubtractToEigen)

left_singular(sample)