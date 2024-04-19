import random

def rolar_dado():
    return random.randint(1, 6)

def desafio_matematico():
    print("Mostrar na tela os números primos até 100")
    # Números primos até 100
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print("Números primos até 100:", primos)

    print("Fazer o somatório dos números de 1 até 10:", sum(range(1, 11)))

    print("Imprimir a série de Fibonacci até o décimo elemento:")
    a, b = 0, 1
    for _ in range(10):
        print(a, end=" ")
        a, b = b, a + b
    print()

    print("Calcular a área de um círculo com raio 2.5:", 3.14 * (2.5 ** 2))

    print("Imprimir o fatorial de 5:", 5 * 4 * 3 * 2 * 1)

    print("Imprimir os 8 primeiros números divisíveis por 2 e por 5:")
    divisiveis = [x for x in range(1, 100) if x % 2 == 0 and x % 5 == 0][:8]
    print(divisiveis)

def escolher_curso():
    print("Escolha um curso:")
    print("1 - Direito")
    print("2 - Medicina")
    print("3 - Jogos Digitais")
    print("4 - Segurança da Informação")
    print("5 - Análise e Desenvolvimento de Sistemas")
    print("6 - Economia")

def novo_amor(jogador):
    if jogador["relacionamento"] == "Solteiro":
        jogador["relacionamento"] = "Casado"

def ganhar_na_loteria(jogador, premio):
    premios = {
        1: "Ganha R$ 2,50 no bolão.",
        2: "Ganha R$ 5.000,00.",
        3: "Ganha R$ 50.000,00.",
        4: "Ganha R$ 500.00,00.",
        5: "Ganha R$ 5.000.000,00.",
        6: "Ganha R$ 100.000.00,00."
    }
    jogador["fama"] = premios[premio]

def ficar_famoso(jogador):
    jogador["fama"] = "Ficou famoso!"

def ficar_divorciado(jogador):
    if jogador["relacionamento"] == "Casado":
        jogador["relacionamento"] = "Solteiro"

def casa_20(jogador):
    jogador["posicao"] = 0
    jogador["relacionamento"] = "Solteiro"
    jogador["fama"] = "Desconhecido"
    jogador["filhos"] = 0
    print("Voltou para o início do jogo!")

def main():
    jogador1 = {
        "nome": input("Nome do jogador 1: "),
        "posicao": 0,
        "relacionamento": "Solteiro",
        "fama": "Desconhecido",
        "filhos": 0
    }

    jogador2 = {
        "nome": input("Nome do jogador 2: "),
        "posicao": 0,
        "relacionamento": "Solteiro",
        "fama": "Desconhecido",
        "filhos": 0
    }

    jogadores = [jogador1, jogador2]
    vencedor = None

    while vencedor is None:
        for jogador in jogadores:
            print(f"\nVez de {jogador['nome']}:")
            input("Pressione ENTER para girar a roleta...")
            valor_dado = rolar_dado()
            print(f"Você tirou {valor_dado}.")

            jogador["posicao"] += valor_dado

            if jogador["posicao"] == 2 or jogador["posicao"] == 8 or jogador["posicao"] == 18:
                print("Você morreu e perdeu o jogo!")
                vencedor = next(x for x in jogadores if x != jogador)
                break

            elif jogador["posicao"] == 1 or jogador["posicao"] == 3 or jogador["posicao"] == 10 or jogador["posicao"] == 17:
                if valor_dado == 1:
                    jogador["posicao"] += 1
                elif valor_dado == 3:
                    jogador["posicao"] -= 1
                elif valor_dado == 6:
                    print("Você perdeu uma rodada.")

            elif jogador["posicao"] == 4 or jogador["posicao"] == 11 or jogador["posicao"] == 19:
                desafio_matematico()

            elif jogador["posicao"] == 5:
                escolher_curso()

            elif jogador["posicao"] == 6 or jogador["posicao"] == 9 or jogador["posicao"] == 13:
                dado = random.randint(1, 6)
                if dado == 5:
                    jogador["filhos"] += 2
                else:
                    jogador["filhos"] += 1

            elif jogador["posicao"] == 7:
                jogador["relacionamento"] = "Casado"

            elif jogador["posicao"] == 12:
                novo_amor(jogador)

            elif jogador["posicao"] == 14:
                premio_lot = rolar_dado()
                ganhar_na_loteria(jogador, premio_lot)

            elif jogador["posicao"] == 15:
                ficar_famoso(jogador)

            elif jogador["posicao"] == 16:
                ficar_divorciado(jogador)

            elif jogador["posicao"] == 20:
                casa_20(jogador)

            elif jogador["posicao"] == 21:
                vencedor = jogador
                break

            print(f"Posição de {jogador['nome']}: {jogador['posicao']}")

    print(f"O jogador {vencedor['nome']} venceu o jogo!")

if __name__ == "__main__":
    main()
