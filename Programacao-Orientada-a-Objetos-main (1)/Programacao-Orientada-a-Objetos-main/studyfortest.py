class Carro:
    # Construtor da classe Carro
    def __init__(self, marca, ano):
        self.marca = marca  # Atributo público para armazenar a marca do carro
        self.__ano = ano    # Atributo privado para armazenar o ano do carro

    # Método para obter o ano do carro
    def get_ano(self):
        return self.__ano  # Retorna o valor do atributo privado __ano

    # Método para definir o ano do carro com validação
    def set_ano(self, ano):
        if ano < 1886:  # Verifica se o ano é menor que 1886
            print("Ano inválido, insira outro ano")  # Mensagem de erro para ano inválido
        else:
            self.__ano = ano  # Define o valor do atributo privado __ano

    # Método para exibir as informações do carro
    def exibir(self):
        print(f"A marca do carro é {self.marca}.")  # Exibe a marca do carro
        print(f"O ano do carro é {self.get_ano()}.")  # Exibe o ano do carro usando o método get_ano()


class CarroEletrico(Carro):
    # Construtor da classe CarroEletrico que herda de Carro
    def __init__(self, marca, ano, autonomia_bateria):
        super().__init__(marca, ano)  # Chama o construtor da superclasse (Carro)
        self.autonomia_bateria = autonomia_bateria  # Atributo público para armazenar a autonomia da bateria

    # Método para exibir informações do carro elétrico, incluindo autonomia
    def exibir_autonomia(self):
        super().exibir()  # Chama o método exibir da superclasse (Carro)
        print(f"Autonomia de {self.autonomia_bateria} km.")  # Exibe a autonomia da bateria


# Criando objetos da classe Carro
carro1 = Carro("Volks", 2020)  # Instância de um carro comum
carro2 = CarroEletrico("BYD", 2024, 500)  # Instância de um carro elétrico com autonomia de 500 km

# Usando os métodos para exibir informações dos carros
carro1.exibir()  # Exibe informações do carro1
carro2.exibir_autonomia()  # Exibe informações do carro2, incluindo a autonomia
