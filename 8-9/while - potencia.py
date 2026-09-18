# while

# 1) Usuario ingrese un número y mostrar su tabla de multiplicar hasta el 10.

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ...

multiplicador = 1
tabla = int(input("Ingrese el número del que quiere ver la tabla de multiplicación: "))

while (multiplicador <= 10):
    print(f"{tabla} X {multiplicador} = {tabla * multiplicador}")
    multiplicador += 1

print(f"Finalizada la tabla del {tabla}.")

# 2) Calcular la potencia de un número usando while

base = int(input("Ingrese la base: "))
base2 = base
potencia = int(input("Ingrese la potencia:"))
contador = 1

while (contador < potencia):
    base *= base2
    contador += 1
    
print(f"{base2} elevado a {potencia} es: {base}")