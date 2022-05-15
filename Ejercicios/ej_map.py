#13-a
from winreg import REG_NOTIFY_CHANGE_ATTRIBUTES


lst1=[10, 20, 30, 40, 50, 60]
lst2=list(map(lambda x:x+5,lst1))
print(lst2)

#13-b
lst3=[10, 20, 30, 40, 50, 60]
lst4=list(map(lambda x:x**2,lst3))
print(lst4)

#13-c
nam=["Antonio", "Eduardo", "Marta", "Jacobo"]
nam2=list(map(lambda x: "Hola"+x,nam))
print(nam2)

#13-d
frio=["Alpino", "Avalancha", "Polvo", "Copo de nieve", "Cumbre"]
frio2=list(map(len,frio))
print=(frio2)

#13-e
num=[100, 200, 300, 400, 500]
num1=[1,10,100,1000,10000]
num3=list(map(lambda x,y:x+y,num,num1))
print(num3)

#13-f
ciu=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
ciu2=list(map(lambda x:x.count("a"),ciu))
print(ciu2)

#13-g
eeuu1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
eeuu2=list (map(lambda x:x.lower().count("a"),eeuu1))
print(eeuu2)

#13-h
numm=[99.3890,-3.5, 5, -0.7123, -9, -0.003]
num1=list(map(abs,numm))
res=sum(num1)
print(res)