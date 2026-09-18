filas = 5
columnas = 5
tablero = [["~" for _ in range(columnas)] for _ in range(filas)]
barco = [(2, 0), (2, 1), (2, 2)]

entrada = input("Ingresá fila y columna separadas por espacio (ej.: 2 3): ")
fila_str, columna_str = entrada.split()
fila_disparo = int(fila_str)
columna_disparo = int(columna_str)

if (fila_disparo, columna_disparo) in barco:
    print("¡Impacto!")
    tablero[fila_disparo][columna_disparo] = "X"
else:
    print("Agua...")
    tablero[fila_disparo][columna_disparo] = "O"

for fila_tablero in tablero:
    print(" ".join(fila_tablero))