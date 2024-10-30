#criar matriz de 4x6
matriz = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    ]

v1 = int(input("Insira o valor da coluna 1 da primeira linha: "))
v2 = int(input("Insira o valor da coluna 2 da primeira linha: "))
v3 = int(input("Insira o valor da coluna 3 da primeira linha: "))
v4 = int(input("Insira o valor da coluna 4 da primeira linha: "))
v5 = int(input("Insira o valor da coluna 5 da primeira linha: "))
v6 = int(input("Insira o valor da coluna 6 da primeira linha: "))

matriz [0] = [v1, v2, v3, v4, v5, v6]

#imprimir
for linha in matriz:
    print (linha)

#B
print("questão B")
matriz [1] = [v6, v5, v4, v3, v2, v1]

for linha in matriz:
    print (linha)

#C
print("questão C")
matriz[2] = [matriz[0][i] + matriz[1][i] for i in range(6)]

for linha in matriz:
    print (linha)

#D
print("questão D")

pares = [x for x in matriz[0] if x %2 == 0]
ímpares = [x for x in matriz[0] if x %2 != 0]

matriz[3] = pares + ímpares

for linha in matriz:
    print (linha)

#E
print("questão E")
transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

for linha in transposta:
    print(linha)