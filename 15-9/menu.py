import random

opcion = 99

while (opcion != 0):
    print(f"1. Saludar \n2. Decir Adiós\n3. Mostrar un número aleatorio\n0. Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if (opcion == 1):
        nombre = input("Ingrese nombre: ")
        print(f"Hola {nombre}, ¿cómo estás?\n")
    
    if(opcion == 2):
        nombre = input("Ingrese nombre: ")
        print(f"Adiós {nombre}, nos vemos pronto.\n")
    
    if(opcion == 3):
        print(f"{random.randint(-99, 99)}\n")
    
    if(opcion == 0):
        print("Saliendo del programa.")