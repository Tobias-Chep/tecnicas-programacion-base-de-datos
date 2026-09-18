# Realizar un programa que:
# -- pida al usuario una cantidad de productos
# -- pida un precio unitario
# -- aplique un descuento del 20% al total

cantidadProductos = int(input("Ingrese la cantidad de productos: "))

precioUnitario = float(input("Ingrese el precio unitario del producto: "))

subTotal = cantidadProductos * precioUnitario

descuento = subTotal * 0.20

precioFinal = subTotal - descuento

print("Cantidad de productos:", cantidadProductos, "\nPrecio unitario:", precioUnitario, "\nPrecio total sin descuento:", subTotal, "\nPrecio final con descuento:", precioFinal, "\nDescuento:", descuento)