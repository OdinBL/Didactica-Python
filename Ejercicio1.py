import os
os.system("cls")

unidades = int(input("unidades: "))

precio = 25

if unidades <= 25 : precio = 27

elif unidades >= 51 : precio = 23

compra = unidades * precio
descuento = (0.15 if unidades > 50 else 0.05) * compra

print ("precio = ", precio)
print ("compra = ",compra)
print ("descuento = ",precio)
print (f"total = {compra - descuento}\n")