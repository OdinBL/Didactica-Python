import os
os.system("cls")

raspa_gana = int(input("Ingrese numero del numero secreto de la tarjeta: "))

if raspa_gana % 2 == 0 and raspa_gana > 100:
    porc = 15
    resultado = raspa_gana * porc / 100
    print(f"El numero secreto de la tarjeta es par y logro obtener el 15% de descuento, el descuento seria...{resultado}", "%")
elif raspa_gana < 100:
    porce = 5
    resultado_1 = raspa_gana * porce / 100
    print(f"El numero secreto y logro obtener el 5% de descuento, el descuento seria... {resultado_1}", "%")

else:
    print("Es impar y no se obtiene descuentos")