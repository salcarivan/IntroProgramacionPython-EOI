#algoritmo cantidad nombre
from math import trunc


nombre=input("Ingrese un nombre: ")
num=int(input("Ingrese número: "))
while num>0:
    print (nombre)
    num=num-1
#algoritmo 3 números
num1=int(input("Ingrese número 1: "))
num2=int(input("Ingrese número 2: "))
num3=int(input("Ingrese número 3: "))
if num1<0 or num2<0 or num3<0:
    Resul=num1*num2*num3
else:
    Resul=num1+num2+num3
print(Resul)
#algoritmo numeros primos
nump=int(input("Ingrese número: "))
divs=2
band=True
if nump==1:
    print("Es primo")
else:
    while band==True and nump>divs:
        if nump%divs==0:
            band=False
        divs=divs+1
    if band==True:
        print("Es primo")
    else:
        print("No es primo")
#algoritmo suma digitos
sumando=int(input("Ingrese número: "))
resul1=0
while sumando>0:
    resul1=resul1+sumando%10
    sumando=trunc(sumando/10)
print(f"El resultado es: {resul1}")