#14-a
lst1=[12, -1, 9, 8, -0.5, -0.2, -100]
lst2=list(filter(lambda x:x<0,lst1))
print(lst2)

#14-b
num=[22, 100, 19, 13, 11, 1, 4, 66]
pares=list(filter(lambda x:x%2==1,num))
print(pares)

#14-c
str1="Los Juegos olímipicos de Invierno de 2022 se llevarán a cabo en Beijing, China"
lst3=list (filter(lambda x:True if x.lower()in "aeiou"else False,str1))
print(lst3)

#14-d
str2="Los Juegos olímipicos de Invierno de 2022 se llevarán a cabo en Beijing, China"
lst4=list(filter(lambda x: True if x in"0123456789"else False,str2))
print(lst4)

#14-e
num1=[1000, 500, 600, 700, 5000, 90000, 17500]
num2=list(map(lambda x:x+2000,filter(lambda x:x<8000,num1)))
print(num2)

#14-f
num3=[1000, 500, 600, 700, 5000, 90000, 17500]
num4=list(filter(lambda x: True if x>0 else False, map(lambda x:x*-1,num3)))
print(num4)