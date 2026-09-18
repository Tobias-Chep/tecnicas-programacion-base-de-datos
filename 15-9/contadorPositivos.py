intentos = 5
positivos = 0
negativos = 0
ceros = 0

while (intentos > 0):
    numero = float(input("Ingrese un número: "))
    
    # while (isinstance(numero, float) != True):
    #     numero = float(input("Ingrese un número válido: "))
    # NO FUNCIONA
        
    if (numero > 0):
        positivos += 1
    elif (numero < 0):
        negativos += 1
    else:
        ceros += 1
    intentos -= 1

print(f"{positivos} números positivos.\n{negativos} números negativos.\n{ceros} ceros.")