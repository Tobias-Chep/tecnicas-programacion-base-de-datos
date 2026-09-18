sigue = True

while (sigue):
    
    numero1 = float(input("\nIngrese un número: "))
    numero2 = float(input("Ingrese otro número: "))

    print("\nOperaciones:\n")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("\nSeleccione una operación: \n"))
    
    match opcion:
            
        case 1:
            print(f"\n{numero1 + numero2}\n")
        case 2:
            print(f"\n{numero1 - numero2}\n")
        case 3:
            print(f"\n{numero1 * numero2}\n")
        case 4:
            if (numero2 == 0):
                print("\nNo se puede dividir por cero.\n")
            else:
                print(f"\n{numero1 / numero2}\n")
        
    continuar = input("\n¿Quiere realizar otra operación? SI/NO\n").lower()
    if (continuar == "si"):
        sigue = True
    elif (continuar == "no"):
        sigue = False