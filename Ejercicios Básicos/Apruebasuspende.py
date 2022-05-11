def evaluacion (Cal1,Cal2,Cal3):
 if((Cal1 in range(0,11)) and (Cal2 in range(0,11)) and (Cal3 in range (0,11)) ):
     Prom=(Cal1+Cal2+Cal3)//3
     if (Prom>=4):
         print ("Arueba con: ", Prom)
     else:
         print ("Suspende con: ", Prom)

 if (Cal1 or Cal2 or Cal3<0):
    raise ValueError("El número no puede ser negativo")

while True:
    try:
        nota1=float(input("Ingrese Calificacion 1: "))
        nota2=float(input("Ingrese calificación 2: "))
        nota3=float(input("Ingrese calificación 3: "))
        evaluacion(nota1,nota2,nota3)
        break
    except ValueError:
     print("por favor ingrese valores en númericos o positivos")


