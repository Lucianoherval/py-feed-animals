class Animal:
    def __init__(self, name: str, consumo_diario: float):
        self.name = name
        self.consumo_diario = consumo_diario

    def comer(self, estoque_comida: float) -> float:
        if estoque_comida > self.consumo_diario:
            estoque_comida -= self.consumo_diario
            print(f"{self.name} comeu {self.consumo_diario}kg de comida.")
        else:
            print(f"{self.name} não tem comida suficiente.")
        return estoque_comida

class Cachorro(Animal):
    def __init__(self, name: str):
        super().__init__(name, consumo_diario=0.5)

    def latir(self):
        print(f"{self.name} fez au au!")

class Gato(Animal):
    def __init__(self, name: str):
        super().__init__(name, consumo_diario=0.2)

    def miar(self):
        print(f"{self.name} fez miau!")
