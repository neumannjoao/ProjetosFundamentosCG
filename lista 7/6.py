import random

def gerar_matriz_notas(num_alunos):
    matriz = []
    for _ in range(num_alunos):
        nota_a = random.uniform(0.0, 10.0)
        nota_b = random.uniform(0.0, 10.0)
        
        media_unisinos = (nota_a + nota_b) /2
    
        matriz.append ([nota_a, nota_b, media_unisinos])
    
    return matriz

matriz_notas = gerar_matriz_notas(10)

print("Matriz de notas:")
for aluno in matriz_notas:
    print(f'Grau A: {aluno[0]:.2f} | Grau B: {aluno[1]:.2f} |Grau parcial: {aluno[2]:.2f}')