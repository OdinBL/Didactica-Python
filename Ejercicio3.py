import os
os.system("cls")

unidades = float(input("cantidad de productos: "))
if unidades >= 1 and unidades <= 50:
    print("5 caramelos de regalo")
elif unidades >= 51 and unidades <= 100:
    print("se regalan 10 caramelos")
else: 
    print("Se regalan 15 caramelos")
importe = unidades * 20

# Para hallar el descuento

if importe > 700:
    descuento = importe * 0.16
    importe_a_pagar = importe - descuento  
    print(f"descuento {importe_a_pagar: 2f}")
elif importe < 700 and importe > 501:
    descuento = importe * 0.14
    importe_a_pagar = importe - descuento  
    print(f"descuento {importe_a_pagar: 2f}")
else :
    descuento = importe * 0.12
    importe_a_pagar = importe - descuento  
    print(f"descuento {importe_a_pagar: 2f}")