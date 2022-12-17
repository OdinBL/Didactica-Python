import os
os.system("cls")

din_juan = float(input("Dinero de Juan: $"))
din_rosa = float(input("Dinero de rosa: $"))
din_daniel = float(input("Dinero de daniel: s/."))

dolares_daniel = din_daniel/ 3
capital_total = din_juan + din_rosa + din_daniel
porc_juan = (din_juan * 100)/ capital_total
porc_rosa = (din_rosa * 100)/ capital_total
porc_daniel = (dolares_daniel * 100)/ capital_total

print("El capital total es: $", format(capital_total,".2f"))
print("Juan ofrecio el: ",format(porc_juan,".2f"),"%")
print("Rosa ofrecio el: ",format(porc_rosa,".2f"),"%")
print("Daniel ofrecio el: ",format(porc_daniel,".2f"),"%")