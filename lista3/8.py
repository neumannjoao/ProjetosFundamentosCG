#entrada
preçocompra=float(input("insira o valor do produto: R$"))

#variáeis
quarentaecinco = ((preçocompra * 45) /100)
trintaecinco = ((preçocompra * 35) /100)
vinteecinco = ((preçocompra * 25) /100)

#condições
if preçocompra < 20:
    print("o valor do produto é: R$", preçocompra + quarentaecinco)
elif preçocompra >= 20 and preçocompra < 50:
    print("o valor do produto é: R$", preçocompra + trintaecinco)
elif preçocompra > 50:
    print("o valor do produto é: R$", preçocompra + vinteecinco)