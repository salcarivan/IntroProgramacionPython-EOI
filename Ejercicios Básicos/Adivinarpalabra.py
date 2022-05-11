palabra1 = "suerte"
print("Adivine la palabra (N para Abandonar): ")
while True:
    palabra2 = input() 
    if palabra2 == palabra1:
        break 
    elif palabra2 == "N":
        break
    print("Vuelve a intentarlo (N para Abandonar): ")
print("Felicidades, has adivinado la palabra")