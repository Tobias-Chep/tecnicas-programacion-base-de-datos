filas = 5
columnas = 5
tablero = [["~" for _ in range(columnas)] for _ in range(filas)]
barcos = [
    [(2, 0), (2, 1), (2, 2)],
    [(0, 4), (1, 4)]
]
impactados = []

while True:
    
    for fila in tablero:
        print(" ".join(fila))

    entrada = input("Ingresá fila y columna separadas por espacio (ej.: 2 3): ")
    fila_str, columna_str = entrada.split()
    fila_disparo = (int(fila_str)) - 1
    columna_disparo = (int(columna_str)) - 1

    impacto = False
    for barco in barcos:
        if (fila_disparo, columna_disparo) in barco:
            impacto = True
            barco.remove((fila_disparo, columna_disparo))
            impactados.append((fila_disparo, columna_disparo))
            break
            
    if impacto:
        print("¡Impacto!")
        tablero[fila_disparo][columna_disparo] = "X"
        if len(barco) == 0:
            print("¡Hundiste un barco!")
    elif ((fila_disparo, columna_disparo) in impactados):
            print("¡Ya disparaste ahí! Probá otro casillero.")
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