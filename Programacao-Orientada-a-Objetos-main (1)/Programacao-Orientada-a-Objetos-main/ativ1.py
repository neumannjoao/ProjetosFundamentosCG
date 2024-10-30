import csv

#leitura do arquivo CSV
with open('registros.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    matriz = list(reader)

#salvar no CSV
def salvar(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for linha in matriz:
            writer.writerow(linha)

def cadastrarPessoa(matriz):
    nome=input('Digite o nome completo da pessoa: ') 
    sexo=input('Digite o sexo da pessoa (M ou F): ')
    idade=int(input('Digite a idade da pessoa: '))
    altura=float(input('Digite a altura da pessoa (0.00): '))
    peso=float(input('Digite o peso da pessoa (0.00): '))


    nova_pessoa = [nome,sexo,idade,altura,peso]
    matriz.append(nova_pessoa)


cadastrarPessoa(matriz)


salvar('registros.csv', matriz)

print(matriz)
