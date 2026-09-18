# 2) Pedir al usuario su nombre de usuario y contraseña
# Validar que la contraseña sea correcta
# Tiene 3 intentos para corregirla

# Definimos y asignamos las variables de usuario, contraseña y preparamos los intentos en cero
usuario = "Pepe"
contrasenia = "1234"
intentos = 0

# While con máximo de intentos de 3 (de 0 a 2)
while (intentos < 3):
    # Petición de usuario y contraseña
    usuarioPeticion = input("Ingrese su nombre de usuario: ")
    contraseniaPeticion = input("Ingrese su contraseña: ")
    # condicional para ver si el usuario o contraseña son incorrectos. de serlo, se notifica al usuario e intentos aumenta en 1 (si se llega a 3 se sale del ciclo while)
    if (usuario != usuarioPeticion or contrasenia != contraseniaPeticion):
        intentos += 1
        print(f"Algún dato es incorrecto. {intentos} de 3 intentos.")
    # si ambos datos son iguales a los hardcodeados, se imprime que están correctos y se sale del ciclo while con un break
    else:
        print("Ha ingresado correctamente.")
        break

# si los intentos son mayores o iguales a 3 se notifica al usuario que se gastaron los tres intentos
if (intentos >= 3):
    print("Ya utilizó los tres intentos. Espere un momento para volver a intentar.")