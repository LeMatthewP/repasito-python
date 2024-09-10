nota1 = int(input("Ingrese la nota 1 del alumno: "))
nota2 = int(input("Ingrese la nota 2 del alumno: "))
nota3 = int(input("Ingrese la nota 3 del alumno: "))
nota4 = int(input("Ingrese la nota 4 del alumno: "))

# Use if para buscar entre las variables si una nota en especifico era menor a la nota evaluada entre las otras
# Use elif en caso del que el if nota 1 no era la nota menor y asi siguiendo
# Use el and para ubicar la nota que sea menor a las demas
# Use el else en caso de que nota 4 sea la menor

if nota1 <= nota2 and nota1 <= nota3 and nota1 <= nota4:
    notamenor = nota1
    print("nota menor:", notamenor)
    promedio = (nota2 + nota3 + nota4) / 3
    print("el promedio del alumno es: ", promedio)
elif nota2 <= nota1 and nota2 <= nota3 and nota2 <= nota4:
    notamenor = nota2
    print("nota menor:", notamenor)
    promedio = (nota1 + nota3 + nota4) / 3
    print("el promedio del alumno es: ", promedio)
elif nota3 <= nota1 and nota3 <= nota2 and nota3 <= nota4:
    notamenor = nota3
    print("nota menor:", notamenor)
    promedio = (nota1 + nota2 + nota4) / 3
    print("el promedio del alumno es: ", promedio)
else:
    notamenor = nota4
    print("nota menor:", notamenor)
    promedio = (nota1 + nota2 + nota3) / 3
    print("el promedio del alumno es: ", promedio)