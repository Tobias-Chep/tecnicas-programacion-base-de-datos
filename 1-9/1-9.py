edad = int(input("Ingrese su edad: "))

if (edad < 10):
    print("Estás muy chiquito.")
    
elif (edad >= 10 and edad < 20):
    print("Sos adolescente.")
    
elif (edad >= 20 and edad <30):
    print("Sos joven (todavía).")

elif (edad >= 40 and edad < 45):
    pass

elif (edad >= 45):
    print("Estás viejo :(")
    

nota = int(input("Ingrese nota del alumno: "))

if (nota < 6):
    print("El alumno está desaprobado.")

elif (nota >= 6 and nota <= 8):
    print("La nota del alumno es muy buena.")

elif (nota > 6 and nota <= 8):
    print("La nota es buena.")

else:
    print("La nota es excelente.")