lado1 = float(input("Ingrese la longitud del lado 1: "))
lado2 = float(input("Ingrese la longitud del lado 2: "))
lado3 = float(input("Ingrese la longitud del lado 3: "))


# use el if para verificar que un lado en especifico sea el mayor a los otros dos lados y asignarle una variante y luego asignarle otra variable a las dos menores


if lado1>lado2 and lado1>lado3:
    ladomayor=lado1
    ladosrestantes= lado2+lado3
elif lado2>lado1 and lado2>lado3:
    ladomayor=lado2
    ladosrestantes= lado1+lado3
elif lado3>lado1 and lado3>lado2:
    ladomayor=lado3
    ladosrestantes= lado2+lado3

# aca use if para verificar si el lado mayor era menor a la suma de los lados menores
# use el else en caso de que no se diera lo anteriormente dicho

if ladomayor < ladosrestantes:
    print("se puede formar un triangulo")
else:
    print("no se puede formar un triangulo")