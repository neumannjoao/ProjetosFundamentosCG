#usuario insere as cotações de U$ e E$
dolar= float(input("insira a cotação do Dólar no dia de hoje:"))
euro= float(input("insira a cotação do Euro no dia de hoje:"))

#opções
print("\n//////// Menu: //////////")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

#usuario insere a conversão que deseja fazer e a quantidade
op_usuario=int(input("Insira o número da opção de conversão desejada:"))
quantidade= float(input("insira a quantidade que deseja converter:"))

#calculos

if op_usuario == 1:
    real_p_euro= quantidade*euro
    print("valor em reais é:", real_p_euro)
elif op_usuario == 2:
    real_p_dolar= quantidade*dolar
    print("valor em reais é:", real_p_dolar)
elif op_usuario == 3:
    euro_p_dolar = ((quantidade*euro) * dolar)
    print("valor em Euros é:", euro_p_dolar)
elif op_usuario == 4:
    euro_p_real = (euro/quantidade)
    print("o valor em Euros é:",euro_p_real)
elif op_usuario == 5:
    dolar_p_euro = dolar * euro
    print("o valor em Dólares é:", dolar_p_euro)
elif op_usuario == 6:
    dolar_p_real = dolar / quantidade
    print("o valor em Dólares é:", dolar_p_real)
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")