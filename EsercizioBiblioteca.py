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
        return f"{self.titolo}-{self.autore}-{self.anno}-{self.genere}-2"

class Saggio(Libro):
    def __init__(self, titolo, autore, anno, tema):
        super().__init__(titolo, autore, anno)
        self.tema = tema
    def __str__(self):
        return f"{self.titolo}, {self.autore}, {self.anno}, {self.tema}"
    def stampaStringa(self):
        return f"{self.titolo}-{self.autore}-{self.anno}-{self.tema}-1"

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
    
    def carica_file(self):
        nomefile = "listalibri.txt"
        with open(nomefile, "r") as file:
            for line in file:
                #print(line.strip()) #metodo strip rimuove a capo alla fine della stringa
                #prendere ogni dato separatamente
                line = line.strip()
                elementi = line.split("-") #divide la stringa in una lista di stringhe in base al carattere indicato
                #elementi = ["Promessi sposi", "Manzoni", 1821, "Racconto"]
                #creo l'oggetto con le stringhe o i dati recuperati dal file
                if int(elementi[4]) == 1: #casting di elementi[4] a int perchè viene letta una stringa
                    libro = Saggio(elementi[0], elementi[1], int(elementi[2]), elementi[3])
                elif elementi[4] == "2":
                    libro = Romanzo(elementi[0], elementi[1], int(elementi[2]), elementi[3])
                #aggiunta libro a lista libri della biblioteca
                self.aggiungi_libro(libro)
#main
#VERSIONE DI BASE
#r1 = Romanzo("Promessi sposi", "Manzoni", 1821, "Racconto")
#s1 = Saggio("Saggio1", "Autore1", 2024, "Psicologia")
#b = Biblioteca()
#b.aggiungi_libro(r1)
#b.aggiungi_libro(s1)
#b.visualizza_libri()
#b.salva_file()
#b.carica_file()

#stampa
#b.visualizza_libri()

#VERSIONE DEFINITIVA
print("caricamento dati...")
b = Biblioteca()
b.carica_file()
print("caricamento dati terminato!")
comando = 1
while comando != 0:
    try: #prova    
        print(f"Benvenuto nella gestione della tua biblioteca!")
        print("Inserisci 1 per inserire un romanzo, 2 un saggio, oppure 3 per visualizzare la lista libri, 4 per salvare la lista libri e 0 per uscire")
        comando = int(input())
        if comando==1:
            titolo = input("Inserisci il titolo: ")
            autore = input("Inserisci l'autore: ")
            anno = int(input("Inserisci l'anno di pubblicazione: "))
            genere = input("Inserisci il genere: ")
            romanzo = Romanzo(titolo, autore, anno, genere)
            b.aggiungi_libro(romanzo)
        elif comando==2:
            aaa = input("Inserisci il titolo: ")
            autore = input("Inserisci l'autore: ")
            anno = int(input("Inserisci l'anno di pubblicazione: "))
            tema = input("Inserisci il tema: ")
            saggio = Saggio(aaa, autore, anno, tema)
            b.aggiungi_libro(saggio)
        elif comando==3:
            b.visualizza_libri()
        elif comando == 4:
            b.salva_file()
        elif comando == 0:
            print("Grazie aver usato il programma, chiusura in corso...")
        else:
            print("Comando non riconosciuto")
    except: #se non va bene esegui questo codice
        print("Ops, qualcosa è andato storto, riprova!")