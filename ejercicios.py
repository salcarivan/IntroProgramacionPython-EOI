#hola mundo
print("Hola mundo")
#a partir de número ingresado giga si es mayor , menor o igigal a 9
num=int(input("Ingrese número por favor: "))
print(num)
if num==9:
    print("El numero es igual a 9")
elif num>9:
    print ("El numero es mayor que 9")
elif num<9:
        print ("El numero es menor que 9")
#a partir de numeri ingresado decir si es par o inpar
num0=int(input("Ingrese número por favor: "))
if (num0%2)==0:
    print (f"El número {num0} es par")
else:
    print (f"El número {num0} es impar")
#igresar 2 números y que te de la suma entre ambos
num1=int(input("Ingrese sumando 1 por favor: "))
print(num1)
num2=int(input("Ingrese sumando 2 por favor: "))
print (num2)
res=num1+num2
print(f"El resultado es: {res}")