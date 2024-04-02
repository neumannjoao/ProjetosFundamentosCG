import sys

#usuário insere se possui algum dependente
possui_dependente = str(input("Insira se possui dependente (S/N):"))

#condições
if possui_dependente == "N":
    print("o valor a ser pago é R$300,00")
    sys. exit()


idade_dependente = int(input("insira a idade do dependente:"))

#condições
if idade_dependente <= 10:
    print("o valor a ser pago é R$400,00")
elif idade_dependente > 10 and idade_dependente <= 30:
    print("o valor a ser pago é R$520,00")
elif idade_dependente > 30 and idade_dependente <= 60:
    print("o valor a ser pago é R$695,00")
elif idade_dependente > 60:
    print("o valor a ser pago é R$780,00")
 