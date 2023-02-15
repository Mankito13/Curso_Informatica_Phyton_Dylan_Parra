print("Digite un numero entero y positivo")
Numero= int(input())
i=0
SumaPar=0
SumaImpar=0
while Numero!=i:
    i=i+1
    if i % 2 == 0:
        SumaPar=SumaPar+i
    else:
        SumaImpar=SumaImpar+i
print("La sumatoria de los IMmpares es: "+str(SumaImpar))
print("La sumatoria de los pares es: "+str(SumaPar))