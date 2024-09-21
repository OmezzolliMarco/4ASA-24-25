class Veicolo:
    def __init__(self, marca: str, modello: str):
        self.marca = marca
        self.modello = modello
    def descrizione(self):
        print(f"Veicolo di marca {self.marca} e modello {self.modello}")

class Auto(Veicolo):
    def __init__(self, marca, modello, porte: int):
        super().__init__(marca, modello)
        self.porte = porte
    def descrizione(self):
        super().descrizione()
        print(f"Ho n. {self.porte} porte")

class Moto(Veicolo):
    def __init__(self, marca, modello, tipo: str):
        super().__init__(marca, modello)
        self.tipo = tipo
    def descrizione(self):
        super().descrizione()
        print(f"Sono di tipo {self.tipo}")

a1 = Auto("Mercedes", "G250", 5)
m1 = Moto("Kawasaki", "Ninja", "Sportiva")

a1.descrizione()
print("\n")
m1.descrizione()