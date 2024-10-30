import csv

class Veículo:
    def __init__(self, código, fabricante, modelo, ano, cor, motor, preco):
        self.código = código
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.preco = preco
        