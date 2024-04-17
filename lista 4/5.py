def calcular_verif_aprovacao (n_alunos):
    media_geral = 0

    for i in range (n_alunos):
        grauA = float(input(f"Nota do grau A {i+1}: "))
        grauB = float(inp(f"Nota do grau B {i+1}: "))

    media = (grauA + 2*grauB)/3.0
    
    if media >= 6:
        print("APROVADO")
    else:
        grauC = float(input(f"Nota do grau C {i+1}: "))
        substituir = input("Qual nota deseja substituir? (A/B): ")

        if substituir.upper()== "A":
            media = (grauC + 2*grauB)/3.0
        else:
            media = (grauA + 2*grauC)/3.0

        if media >= 6:
            print("APROVADO")
        else:
            print("REPROVADO")

        media_geral += media
    media_geral /= n_alunos
    print(f"A média geral dos alunos é: {media_geral}")