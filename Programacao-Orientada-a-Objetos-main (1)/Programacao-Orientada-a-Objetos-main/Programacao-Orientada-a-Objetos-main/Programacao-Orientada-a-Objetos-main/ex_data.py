import os

os.system('cls') or None

class Data:
    def __init__ (self, dia, mês, ano):
        self.dia = int(dia)
        self.mês = int(mês)
        self.ano = int (ano)

        if self.ano < 1:
            self.ano = 0
        else:
            self.ano = 0
        if(mês >=1 or mês < 12):
            self.mês = 0
        else:
            self.mês = 0

        if self.mês in [4, 6, 9, 11]:
            if self.dia < 1 or self.dia > 30:
                self.dia = 0
        elif self.mês == 2:
            if(self.ano % 4 ==0 and self.ano % 100 != 0) or (self.ano %400 == 0):
                if self.dia < 1 or self.dia > 29:
                    self.dia = 0
            
            else:
                if self.dia < 1 or self.dia > 28:
                    self.dia = 0

        else:
            if self.dia < 1 or self.dia > 31:
                self.dia = 0
        

    def stringdata(self):
        return "{:02d}/{}/{}".format(self.dia, self.mês, self.ano)

if __name__ == "__main__":
    data = Data (18, 6, 2025)
    print(data.stringdata())
    
