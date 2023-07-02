# programa 25 - que muestre clasificación de triangulo

verticeA = float(input("Ingrese la longitud primera vertice: "))
verticeB = float(input("Ingrese la longitud segunda vertice: "))
verticeC = float(input("Ingrese la longitud tercera vertice: "))

if verticeA == verticeB == verticeC:
    print("El triángulo es equilátero")
    
elif verticeA == verticeB or verticeA == verticeC or verticeB == verticeC:
    print("El triángulo es isósceles")
    
else:
    print("El triángulo es escaleno")
    
print("/n final del programa")