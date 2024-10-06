class MetodoPagamento:
    def __init__(self, #...):
        #...
    def paga(self, importo):
        print("Questo metodo deve essere implementato nelle classi derivate")

class CartaDiCredito(MetodoPagamento):
    #aggiungere il costruttore

    def paga(self, importo):
        print(f"Pagato {importo} con carta di credito.")

class PayPal(MetodoPagamento):
    def paga(self, importo):
        print(f"Pagato {importo} tramite PayPal.")

#aggiungi un altro metodo di pagamento a tua scelta, esegui l'overrife della funzione paga

def effettua_pagamento(metodo, importo):
    #utilizzando il polimorfismo di tipo completa questa funzione

#crea un ciclo infinito che continua a chiedere all'utente che pagamento vuole 
#effetturare, 1 - carta di credito, 2 - PayPal, 3 - Metodo aggiunto e 0 per uscire.
#Chiedi quindi un importo e richiama il pagamento sull'istanza creata.
#ATTENZIONE, SI POTREBBE OTTIMIZZARE IL CODICE PER CREARE SOLO 3 ISTANZE DEGLI OGGETTI PAGAMENTO E
#RICHIAMARE DI VOLTA IN VOLTA QUELLA CHE SCEGLIE L'UTENTE