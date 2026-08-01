while True:
    opcion = int(input("Escribe la opcion que vas a saleccionar, en donde..(1=sumar,2=restar,3=multiplicar,4=dividir,5=salir): "))
    if opcion == 5:
        break
    num1 = float(input("Escriba el primer numero: "))
    num2 = float(input("Escriba el segundo numero: "))
    if opcion == 1:
        print("El resultado de la suma seria:", num1 + num2)
    elif opcion == 2:
        print("El resultado de la resta seria:", num1 - num2)
    elif opcion == 3:
        print("El resultado de la multiplicacion seria:", num1 * num2)
    elif opcion == 4:
        if num2 != 0:
            print("El resultado de la division seria:", num1 / num2)
        else:
            print("No se puede dividir entre cero...")