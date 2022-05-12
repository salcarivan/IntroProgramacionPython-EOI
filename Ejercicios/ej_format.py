nombre=input("Por favor ingrese su nombre: ")
#Pon tu respuesta aquí
print ("Hola "+ nombre+"!!!!")
print ("Hola {}!!!".format(nombre))
print("Hola {s}!!!".format(s=nombre))
print (f"Hola {nombre}!!!")

#Format method to type a number
print ("El número es {}".format(5))

# Format method to fill multiple values
print ("Los números son {},{},{}".format(1,2,3))

#multiplas valores 2
str= "Un año tiene {} meses, {} semanas y {} días".format(12,52,365)
print(str)

#mapeo de posición de valor
str= "Un año tiene {2} meses, {0} semanas y {1} días".format(52,365,12)
print(str)

#Asignación de puntajes de exámenes con el método Format
John=75
Ann=80
Ally=60

str="Scores were as following: John:{}, Ann:{}, Ally:{}"
str=str.format(John,Ann,Ally)
print(str)
