# programa 25 - que muestre calculadora de descuento

precio_original = float(input("Ingrese el precio original del producto:"))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento a aplicar:"))

precio_final = precio_original * (1 - porcentaje_descuento / 100)

if precio_final < 50:
    print("Oferta especial")

print("El precio final es:", precio_final)

print("/n final del programa")