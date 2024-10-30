import csv

# Nome do arquivo CSV
filename = 'dados_programacao.csv'

# Lendo o arquivo CSV e exibindo as colunas
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Ler o cabeçalho
    print(f"{header[0]:<10} {'CPU':>5} {'Memória':>10} {'Tempo':>5} {'Linhas':>5}")

    for row in reader:
        linguagem = row[0]
        cpu = float(row[1])
        memoria = float(row[2])
        tempo = int(row[3])
        linhas = int(row[4])

        print(f"{linguagem:<10} {cpu:>5.2f} {memoria:>10.2f} {tempo:>5} {linhas:>5}")
    
    # Reiniciando o leitor do arquivo para calcular as médias e desempenhos
    file.seek(0)
    reader = csv.reader(file)
    header = next(reader)  # Ler o cabeçalho novamente

    soma_cpu = soma_memoria = soma_tempo = soma_linhas = 0
    contador = 0
    desempenhos = {}

    # Variáveis para rastrear a linguagem com o menor número de linhas
    menor_linhas = float('inf')
    linguagem_menor_linhas = ""

    # Função para calcular o desempenho
    def calc_desempenho(cpu, memoria, tempo, linhas):
        return 10**6 / (cpu * 100 + memoria + tempo + linhas)

    # Iterar novamente sobre o arquivo para calcular médias e desempenhos
    for row in reader:
        cpu = float(row[1])
        memoria = float(row[2])
        tempo = int(row[3])
        linhas = int(row[4])

        soma_cpu += cpu
        soma_memoria += memoria
        soma_tempo += tempo
        soma_linhas += linhas

        # Calcular desempenho para cada linguagem
        linguagem = row[0]
        desempenho = calc_desempenho(cpu, memoria, tempo, linhas)
        desempenhos[linguagem] = desempenho


        # Verificar se esta linguagem tem o menor número de linhas
        if linhas < menor_linhas:
            menor_linhas = linhas
            linguagem_menor_linhas = linguagem

        contador += 1

    # Calcular as médias
    media_cpu = soma_cpu / contador
    media_memoria = soma_memoria / contador
    media_tempo = soma_tempo / contador
    media_linhas = soma_linhas / contador

    # Exibir as médias
    print("\nMédia das Métricas:")
    print(f"CPU: {media_cpu:.3f}")
    print(f"Memória: {media_memoria:.3f}")
    print(f"Tempo: {media_tempo:.3f}")
    print(f"Linhas: {media_linhas:.3f}")

    # Exibir os desempenhos calculados para cada linguagem
    print("\nDesempenho das Linguagens:")
    for linguagem, desempenho in desempenhos.items():
        print(f"{linguagem:<10}: {desempenho:.2f}")

    # Encontrar a linguagem com maior desempenho
    melhor_linguagem = max(desempenhos, key=desempenhos.get)
    print(f"\nLinguagem com o melhor desempenho: {melhor_linguagem} ({desempenhos[melhor_linguagem]:.2f})")

    # Exibir a linguagem com o menor número de linhas
    print(f"\nLinguagem com o menor número de linhas: {linguagem_menor_linhas} ({menor_linhas} linhas)")
