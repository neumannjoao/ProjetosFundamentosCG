#criação de um array ja inicializado com 10 elementos
A=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#armazenar o tamanho do array em uma variavel
tamanhoA= len(A)

print(A)
print('este array possui', tamanhoA, 'elementos')

#imprimir primeiro elemento do array
print('primeiro elemento do array;', A[0]) #os arrays sempre iniciam com 0

#imprimir ultimo elemento do array
print('ultimo elemento do array:', A[tamanhoA - 1])

#imprimir (acessar) um elemento a partir de uma posição(variavel que armazena a posição e não o indice)
pos=5 # esta variavel é pra indicar que queremos a 5ª posição do vetor
print('elemento que está na posição', pos, 'do array:',A[pos-1])