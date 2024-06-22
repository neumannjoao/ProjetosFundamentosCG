def matriz_identidade(n):
    matriz=[]

    for i in range(n):
        linha = []
        for j in range(n):
            if i ==j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
        
    return matriz

matriz_4x4 = matriz_identidade(4)
for linha in matriz_4x4:
    print(linha)