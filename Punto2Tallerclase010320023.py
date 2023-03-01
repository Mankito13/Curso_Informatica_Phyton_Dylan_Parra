#punto numero 2
estudiantes = []
def calcular_nota_final(p1, p2, p3):
    nota_final = (p1 + p2 + p3) / 3
    return nota_final

num_aprobados = 0

num_reprobados = 0

suma_notas_finales = 0

num_estudiantes = 0

while True:
    nombre = input("Ingrese el nombre del estudiante: ")

    p1 = float(input("Ingrese la nota de la primer corte: "))
    p2 = float(input("Ingrese la nota de la segundo corte: "))
    p3 = float(input("Ingrese la nota de la tercer corte: "))

    nota_final = calcular_nota_final(p1, p2, p3)

    estudiantes.append({
        "nombre": nombre,
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "nota_final": nota_final
    })

    continuar = input("¿Desea continuar? (si /no ): ")

    if continuar.lower() == "no":
        break

for estudiante in estudiantes:
    nota_final = estudiante["nota_final"]
    suma_notas_finales += nota_final
    num_estudiantes += 1
    if nota_final >= 3.0:
        num_aprobados += 1
    else:
        num_reprobados += 1

promedio_notas_finales = suma_notas_finales / num_estudiantes

print("Resumen:")
print("-" * 20)
print(f"Total estudiantes: {num_estudiantes}")
print(f"Aprobados: {num_aprobados}")
print(f"Reprobados: {num_reprobados}")
print(f"Promedio de notas finales: {promedio_notas_finales:.2f}")