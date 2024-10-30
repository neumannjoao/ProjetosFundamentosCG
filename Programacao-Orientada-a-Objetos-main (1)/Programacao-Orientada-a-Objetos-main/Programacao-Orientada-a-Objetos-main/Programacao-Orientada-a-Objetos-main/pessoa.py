# Aqui, estamos criando uma classe chamada Pessoa.
class Pessoa:
    # O __init__ é um método especial chamado de construtor. Ele é chamado quando criamos uma nova Pessoa.
    def __init__(self, nome, sexo, cor_olhos, pai=None, mae=None):
        # Aqui estamos verificando se o sexo é válido. Pode ser 'M' para Masculino ou 'F' para Feminino.
        if sexo not in {'M', 'F'}:
            raise ValueError("Sexo inválido. Use 'M' ou 'F'.")
        # Aqui estamos verificando se a cor dos olhos é válida. Pode ser 'C' para Castanho, 'V' para Verde, ou 'A' para Azul.
        if cor_olhos not in {'C', 'V', 'A'}:
            raise ValueError("Cor dos olhos inválida. Use 'C', 'V' ou 'A'.")
        
        # Aqui estamos guardando o nome, sexo, cor dos olhos, pai e mãe da pessoa.
        self.nome = nome
        self.sexo = sexo
        self.cor_olhos = cor_olhos
        self.pai = pai
        self.mae = mae

    # Este método é usado para mudar o sexo da pessoa.
    def set_sexo(self, sexo):
        # Verifica se o novo sexo é válido e, se for, atualiza o sexo da pessoa.
        if sexo in {'M', 'F'}:
            self.sexo = sexo
        else:
            print("Sexo inválido. Use 'M' ou 'F'.")

    # Este método é usado para mudar a cor dos olhos da pessoa.
    def set_cor_olhos(self, cor_olhos):
        # Verifica se a nova cor dos olhos é válida e, se for, atualiza a cor dos olhos da pessoa.
        if cor_olhos in {'C', 'V', 'A'}:
            self.cor_olhos = cor_olhos
        else:
            print("Cor dos olhos inválida. Use 'C', 'V' ou 'A'.")

    # Este método retorna o nome da pessoa.
    def get_nome(self):
        return self.nome

    # Este método retorna o sexo da pessoa em formato completo, como "Masculino" ou "Feminino".
    def get_sexo_str(self):
        return "Masculino" if self.sexo == 'M' else "Feminino"

    # Este método retorna a cor dos olhos da pessoa em formato completo, como "Castanho", "Verde" ou "Azul".
    def get_cor_olhos_str(self):
        cor_olhos_dict = {'C': 'Castanho', 'V': 'Verde', 'A': 'Azul'}
        return cor_olhos_dict.get(self.cor_olhos, 'Desconhecido')

    # Este método cria um novo filho com base nos pais.
    def gera_pessoa(self, nome, sexo, pai):
        # Só pode criar um novo filho se a pessoa for mãe ('F') e o pai for do sexo masculino ('M').
        if self.sexo == 'F' and pai and pai.sexo == 'M':
            # Determina a cor dos olhos do filho com base nas cores dos olhos dos pais.
            if pai.cor_olhos == 'C' or self.cor_olhos == 'C':
                cor_olhos_filho = 'C'
            elif pai.cor_olhos == 'V' or self.cor_olhos == 'V':
                cor_olhos_filho = 'V'
            else:
                cor_olhos_filho = 'A'
            # Cria e retorna o novo filho.
            return Pessoa(nome, sexo, cor_olhos_filho, pai, self)
        else:
            # Se não puder criar o filho, mostra uma mensagem de erro.
            print("A geração de uma nova pessoa falhou. Verifique o sexo da mãe e do pai.")
            return None

    # Este método imprime todas as informações sobre a pessoa.
    def imprime_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Sexo: {self.get_sexo_str()}")
        print(f"Cor dos olhos: {self.get_cor_olhos_str()}")
        if self.pai:
            print(f"Nome do pai: {self.pai.nome}")
        if self.mae:
            print(f"Nome da mãe: {self.mae.nome}")

    # Método para verificar se duas pessoas são semanticamente iguais
    def sao_iguais(self, outra_pessoa):
        # Duas pessoas são iguais se têm o mesmo nome e a mesma mãe.
        return (self.nome == outra_pessoa.nome) and (self.mae == outra_pessoa.mae)

    # Método para verificar se duas pessoas são irmãs
    def sao_irmas(self, outra_pessoa):
        # Duas pessoas são irmãs se têm a mesma mãe e pais diferentes.
        return (self.mae == outra_pessoa.mae) and (self.pai != outra_pessoa.pai)

    # Método para verificar se uma pessoa é antecessora (pai ou mãe, ou antecessor do pai ou mãe)
    def eh_antecessora(self, outra_pessoa):
        # Função auxiliar para verificar se uma pessoa é antecessora de outra.
        def verifica_antecessor(pessoa):
            if pessoa is None:
                return False
            # Se a pessoa for igual à outra pessoa, é antecessora.
            if pessoa == outra_pessoa:
                return True
            # Verifica se a pessoa é pai ou mãe da outra pessoa ou antecessor dos pais dela.
            return verifica_antecessor(pessoa.pai) or verifica_antecessor(pessoa.mae)
        
        return verifica_antecessor(self)

# Esta é a função principal que mostra como usar a classe Pessoa.
def main():
    # Criando os pais
    pai = Pessoa("João", 'M', 'C')
    mae = Pessoa("Maria", 'F', 'V')

    # Criando filhos
    filho1 = mae.gera_pessoa("Pedro", 'M', pai)
    filho2 = mae.gera_pessoa("Ana", 'F', pai)
    meio_irmao = mae.gera_pessoa("Lucas", 'M', pai)  # Irmão de Pedro e Ana

    # Imprimindo os dados
    print("Dados do pai:")
    pai.imprime_dados()
    print("\nDados da mãe:")
    mae.imprime_dados()
    print("\nDados do filho 1:")
    if filho1:
        filho1.imprime_dados()
    print("\nDados do filho 2:")
    if filho2:
        filho2.imprime_dados()
    
    # Verificando se Pedro e Ana são iguais
    print("\nPedro e Ana são iguais? ", filho1.sao_iguais(filho2))

    # Verificando se Pedro e Ana são irmãs
    print("Pedro e Ana são irmãs? ", filho1.sao_irmas(filho2))
    
    # Verificando se Maria é antecessora de Pedro
    print("Maria é antecessora de Pedro? ", mae.eh_antecessora(filho1))
    # Verificando se João é antecessor de Pedro
    print("João é antecessor de Pedro? ", pai.eh_antecessora(filho1))

# Aqui chamamos a função principal para rodar o programa.
if __name__ == "__main__":
    main()
