#apresentar a pergunta e opções
print('QUAL É O VERDADEIRO NOME DO BATMAN?')
print('a) Bruce Wayne')
print('b) Clark Kent')
print('c) Peter Parker')
print('d) Tony Stark')
print('e) Steve Rogers')

#variavel correta
respostacorreta='a) Bruce Wayne'

#usuario insere a resposta
respostadousuario=str(input('insira a alternativa correta:'))

#resposta correta
if respostadousuario =='a' : print('Sua resposta está correta')
else:
    print('Sua resposta está incoreta. Tente novamente!')

#print('Você digitou a resposta', respostadousuario,'. A resposta correta é', respostacorreta)

