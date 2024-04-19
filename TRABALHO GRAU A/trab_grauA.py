import random
import os

############  FUNÇÕES ############

#rodar a roleta
def roleta():
    roleta = random.randint(1,6)

#regra do dado
def rolar_dado ():
    dado = random.randint (1,6)

#regra da morte


#regra do desafio matemático


#regra da formatura


#regra dos filhos


#regra do casamento


#regra ficou famoso


#regra divorcio


#regra loteria


#regra da maquina do tempo




############  PROGRAMA PRINCIPAL ############
def main():
    jogador1 = {
        "nome": input("Nome do jogador 1: "),
        "posicao": 0,
        "filhos" : 0,
        "dinheiro" : 0,
        "casado": False,
        "divorciado": False,
        "famoso": False,
        "formado" : False,
        "vivo": True
    }

    jogador2 = {
        "nome": input("Nome do jogador 2: "),
        "posicao": 0,
        "filhos" : 0,
        "dinheiro" : 0,
        "casado": False,
        "divorciado": False,
        "famoso": False,
        "formado" : False,
        "vivo": True
    }
    
    jogadores = [jogador1, jogador2]
    vencedor = None

    while vencedor is None:
        for jogador in jogadores:
            print(f"\nVez de {jogador['nome']}:")
            input("Pressione ENTER para girar a roleta...")
            num_roleta = roleta()
            print(f"Você tirou{num_roleta}")

            jogador ['posicao'] += num_roleta

            if jogador['posicao'] in [1, 3, 10, 17]:
                rolar_dado()
                if dado == 1:
                    jogador["posicao"] += 1
                elif dado == 3:
                    jogador["posicao"] -= 1
                elif dado == 6:
                    print("Você perdeu uma rodada")
            
            print(f"Status de {jogador['nome']}:")
            print(f"Posição: {jogador['posicao']}")
            print(f"Número de filhos: {jogador['filhos']}")
            print(f"Dinheiro: {jogador['dinheiro']}")
            print(f"Casado: {jogador['casado']}")
            print(f"Divorciado: {jogador['divorciado']}")
            print(f"Famoso: {jogador['famoso']}")
            print(f"Formado: {jogador['formado']}")
            print(f"Vivo: {jogador['vivo']}")

               

        





"""posicao_jogador1 = 0
filhos_jogador1 = 0
dinheiro_jogador1 = 0
jogador1Casado = False
jogador1Divorciado = False
jogador1Formado = False
jogador1Famoso = False
jogador1Vivo = True"""