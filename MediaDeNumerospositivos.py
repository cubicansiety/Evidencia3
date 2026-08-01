suma = 0
contador = 0
while True:
    dato = input("Ingrese un número positivo (o escriba 'fin' para terminar): ")
    if dato.lower() == "fin":
        break
    num = int(dato)
    if num > 0:
        suma += num
        contador += 1
if contador > 0:
    media = suma / contador
    print("La media de los números positivos es:", media)
else:
    print("No se ingresaron números positivos.")