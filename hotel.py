
#esercizio per casa su Hotel e prenotazioni
class Prenotazione:
    def __init__(self, nome, numero_stanza, durata):
        self.nome = nome
        self.numero_stanza = numero_stanza
        self.durata = durata
    def stampaPrenotazione(self):
        print(f"...")
    def __str__(self):
        return f"..."
    
class PrenotazioneStandard(Prenotazione):
    def __init__(self, nome, numero_stanza, durata, extra:str):
        super().__init__(nome, numero_stanza, durata)
        self.extra = extra
    def stampaPrenotazione(self):
        super().stampaPrenotazione()
        print(f"{self.extra}")
    def __str__(self):
        return super().__str__() + f", {self.extra}"
        

class PrenotazioneSuite(Prenotazione):
    def __init__(self, nome, numero_stanza, durata, extra:list):
        super().__init__(nome, numero_stanza, durata)
        self.extra = extra
    def stampaPrenotazione(self):
        super().stampaPrenotazione()
        print(f"{self.extra}")
    
class Hotel:
    def __init__(self):
        self.camere = []
        self.prenotazioni = []
    def aggiungiPrenotazione(self, prenotazione:Prenotazione):
        self.prenotazioni.append(prenotazione)
    def aggiungiCamera(self, camera:int):
        self.camere.append(camera)

p = PrenotazioneStandard("Ciccio", 3, 5, 1)
print(p)

hotel = Hotel()
hotel.camere.append(1)

hotel.prenotazioni.append(p)