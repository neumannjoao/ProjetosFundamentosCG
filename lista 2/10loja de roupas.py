#comandos de entrada, inserir numero de peças compradas
camisetas = float(input('insira o numero de camisetas compradas:'))
calças = float (input('insira o numero de calças compradas:'))
cintos = float (input('insira o numero de cintos comprados:'))

#calculos
valcam = (camisetas * 25)
valcal = (calças * 100)
valcin = (cintos * 40)

#saída
print("camisetas: R$", valcam)
print('calças: R$', valcal)
print('cintos: R$', valcin)

total = (valcam + valcal + valcin)

print('TOTAL: R$', total)

# calcular 10%
desconto = ((total * 10) /100)

#desconto
print('DESCONTO: R$', - desconto)

# descontar do valor da compra
print('o valor a ser pago é: R$', total - desconto)

