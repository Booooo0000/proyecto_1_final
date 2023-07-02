# programa 39
def calcular_area_triangulo(base,altura):
    area = (base*altura)/2
    return area

base = float(input("introduce base del trianfulo"))
altura = float(input("introduce altura del trianfulo"))

area = calcular_area_triangulo(base,altura)
print(f"el area del triangulo es:{area}")
