class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def detalhes(self):
        print(f"Marca:{self.marca}, Ano:{self.ano}")


carro1 = Carro ("Toyota", 2024)
carro2 = Carro ("Honda", 2015)

carro1.detalhes()
carro2.detalhes()
