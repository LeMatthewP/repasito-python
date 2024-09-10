anio = int(input("Ingrese el anio: "))
peso = int(input("Ingrese el peso: "))

if anio <= 1970:
    if peso <= 2700:
        print("Su peso de categoría es 1 y su tarifa es $11600")
    elif 2700 < peso <= 3800:
        print("Su peso de categoría es 2 y su tarifa es $23200")
    elif peso > 3800:
        print("Su peso de categoría es 3 y su tarifa es $34800")

elif 1971 <= anio <= 1979:
    if peso <= 2700:
        print("Su categoría de peso es 4 y su tarifa es $13000")
    elif 2700 < peso <= 3800:
        print("Su categoría de peso es 5 y su tarifa es $26000")
    elif peso > 3800:
        print("Su categoría de peso es 6 y su tarifa es $39000")

elif anio >= 1980:
    if peso < 3500:
        print("Su categoría de peso es 7 y su tarifa es $12000")
    elif peso >= 3500:
        print("Su categoría de peso es 8 y su tarifa es $46000")