print("Programa 20. \n calcular salario neto \n")
Salario = int(input("leer el salario bruto"))

SeguroSocial = Salario * 0.08
SeguroEducativo = Salario * 0.02
Impuesto = Salario * 0.15
Prestamo = 100

Pago = Salario - SeguroSocial - SeguroEducativo - Impuesto - Prestamo

print("cantidad a pagar del Seguro Social es", SeguroSocial)
print("cantidad a pagar del Seguro Educativo es", SeguroEducativo)
print("cantidad a pagar del Seguro Prestamo es", Prestamo)
print("cantidad a pagar del Seguro Impuesto es", Impuesto)

print("El salario neto del empleado es:", Pago)