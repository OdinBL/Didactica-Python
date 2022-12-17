import os
os.system("cls")

n = int(input("Ingrese valor del 1 al 7: "))

if n == 1:
    print("El dia de la semana es lunes")
elif n == 2:
    print("El dia de la semana es marte")
elif n == 3:
    print("El dia de la semana es miercoles")
elif n == 4:
    print("El dia de la semana es jueves")
elif n == 5:
    print("El dia de la semana es viernes")
elif n == 6:
    print("El dia de la semana es sabado")
elif n == 7:
    print("El dia de la semana es domingo")
else:
    print("el dia no existe")