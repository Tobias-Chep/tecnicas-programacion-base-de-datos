# 1) Pedir al usuario una cantidad de notas. Contar aprobados y desaprobados.

alumno = 1
aprobados = 0
desaprobados = 0
nota_mas_alta = 0
alumno_nota_alta = 0

while (alumno < 11):

    nota = float(input(f"Ingrese la nota del alumno {alumno} (entre 1 y 10): "))
    
    while (nota > 10 or nota < 1):
        nota = float(input(f"¡Dato incorrecto! Ingrese la nota del alumno {alumno} (entre 1 y 10): "))
    
    if (nota > nota_mas_alta):
        nota_mas_alta = nota
        alumno_nota_alta = alumno
    
    if (nota >= 4):
        aprobados += 1
    else:
        desaprobados += 1
    
    alumno += 1

print(f"ALUMNOS APROBADOS: {aprobados}\nALUMNOS DESAPROBADOS: {desaprobados}\n")
if (alumno_nota_alta != 0):
    print(f"ALUMNO {alumno_nota_alta} TUVO LA NOTA MÄS ALTA: {nota_mas_alta}.")