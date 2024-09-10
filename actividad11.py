edad = int(input("ingrese edad= "))
hemo = int(input("ingrese la hemoglobina= "))


if edad <= 5 and edad >= 1:
    if hemo == 11.5 and hemo < 15:
        print("está en el rango")
    else:
        print("está fuera de rango")


if edad <= 10 and edad >= 5:
    if hemo == 12.6 and hemo < 15.5:
        print("está en el rango")
    else:
        print("está fuera de rango")


if edad <= 15 and edad >= 10:
    if hemo == 13 and hemo < 15.5:
        print("está en el rango")
    else:
        print("está fuera de rango")