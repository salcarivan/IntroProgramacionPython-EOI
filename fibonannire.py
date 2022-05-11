#algoritmo Fibonnaci recursivo
def Fib (N):
    if (N==1):
        return 0
    elif (N==2):
        return 1
    else:
        return Fib(N-1)+Fib(N-2)

n=input("¿Que numero de la serie fionacci quiere?: ")
try:
    n=int(n)
    serieFib=[]
    for i in range(1,n+1):
        r=Fib(i)
        serieFib.append(r)
    print(f"el numero en esa posicion es {r}")
    print ("La serie es:", *serieFib)
except TypeError:
    print ("Numero no valido")
except ValueError:
    print("Numero invalido")
except:
    print ("Fallo")
    

