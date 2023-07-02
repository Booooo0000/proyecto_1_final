# programa 40
def evaluar_nota(nota):
 if nota >= 90 and nota <= 100:
  return "a"
 elif nota >= 80 and nota <= 89:
  return "b"
 elif nota >= 70 and nota <= 79:
  return "c"
 elif nota >= 60 and nota <= 69:
  return "d"
 else:
     return "f"
nota = float(input("ingresa una nota:"))
letra = evaluar_nota(nota)
print("la letra corresponde a la nota es", letra)