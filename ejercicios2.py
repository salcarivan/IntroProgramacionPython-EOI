#sumar numeros pares entre 2 y 100
num=2
suma=0
while num<=100:
    if num%2==0:
        suma=suma+num
    num=num+1
print(f"la suma de los pars entre dos y 100 es: {suma} ")
#ingresar un numero y muestre todos los divisores del mismo
num1=int(input("Ingrese número por favor: "))
divs=1
while divs<=num1:
    if num1%divs==0:
        print(divs)
    divs=divs+1
#algoritmo calificación
cal1=int(input("Escribe calificación examen 1: "))
cal2=int(input("Escribe calificación examen 2: "))
cal3=int(input("Escribe calificación examen 3: "))
Prom=(cal1+cal2+cal3)/3
if Prom<5:
    print("Insuficiente")
elif Prom<6:
    print("Suficiente")
elif Prom<7:
    print("Bien")
elif Prom<8:
    print ("Notable")
else:
    print("Sobresaliente")