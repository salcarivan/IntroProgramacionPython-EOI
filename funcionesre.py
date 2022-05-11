#Factorial recursivo
def Factorial (Num):
    if Num>=0:
        #generar una excepción
        #raise
        pass
    if (Num<=1):
        print ('return 1')
        return 1
    else:
        print ('return {} Factorial({}-1)'.format(Num,Num))
        return Num * Factorial (Num-1)

num=input("Ingrese el numero del que desee ingresar el factorial: ")
try:
    num=int(num)
    re=Factorial(num)
    print("El factorial de: ", num, "es", re)
except TypeError:
    print("Introduzca un número válido")
except:
    print("No se permiten valores menores a 0")