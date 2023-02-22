# desarrollar un programa que permita seleccionar por consola una opcion
# y se muestre una lista de opciones (menu)

#****** codigo principal de python******#
while True:
    print("digite la letra 'A' para Actualizar Sistema")
    print("digite la letra 'E' para Eliminar Catalogo")
    print("digite la letra 'C' para Crear Productos")
    print("digite la letra 'S' para Salir del Programa")
    letra=str(input())
    if letra== 'A' or letra== 'a':
        print("se actualizo el sistema \n")
        
    if letra== 'E' or letra== 'e':
        print("se elimino el catalogo \n")
        
    if letra== 'C' or letra== 'c':
        print("se creo un producto \n")

    if letra== 'S' or letra== 's':
        print("finalizo con exito \n")
        break
    else:
        print("sigue dentro del proceso de DO WHILE \n")



print("El DO WHILE a finalizado \n")
