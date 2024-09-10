manzkm = int(input("ingrese los kilos de las manzanas= "))


if manzkm <= 2 :
    print("descuento del 0%")

if manzkm == 2.01 or manzkm <= 5:
    print("descuento del 10%")


if manzkm == 5.01 or manzkm <= 10:
    print("descuento del 15%")

if manzkm >= 10.01 :
    print("descuento del 20%")