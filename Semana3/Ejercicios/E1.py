"""
Maximo de un arreglo de enteros, 
dividiendo el arreglo en dos partes y 
comparando los maximos de cada parte 
con recursividad.

"""

import random as r


def maximo(arr, i, j):
    # En caso de que el arreglo tenga un solo elemento
    if i == j:
        return arr[i]
    else:
        m = (i + j) // 2
        max1 = maximo(arr, i, m)
        max2 = maximo(arr, m + 1, j)
        return max(max1, max2)


# Generar un arreglo de 10 elementos
A = [r.randint(0, 100) for i in range(10)]
print(A)
print(maximo(A, 0, len(A) - 1))
