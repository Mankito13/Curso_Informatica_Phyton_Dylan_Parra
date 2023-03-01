#punto numero 3
n = int(input("Ingresa un número para calcular su factorial: "))

pares = 0
impares = 0
acum_pares = 0
acum_impares = 0

factorial = 1
for i in range(1, n+1):
    factorial *= i

for i in range(1, n+1):
    if i % 2 == 0:
        pares += 1
        acum_pares += i
    else:
        impares += 1
        acum_impares += i

print(f"El factorial de {n} es: {factorial}")
print(f"Hay {pares} números pares con valor acumulado de {acum_pares}")
print(f"Hay {impares} números impares con valor acumulado de {acum_impares}")