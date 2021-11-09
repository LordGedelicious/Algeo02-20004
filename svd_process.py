from itertools import count
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
    for i in range(0,length):
        for j in range(0,width):
            if (identity[i,j] == 1):
                identity[i,j] = x
    result = identity - matrix
    eigenvalues = sympy.solve(result.det(),x)
    eigenvalues_np = np.array(eigenvalues).astype(np.int64)
    eigenvalues_np[::-1].sort()
    eigenvalues = sympy.Matrix(eigenvalues_np)
    zeroMatrix = zeros(length,1)
    final_eigenvector = sympy.Matrix([[]])
    for i in range(0,sympy.shape(eigenvalues)[0]): #ini baru bisa manggil eigen value pertama
        for j in range(0,length):
            for k in range(0,width):
                if (identity[j,k] == x or identity[j,k] == eigenvalues[i-1,0]):
                    identity[j,k] = eigenvalues[i,0]
        subtractToEigen = identity - matrix
        solutions, params = subtractToEigen.gauss_jordan_solve(zeroMatrix)
        for i in params:
            sum = 0
            partial_solution_temp = solutions.xreplace({i:1})
            partial_solution = partial_solution_temp.xreplace({i:0 for i in params})
            print(partial_solution)
            for i in partial_solution:
                sum += i ** 2
            sum = (sum ** 0.5) ** (-1)
            partial_solution = sum * partial_solution
            final_eigenvector = (final_eigenvector.col_insert(length,partial_solution))
            print(final_eigenvector)



left_singular(sample)