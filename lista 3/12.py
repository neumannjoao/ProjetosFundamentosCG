#usuario insere a idade do nadador
idade_nadador = int(input('insira a idade do nadador:'))

#conições
if idade_nadador >=5 and idade_nadador <= 7:
    print("a categoria do nadador é: Infantil A")
elif idade_nadador >= 8 and idade_nadador <=10:
    print("a categoria do nadador é: Infantil B")
elif idade_nadador >= 11 and idade_nadador <= 13:
    print("a categoria do nadador é: Juvenil A")
elif idade_nadador >= 14 and idade_nadador <= 17:
    print ("a categoria do nadador é: Juvenil B")
elif idade_nadador >= 18:
    print("a categoria do nadador é: Sênior")
    