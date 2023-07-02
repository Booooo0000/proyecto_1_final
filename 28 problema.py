# programa 28 - que muestre una solicitud de una nota

nota = int(input("Ingrese la nota:"))

if nota >= 90 and nota <= 100:
    print("la letra corresponde es A")
    
elif nota >= 80 and nota <= 89:
    print("la letra corresponde es B")

elif nota >= 70 and nota <= 79:
    print("la letra corresponde es C")
    
elif nota >= 60 and nota <= 69:
    print("la letra corresponde es D")
    
else:
    print("la nota corresponde es F")

print("\n final del programa")