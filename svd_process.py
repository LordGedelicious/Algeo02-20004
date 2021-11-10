import numpy as np
from numpy.core.fromnumeric import sort, transpose
import sympy
from sympy import symbols, Matrix, solve, zeros


def singular_vectors(matrix, left=True):
    """ Menghitung matriks singular kiri atau kanan.\n
        Untuk menghitung matriks singular kiri, 
            Argumen matrix berupa matriks AAT dan left = True.\n
        Untuk menghitung matriks singular kanan, 
            Argumen matrix berupa matriks ATA dan left = False.\n
        
        Prekondisi: matrix berupa matriks persegi."""
    print(matrix)
    length, width = matrix.shape
    
    x = symbols('x')
    identity = create_identity(matrix)
    eigen_val = eigen_values(matrix)
    zero_matrix = zeros(length,1)
    print(zero_matrix)
    final_eigen_vector = Matrix([[]])
    
    # menghitung vektor eigen
    for i in range(eigen_val.cols):
        # subtitusi x pada identity menjadi nilai eigennya
        for j in range(length):
            for k in range(width):
                if (identity[j,k] == x or identity[j,k] == eigen_val[0,i-1]):
                    identity[j,k] = eigen_val[0,i]
        identity_subtract_matrix = identity - matrix
        solutions, params = identity_subtract_matrix.gauss_jordan_solve(sympy.Matrix([[0],[0],[0]]))
        print(solutions)
        for p in params:
            # subtitusi 1 ke parameter pada solutions
            partial_solution_temp = solutions.xreplace({p:1})
            partial_solution = partial_solution_temp.xreplace({p:0 for p in params})
            
            # normalisasi vektor
            vector_len = 0
            for q in partial_solution:
                vector_len += q ** 2
            vector_len = (vector_len ** 0.5) ** (-1)
            partial_solution *= vector_len
            
            final_eigen_vector = final_eigen_vector.col_insert(length,partial_solution)
        print(final_eigen_vector)
    if left:
        return final_eigen_vector
    else:
        return transpose(final_eigen_vector)


def eigen_values(matrix):
    """ Fungsi mengembalikan matriks berisi
        nilai eigen.
        
        Prekondisi: matrix berupa matriks persegi."""
        
    x = symbols('x')
    identity = create_identity(matrix)
    identity_subtract_matrix = identity - matrix
    eigen_val = sympy.Poly(identity_subtract_matrix.det()).all_coeffs()
    eigen_val_np = np.array(eigen_val).astype(np.float64)
    eigen_val = Matrix([np.roots(eigen_val_np)])

    return eigen_val


def eigen_sort(mat):
    for i in range(0,mat.rows):
        for j in range(0,mat.rows):
            if mat[i] > mat[j]:
                temp = mat[i]
                mat[i] = mat[j]
                mat[j] = temp
    return mat


def create_identity(matrix):
    """ Fungsi mengembalikan matriks identitas
        yang tiap angka 1 diganti dengan simbol x.
        
        Prekondisi: matrix berupa matriks persegi."""
        
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
        nilai-nilai singular.
        
        Prekondisi: matrix berupa matriks persegi."""
        
    length, width = matrix.shape
    final_singular_matrix = [[0 for _ in range(width)] for _ in range(length)]
    eigen_val = eigen_values(matrix)
    
    for i in range(min(length, width)):
        if eigen_val[i] != 0:
            final_singular_matrix[i][i] = eigen_val[i] ** 0.5
            
    final_singular_matrix = Matrix(final_singular_matrix)
    
    return final_singular_matrix
    
# sample adalah matrix AAT yang siap dibuat jadi matriks singular kiri
sample = np.array([[96809,65909,70644], [65909,98633,58618], [70644,58618,82918]])
print(singular_vectors(sample, True))