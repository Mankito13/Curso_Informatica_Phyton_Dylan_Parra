#punto numero 5
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas_semana = [0] * 7

while True:
    print("\nControl de ventas")
    print("1. Ingresar ventas por día")
    print("2. Imprimir total de ventas")
    print("3. Imprimir promedio de ventas por semana")
    print("4. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 4:
        print("Adiós!")
        break

    elif opcion == 1:
        for i in range(len(dias_semana)):
            ventas_dia = float(input(f"Ingrese las ventas del día {dias_semana[i]}: "))
            ventas_semana[i] += ventas_dia
        print("Ventas ingresadas correctamente")

    elif opcion == 2:
        total_ventas = sum(ventas_semana)
        print(f"El total de ventas de la semana es: ${total_ventas}")

    elif opcion == 3:
        promedio_ventas = sum(ventas_semana) / len(dias_semana)
        print(f"El promedio de ventas por semana es: ${promedio_ventas}")

    else:
        print("Opción inválida. Por favor seleccione una opción del menú.")