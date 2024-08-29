"""
Realizar un algoritmo que multiplique dos numeros enteros
de n digitos, dividiendo los numeros en dos partes y
multiplicando las partes con recursividad.

"""

def multi(x: int, y: int) -> int:
    n = len(str(x))
    # Descomponer los numeros en dos partes
    a1 = x // 10**(n//2)
    a2 = x % 10**(n//2)
    b1 = y // 10**(n//2)
    b2 = y % 10**(n//2)

    if n <= 2:
        return x * y
    else:
        # Multiplicar las partes
        z1 = multi(a1, b1) * 10**n
        z2 = (multi(a1, b2) + multi(a2, b1)) * 10**(n//2) 
        z3 = multi(a2, b2)

        return z1 + z2 + z3
    

print(multi(1231, 5671))
