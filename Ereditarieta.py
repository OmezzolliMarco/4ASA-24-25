#definisco una classe, che diventerà classe padre di quella derivata
class Padre:
    def __init__(self, nome):
        self.nome = nome
    def saluta(self):
        print(f"Ciao, sono {self.nome}")
    
class Figlio(Padre): #in questa riga dichiaro che la classe Figlio eredita da Padre
    def __init__(self, nome, scuola):
        super().__init__(nome) #richiamo il costruttore del padre essendo classe ereditata
        self.scuola = scuola
    def info_scuola(self):
        print(f"Sono iscritto alla scuola {self.scuola}")
    def saluta(self): #override del metodo saluta
        super().saluta()
        print(f"Sono uno studente della scuola {self.scuola}")

p = Padre("Mario") #creo l'istanza di padre
f = Figlio("Carlo", "Scuola Martino Rossi") #creo l'istanza del figlio

f.saluta() #il figlio può usare il metodo del padre
f.info_scuola() #il figlio può usare i suoi metodi
f.saluta() #in questo caso saluto con il metodo che ha eseguito override
#ERRORE!
p.info_scuola() #il metofo info_scuola() non fa parte della classe del padre e non può usarlo

