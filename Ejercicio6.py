import os
os.system("cls")

rad = float(input("Ingrese el radio del cilindro: "))
altu = float(input("Ingrese la altura del cilindro: "))

areatt = 2 * 3.1416 * rad * (rad + altu)
volumen = 3.1416 * rad * 2 * altu

print("El area total del cilindro es: ", format(areatt,".2f"))
print("El volumen del cilindro es: ", format(volumen,".2f"))