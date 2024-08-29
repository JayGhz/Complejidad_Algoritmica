"""
Algoritmo para multiplicar 2 matrices cuadradas de dimension n,
dividiendo cada matriz en 4 sub-matrices de dimension n/2.

"""
import numpy as np

def mult(A, B):
    a_rows, a_cols = A.shape
    b_rows, b_cols = B.shape

    if  a_cols != b_rows:
        raise ValueError("Las matrices no se pueden multiplicar")
    
    c = np.zeros((a_rows, b_cols))

    for i in range(a_rows):
        for j in range(b_cols):
            temp = 0
            for k in range(a_cols):
                temp += A[i, k] * B[k, j]
            c[i, j] = temp
    return c.astype(int)
    
# Creando matrices de prueba
A = np.random.randint(1, 5, size = (3, 4))
B = np.random.randint(1, 5, size = (4, 2))

print(A)
print(B)

C = mult(A, B)
print(C)