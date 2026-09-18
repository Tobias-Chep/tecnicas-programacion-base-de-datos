saldo = 0
opcion = 5

while (opcion != 4):
    print("\n1. Depositar\n2. Retirar\n3. Ver saldo actual\n4. Salir\n")
    
    try:
        opcion = int(input("Ingrese una opción: \n"))

        while (opcion > 4 or opcion <= 0):
            opcion = int(input("\nPor favor ingrese un número válido (1-4): "))
            
        if (opcion == 1):
            saldo += float(input("\nIngrese el monto a depositar: \n"))
        
        if (opcion == 2):
            retiro = float(input("\nIngrese el monto a retirar: "))
            if ((saldo - retiro) < 0):
                print("\nNo puede retirar más de lo que tiene depositado.\n")
            else:
                saldo -= retiro
                print(f"\nSu nuevo saldo es: $ {saldo}\n")
                
        if (opcion == 3):
            print(f"\nSu saldo actual es: $ {saldo}\n")
                
        if (opcion == 4):
            print("\nGracias por utilizar nuestro programa.")
            
    except ValueError:
        print("\nPor favor, sólo ingrese números enteros para las opciones.\n")