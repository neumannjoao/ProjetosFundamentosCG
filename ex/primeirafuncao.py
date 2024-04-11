#Área com a implementação das funções que o código vai usar

def minhafuncao():
    #comandos que serão executados quando a função minhafuncao for chamada
    print("Olá funções!")

def FuncaoComParametros(p1,p2,p3):
    print("ola funcao com parametros!")
    print("parametro 1:", p1)
    print("parametro 2:", p2)
    print("parametro 3:", p3)

##### PROGRAMA PRINCIPAL #####
print("olá!")

minhafuncao()

FuncaoComParametros(1,2,3)
a = "Joao"
b = int(input("digite un número:"))

FuncaoComParametros(a,b,True)