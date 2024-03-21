#entrada
numero = int(input("digite um número inteiro:"))

modulo = numero % 3

if modulo != 0:
    print("o número não é divisível por 3")
else:
    print("O número é divisível por 3")