def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 1]
    resultado = {}
    if valor >= 100:
        resultado[100] = valor // 100
        valor %= 100
    if valor >= 50:
        resultado[50] = valor // 50
        valor %= 50
    if valor >= 20:
        resultado[20] = valor // 20
        valor %= 20
    if valor >= 10:
        resultado[10] = valor // 10
        valor %= 10
    if valor >= 5:
        resultado[5] = valor // 5
        valor %= 5
    if valor >= 1:
        resultado[1] = valor
    return resultado

def exibir_resultado(resultado):
    for cedula, quantidade in resultado.items():
        print(f"{quantidade} nota(s) de R${cedula}.")

def main():
    valor = int(input("Informe o valor desejado: "))
    resultado = calcular_cedulas(valor)
    exibir_resultado(resultado)

if __name__ == "__main__":
    main()
