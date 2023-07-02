print("Programa 19. \n Programa que calcule la compra de 5 articulos \n")

valor1 = float(input("precio del articulo 1"))
valor2 = float(input("precio del articulo 2"))
valor3 = float(input("precio del articulo 3"))
valor4 = float(input("precio del articulo 4"))
valor5 = float(input("precio del articulo 5"))

total1 = valor1 + valor2 + valor3 + valor4 + valor5
total2 = total1 * 1.07
promedio = (valor1 + valor2 + valor3 + valor4 + valor5)

RD1 = round(total1, 2)
RD2 = round(total2, 2)
RD3 = round(promedio, 2)

print("el total1 es", RD1)
print("el total2 es", RD2)
print("el promedio es", RD3)
