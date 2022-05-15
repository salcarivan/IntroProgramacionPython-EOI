magd=input("Unidad de distancia (km o m): ")
dist=int(input("Ingrese distancia recorrida: "))
magt=input("Unidad de tiempo (s o h): ")
tiem=int(input("Ingrese tiempo transurrrido: "))

if magd=="km" or magd=="m":
    var=True
else:
    var=False

if magt=="s" or magt=="h":
    var=True
else:
    var=False
while var==False:
    print ("Por favor ingrese una variable válida")
    magd=input("Unidad de distancia (km o m): ")
    magt=input("Unidad de tiempo (s o h): ")

def velocidad (num1,num2):
   if magd=="km" and magt=="s":
       num1=num1/1000
   elif magd=="m" and magt=="h":
      num2=num2/3600
   try:
     return num1/num2
   except ZeroDivisionError:
       print ("No se puede dividir entre 0")


print("Si ha recorrido:", dist,magd, "y su velocidad ha sido:", tiem,magt,
"su velocidad ha sido:", velocidad(dist,tiem), magd,"/",magt)

























