# Maximo de un arreglo de enteros, 
# dividiendo el arreglo en dos partes y 
# comparando los maximos de cada parte 
# con recursividad.

def maximo(arr, i, j):
    # En caso de que el arreglo tenga un solo elemento
    if i == j:
        return arr[i]
    else:
        m = (i + j) // 2
        max1 = maximo(arr, i, m)
        max2 = maximo(arr, m + 1, j)
        return max(max1, max2)

    
A = [1, 19, 45, 10, 23]
print(maximo(A, 0, len(A) - 1))