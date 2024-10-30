class ContaBancaria:
    def __init__ (self, saldo, titular):
        self.__saldo = float(saldo)
        self.titular = titular

    def depositar(self, valor):
        self.__saldo += float(valor)   
    
    def sacar(self, valor):
        # "se o valor for menor que o saldo"
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular} é de: R${self.__saldo}")

# Corrigindo a ordem dos argumentos: saldo primeiro, titular depois
conta = ContaBancaria(100, "Maria")

conta.depositar(5000)
conta.sacar(1000)

conta.mostrar_saldo()
