class País:
    def __init__ (self, iso, nome, populacao, dimensao):
        self._iso = iso
        self._nome = nome
        self._populacao = populacao
        self._dimensao = dimensao
        self._fronteiras = []

    #Getter para código ISO
    @property
    def iso(self):
        return self._iso
    
    #Setter para código ISO
    @iso.setter
    def iso(self, valor):
        self._iso = valor



    
    #Getter para nome
    @property
    def nome(self):
        return self._nome
    
    #Setter para nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor



    
    #Getter para populacao
    @property
    def populacao(self):
        return self._populacao
    
    #Setter para populacao
    @populacao.setter
    def populacao(self, valor):
        self._populacao = valor





    #Getter para dimensao   
    @property
    def dimensao(self):
        return self._dimensao
    
    #Setter para dimensao
    @dimensao.setter
    def dimensao(self, valor):
        self._dimensao= valor


#método para verificar países iguais
        def verificarDuplicidade(self, outro_pais):
            return (self._iso == outro_pais._iso)
        print("\nOs países são iguais? ", pais1.verificarDuplicidade(pais2))

        

#método para imprimir todas informações
    def exibir_infos (self):
        print(f"Código ISO: {self._iso}")
        print(f"Nome: {self._nome}")
        print(f"Dimensão: {self._dimensao} Km²")
        #print(f"O país {self._nome} faz fronteira com: {self._fronteiras}")

#metodo para calcular densidade populacional
        def densidade(self, populacao, dimensao):
            densidade_populacional = populacao/dimensao
            print("A densidade populacional é de {densidade_populacional}")





pais1 = País("BRA", "Brasil", 52, 100)
pais2 = País("EUA", "ESTADOS UNIDOS DA AMERICA", 52, 100)

pais1.exibir_infos()
pais2.exibir_infos()

pais1.densidade()
