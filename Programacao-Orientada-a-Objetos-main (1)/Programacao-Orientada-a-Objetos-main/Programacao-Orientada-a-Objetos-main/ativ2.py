import csv

#leitura do arquivo CSV
with open('registros.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    matriz = list(reader)

def leitura(matriz):
    print("\nLista de pessoas:")
    for idx, pessoa in enumerate(matriz):
        print(f"{idx + 1}: {pessoa[0]}")

    escolha = int(input("Escolha o número da pessoa que deseja consultar: ")) - 1   
    print(f"Nome: {matriz[escolha][0]}")
    print(f"Sexo: {matriz[escolha][1]}")
    print(f"Idade: {matriz[escolha][2]}")
    print(f"Altura: {matriz[escolha][3]}")
    print(f"Peso: {matriz[escolha][4]}")

leitura(matriz)

