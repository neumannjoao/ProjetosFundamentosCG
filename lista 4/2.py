import random

sorteado = random.randint (1,10)

print("A máquina sorteou um número....")

for i in range (3):
    resposta = int(input("tente adivinhar o número: "))
    if resposta < sorteado:
        print("Sua resposta está abaixo do número sorteado!")
    elif resposta > sorteado:
        print ("Sua resposta está acima do número sorteado!")
    else:        
        print ("Parabéns!! \nvocê acertou!")