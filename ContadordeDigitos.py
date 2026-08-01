num=int(input("Escriba un numero entero:"))
if num==0:
    digitos=1
else:
    digitos=0
    num=abs(num)
    while num>0:
        num//=10
        digitos+=1
print("El numero que escribio tiene ",digitos,"digitos en total")