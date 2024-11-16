import tkinter as tk

#classe Plancia
class Plancia():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")

        self.lista_pulsanti = []

        self.player = "X"
        global griglia
        for i in range(3):
            for j in range(3):
                griglia[i][j] = ""

        self.creaTavoloGioco()
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
    
    def creaTavoloGioco(self):
        for i in range(9):
            button = tk.Button(self.root, text="", width=10, height=10, command=lambda i=i: self.premiPulsante(i))
            button.grid(row=i//3, column=i%3, sticky="NSWE")
            self.lista_pulsanti.append(button)

    def premiPulsante(self, i):
        if self.lista_pulsanti[i].cget("text") == "X" or self.lista_pulsanti[i].cget("text") == "O":
            #non devo fare niente
            pass
        else:
            self.lista_pulsanti[i].configure(text=self.player)
            #trovo in che posizione della griglia si trova
            righe = i//3
            colonne = i%3
            griglia[righe][colonne] = self.player

            self.controllaVincita()

            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

#main 
root = tk.Tk()

#creazione della griglia per i controlli
griglia = []
for i in range(3):
    griglia.append([])
    for j in range(3):
        griglia[i].append("")

#crea la plancia di gioco
plancia = Plancia(root)

root.mainloop()