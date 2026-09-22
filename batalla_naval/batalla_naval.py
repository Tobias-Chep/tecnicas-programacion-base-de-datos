filas = 5
columnas = 5
tablero = [["~" for _ in range(columnas)] for _ in range(filas)]
barcos = [
    [(2, 0), (2, 1), (2, 2)],
    [(0, 4), (1, 4)]
]
disparos_realizados = []

while True:
    
    for fila in tablero:
        print(" ".join(fila))

    while True: # While de verificación de entrada

        try:
            entrada = input("Ingresá fila y columna separadas por espacio (ej.: A 3): ")
            partes = entrada.split()
            if len(partes) != 2:
                print("Tenés que ingresar dos valores separados por un espacio.")
                continue

            fila_str, columna_str = partes

            fila_disparo = (ord(fila_str.upper())) - ord("A")
            columna_disparo = (int(columna_str)) - 1
        except (ValueError, TypeError):
            print("Ingrese datos válidos (letra y número)")
            continue

        if (fila_disparo < 0 or fila_disparo >= filas):
            print("Esa fila no existe en el tablero.")
            continue

        if (columna_disparo < 0 or columna_disparo >= columnas):
            print("Esa columna no existe en el tablero.")
            continue
        
        break

    if ((fila_disparo, columna_disparo) in disparos_realizados):
        print("¡Ya disparaste ahí! Probá otro casillero.")
        continue
    disparos_realizados.append((fila_disparo, columna_disparo))

        

    impacto = False
    for barco in barcos:
        if (fila_disparo, columna_disparo) in barco:
            impacto = True
            barco.remove((fila_disparo, columna_disparo))
            break
            
    if impacto:
        print("¡Impacto!")
        tablero[fila_disparo][columna_disparo] = "X"
        if len(barco) == 0:
            print("¡Hundiste un barco!")
    else:
        print("Agua...")
        tablero[fila_disparo][columna_disparo] = "O"

    barcos_restantes = [b for b in barcos if len(b) > 0]
    print(len(barcos_restantes))
    if len(barcos_restantes) == 0:
        for fila in tablero:
                print(" ".join(fila))
        print("¡Ganaste, hundiste toda la flota!")
        break