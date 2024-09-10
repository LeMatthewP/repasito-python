numero = input("Introduce un número de tres cifras: ")


if (numero[0] in '0123456789' and 
    numero[1] in '0123456789' and 
    numero[2] in '0123456789'):

    if numero[0] == numero[2]:
        print("El número", numero ,"es capicúa.")
    else:
        print("El número", numero ,"no es capicúa.")
else:
    print("Por favor, introduce un número de exactamente tres cifras y que solo contenga dígitos.")


