#definizione delle classi
class Libro:
    def __init__(self, titolo: str, autore, anno: int):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

class Romanzo(Libro):
    def __init__(self, titolo, autore, anno, genere):
        super().__init__(titolo, autore, anno)
        self.genere = genere
    #override    
    def __str__(self):
        return f"{self.titolo}, {self.autore}, {self.anno}, {self.genere}"
    #serve solo a generare la stringa che verrà salvata su file
    def stampaStringa(self):
        return f"{self.titolo}-{self.autore}-{self.anno}-{self.genere}"

class Saggio(Libro):
    def __init__(self, titolo, autore, anno, tema):
        super().__init__(titolo, autore, anno)
        self.tema = tema
    def __str__(self):
        return f"{self.titolo}, {self.autore}, {self.anno}, {self.tema}"
    def stampaStringa(self):
        return f"{self.titolo}-{self.autore}-{self.anno}-{self.tema}"

class Biblioteca:
    def __init__(self):
        self.lista_libri = [] #all'inizio lista vuota per accogliere i libri

    def aggiungi_libro(self, libro: Libro):
        self.lista_libri.append(libro)

    def visualizza_libri(self):
        for libro in self.lista_libri:
            print(libro)

    def salva_file(self):
        nomefile = "listalibri.txt"
        with open(nomefile, "w") as file:
            for libro in self.lista_libri:
                stringaLibro = libro.stampaStringa()
                file.write(stringaLibro)
                file.write("\n")

#main

r1 = Romanzo("Promessi sposi", "Manzoni", 1821, "Racconto")
s1 = Saggio("Saggio1", "Autore1", 2024, "Psicologia")
b = Biblioteca()
b.aggiungi_libro(r1)
b.aggiungi_libro(s1)
b.visualizza_libri()
b.salva_file()