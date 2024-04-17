def calcular_media_e_verificar_aprovacao(n_alunos):
    media_geral = 0

    for i in range(n_alunos):
        grau_a = float(input(f"Nota do grau A do aluno {i+1}: "))
        grau_b = float(input(f"Nota do grau B do aluno {i+1}: "))

        media = (grau_a + grau_b) / 2

        if media >= 6:
            print("APROVADO")
        else:
            grau_c = float(input(f"Nota do grau C do aluno {i+1}: "))
            substituir = input("Qual o grau que deve ser substituído (A ou B, maiúsculo ou minúsculo)? ")

            if substituir.upper() == 'A':
                media = (grau_b + grau_c) / 2
            elif substituir.upper() == 'B':
                media = (grau_a + grau_c) / 2

            if media >= 6:
                print("APROVADO")
            else:
                print("REPROVADO")

        media_geral += media

    media_geral /= n_alunos
    print(f"Média geral dos alunos: {media_geral}")

n_alunos = int(input("Quantos alunos da Unisinos serão analisados? "))
calcular_media_e_verificar_aprovacao(n_alunos)
