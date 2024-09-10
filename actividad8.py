tdef = int(input("Ingrese los tornillos defectuosos= "))
tpro = int(input("Ingrese los tornillos producidos= "))

if tdef > 200 and tpro < 10000:
    print("grado 5")


if tdef < 200 and tpro < 10000:
    print("grado 6")

if tdef > 200 and tpro > 10000:
    print("grado 7")

if tdef < 200 and tpro > 10000:
    print("grado 8")
