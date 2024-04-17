opcao ='' #palavra vazia
while opcao != 'C':
print('Menu')
print('A - fazer tarefa A')
print('B - fazer tarefa B')
print('C - sair do programa')
opcao = input('Digite uma opção')
if (opcao != 'A' and opcao != 'B' and opcao != 'C'):
print('Opção inválida!')    