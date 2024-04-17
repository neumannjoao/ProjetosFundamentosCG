import random

#opções
print("\n//////// Menu: //////////")
print("1) Dado de 4 lados;")
print("2) Dado de 6 lados;")
print("3) Dado de 8 lados;")
print("4) Dado de 12 lados;")
print("5) Dado de 16 lados;")

#usuário insere o número de faces
numero_faces = int(input("Insira a opção desejada:"))

#condições
if numero_faces == 1:
    quatro_lados = random.randint (1,4)
    print("o número sorteado foi:", quatro_lados)
elif numero_faces  == 2:
    seis_lados = random.randint (1,6)
    print  ("o número sorteado foi:", seis_lados)
elif numero_faces == 3:
    oito_lados = random.randint (1,8)
    print ("o número sorteado foi:", oito_lados)
elif numero_faces == 4:
    doze_lados = random.randint (1,12)
    print ("o número sorteado foi:", doze_lados)
elif numero_faces == 5:
    dezesseis_lados = random.randint (1,16)
    print ("o número sorteado foi:", dezesseis_lados)
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")


