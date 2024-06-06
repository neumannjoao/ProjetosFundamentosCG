import random

# Inicializando o vetor com 10 elementos
v = []

# Preenchendo o vetor com números entre 10 e 90
for i in range(10):
    numero_aleatorio = random.randint(10, 90)
    v.append(numero_aleatorio)

print("Vetor gerado:", v)



#b)procurando o número 50
valor_procurado = 50

for i in range(len(v)):
    if v[i] == valor_procurado:
        print("valor encontrado")
    else:
        print("valor não encontrado")
    
#c) ocorrências do número:
ocorrencias = 0
for numero in v:
    if numero == valor_procurado:
        ocorrencias += 1

print(f"o número foi encontrado {ocorrencias} vezes")

#d) média dos valores do vetor
media = sum(v) / len(v)
print("A média dos valores do vetor é:", media)

#e) maior valor
maior_valor = max(v)
print("o maior valor é o:", maior_valor)