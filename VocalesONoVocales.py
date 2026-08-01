while True:
    letra = input("Escribe una letra(si desea terminar, solo presione Enter sin escribir una letra): ")
    if letra == "":
        break
    elif letra in "aeiou":
        print("La letra es una vocal")
    else:
        print("La letra es una consonante")
print("Fin del programa")