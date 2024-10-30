class Veiculo:
    def __init__(self, ano, peso, tanque, modelo):
        self.ano = int(ano)
        self.peso = int(peso)
        self.tanque = float(tanque)
        self.modelo = str(modelo)

    def setAno(self, ano):
        self.ano = int(ano)

    def setPeso(self, peso):
        self.peso = int(peso)

    def setTanque(self, tanque):
        self.tanque = float(tanque)

    def setModelo(self, modelo):
        self.modelo = str(modelo)
    

    def getAno(self):
        return self.ano
    
    def getPeso(self):
        return self.peso
    
    def getTanque(self):
        return self.tanque
    
    def getModelo(self):
        return self.modelo
    
    def info(self):
        print(f'Ano: {self.ano}')
        print(f'Peso: {self.peso} Kg')
        print(f'Tanque: {self.tanque} L')
        print(f'Modelo: {self.modelo}')

class Terrestre(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qtRoda, qtPorta):
        super().__init__(ano, peso, tanque, modelo)
        self.qtRoda =  int(qtRoda)
        self.qtPorta = int(qtPorta)

    def info(self):
        super().info()
        print(f'Quantidade de Rodas: {self.qtRoda} ')
        print(f'Quantidade de Portas: {self.qtPorta}')

    def consumo(self):
        self.calcConsumo = 1 / ((self.peso * 0.00005) + (self.qtRoda * 0.005))
        print(f'O Consumo do veículo é: {self.calcConsumo:.2f} km/l')
        return self.calcConsumo
        
    def autonomia(self):
        calcAutonomia = self.tanque * self.calcConsumo
        print(f'O Veículo tem autonomia de {calcAutonomia:.2f} km')
        return calcAutonomia
    
class Aereo (Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qtAsa, qtMotor):
        super().__init__(ano, peso, tanque, modelo)
        self.qtAsa =  int(qtAsa)
        self.qtMotor = int(qtMotor)

    def info(self):
        super().info()
        print(f'Quantidade de Asas: {self.qtAsa} ')
        print(f'Quantidade de Motores: {self.qtMotor}')

    def consumo(self):
        self.calcConsumo = 1 / ((self.peso * 0.00003) + (self.qtMotor * 0.01))
        print(f'O Consumo do veículo é: {self.calcConsumo:.2f} km/l')
        return self.calcConsumo
        
    def autonomia(self):
        calcAutonomia = self.tanque * self.calcConsumo
        print(f'O Veículo tem autonomia de {calcAutonomia:.2f} km')
        return calcAutonomia
    
class Aquatico(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qtMotor, qtconves):
        super().__init__(ano, peso, tanque, modelo)
        self.qtMotor =  int(qtMotor)
        self.qtconves = int(qtconves)

    def info(self):
        super().info()
        print(f'Quantidade de Motores: {self.qtMotor} ')
        print(f'Quantidade de Conves: {self.qtconves}')

    def consumo(self):
        self.calcConsumo = 1 / ((self.peso * 0.00002) + (self.qtMotor * 0.02))
        print(f'O Consumo do veículo é: {self.calcConsumo:.2f} km/l')
        return self.calcConsumo
        
    def autonomia(self):
        calcAutonomia = self.tanque * self.calcConsumo
        print(f'O Veículo tem autonomia de {calcAutonomia:.2f} km')
        return calcAutonomia    
    
# Exemplo de uso
meu_carro = Terrestre(2020, 1500, 50, "Fusca", 4, 2)
meu_carro.info()
meu_carro.consumo()
meu_carro.autonomia()

print ('############################################')

meu_aviao = Aereo(2021, 3000, 200, "Boeing", 2, 2)
meu_aviao.info()
meu_aviao.consumo()
meu_aviao.autonomia()

print ('############################################')

meu_bote = Aquatico(2019, 800, 40, "Lancha", 2, 1)
meu_bote.info()
meu_bote.consumo()
meu_bote.autonomia()
