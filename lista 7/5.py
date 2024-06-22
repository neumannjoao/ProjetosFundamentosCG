import random

def const_matriz(linhas, colunas, minimo, maximo):
    
    matriz=[]
    
    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            linha.append(random.randint(minimo, maximo))
        
        matriz.append(linha)
    
    return matriz

#tamanho da matriz desejada:
linhas = 4
colunas = 6

#intervalo de números aleatórios
minimo = -10
maximo = 10

#gerar matriz
matriz = const_matriz(linhas, colunas, minimo, maximo)

#imprimir matriz
for linha in matriz:
    print(linha)
    
#buscar o menor e o maior numero
menor_numero = float('inf')
maior_numero= float('-inf')
    
for linha in matriz:
    for elemento in linha:
        if elemento < menor_numero:
            menor_numero = elemento
        if elemento > maior_numero:
            maior_numero = elemento

print('Menor número na matriz:', menor_numero)
print('Maior número na matriz: ', maior_numero)