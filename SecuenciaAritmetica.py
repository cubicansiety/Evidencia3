inicio=int(input("Escribe el primer numero:"))
diferencia=int(input("Escribe la diferencia:"))
limite=int(input("Escribee el limite:"))
num=inicio
while True:
    print(num, end=" ")
    num+=diferencia
    if num>limite:
        break
print("\nsecuencia aritmetica desde",inicio,"hasta",limite)