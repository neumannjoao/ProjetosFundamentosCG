import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.posicao = 0
        self.relacionamento = "Solteiro"
        self.fama = "Desconhecido"
        self.filhos = 0

    def avancar(self, valor):
        self.posicao += valor

    def voltar(self, valor):
        self.posicao -= valor

    def casar(self):
        self.relacionamento = "Casado"

    def divorciar(self):
        if self.relacionamento == "Casado":
            self.relacionamento = "Solteiro"

    def ganhar_loteria(self, premio):
        if premio == 1:
            self.fama = "Ganhou R$ 2,50 no bolão."
        elif premio == 2:
            self.fama = "Ganhou R$ 5.000,00."
        elif premio == 3:
            self.fama = "Ganhou R$ 50.000,00."
        elif premio == 4:
            self.fama = "Ganhou R$ 500.00,00."
        elif premio == 5:
            self.fama = "Ganhou R$ 5.000.000,00."
        elif premio == 6:
            self.fama = "Ganhou R$ 100.000.00,00."

    def ter_filho(self):
        dado = random.randint(1, 6)
        if dado == 5:
            self.filhos += 2
        else:
            self.filhos += 1


def rolar_dado():
    return random.randint(1, 6)

def desafio_matematico():
    print("Mostrar na tela os números primos até 100")
    # Código para mostrar números primos
    print("Fazer o somatório dos números de 1 até 10:", sum(range(1, 11)))
    print("Imprimir a série de Fibonacci até o décimo elemento")
    # Código para imprimir série de Fibonacci
    print("Calcular a área de um círculo com raio 2.5:", 3.14 * (2.5 ** 2))
    print("Imprimir o fatorial de 5:", 5 * 4 * 3 * 2 * 1)
    print("Imprimir os 8 primeiros números divisíveis por 2 e por 5:")
    # Código para imprimir números divisíveis por 2 e por 5

def escolher_curso():
    print("Escolha um curso:")
    print("1 - Direito")
    print("2 - Medicina")
    print("3 - Jogos Digitais")
    print("4 - Segurança da Informação")
    print("5 - Análise e Desenvolvimento de Sistemas")
    print("6 - Economia")

def main():
    jogador1 = Jogador(input("Nome do jogador 1: "))
    jogador2 = Jogador(input("Nome do jogador 2: "))

    jogadores = [jogador1, jogador2]
    vencedor = None

    while vencedor is None:
        for jogador in jogadores:
            print(f"\nVez de {jogador.nome}:")
            input("Pressione ENTER para rolar o dado...")
            valor_dado = rolar_dado()
            print(f"Você tirou {valor_dado}.")

            jogador.avancar(valor_dado)

            if jogador.posicao == 2 or jogador.posicao == 8 or jogador.posicao == 18:
                print("Você morreu e perdeu o jogo!")
                vencedor = next(x for x in jogadores if x != jogador)
                break

            elif jogador.posicao == 1 or jogador.posicao == 3 or jogador.posicao == 10 or jogador.posicao == 17:
                if valor_dado == 1:
                    jogador.avancar(1)
                elif valor_dado == 3:
                    jogador.voltar(1)
                elif valor_dado == 6:
                    print("Você perdeu uma rodada.")

            elif jogador.posicao == 4 or jogador.posicao == 11 or jogador.posicao == 19:
                desafio_matematico()

            elif jogador.posicao == 5:
                escolher_curso()

            elif jogador.posicao == 6 or jogador.posicao == 9 or jogador.posicao == 13:
                jogador.ter_filho()

            elif jogador.posicao == 7:
                jogador.casar()

            elif jogador.posicao == 12:
                if jogador.relacionamento == "Solteiro":
                    jogador.casar()

            elif jogador.posicao == 14:
                premio_lot = rolar_dado()
                jogador.ganhar_loteria(premio_lot)

            elif jogador.posicao == 15:
                jogador.fama = "Ficou famoso!"

            elif jogador.posicao == 16:
                jogador.divorciar()

            elif jogador.posicao == 20:
                jogador.posicao = 0
                jogador.relacionamento = "Solteiro"
                jogador.fama = "Desconhecido"
                jogador.filhos = 0
                print("Voltou para o início do jogo!")

            elif jogador.posicao == 21:
                vencedor = jogador
                break

            print(f"Posição de {jogador.nome}: {jogador.posicao}")

    print(f"O jogador {vencedor.nome} venceu o jogo!")

if __name__ == "__main__":
    main()
