import csv

class Studente:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def calcola_media(self):
        if self.voti:
            return sum(self.voti) / len(self.voti)
        return 0

    def salva_su_file(self, filename):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.nome, self.cognome, self.matricola, self.calcola_media()])

#creazione delle istanze e chiamata dei metodi
studente1 = Studente("Mario", "Rossi", "12345")
studente1.aggiungi_voto(8)
studente1.aggiungi_voto(7)
studente1.salva_su_file("studenti.csv")