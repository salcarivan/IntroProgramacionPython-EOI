#9-a
contador=0
total=0
while contador<=100:
    total=total+contador
    contador=contador+1
print(total)

#9-b
lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
i=0
while i<len(lst):
    if lst[i]==100:
      print("el número 100 está en la poscion: "+ str(i))
    i=i+1

#9-c
lst1=["Juan", "Sara","Migüel", "Jesica","","Marco","","Alex"]
def nombre(list):
 i=0
 lstn=[]
 while i<len(lst):
     if lst1 [i]!="":
         lstn.append(list[i])
     i=i+1
     return lstn 
print(nombre(lst1))

#9-d
lst2=["Olivia","","Nico","Ben","Alicia"]
def addname (lst2):
    i=0
    lstn2=[]
    while i<len(list):
        if lst2[i]!="":
            lstn2.append(list[i])
        else:
            break
        i=i+1
    return lstn2

print(addname)