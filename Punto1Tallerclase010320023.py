#punto numero 1
import math

def calcular_triangulo():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    lado1 = float(input("Introduce el primer lado del triángulo: "))
    lado2 = float(input("Introduce el segundo lado del triángulo: "))
    area = (base * altura) / 2
    perimetro = base + lado1 + lado2
    print("El área del triángulo es:", area)
    print("El perímetro del triángulo es:", perimetro)

def calcular_cuadrado():
    lado = float(input("Introduce el lado del cuadrado: "))
    area = lado ** 2
    perimetro = lado * 4
    print("El área del cuadrado es:", area)
    print("El perímetro del cuadrado es:", perimetro)

def calcular_circunferencia():
    radio = float(input("Introduce el radio de la circunferencia: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print("El área de la circunferencia es:", area)
    print("El perímetro de la circunferencia es:", perimetro)

while True:
    print("Selecciona una opción: \n1. Calcular el área y perímetro de un triángulo \n2. Calcular el área y perímetro de un cuadrado"+
    "\n3. Calcular el área y perímetro de una circunferencia \n4. Salir")    
    opcion = int(input("Introduce el número de la opción: "))
    if opcion == 1:
        calcular_triangulo()
    elif opcion == 2:
        calcular_cuadrado()
    elif opcion == 3:
        calcular_circunferencia()
    elif opcion == 4:
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")