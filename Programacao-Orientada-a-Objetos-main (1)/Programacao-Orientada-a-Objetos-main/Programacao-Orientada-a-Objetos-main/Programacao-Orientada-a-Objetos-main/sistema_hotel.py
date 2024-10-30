class Hotel:
    def __init__(self, nome, endereco, quartos):
        self.nome = nome
        self.endereco = endereco
        self.quartos = []

    def adicionar_quarto(self, quarto):
        self.quarto.append(quarto)
    
    def verificar_disponibilidade(self, data_entrada, data_saida):
        for quarto in self.quartos:
            if quarto_disponível