value = 1
while value <= 5:
    nota = int(input("Ingrese la nota:"))
    print(value)
    break
if nota >= 90 and nota <= 100:
    print("la nota es una A")
    
elif nota >= 80 and nota <= 89:
    print("la nota es una B")
    
elif nota >= 70 and nota <= 79:
    print("la nota es una C")
    
elif nota >= 60 and nota <= 69:
    print("la nota es una D")
    
else:
    print("la nota es una F")  
    
    value += 1