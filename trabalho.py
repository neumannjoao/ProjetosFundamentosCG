import csv

# Função para carregar os dados do arquivo CSV
def carregar_dados_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            matriz = list(reader)
        return matriz
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com matriz vazia.")
        return []

# Função para salvar a matriz de volta no arquivo CSV
def salvar_dados_csv(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for linha in matriz:
            writer.writerow(linha)
    print(f"Dados salvos no arquivo '{nome_arquivo}' com sucesso.")

# Função para cadastrar um novo felino na matriz
def CadastrarFelino(matriz):
    nome = input('Digite o Nome do Felino: ')
    sexo = input('Digite o sexo do Felino (M ou F): ')
    idade = input('Digite a idade do Felino: ')
    raca = input('Digite a raça do Felino: ')
    cor = input('Digite a cor predominante do Felino: ')
    castrado = input('O felino é castrado? (S ou N): ')
    data_resgate = input('Digite a data do resgate: [dd/mm/aaaa]')
    adotado = input('O felino foi adotado? (S ou N): ')
    nova_linha = [nome, sexo, idade, raca, cor, castrado, data_resgate, adotado]
    matriz.append(nova_linha)

    print("Novo felino cadastrado com sucesso.")

# Função para alterar o status de um felino na matriz
def alterar_status(matriz):
    while True:
        print("******* Lista de Felinos *******")
        for i, felino in enumerate(matriz):
            print(f"{i + 1}: Nome: {felino[0]}, Idade: {felino[2]}, Raça: {felino[3]}")
        
        escolha = input("Escolha o número do felino que deseja alterar ou '0' para voltar ao menu principal: ")

        try:
            escolha = int(escolha)
            if escolha == 0:
                print("Voltando ao menu principal...")
                return
            elif 1 <= escolha <= len(matriz):
                felino_selecionado = matriz[escolha - 1]
                print("\n******* Informações do Felino Selecionado *******")
                for j, info in enumerate(felino_selecionado):
                    print(f"{j + 1}: {info}")
                
                while True:
                    num_info = input("\nEscolha o número da informação que deseja alterar ou '0' para voltar ao menu anterior: ")
                    try:
                        num_info = int(num_info)
                        if num_info == 0:
                            break
                        elif 1 <= num_info <= len(felino_selecionado):
                            nova_info = input(f"Digite a nova informação para '{felino_selecionado[num_info - 1]}': ")
                            felino_selecionado[num_info - 1] = nova_info
                            print("Informação alterada com sucesso.")
                        else:
                            print("Número de informação inválido.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
            else:
                print("Número de felino inválido. Por favor, digite um número válido para escolher o felino.")
                break
            
# Nome do arquivo CSV
nome_arquivo = 'registros.csv'

# Carregar dados do arquivo CSV para a matriz inicial
matriz = carregar_dados_csv(nome_arquivo)

########################## Código Principal ##########################
while True:  
    print ('******* MENU *******')
    print('1) Cadastrar felino ')
    print('2) Alterar status de felino')
    print('3) Consultar informações sobre felino')
    print('4) Apresentar estatísticas gerais')
    print('5) Filtragem de dados')
    print('6) Salvar')
    print('7) Sair do programa')

    opcaousuario = input("Digite o número da opção que deseja: ")

    if opcaousuario == '1':
        CadastrarFelino(matriz)
    elif opcaousuario == '2':
        alterar_status(matriz)
    #elif opcaousuario == '3':
        #
    #elif opcaousuario == '4':
        #
    #elif opcaousuario == '5':
        #
    elif opcaousuario == '6':
        salvar_dados_csv(nome_arquivo, matriz)
    elif opcaousuario == '7':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, digite uma opção válida")

