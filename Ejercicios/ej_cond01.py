#7-a
nombre=input("Escribir nombre: ")
if nombre=="Bond":
    print ("Bienbenido a bordo 007")
else:
    print("Buenos días", nombre)

#7-b
nombre1=input("Escribir nombre: ")
if nombre1.lower()=="bond":
    print ("Bienbenido a bordo 007")
else:
    print("Buenos días", nombre1)

#7-c
num=int(input("Ingrese un número: "))
def pares(num):
 if num%2==0:
      print (f"El número {num} es par")
 else:
     print(f"El número {num} es impar")
print(pares(num))

#7-d
def decimal (i):
    if i-int(i)!=0:
        return i-int(i)
    else:
        return "INTEGER"

print(decimal(99.09))
print(decimal(99.00))

#7-e
treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}
def moretrees(dict):
    lst=[]
    for i in dict:
        if dict[i]>20000:
            lst.append(i)
        else:
            pass
    return lst
print(moretrees(treepersqkm))

#7-f
str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"
def count_l(a):
    cont=0
    for i in a.split():
        if "l"in i:
            cont=cont+1
        else:
            pass
    return cont
print(count_l(str))