"Programa 24. Calcular el mayor de 3 numeros: \n"

a = float(input("Escribir primer número : "))
b = float(input("Escribir segundo número : "))
c = float(input("Escribir tercer número : "))

if a > b and a > c:
    print("El número mayor es a: ", a)
if b > a and b > c:
    print("El número mayor es b:", b)
if c > a and c > b:
    print("El número mayor es c:", c)
    
print("\n Fin del programa")