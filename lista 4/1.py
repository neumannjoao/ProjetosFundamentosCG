#a) números naturais de 0 a 100
"""for i in range(101):
    print (i)"""

#---------------------------------------------------------------------------------#

#b)números pares de 20 a 50
"""for i in range (20,51):
    if i % 2 ==0:
        print (i)"""

#---------------------------------------------------------------------------------#

#c)Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente
"""for i in range(70, 24, -1):
    print(i)"""

#---------------------------------------------------------------------------------#

#d)Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente.
"""for i in range (95,25,-1):
    if i % 2 !=0:
        print(i)"""

#---------------------------------------------------------------------------------#

#e)Ler 15 números e escrever a soma e a média dos números lidos.
"""soma = 0
media = 0

#### ler 15 números ####
for i in range (15):
    numero = float(input("Digite o {}° número: " .format(i+1)))
    soma += numero

#### calculando media ####
media = soma/15

print("A somados números é:", soma)
print("A média dos números é:", media)"""

#---------------------------------------------------------------------------------#

#f)Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos.
"""numeros_pares= 0
numeros_impares= 0

for i in range (10):
    numero=int(input("Digite o {}° número:" .format(i+1)))
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print("Quantidade de números pares: ", numeros_pares)
print("Quantidade de números ímpares: ", numeros_impares)"""

#---------------------------------------------------------------------------------#

#g) Sortear 20 números inteiros entre -10 e 10...
"""import random

numeros_positivos = 0
numeros_negativos= 0
nulo= 0
for _ in range (20):
    numero = random.randint (-10,10)
    if numero < 0:
        print(numero, "É NEGATIVO")
        numeros_negativos += 1
    elif numero > 0:
        print(numero, "É POSITIVO")
        numeros_positivos += 1
    else:
        print(numero, "É NULO")

print("A quantidade de números positivos é: ", numeros_positivos)
print("A quantidade de números negativos é: ", numeros_negativos)"""

#---------------------------------------------------------------------------------#
#h) Ler n números e imprimir no final a soma dos números lidos
"""soma=0
n = int(input("digite a quantidade de números:"))
for i in range (n):
    numero = float(input("digite o {}° número: ". format (i+1)))
    soma += numero

print("A soma dos {} numeros é: {}".format(n, soma))"""

#---------------------------------------------------------------------------------#

