print("Haciendo converciones...")

met = int(input("ingrese la cantidad en metros: "))
 centi = met * 100 
 pulga = centi / 2.54
 pies = pulga / 12
 yardas = pies / 3

 print(("Centimetros: ",format(centi,".2f")),"cm")
 print(("Pulgadas: ",format(pulga,".2f")),"in")
 print(("Pies: ",format(pies,".2f")),"ft")
 print(("Yardas: ",format(yardas,".2f")),"yd")