class MetodoPagamento:
    def __init__(self, nome):
        self.nome = nome
    def paga(self, importo):
        print("Questo metodo deve essere implementato nelle classi derivate")

class CartaDiCredito(MetodoPagamento):
    #aggiungere il costruttore
    def __init__(self, nome):
        super().__init__(nome)
    def paga(self, importo):
        print(f"Pagato {importo} con carta di credito.")

class PayPal(MetodoPagamento):
    def __init__(self, nome):
        super().__init__(nome)
    def paga(self, importo):
        print(f"Pagato {importo} tramite PayPal.")

#aggiungi un altro metodo di pagamento a tua scelta, esegui l'overrife della funzione paga

def effettua_pagamento(metodo: MetodoPagamento, importo):
    #utilizzando il polimorfismo di tipo completa questa funzione
    metodo.paga(importo)

#crea un ciclo infinito che continua a chiedere all'utente che pagamento vuole 
#effetturare, 1 - carta di credito, 2 - PayPal, 3 - Metodo aggiunto e 0 per uscire.
#Chiedi quindi un importo e richiama il pagamento sull'istanza creata.
#ATTENZIONE, SI POTREBBE OTTIMIZZARE IL CODICE PER CREARE SOLO 3 ISTANZE DEGLI OGGETTI PAGAMENTO E
#RICHIAMARE DI VOLTA IN VOLTA QUELLA CHE SCEGLIE L'UTENTE

#modo 1- oggetti distinti
paypal = PayPal("Paypal")
cc = CartaDiCredito("Carta di credito")

#modo 2 - lista di oggetti
pagamenti = [PayPal("Paypal"), CartaDiCredito("CC")]

scelta = 0
while scelta != 3:
    scelta = int(input("Inserisci con cosa vuoi pagare: 1-Paypal, 2-Carta di credito, 3 - Uscire"))
    if scelta == 1:
        effettua_pagamento(pagamenti[0], 10)
    elif scelta == 2:
        effettua_pagamento(cc, 15)
    elif scelta == 3:
        print("Hai deciso di uscire dal programma")
    else:
        print("Valore non riconosciuto, riprova")