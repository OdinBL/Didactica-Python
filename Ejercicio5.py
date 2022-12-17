gigaby = int(input("ingrese capacidad de disco en GB: "))

megaby = gigaby * 1024
kiloby = megaby * 1024
cbytes = kiloby * 1024

print("La capacidad del disco duro es: ",gigaby,"GB")
print("En Megabytes es: ",kiloby,"KB")
print("En bytes es: ",cbytes,"B")