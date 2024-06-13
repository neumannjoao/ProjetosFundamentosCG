def cifrarMensagem(msg):
    msgCifrada = ''
    for i in range(len(msg)):
        code = ord(msg [i]) - 1
        msgCifrada = msgCifrada + chr(code)
    return msgCifrada

def decifrarMensagem(msg):
    msgDecifrada = ''
    for i in range (len(msg)):
        code = ord(msg[i]) + 1
        msgDecifrada += chr(code) #significa o mesmo que [msgDecifrada = msgDecifrada + chr(code)]
    return msgDecifrada

###################################

msg = input("Digite uma mensagem que você quer decifrar:")

msgCifrada = cifrarMensagem(msg)

print(msgCifrada)

nomeArquivo = input('digite o nome do arquivo: ')

arqSaida = open(nomeArquivo, 'w')

arqSaida.write(msgCifrada)

arqSaida.close()

#ler e decifrar arquivo
nomeArquivo = input('digite o nome do arquivo que quer abrir:')

arqEntrada = open(nomeArquivo, 'r')

mensagemCifrada = arqEntrada.read() #armazena todo o conteudo do arquivo

arqEntrada.close()

mensagemDecifrada = decifrarMensagem(mensagemCifrada)

print(mensagemDecifrada)
