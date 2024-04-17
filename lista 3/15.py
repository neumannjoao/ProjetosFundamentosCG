#inserir o valor a ser pago
valor = float(input('insira o valor a ser pago: R$'))

#opções de pagamento
print("Opções de pagamento:")
print("1 - À vista em dinheiro, recebe 15% de desconto")
print("2 - À vista no cartão de crédito, recebe 10% de desconto")
print("3 - Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em três vezes, preço normal de etiqueta mais juros de 10%")

#inserir opção desejada
opção_desejada = int(input("insira a opção desejada:"))

if opção_desejada == 1:
    a_vista = ((valor * 15)/100)
    print('o valor a ser pago é: R$', valor - a_vista)
elif opção_desejada == 2:
    cartao = ((valor * 10)/100)
    print('o valor a ser pago é: R$', valor - cartao)
elif opção_desejada == 3:
    duas_vzs = valor/2
    print('o valor a ser pago é: 2x de R$', duas_vzs)
elif opção_desejada == 4:
    juros = valor * 0.15
    tres_vzs = ((valor/3) + (juros/3))
    print(" o valor a ser pago é: 3x de R$", tres_vzs)
    
