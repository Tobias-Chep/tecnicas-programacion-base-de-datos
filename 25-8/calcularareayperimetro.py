# 1. Pedir al usuario el diámetro del círculo
diametro = float(input("Ingresá el diámetro del círculo: "))

# 2. Forzar el radio a ser 6 para el área
radio = 6

# 3. Definir el valor de PI solicitado
pi = 3.14

# 4. Calcular el área usando pow()
area = pi * pow(radio, 2)

# 5. Calcular el perímetro usando el diámetro ingresado
perimetro = diametro * pi

# 6. Mostrar todos los resultados
print(f"Diámetro ingresado: {diametro}")
print(f"Radio utilizado para el área: {radio}")
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")