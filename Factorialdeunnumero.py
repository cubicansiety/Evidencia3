num=int(input("Numero para factorial: "))
factorial=1
if num<0:
    print("No se puede obtener un numero factorial de este numero...")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("El factorial de ", num," es: ", factorial)