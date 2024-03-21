#entrada
A=float(input("Digite o primeiro número:"))
B=float(input("Digite o segundo número:"))
C=float(input("Digite o terceiro número:"))

#soma de A+B
AB = A + B

#soma de A+C
AC = A + C

#Resultados
print("A soma de", A,'+', B, 'é igual a:', AB)
print("A soma de", A,'+', C, 'é igual a:', AC)

#CONDIÇÃO
if AB < AC:
    print(AB, "é menor que", AC)
else:
    print(AB, "é maior que", AC)