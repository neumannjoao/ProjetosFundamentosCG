class Pessoa:
    def __init__(self, nome, sexo, idade, altura, peso):
        if sexo not in {'M', 'F'}:
            raise ValueError("Sexo inválido. Use 'M' ou 'F'.")
        
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.altura = altura
        self.peso = peso

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        self._sexo = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        self._peso = valor

    def visualizar(self):
        print(f"Nome: {self.nome}")
        print(f"Sexo: {self.sexo}")
        print(f"Idade: {self.idade}")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} Kg")

# Exemplo de uso
pessoa1 = Pessoa("João", "M", 19, 1.90, 90)
pessoa1.visualizar()
