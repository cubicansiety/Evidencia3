palabra = input("Escriba una palabra: ").lower()
contador = 0
for letra in palabra:
    if letra == "a":
        contador += 1
print("La palabra que escribio","(",palabra,")", "cuenta con", contador, "letras a...")