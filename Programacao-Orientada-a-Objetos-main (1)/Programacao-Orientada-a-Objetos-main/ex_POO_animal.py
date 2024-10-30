class Animal:
    def falar(self):
        print("animal falando")

class Cachorro(Animal):
    def falar (self):
        print("O cachorro late")

animal = Animal()
cachorro = Cachorro()

animal.falar()
cachorro.falar()
