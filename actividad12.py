numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))


if numero1 % 2 == 0:

    if numero2 % 3 == 0 or numero2 % 5 == 0:
        print("El primer número" , numero1 , "es par y el segundo número", numero2 ,",es múltiplo de 3 o de 5.")
    else:
        print("El primer número" ,numero1, "es par, pero el segundo número", numero2, "no es múltiplo de 3 ni de 5.")
else:

    if numero1 % 3 == 0 or numero1 % 5 == 0:
        print("El segundo número" ,numero2, "es par y el primer número" ,numero1, "es múltiplo de 3 o de 5.")
    else:
        print("El segundo número" ,numero2, "es par, pero el primer número" ,numero1, "no es múltiplo de 3 ni de 5.")