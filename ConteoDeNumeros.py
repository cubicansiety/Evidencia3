intentos = int(input("Ingrese la cantidad de numeros a escribir: "))
mayores = 0
menores = 0
iguales = 0
for i in range(intentos):
    num = int(input("Escriba un numero :"))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1
print("Hay",mayores,"numero/s mayores que cero")
print("Hay",menores,"numero/s menores que cero")
print("Hay",iguales,"numero/s iguales a cero")