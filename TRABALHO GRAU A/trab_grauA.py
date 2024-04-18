import random

# Variáveis de jogador
posJogador1 = 0
posJogador2 = 0
filhosJogador1 = 0
filhosJogador2 = 0
dinheiroJogador1 = 0
dinheiroJogador2 = 0
jogador1Casado = False
jogador1Divorciado = False
jogador1Formado = False
jogador1Famoso = False
jogador1Vivo = True
jogador2Casado = False
jogador2Divorciado = False
jogador2Formado = False
jogador2Famoso = False
jogador2Vivo = True

# Função para girar a roleta
def girar_roleta():
    return random.randint(1, 6)

# Função para mover o jogador
def mover_jogador(jogador, posicao):
    if jogador == 1:
        posicao = posJogador1 + 1
        print(posicao)
    else:
        posJogador2 = posicao

# Função para aplicar as regras da casa
def aplicar_regra(jogador, casa):
    if casa == 1:
        # Regra para a casa 1
        pass
    elif casa == 2:
        # Regra para a casa 2
        pass
    # Continue para todas as casas

# Função principal do jogo
def jogo_da_vida():
    while True:
        # Gira a roleta para o jogador 1
        roleta = girar_roleta()
        # Move o jogador 1
        mover_jogador(1, posJogador1 + roleta)
        # Aplica a regra da casa onde o jogador 1 caiu
        aplicar_regra(1, posJogador1)
        # Verifica se o jogador 1 venceu
        if posJogador1 >= 21:
            print("Jogador 1 venceu!")
            break
        # Gira a roleta para o jogador 2
        roleta = girar_roleta()
        # Move o jogador 2
        mover_jogador(2, posJogador2 + roleta)
        # Aplica a regra da casa onde o jogador 2 caiu
        aplicar_regra(2, posJogador2)
        # Verifica se o jogador 2 venceu
        if posJogador2 >= 21:
            print("Jogador 2 venceu!")
            break

# Inicia o jogo
jogo_da_vida()