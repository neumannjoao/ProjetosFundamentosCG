#comando de entrada
dividendo=float(input("digite o número que será o dividendo:"))
divisor=float(input("digite o número que será o divisor:"))

#mensagem de erro
if divisor == 0:
    print("O divisor deve ser diferente de zero")
else:
    resultado = dividendo / divisor
    print("o resultado da divisão é:", resultado)
