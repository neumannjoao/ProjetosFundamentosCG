def numeros_divisiveis (divisor, inicio_intervalo, fim_intervalo):
    print(f"Números divisíveis por {divisor} no intervalo de {inicio_intervalo} à {fim_intervalo}")
    for numero in range (inicio_intervalo, fim_intervalo + 1):
        if numero % divisor == 0:
            print (numero)

def main():
    divisor = int(input("Digite o número divisor: "))
    inicio_intervalo = int(input("Digite o valor inicial do intervalo: "))
    fim_intervalo = int(input('Digite o valor final do intervalo: '))

    print("\nResultados: ")
    numeros_divisiveis(divisor, inicio_intervalo, fim_intervalo)

if __name__ == "__main__":
    main()