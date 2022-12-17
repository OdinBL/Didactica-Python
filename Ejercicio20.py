dinero=int(input("la cantidad de dinero:s/."))

billetes_200=dinero//200
billetes_100=billetes_200//100
billetes_50=(billetes_200)%100 //50
billetes_20=((billetes_200)%100)%50 //20
billetes_10=(((billetes_200)%100)%50)%20 //10

moneda_5=((((billetes_200)%100)%50)%20)%10 //5
moneda_2=(((((billetes_200)%100)%50)%20)%10)%5 //2
moneda_1=((((((billetes_200)%100)%50)%20)%10)%5)%2 //1

print("billetes de 200:",billetes_200)
print("billetes de 100:",billetes_100)
print("billetes de 50:",billetes_50)
print("billetes de 20:",billetes_20)
print("billetes de 10:",billetes_10)
print("moneda de 5:",moneda_5)
print("moneda de 2:",moneda_2)
print("moneda de 1:", moneda_1)