# Hacer un juego donde:
#   salga un número aleatorio cada ronda
#   por cada ronda, se debe adivinar si el número que sale es mayor o menor que el anterior

import random
import time

jugar = True
numero_actual = random.randint(1, 100)


while True:

    numero_siguiente = random.randint(1, 100)

    while True:
        print(f"\nEl número actual es {numero_actual}.")
        print(f"¿El siguiente número será mayor o menor?\n")
        input_usuario = input("MAYOR\nMENOR\n\n").upper()
        if (input_usuario in ("MAYOR", "MENOR")):
            break

    es_mayor = numero_siguiente > numero_actual
    acierto = (input_usuario == "MAYOR" and es_mayor) or (input_usuario == "MENOR" and not es_mayor)

    relacion = "mayor" if es_mayor else "menor"

    if acierto:
        print(f"¡Correcto! El número siguiente ({numero_siguiente}) es {relacion} al actual ({numero_actual})\n")
    else:
        print(f"¡Incorrecto! El número siguiente ({numero_siguiente}) es {relacion} al actual ({numero_actual})\n")


    # VERSIÓN NO DEPURADA
    # if (numero_siguiente > numero_actual):
    #     if (input_usuario == "MAYOR"):
    #         print(f"¡Correcto!\nEl número siguiente ({numero_siguiente}) es mayor al número actual ({numero_actual}).")
    #     elif (input_usuario == "MENOR"):
    #         print(f"¡Incorrecto!\nEl número siguiente ({numero_siguiente}) es mayor al número actual ({numero_actual})")
    # elif (numero_siguiente < numero_actual):
    #     if (input_usuario == "MAYOR"):
    #         print(f"¡Incorrecto!\nEl número siguiente ({numero_siguiente}) es menor al número actual ({numero_actual}).")
    #     elif (input_usuario == "MENOR"):
    #         print(f"¡Correcto!\nEl número siguiente ({numero_siguiente}) es menor al número actual ({numero_actual})")

    numero_actual = numero_siguiente

    seguir_jugando = ""
    while True:
        seguir_jugando = input("\n¿Quiere seguir jugando?\nSÍ\nNO\n\n").upper()
        if seguir_jugando in ("SI", "NO"):
            break

    if (seguir_jugando == "NO"):
        print("¡Gracias por jugar!")
        time.sleep(3)
        break