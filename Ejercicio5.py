import os
os.system("cls")

numero = input("Ingrese el numero de 4 cifras: ")

if len(numero) != 4:
    print("El numero debe ser de 4 cifras")

else:
    cf_men = 10;
    cf_may = 0;

    for cifra in numero:
        if (int(cifra) < cf_men):
            cf_men = int(cifra);

        elif (int(cifra) > cf_may):
            cf_may = int(cifra);
    
    print(f"El mayor número posible es: {str(cf_may)}{str(cf_men)}");
