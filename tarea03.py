num1=int (input("Ingrese valor 1: "))
num2=int(input("ingrese valor 2: "))
def suma():
    print (num1 + num2)
def resta():
    print(num1-num2)
def producto():
    print(num1*num2)
def division():
    print (num1/num2)
operacion=int (input("¿Que operacion quiere realizar: 0.Suma, 1.Resta, 2.Producto, 3.División?: "))
if operacion ==0:
    suma()
elif operacion ==1:
    resta()
elif operacion==2:
    producto()
elif operacion==3:
    division()