class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def obter_base(self):
        return self.base

    def obter_altura(self):
        return self.altura
    
    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2*(self.base + self.altura)

    def __str__(self):
        return (f"Retângulo com base= {self.base} e altura = {self.altura}, "
        f"area= {self.calcular_area()} e perimetro= {self.calcular_perimetro()}")

retangulo = retangulo(6,7)

print(f"base do retangulo = {retangulo.obter_base()}")
print(f"altura do retangulo = {retangulo.obter_altura()}")
print(f"area do retangulo = {retangulo.calcular_area()}")
print(f"perimetro do retangulo = {retangulo.calcular_perimetro()}")
print(retangulo)