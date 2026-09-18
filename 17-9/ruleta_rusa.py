import random as r
import time

jugar_de_nuevo = True

print("""
      ***********************************************************************************************
      ******                                                                                   ******
      ******                         RULETA                                                    ******
      ******                                              RUSA                                 ******
      ******                                                                                   ******
      ***********************************************************************************************""")

while (jugar_de_nuevo == True):

    murio = True
    intento = 7
    bala = r.randint(1, 6)
    
    while (intento != bala):
        tirar = input("\n¿Quiere tirar del gatillo? (SI/NO)\n").upper()
        if (tirar == "SI"):
            intento -= 1
            time.sleep(1)
            if (intento != bala):
                print("Clic.")
                time.sleep(1)
                print("\nAhora probaré yo.")
                intento -= 1
                time.sleep(1.5)
                if (intento != bala):
                    print("Clic.")
                    time.sleep(1)
                    print("Sigo vivo.\n")
                    time.sleep(1)
                else:
                    print("¡BAM!")
                    time.sleep(1)
                    print("Se salvó...")
                    time.sleep(1)
                    print("... por ahora.")
                    time.sleep(1)
                    murio = False
                    break
        elif (tirar == "NO"):
            print("Sobrevivió para morir otro día.")
            murio = False
            break

    if murio:
        time.sleep(1)
        print("¡BAM!\nLamentablemente encontró la bala.")
        
    volver_a_jugar = input("\n¿Jugar de nuevo? SI/NO\n").lower()
    if (volver_a_jugar == "si"):
        jugar_de_nuevo = True
    elif (volver_a_jugar == "no"):
        jugar_de_nuevo = False