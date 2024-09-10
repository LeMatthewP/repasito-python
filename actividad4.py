numero = input("Introduce un número de tres cifras: ")


if (numero[0] in '0123456789' and 
    numero[1] in '0123456789' and 
    numero[2] in '0123456789'):

    
    if numero[0] < numero[1] < numero[2]:
        print("el numero", numero, "está ordenado de menor a mayor")
    else:
        print("el numero", numero, "no está ordenado de menor a mayor")
