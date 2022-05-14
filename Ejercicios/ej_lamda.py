#11-a
from re import X


i=6
L=lambda x:x+2
print(L(i))

#11-b
j=9
f=lambda z:z*11
print(f(j))

#11-c
m,n=5,10
o=lambda m,n:n*m
print(o(m,n))

#11-d
lst=[100, 10, 10000, 1, 9, 999, 99]
clave=lambda x: 100/x
vuelta=lst.sort(clave)
print(lst)

#11-e
lst1=[100, 10, 10000, 1, 9, 999, 99]
lst1= sorted(lst1, key=lambda x: x)
print(lst1)

#11-f
lst2=["nutria", "ballena", "ganso", "ardilla", "zorro", "oveja","conejo","erizo" ]
lst2=sorted(lst2,key1=lambda x:x[1])
print(lst2)

#11-g
lst3=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
lst3=sorted(lst3,key2=lambda x:x[1])
print(lst3)

#11-h
lst4=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
lst4=sorted(lst4,key=lambda x:x[1][-1])
print(lst4)

#11-i
lst5=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
lst5=sorted (lst5,lambda x:[1],[-1],reverse=True)
print(lst5)