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
    
# a) soma dos elementos da primeira coluna
soma_primeira_linha = sum(matriz[0])

print('a soma dos elementos da primeira linha é: ', soma_primeira_linha)
    
# b) soma dos elementos da quinta coluna
soma_quinta_coluna = 0
for linha in matriz:
    soma_quinta_coluna += linha[4]
print('a soma dos elementos da quinta coluna é: ', soma_quinta_coluna)

# c) multiplicação dos elementos da primeira linha pelos elementos da quarta linha
multiplicacao = 0
for j in range(colunas):
    multiplicacao += matriz[0][j] * matriz[3][j]
print('a multiplicação dos elementos da primeira linha com os elementos da quarta linha dá: ', multiplicacao)

#d) soma dos elementos das colunas com ídice par:
soma_colunas_pares = 0
for i in range(colunas):
    if i % 2 == 0:
        for j in range(linhas):
            soma_colunas_pares += matriz[j][i]

print('soma dos elementos das colunas com indices pares: ', soma_colunas_pares)

#soma dos elementos das colunas com índice ímpar
soma_colunas_impares = 0
for i in range(colunas):
    if i % 2 != 0:
        for j in range(linhas):
            soma_colunas_impares += matriz[j][i]
            
print('soma dos elementos das colunas com indices ímpares: ', soma_colunas_impares)           
    