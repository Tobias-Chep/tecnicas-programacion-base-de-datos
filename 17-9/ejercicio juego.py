# Hacer un juego donde:
#   salga un número aleatorio cada ronda
#   por cada ronda, se debe adivinar si el número que sale es mayor o menor que el anterior

import random

jugar = True
numero_actual = random.randint(1, 100)


while (jugar):

    input_usuario = ""
    numero_siguiente = random.randint(1, 100)

    while (input_usuario not in ("MAYOR", "MENOR")):
        print(f"\nEl número actual es {numero_actual}.")
        print(f"¿El siguiente número será mayor o menor?\n")
        input_usuario = input("MAYOR\nMENOR\n\n").upper()

    if (numero_siguiente > numero_actual):
        if (input_usuario == "MAYOR"):
            print(f"¡Correcto!\nEl número siguiente ({numero_siguiente}) es mayor al número actual ({numero_actual}).")
        elif (input_usuario == "MENOR"):
            print(f"¡Incorrecto!\nEl número siguiente ({numero_siguiente}) es mayor al número actual ({numero_actual})")
    elif (numero_siguiente < numero_actual):
        if (input_usuario == "MAYOR"):
            print(f"¡Incorrecto!\nEl número siguiente ({numero_siguiente}) es menor al número actual ({numero_actual}).")
        elif (input_usuario == "MENOR"):
            print(f"¡Correcto!\nEl número siguiente ({numero_siguiente}) es menor al número actual ({numero_actual})")

    numero_actual = numero_siguiente

    seguir_jugando = ""
    while (seguir_jugando not in ("SI", "NO")):
        seguir_jugando = input("\n¿Quiere seguir jugando?\nSÍ\nNO\n\n").upper()
    if (seguir_jugando == "SI"):
        jugar
    else:
        break