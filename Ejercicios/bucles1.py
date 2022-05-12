#8-a
lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for i in lst:
    print(i)

#8-b
lst1=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for i in lst1:
    print("Hello", i)

#8-c
str="Antarctica"
for i in str:
    print(i)

#8-d
str2="Civilization"

c=0
for i in str2:
   c=c+1
   print(c)

#8-e
list1=["Phil", "Oz", "Seuss", "Dre"]
list2=[]
for i in list1:
   list2.append("Dr. "+ i)
print(list2)

#8-f
nums=[3, 7, 6, 8, 9, 11, 15, 25]
nums2=[]
for i in nums:
    nums2.append(i**2)
print(nums2)

#8-g
numl=[111, 32, -9, -45, -17, 9, 85, -10]
numl2=[]
for i in numl:
    if i>0:
        numl2.append(i)
print(numl2)

#8-h
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst3=[]
for i in dict:
    if dict [i]>1000:
        lst3.append(dict[i]-1000)
print(lst3)

#8-i
lst4=[3.14,66,"Teddy Bear",True, [],{}]
lst5=[]
for i in lst4:
    lst5.append(type(i))
print(lst5)