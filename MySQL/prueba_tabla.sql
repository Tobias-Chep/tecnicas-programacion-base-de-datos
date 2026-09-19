CREATE DATABASE alumnos;

USE alumnos;

CREATE TABLE alumnos (
id_alumnos INT PRIMARY KEY,
nombre VARCHAR(100),
fecha_nac DATE,
direccion VARCHAR(250),
activo BOOLEAN
);

SELECT * FROM alumnos;

INSERT INTO alumnos
VALUES (1, "Tomás", "2000-11-02", "Calle Falsa 123", True);

INSERT INTO alumnos
VALUES (2, "Calle Falsa 123", "2001-04-14", "Pedro", False);

DELETE FROM alumnos WHERE id_alumnos = 2;