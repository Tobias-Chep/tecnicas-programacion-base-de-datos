# Crear una base de datos llamada “Comics”.
CREATE DATABASE comics;

# Activar el USE
USE comics;

# Crear una tabla llamada “Superheroes” que tenga los siguientes campos:
CREATE TABLE superheroes (
id_superheroe INT PRIMARY KEY,
nombre VARCHAR(50),
universo VARCHAR(50),
poder VARCHAR(50),
año_aparicion INT,
puntuacion DECIMAL(3,1)
);

# Hacer los “inserts” de los datos de cada registro utilizando este modelo:
INSERT INTO superheroes (id_superheroe, nombre, universo, poder, año_aparicion, puntuacion)
VALUES
(1, "Spider-Man", "Marvel", "Sentido arácnido", 1962, 9.5),
(2, "Batman", "DC", "Inteligencia", 1939, 9.8),
(3, "Linterna Verde", "DC", "Anillo Mágico", 1940, 7.9),
(4, "El Increíble Hulk", "Marvel", "Furia monstruosa", 1962, 8.2),
(5, "La Mujer Maravilla", "DC", "Volar y la justicia", 1941, 8.8),
(6, "Deadpool", "Marvel", "Inmortalidad", 1991, 8.5),
(7, "Wolverine", "Marvel", "Regeneración infinita", 1982, 8.3),
(8, "Iron Man", "Marvel", "Robótica de guerra", 1963, 9.4),
(9, "Superman", "DC", "Súper hombre", 1938, 9.9),
(10, "Astroboy", "Tezuka Productions", "Niño androide", 1952, 8.1);

# Realizar las consultas correspondientes para los siguientes puntos:

# a) Mostrar todos los superhéroes.
SELECT * FROM superheroes;

# b) Mostrar solamente el nombre y el universo de cada superhéroe.
SELECT nombre, universo FROM superheroes;

# c) Mostrar todos los superhéroes de Marvel.
SELECT * FROM superheroes WHERE universo = "Marvel";

# d) Mostrar los superhéroes cuya primera aparición fue después del año 1960.
SELECT * FROM superheroes WHERE año_aparicion > 1960;

# e) Mostrar los superhéroes cuya puntuación sea mayor a 9.
SELECT * FROM superheroes WHERE puntuacion > 9;

# f) Buscar superhéroes con una puntuación mayor a 9.5.
SELECT * FROM superheroes WHERE puntuacion > 9.5;

# g) Mostrar los superhéroes del universo DC.
SELECT * FROM superheroes WHERE universo = "DC";

# h) Mostrar los superhéroes cuya primera aparición fue entre 1939 y 1962.
SELECT * FROM superheroes WHERE año_aparicion BETWEEN 1939 AND 1962;

# i) Mostrar los superhéroes cuya puntuación sea menor a 9.
SELECT * FROM superheroes WHERE puntuacion < 9;

# j) Buscar superhéroes cuyo nombre comience con la letra S.
SELECT * FROM superheroes WHERE nombre LIKE "S%";

# k) Mostrar los superhéroes ordenados por año de aparición, desde el más antiguo hasta el más reciente.
SELECT * FROM superheroes ORDER BY año_aparicion;

# l) Mostrar los superhéroes ordenados de mayor a menor puntuación.
SELECT * FROM superheroes ORDER BY puntuacion DESC;

# m) Mostrar los superhéroes ordenados alfabéticamente por nombre.
SELECT * FROM superheroes ORDER BY nombre;

# n) Mostrar los superhéroes cuya puntuación esté entre 9.0 y 9.5.
SELECT * FROM superheroes WHERE puntuacion >= 9.0 AND puntuacion <= 9.5;

# o) Mostrar los superhéroes cuya primera aparición esté entre 1940 y 1960.
SELECT * FROM superheroes WHERE año_aparicion BETWEEN 1940 AND 1960;

# p) Mostrar los superhéroes cuyo nombre termine con la letra n.
SELECT * FROM superheroes WHERE nombre LIKE "%n";

# q) Mostrar los superhéroes cuyo nombre contenga la palabra Man.
SELECT * FROM superheroes WHERE nombre LIKE "%man%";

# r) Mostrar los superhéroes cuyo año de aparición sea 1938, 1939 o 1940.
SELECT * FROM superheroes WHERE año_aparicion IN (1938, 1939, 1940);

# s) Mostrar los superhéroes de Marvel cuya puntuación esté entre 9.0 y 9.5.
SELECT * FROM superheroes WHERE universo = "Marvel" and puntuacion BETWEEN 9.0 AND 9.5;

# t) Mostrar los superhéroes cuyo nombre contenga la letra a y cuya puntuación esté entre 8.5 y 9.5.
SELECT * FROM superheroes WHERE nombre LIKE "%a%" AND puntuacion BETWEEN 8.5 AND 9.5;

# USANDO LAS FUNCIONES SQL NATIVAS
SELECT min(año_aparicion) FROM superheroes;


# APRENDÍ HOY:
# BETWEEN X AND Z : toma "entre" incluyendo los límites
# IN (X, Y, Z) : toma sólo si está en esos casos