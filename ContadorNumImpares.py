num = int(input("Escriba un numero: "))
i = 1
while i <= num:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print("\nSon los numero impares hasta llegar a", num)