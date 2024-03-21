#entrada
salario = float(input("insira o seu salário: R$"))

#cálcular 11% sobre o salario
onzeporcento = ((salario * 11) / 100)

#condição
if onzeporcento > 318.20:
    print( "o desconto previdenciário é de R$318.20")
else:
    print("o desconto previdenciário é de R$", onzeporcento)
