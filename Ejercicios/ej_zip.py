#12-a
lst1=[19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst2=["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]
lst3=list(zip(lst1,lst2))
print(lst3)

#12-b
lst4=["Energía", "Agricultura", "Industria", "Tecnología", "Finanzas","Sivicultura"]
rg1=list(range(1,8))
lst5=list(zip(lst4,rg1))
print(lst5)

#12-c
lst6= ["Netflix", "Hulu", "Sling", "HBO"]
lst7= [198, 166, 237, 125]
punt=dict(zip(lst6,lst7))
print(punt)

#12-d
lst8=["Mike", "Danny", "Jim", "Annie"]
lst9=[4, 12, 7, 19]
lsts=sorted(list(zip(lst8,lst9)))
print(lsts)