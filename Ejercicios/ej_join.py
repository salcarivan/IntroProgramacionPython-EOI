#Método de unión de cadenas con listas
lst=["Cádiz","Huelva","Sevilla","Málaga","Córdoba","Almería","Jaen","Granada"]
join="+ + +".join(lst)
print(join)

#método de unión de cadenas con tuplas
adr=("ejemplo_ejemplar", "anyemail.com")
email= "@".join(adr)
print(email)

#Ejercicio 2-c: método Join con un carácter especial
lst=['Everything', 'has', 'beauty,', 'but', 'not', 'everyone', 'can', 'see.']
str=" ".join(lst)
print(str)

#Ejercicio 2-d: método de unión de cadenas con diccionarios
economic_growth={"India": 7.0, "Cambodia": 7, "Tanzania": 6.9, "Bangladesh": 6.6, "Senegal": 6.6}
str1=",".join(economic_growth)
print(str1)

#Ejercicio 2-e: método de unión de Python con carácter de nueva línea
poem_lst=["Not enjoyment, and not sorrow,", "Is our destined end or way;", "But to act, that each tomorrow", "Find us farther than today."]
poem_str="\n".join(poem_lst)
print(poem_str)