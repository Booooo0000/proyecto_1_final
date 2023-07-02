print("Programa 13. \nPrograma que calcule el salario bruto \n")

Salario = int(input("leer el salario bruto de empleado"))

SeguroSocial = Salario * 0.0514
SeguroEducativo = Salario * 0.02
Prestamo = 50

Pago = Salario - SeguroSocial - SeguroEducativo - Prestamo

print("cantidad a pagar del Seguro Social es", SeguroSocial)
print("cantidad a pagar del Seguro Educativo es", SeguroEducativo)
print("cantidad a pagar del Seguro Prestamo es", Prestamo)

print("El salario neto del empleado es:", Pago)