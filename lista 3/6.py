#entrada
escolhausuario = str(input("escolha PAR OU ÍMPAR:"))

numerousuario = int(input("escolha um número inteiro de 1 a 5:"))

import random

numerosorteado = random.randint (1,5)

print("o numero sorteado pela máquina é:",numerosorteado)

soma = numerousuario + numerosorteado
print("a soma dos números é:", soma)

modulo = soma % 2

if (escolhausuario =='par' and modulo == 0):
    print("parabéns, você venceu!")
else:
    print("a máquina venceu!")