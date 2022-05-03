contadornumero=0
for numero in range (1,21,2):
    contadornumero+=1
    if(contadornumero>0):
        break #salta a la linea despues del bloque for
    print(numero)
    #print("otra instruccion 1")
    #print("otra instruccion 2")
    #print("otra instruccion 3")
    #print ("otra instuccion 4")
print("numeros de la serie", contadornumero)
