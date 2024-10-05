class Animale():
    def __init__(self, nome):
        self.nome = nome
    def fai_suono(self):
        pass

#creo la classe gatto che eredita da Animale
class Gatto(Animale):
    def __init__(self, nome):
        super().__init__(nome)
    def fai_suono(self):    #override della funzione fai_suono()
        print("Il gatto miagola")

#creo la classe cane che eredita da animale
class Cane(Animale):
    def __init__(self, nome):
        super().__init__(nome)
    def fai_suono(self): #override del metodo della classe padre
        print("Il cane abbaia")

#polimorfismo di base
cane = Cane("Pucci")
gatto = Gatto("Perla")

cane.fai_suono()
gatto.fai_suono()

#utilizzando invece un'interfaccia comune e il polimorfismo di tipo
def suonoAnimale(animale: Animale): #posso specificare il tipo dell'argomento
    animale.fai_suono()

#in questo caso la cosa più importante non è il tipo di oggetto
#ma il suo comportamento.

suonoAnimale(gatto)
suonoAnimale(cane)