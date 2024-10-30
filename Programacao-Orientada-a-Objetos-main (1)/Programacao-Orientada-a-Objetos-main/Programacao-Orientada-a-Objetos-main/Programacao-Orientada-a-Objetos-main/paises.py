class Pais:
    def __init__(self, codigo_iso, nome, dimensao):
        """
        Esse é o **construtor** da classe País.
        Ele é chamado quando criamos um novo país e configura as seguintes informações:
        - código ISO: um código que identifica cada país de forma única (ex: 'BRA' para o Brasil);
        - nome: o nome do país (ex: 'Brasil');
        - dimensão: o tamanho do país em Km² (ex: 8.515.767,049 Km²).
        Também inicializa a população com zero e uma lista vazia de países que fazem fronteira com esse país.
        """
        self.codigo_iso = codigo_iso  # Salva o código ISO do país (como 'BRA')
        self.nome = nome  # Salva o nome do país (como 'Brasil')
        self.dimensao = dimensao  # Salva a dimensão do país (em Km²)
        self.populacao = 0  # Inicializa a população como 0 (será configurada mais tarde)
        self.fronteiras = []  # Inicializa uma lista vazia para armazenar os países que fazem fronteira

    # Método "getter" para o código ISO
    def get_codigo_iso(self):
        """
        Esse método devolve o código ISO do país quando for chamado.
        """
        return self.codigo_iso

    # Método "setter" para o código ISO
    def set_codigo_iso(self, codigo_iso):
        """
        Esse método permite alterar o código ISO do país para um novo valor.
        """
        self.codigo_iso = codigo_iso

    # Método "getter" para o nome
    def get_nome(self):
        """
        Esse método devolve o nome do país quando for chamado.
        """
        return self.nome

    # Método "setter" para o nome
    def set_nome(self, nome):
        """
        Esse método permite alterar o nome do país para um novo valor.
        """
        self.nome = nome

    # Método "getter" para a população
    def get_populacao(self):
        """
        Esse método devolve a população do país quando for chamado.
        """
        return self.populacao

    # Método "setter" para a população
    def set_populacao(self, populacao):
        """
        Esse método permite alterar a população do país para um novo valor.
        """
        self.populacao = populacao

    # Método "getter" para a dimensão
    def get_dimensao(self):
        """
        Esse método devolve a dimensão (tamanho) do país quando for chamado.
        """
        return self.dimensao

    # Método "setter" para a dimensão
    def set_dimensao(self, dimensao):
        """
        Esse método permite alterar a dimensão (tamanho) do país para um novo valor.
        """
        self.dimensao = dimensao

    # Método para verificar se dois países são iguais
    def pais_igual(self, outro_pais):
        """
        Esse método compara dois países com base no código ISO.
        Se os códigos ISO forem iguais, considera-se que são o mesmo país.
        """
        return self.codigo_iso == outro_pais.get_codigo_iso()

    # Método para verificar se dois países fazem fronteira
    def eh_limitrofe(self, outro_pais):
        """
        Esse método verifica se o outro país faz fronteira (limítrofe) com este país.
        Um país faz fronteira se estiver na lista de fronteiras.
        """
        return outro_pais in self.fronteiras

    # Método para calcular a densidade populacional
    def densidade_populacional(self):
        """
        Esse método calcula a densidade populacional do país.
        A densidade é a população dividida pela dimensão (área em Km²).
        """
        if self.dimensao > 0:  # Verifica se a dimensão é maior que 0
            return self.populacao / self.dimensao  # Calcula a densidade populacional
        return 0  # Se a dimensão for 0, a densidade é 0

    # Método para encontrar vizinhos comuns entre dois países
    def vizinhos_comuns(self, outro_pais):
        """
        Esse método devolve uma lista de países que fazem fronteira com ambos os países.
        Ou seja, ele devolve os vizinhos em comum.
        """
        vizinhos_comuns = []
        for pais in self.fronteiras:  # Verifica cada país na lista de fronteiras
            if pais in outro_pais.fronteiras:  # Se o país também faz fronteira com o outro país
                vizinhos_comuns.append(pais)  # Adiciona o país à lista de vizinhos comuns
        return vizinhos_comuns

    # Método para adicionar um país à lista de fronteiras
    def adicionar_fronteira(self, pais_vizinho):
        """
        Esse método adiciona outro país à lista de países que fazem fronteira com este.
        """
        if pais_vizinho not in self.fronteiras and len(self.fronteiras) < 40:
            self.fronteiras.append(pais_vizinho)  # Adiciona o país à lista de fronteiras


class Continente:
    def __init__(self, nome):
        """
        Esse é o **construtor** da classe Continente.
        Ele cria um novo continente com um nome e uma lista vazia para armazenar os países que fazem parte do continente.
        """
        self.nome = nome  # Nome do continente
        self.paises = []  # Lista vazia de países

    # Método para adicionar países ao continente
    def adicionar_pais(self, pais):
        """
        Esse método adiciona um país à lista de países do continente.
        """
        self.paises.append(pais)

    # Método para calcular a dimensão total do continente
    def dimensao_total(self):
        """
        Esse método calcula e devolve o tamanho total do continente.
        Ele soma a dimensão de todos os países que fazem parte do continente.
        """
        total = 0
        for pais in self.paises:
            total += pais.get_dimensao()  # Soma a dimensão de cada país
        return total

    # Método para calcular a população total do continente
    def populacao_total(self):
        """
        Esse método calcula e devolve a população total do continente.
        Ele soma a população de todos os países do continente.
        """
        total = 0
        for pais in self.paises:
            total += pais.get_populacao()  # Soma a população de cada país
        return total

    # Método para calcular a densidade populacional do continente
    def densidade_populacional(self):
        """
        Esse método calcula a densidade populacional do continente.
        A densidade é a população total dividida pela dimensão total.
        """
        dimensao_total = self.dimensao_total()
        if dimensao_total > 0:  # Verifica se a dimensão total é maior que 0
            return self.populacao_total() / dimensao_total  # Calcula a densidade populacional
        return 0

    # Método para encontrar o país com maior população
    def maior_populacao(self):
        """
        Esse método encontra e devolve o país com a maior população no continente.
        """
        if not self.paises:  # Verifica se não há países no continente
            return None
        maior = self.paises[0]  # Assume que o primeiro país tem a maior população
        for pais in self.paises:
            if pais.get_populacao() > maior.get_populacao():
                maior = pais  # Atualiza o país com maior população
        return maior

    # Método para encontrar o país com menor população
    def menor_populacao(self):
        """
        Esse método encontra e devolve o país com a menor população no continente.
        """
        if not self.paises:  # Verifica se não há países no continente
            return None
        menor = self.paises[0]  # Assume que o primeiro país tem a menor população
        for pais in self.paises:
            if pais.get_populacao() < menor.get_populacao():
                menor = pais  # Atualiza o país com menor população
        return menor

    # Método para encontrar o país com maior dimensão territorial
    def maior_dimensao(self):
        """
        Esse método encontra e devolve o país com a maior dimensão (território) no continente.
        """
        if not self.paises:  # Verifica se não há países no continente
            return None
        maior = self.paises[0]  # Assume que o primeiro país tem a maior dimensão
        for pais in self.paises:
            if pais.get_dimensao() > maior.get_dimensao():
                maior = pais  # Atualiza o país com maior dimensão
        return maior

    # Método para encontrar o país com menor dimensão territorial
    def menor_dimensao(self):
        """
        Esse método encontra e devolve o país com a menor dimensão (território) no continente.
        """
        if not self.paises:  # Verifica se não há países no continente
            return None
        menor = self.paises[0]  # Assume que o primeiro país tem a menor dimensão
        for pais in self.paises:
            if pais.get_dimensao() < menor.get_dimensao():
                menor = pais  # Atualiza o país com menor dimensão
        return menor

    # Método para calcular a razão territorial do maior país em relação ao menor
    def razao_territorial(self):
        """
        Esse método devolve a razão (divisão) entre a dimensão do maior país e a do menor país.
        """
        maior = self.maior_dimensao()  # Obtém o país com maior dimensão
        menor = self.menor_dimensao()  # Obtém o país com menor dimensão
        if menor and menor.get_dimensao() > 0:  # Verifica se o menor país tem dimensão maior que 0
            return maior.get_dimensao() / menor.get_dimensao()  # Calcula a razão entre as dimensões
        return 0

#///////////////////////////////////////////CÓDIGO FUNCIONAMENTO///////////////////////////////////////////

# Criando países
brasil = Pais("BRA", "Brasil", 8515767.049)
argentina = Pais("ARG", "Argentina", 2780400)
uruguai = Pais("URY", "Uruguai", 176215)

# Definindo a população
brasil.set_populacao(213000000)  # 213 milhões de habitantes
argentina.set_populacao(45100000)  # 45,1 milhões de habitantes
uruguai.set_populacao(3474000)  # 3,474 milhões de habitantes

# Adicionando fronteiras
brasil.adicionar_fronteira(argentina)
brasil.adicionar_fronteira(uruguai)
argentina.adicionar_fronteira(brasil)
uruguai.adicionar_fronteira(brasil)

# Verificando vizinhos comuns entre Brasil e Argentina
vizinhos_comuns = brasil.vizinhos_comuns(argentina)
print("Vizinhos em comum entre Brasil e Argentina:", [pais.get_nome() for pais in vizinhos_comuns])

# Calculando a densidade populacional do Brasil
densidade_brasil = brasil.densidade_populacional()
print("Densidade populacional do Brasil:", densidade_brasil)


# Criando o continente América do Sul
america_do_sul = Continente("América do Sul")

# Adicionando países ao continente
america_do_sul.adicionar_pais(brasil)
america_do_sul.adicionar_pais(argentina)
america_do_sul.adicionar_pais(uruguai)

# Calculando a dimensão total do continente
dimensao_total = america_do_sul.dimensao_total()
print("Dimensão total da América do Sul:", dimensao_total, "km²")

# Calculando a população total do continente
populacao_total = america_do_sul.populacao_total()
print("População total da América do Sul:", populacao_total)

# Encontrando o país com maior e menor população
pais_maior_populacao = america_do_sul.maior_populacao()
pais_menor_populacao = america_do_sul.menor_populacao()
print("País com maior população:", pais_maior_populacao.get_nome())
print("País com menor população:", pais_menor_populacao.get_nome())

# Calculando a razão territorial entre o maior e menor país
razao_territorial = america_do_sul.razao_territorial()
print("Razão territorial entre maior e menor país:", razao_territorial)

