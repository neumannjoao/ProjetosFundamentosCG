class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario (self):
        self.idade += 1

pessoa1 = Pessoa ("João", 19)

pessoa1.aniversario()
pessoa1.aniversario()
pessoa1.aniversario()

print(f"Idade:{pessoa1.idade}")