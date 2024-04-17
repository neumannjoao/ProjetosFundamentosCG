def tabuada (numero):
    print(f"Tabuada de multiplicação do {numero}:")
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x  {i} = {resultado}")
def main():
    while True:
        numero = int(input("Digite um número de 1 a 9: "))
        if numero < 1 or numero > 9:
            print("Número inválido. Por favor, digite um número de 1 a 9.")
        else:
            tabuada (numero)
        
        continuar = input("Calcular outro número? (s/n): ").lower()
        if continuar != 's':
            break
if __name__ == "__main__":
    main()