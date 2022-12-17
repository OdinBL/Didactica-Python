import os
os.system("cls")

r = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cil"))

area_base = 3.1416 * r(r ** 2)
area_lateral = 2 * 3.1416 * r * h
area_total = 2 * area_base * area_lateral

print("El area base del cilindro es:",format(area_base, ".2f"))
print("El area lateral del cilindro es:",format(area_lateral, ".2f"))
print("El area total del cilindro es:",format(area_total, ".2f"))