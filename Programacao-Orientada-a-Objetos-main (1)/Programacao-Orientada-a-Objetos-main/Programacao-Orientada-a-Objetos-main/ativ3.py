import csv

#leitura do arquivo CSV
with open('registros.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    matriz = list(reader)

#salvar no CSV
def salvar(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for linha in matriz:
            writer.writerow(linha)

class Pessoa:
    def __init__(self, nome, sexo, idade, altura, peso):
        if sexo not in {'M', 'F'}:
            raise ValueError("Sexo inválido. Use 'M' ou 'F'.")
        
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._altura = altura
        self._peso = peso


#GETTERS
    def get_nome(self):
        return self._nome
    
    def get_sexo(self):
        return self._sexo
    
    def get_idade(self):
        return self._idade
    
    def get_altura(self):
        return self._altura
    
    def get_peso(self):
        return self._peso
    
#SETTERS
    def set_nome(self, nome):
        self._nome = nome

    def set_sexo(self, sexo):
        self._sexo= sexo

    def set_idade(self, idade):
        self._idade = idade

    def set_altura (self, altura):
        self._altura = altura
    
    def set_peso(self,peso):
        self._peso= peso


    def visualizar(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Sexo: {self.get_sexo()}")
        print(f"Idade: {self.get_idade()}")
        print(f"Altura: {self.get_altura()}")
        print(f"Peso: {self.get_peso()}")

pessoa = Pessoa("João da Silva", "M", 30, 1.75, 70.5)
pessoa.visualizar()
