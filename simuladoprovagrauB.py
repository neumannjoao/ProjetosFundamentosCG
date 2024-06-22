def corretor_provas():

    gabarito = input("Digite o gabarito da prova (de 'a' a 'f', separadas por espaço):").split()
    respostas = input("Digite as respostas do estudante (de 'a' a 'f', separadas por espaço):").split()
    
    if len(gabarito) != 10 or len(respostas) != 10:
        print("O gabarito e as respostas devem ter 10 questões")
        return
    
    
    acertos=0
    for i in range(10):
        if gabarito[i] == respostas[i]:
            print(f'Questão{i+1}: resposta correta')
            acertos += 1
        else:
            print(f'Questão {i+1}: resposta incorreta, a resposta correta é {gabarito[i]}')
    pontuacao = acertos /10
    print('a pontuação do estudante é', acertos, '/10')

corretor_provas()