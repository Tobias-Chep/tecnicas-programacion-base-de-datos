# Hacer un juego donde:
#   salga un número aleatorio cada ronda
#   por cada ronda, se debe adivinar si el número que sale es mayor o menor que el anterior

import random

seguir_jugando = True
numero_previo = random.randint(1, 100)
numero_siguiente = random.randint(1, 100)

while (seguir_jugando):
    
    print(f"{numero_previo} es el número actual.\n")

    adivinar = input("¿El número siguiente será menor o mayor?\nMayor\nMenor\n").lower()

    print(f"El número siguiente es: {numero_siguiente}.")
    if (adivinar == "menor" and numero_siguiente < numero_previo):
        print("¡Correcto!")
    elif (adivinar == "menor" and numero_siguiente > numero_previo):
        print("Incorrecto.")
    elif (adivinar == "mayor" and numero_siguiente < numero_previo):
        print("Incorrecto.")
    else:
        print("¡Correcto!")

    jugar_de_nuevo = input("\n¿Seguir jugando?\nSI\nNO\n").lower()
    
    numero_previo = numero_siguiente

    if (jugar_de_nuevo == "si"):
        seguir_jugando = True
    elif (jugar_de_nuevo == "no"):
        seguir_jugando = False
        

numero_previo = numero_siguiente
    