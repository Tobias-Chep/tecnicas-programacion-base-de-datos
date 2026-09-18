from datetime import datetime

# 1. Configuración del Día de Promoción (Miércoles=2, Jueves=3)
dia_actual_num = datetime.now().weekday()
es_dia_promo = dia_actual_num in [2, 3]

# Obtener nombre del día para el reporte en pantalla
nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
nombre_hoy = nombres_dias[dia_actual_num]

# Inicializamos el contador de compras procesadas
contador_compras = 0

print("====================================================")
print("       SISTEMA DE GESTIÓN DE COBROS ACTIVO          ")
print("====================================================")
print(f"Día actual del sistema: {nombre_hoy}")

# Bucle continuo para registrar múltiples compras sin que se corte el programa
while True:
    contador_compras += 1
    print(f"\n--- PROCESANDO COMPRA #{contador_compras} ---")
    
    # [Entrada de datos]: Monto total de la compra
    monto_compra = float(input("Ingresa el monto total de la compra: $"))
    
    # [Validación de membresía]: Tarjeta de cliente
    respuesta_tarjeta = input("¿Tiene tarjeta de cliente? (sí / no): ").strip().lower()
    tiene_tarjeta = respuesta_tarjeta == "sí" or respuesta_tarjeta == "si"

    # [Política de Descuentos]: Evaluar si es día de promoción (10% o 0%)
    if es_dia_promo:
        porcentaje_desc = "10%"
        descuento = monto_compra * 0.10
        print("📢 ¡SÍ es día de promoción! Se aplicará automáticamente un 10% de descuento.")
    else:
        porcentaje_desc = "0%"
        descuento = 0.0
        print("📅 NO es día de promoción. El descuento aplicado será del 0%.")

    monto_final = monto_compra - descuento

    # [Validación de monto mínimo] usando IF Anidado legible
    print("\n[Estado de Membresía y Monto]")
    if tiene_tarjeta:
        print("💳 Cliente Registrado: Cuenta con tarjeta de cliente.")
        # Un único nivel de anidación para evaluar el monto mínimo de $20,000
        if monto_compra >= 20000:
            print("💰 Validación: El monto es mayor o igual a $20,000. Aplica estatus Premium.")
        else:
            print("📉 Validación: El monto es menor a $20,000.")
    else:
        # Registro como cliente invitado regular si no tiene tarjeta
        print("👤 Estado: El sistema registra al usuario como un cliente invitado regular.")

    # Resumen del Ticket de Cobro con el porcentaje al costado solicitado
    print("\n--- RESUMEN DE COBRO ---")
    print(f"Monto Base:     ${monto_compra:.2f}")
    print(f"Descuento:     -${descuento:.2f} ({porcentaje_desc} aplicado)")
    print(f"Total a Pagar:  ${monto_final:.2f}")
    print("----------------------------------------------------")
    print(f"Total de compras gestionadas en esta sesión: {contador_compras}")

    # Pregunta de control para mantener el bucle activo sin cortar la compilación
    otro_dato = input("\n¿Deseas ingresar otra compra o dato? (sí / no): ").strip().lower()
    if otro_dato == "no":
        print("\n====================================================")
        print(f"🛑 Programa finalizado. Se procesaron {contador_compras} compras en total.")
        print("====================================================")
        break  # Rompe el bucle de forma limpia