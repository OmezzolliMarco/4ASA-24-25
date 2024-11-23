import tkinter as tk
import os

class Lista:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Lista della spesa")
        self.root.geometry("400x300")

        self.listaSpesa = []

        self.variabileProdotto = tk.StringVar()

        self.frame1 = tk.Frame(root, bg="blue")
        self.frame1.grid(row=0, column=0, sticky="NSWE")

        self.frame2 = tk.Frame(root, bg="red")
        self.frame2.grid(row=0, column=1, sticky="NSWE")
        
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        #gestico il frame 1
        self.label1 = tk.Label(self.frame1, text="Inserisci un prodotto")
        self.label1.pack(pady=10, padx=10)

        self.prodotto = tk.Entry(self.frame1, width=30, textvariable=self.variabileProdotto)
        self.prodotto.pack(padx=10, pady=5)

        self.btn_add = tk.Button(self.frame1, text="Aggiungi", command=self.aggiungiProdotto)
        self.btn_add.pack(padx=10, pady=10)

        self.btn_remove = tk.Button(self.frame1, text="Rimuovi", command=self.rimuoviProdotto)
        self.btn_remove.pack(padx=10, pady=5)

        self.label2 = tk.Label(self.frame2, text="Lista prodotti")
        self.label2.pack(pady=10, padx=10)

        self.listbox = tk.Listbox(self.frame2, width=40, height=10)
        self.listbox.pack(pady=5)

    def aggiungiProdotto(self):
        str_prodotto = self.variabileProdotto.get()
        self.listaSpesa.append(str_prodotto)

        self.listbox.insert(tk.END, str_prodotto)
    def rimuoviProdotto(self):
        #trovo elemento selezionato
        indice_selezionato = self.listbox.curselection()[0]
        #capire che elemento sto estraendo
        prodotto_selezionato = self.listbox.get(indice_selezionato)
        self.listaSpesa.remove(prodotto_selezionato)
        self.listbox.delete(indice_selezionato)
#main
root = tk.Tk()

lista = Lista(root)

root.mainloop()