import os

os.system("cls")

n = int(input("Coloque un número: "))

a = int(input("El primer digito es: "))
b = int(input("El segundo digito es: "))
c = int(input("El tercer digito es: "))

if a < b < c :
    print("El numero esta ordenado en ascendente")
elif a > b > c :
    print("El numero esta ordenado en descendente")
else :
    print("El numero esta desordenado")