# programa 38
def sumar_numeros_pares(n):
    suma = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            suma += i
    return suma

resultado = sumar_numeros_pares(20)
print(resultado)
            
