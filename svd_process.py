from mpmath.functions.rszeta import zeta_offline
import numpy as np
from numpy.core.fromnumeric import shape, sort, transpose
from numpy.core.numeric import full
import sympy
from sympy import symbols, Matrix, solve, zeros
from sympy.matrices.dense import ones


def singular_vectors(matrix, left=True):
    """ Menghitung matriks singular kiri atau kanan.\n
        Untuk menghitung matriks singular kiri, 
            Argumen matrix berupa matriks AAT dan left = True.\n
        Untuk menghitung matriks singular kanan, 
            Argumen matrix berupa matriks ATA dan left = False.\n
        
        Prekondisi: matrix berupa matriks persegi."""
    length, _ = matrix.shape
    
    x = symbols('x')
    identity = create_identity(matrix)
    eigen_val = eigen_values(matrix)
    zero_matrix = zeros(length,1)
    final_eigen_vector = Matrix([[]])

    for i in range(eigen_val.cols):
        # ganti elemen diagonal dengan nilai eigen ke-i
        for j in range(length):
            identity[j,j] = eigen_val[0,i]
        

        # lakukan pengurangan kemudian dibulatkan (agar gauss jordan bekerja)
        identity_subtract_matrix = np.array(identity - matrix).astype(np.float64)
        identity_subtract_matrix = np.around(identity_subtract_matrix)
        identity_subtract_matrix = Matrix(identity_subtract_matrix)

        # cari vektor eigen
        tau0 = symbols(['tau0'])
        solutions, params, freevars = (identity_subtract_matrix).gauss_jordan_solve(zero_matrix, freevar=True)
        print(solutions)
        print(params)
        print(freevars)

    if left:
        return final_eigen_vector
    else:
        return Matrix(transpose(final_eigen_vector))


def eigen_values(matrix):
    """ Fungsi mengembalikan matriks berisi
        nilai eigen.
        
        Prekondisi: matrix berupa matriks persegi."""
        
    x = symbols('x')
    identity = create_identity(matrix)
    identity_subtract_matrix = identity - matrix
    eigen_val = sympy.Poly(identity_subtract_matrix.det()).all_coeffs()
    eigen_val_np = np.array(eigen_val).astype(np.float64)
    eigen_valuesssss = np.roots(eigen_val_np)
    eigen_valuesssss = np.unique(eigen_valuesssss)
    eigen_valuesssss = np.sort(eigen_valuesssss)[::-1]
    eigen_val = Matrix([eigen_valuesssss])
    return eigen_val


def create_identity(matrix):
    """ Fungsi mengembalikan matriks identitas
        yang tiap angka 1 diganti dengan simbol x.
        
        Prekondisi: matrix berupa matriks persegi.
        Contoh: misalkan matrix memiliki ukuran 3x3
                maka outputnya merupakan matriks berikut.
                [[x, 0, 0],
                 [0, x, 0],
                 [0, 0, x]]
    """
        
    length, width = matrix.shape
    identity = Matrix.eye(length)
    x = symbols('x')
    for i in range(length):
        for j in range(width):
            if (identity[i,j] == 1):
                identity[i,j] = x
    
    return identity


def singular_values(matrix):
    """ Fungsi mengembalikan matriks berisi
        nilai-nilai singular."""
        
    length, width = matrix.shape
    final_singular_matrix = [[0 for _ in range(width)] for _ in range(length)]
    A = matrix.T @ matrix
    eigen_val = eigen_values(A)
    
    for i in range(eigen_val.cols):
        if eigen_val[i] != 0:
            final_singular_matrix[i][i] = eigen_val[i] ** 0.5
            
    final_singular_matrix = Matrix(final_singular_matrix)
    
    return final_singular_matrix

    

# A adalah matriks yang akan dicari matriks SVD nya
# 11/11/2021, 10.43 WIB, udah berhasil, kalau matriksnya besar masih ngebug
# A = np.array([[3, 1, 1], [-1, 3, 1]])
# AAT = A @ A.T
# ATA = A.T @ A
# us = singular_vectors(AAT, True)
# ss = singular_values(A)
# vs = singular_vectors(ATA, False)
# print(us)
# print(ss)
# print(vs)
# A = (us @ ss) @ vs
# print(A)

# C = np.array([[3, 1, 1], [-1, 3, 1]])
# # tes dengan library SVD
# u,s,v = np.linalg.svd(C, full_matrices=True)
# print(u)
# print(s)
# print(v)
# B = (u @ s) @ v
# print(B)