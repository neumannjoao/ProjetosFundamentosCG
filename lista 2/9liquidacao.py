#comando de entrada
valor = float(input('insira o valor da compra: R$'))

# calcular 15%
desconto = ((valor * 15) /100)

# descontar do valor da compra
print('o valor a ser pago é: R$', valor - desconto)
