# 1) Calcular la multiplicación continua de un rango de números indicado por el usuario.
# Número_Inicial
# Número_Final
# Número_Final no puede ser menor que Número_Inicial

# Asigno a numeroInicial y numeroFinal los números que están al principio y al final del rango.
numeroInicial = int(input("Ingrese el número del principio del rango: "))
numeroFinal = int(input("Ingrese el número final del rango: "))

# Si el número inicial es mayor al otro lo invierto con una validación if.
if (numeroInicial > numeroFinal):
    depositoTemporal = numeroInicial
    numeroInicial = numeroFinal
    numeroFinal = depositoTemporal

# Si el número inicial es cero le pido al usuario que lo cambie por otro.
while (numeroInicial == 0):
    print("El número inicial no puede ser 0.")
    numeroInicial = int(input("Ingrese otro número: "))

# Determino el límite superior del rango fijo para usarlo como límite del while.
limiteSuperior = numeroFinal

# Determino el contador como el número inicial para determinar desde dónde empieza el while.
contador = numeroInicial

# Construyo el while con el contador como el número inicial inferior y el número final como límite superior como el número final superior.
while (contador < limiteSuperior):
    numeroFinal *= contador
    contador += 1

# Imprimo el resultado.
print(f"La multiplicación continua entre {numeroInicial} y {limiteSuperior} da como resultado:  {numeroFinal}.")
