import random
numale = random.randint(1, 100)
while True:
    numerousuario = int(input("Escribe un numero del 1 hasta el 100: "))
    if numerousuario < numale:
        print("El numero es mayor")
    elif numerousuario > numale:
        print("El numero es menor")
    elif numerousuario == numale:
        print("Perfecto!, el numero era", numale)
        break