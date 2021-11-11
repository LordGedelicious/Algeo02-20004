import numpy
import sympy

# mat = sympy.Matrix([[-3,8,-11,6,2,0,-6,9,1,7,0,-2]])
# for i in range(0,mat.cols):
#     for j in range(0,mat.cols):
#         if mat[i] > mat[j]:
#             temp = mat[i]
#             mat[i] = mat[j]
#             mat[j] = temp

# print(mat)
# x = sympy.symbols('x')
# solution = sympy.solve(x**3 - 278360*x**2 + 12983580912*x - 152533992248140,x)
# print(solution)

# arr = [1,-278360,12983580912,-152533992248140]
# print(numpy.roots(arr))

# polynoms = sympy.Poly(x**3 - 278360*x**2 + 12983580912*x - 152533992248140)
# print(polynoms.all_coeffs())

# a = sympy.Matrix([[1,-1,2,-1],[2,1,-2,-2],[-1,2,-4,1],[3,0,0,-3]])
# sol, params = a.gauss_jordan_solve(sympy.Matrix([-1,-2,1,-3]))
# print(sol)
# print(params)

# a = sympy.Matrix([[1,-1,2,-1],[2,1,-2,-2],[-1,2,-4,1],[3,0,0,-3]])
# v  = a.nullspace()[0]
# x = sympy.lcm([val.q for val in v])
# ans = x*v
# print(ans)

a = sympy.Matrix([[126460, 65909, 70644], [65909, 124634.344, -58618], [-70644, -58618, 140349.344]])
zero_mat = sympy.Matrix([0,0,0])
print(a.shape)
print(sympy.Matrix([[0,0]]).shape)
print(sympy.Matrix([0,0]).shape)
sol, par = a.gauss_jordan_solve(zero_mat)
print(sol)

# Dump dari svd_process :
# partial_solution = Matrix([[]])
# for p in params:
#     # subtitusi 1 ke parameter pada solutions
#     partial_solution_temp = solutions.xreplace({p:1})
#     partial_solution = partial_solution_temp.xreplace({p:0 for p in params})
#     print("ini partial 1",partial_solution)
#     # normalisasi vektor
#     vector_len = 0
#     for q in partial_solution:
#         vector_len += q ** 2
#         vector_len = (vector_len ** 0.5) ** (-1)
#         partial_solution *= vector_len
#     print("ini partial 2",partial_solution)
#     final_eigen_vector = final_eigen_vector.col_insert(length,partial_solution)
# print(final_eigen_vector)