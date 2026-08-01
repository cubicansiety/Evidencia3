N=int(input("Escribe un numero positivo:"))
i=1
while True:
    print(i**2, end=" ")
    i+=1
    if i > N:
        break
print("Seria la secuencia de cuadrados hasta:",N)