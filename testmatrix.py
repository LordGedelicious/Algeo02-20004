import numpy
import sympy

mat = sympy.Matrix([[-3,8,-11,6,2,0,-6,9,1,7,0,-2]])
for i in range(0,mat.cols):
    for j in range(0,mat.cols):
        if mat[i] > mat[j]:
            temp = mat[i]
            mat[i] = mat[j]
            mat[j] = temp

print(mat)
x = sympy.symbols('x')
solution = sympy.solve(x**3 - 278360*x**2 + 12983580912*x - 152533992248140,x)
print(solution)

arr = [1,-278360,12983580912,-152533992248140]
print(numpy.roots(arr))

polynoms = sympy.Poly(x**3 - 278360*x**2 + 12983580912*x - 152533992248140)
print(polynoms.all_coeffs())