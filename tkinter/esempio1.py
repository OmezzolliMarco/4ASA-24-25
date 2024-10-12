import tkinter as tk

#funzioni
#definizione della funzione che cambia il testo
def cambia_testo():
    label.config(text="Ciao sono ...")
#main

root = tk.Tk() #creazione dell'istanza della classe TK (la finestra principale)
root.title("Introduzione a Tkinter") #il titolo della nostra finestra
root.geometry("300x400") #la dimensione della finestra

#creo un contenitore generale nel quale inserire tutti gli elementi, chiamato Frame (possono esserci più frame in una finestra)
frm = tk.Frame(root, bg="blue")
frm.pack(padx=10, pady=10, fill="both", expand=True) #lo visualizzo espandendolo e facendo occupare tutto lo spazio disponibile
#inizio a popolare di elementi la mia finestra

#inizio creando del testo statico
label = tk.Label(frm, text="Benvenuto!") #etichetta che mostra il messaggio Benvenuto
label.pack(pady=20) #per visualizzare l'etichetta nella finestra è necessario posizionarla, in questo caso con un padding dal bordo in alto di 20 pixel

#creazione di un semplice pulsante
button = tk.Button(frm, text='Cliccami', command=cambia_testo)
button.pack(pady=50)

#avvio del loop principale per visualizzare la finestra
root.mainloop() #mantiene aperta la finestra fino a quando non viene chiusa manualmente o il programma viene interrotto