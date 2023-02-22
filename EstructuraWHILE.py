#realizar un programa que la variable sea diferente a cero
#este pidiendo un valo por consola e indicar si el numeor
#digitado es par o impar}

#***Codigo principa de Python***#

num=1
while num!=0:
    print("digite un numero: ")
    num=int(input())
    if num%2==0:
        print("el numero es par")
    else:
        print("el numero es impar")


print("finalizo el programa ")