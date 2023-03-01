#punto numero 4
while True:
    print("\nCalculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))
    if opcion == 5:
        print("Adiós!")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif opcion == 4:
        if num2 == 0:
            print("Error: no se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
    else:
        print("Opción inválida. Por favor seleccione una opción del menú.")