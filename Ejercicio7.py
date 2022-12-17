import os
os.system("cls")

num_1 = input("Escribir el primer numero: ")
num_2 = input("Escribir el segundo  numero: ")
num_3 = input("Escribir el tercer numero: ")


if num_1 > num_2:
   medio = num_1
   xtem = num_2

else:
   medio = num_2
   xtem = num_1

if medio > num_3 :
   medio = num_3

if medio < xtem :
   medio = xtem

print("El número Medio es : ", medio)