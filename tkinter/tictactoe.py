import tkinter as tk
from tkinter import messagebox

#classe Plancia
class Plancia():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")

        self.lista_pulsanti = []

        self.player = "X"
        global griglia
        # for i in range(3):
        #     for j in range(3):
        #         griglia[i][j] = ""

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

            winner = self.controllaVincita()

            #comunicare chi ha vinto
            if winner: #se non è None
                if winner == "X":
                    messagebox.showinfo("Vincita", "Vince il giocatore X")
                elif winner == "O":
                    messagebox.showinfo("Vincita", "Vince il giocatore O")
                elif winner == "Pareggio":
                    messagebox.showinfo("Pareggio", "Pareggio")
                #resettare la board di gioco
                self.resetGame()

            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

    def resetGame(self):
        #reset visuale
        for button in self.lista_pulsanti:
            button.configure(text="")
        #reset della griglia di controllo
        for i in range(3):
            for j in range(3):
                griglia[i][j] = ""

    def controllaVincita(self):
        for i in range(3):
            #righe
            if griglia[i][0] == griglia[i][1] == griglia[i][2] != "":
                return griglia[i][0]
            #colonne
            if griglia[0][i] == griglia[1][i] == griglia[2][i] != "":
                return griglia[0][1]
        #controllo delle diagonali
        if griglia[0][0] == griglia[1][1] == griglia[2][2] != "":
            return griglia[0][0]
        if griglia[0][2] == griglia[1][1] == griglia[2][0] != "":
            return griglia[0][2]

        #controllare se ci sono caselle libere, se non ce ne sono allora pareggio

        if all(all(cell != "" for cell in row) for row in griglia):
            return "Pareggio"
        else:
            return None
        #opzione con istruzioni classiche
        # controllo = False
        # for i in range(3):
        #     for j in range(3):
        #         if griglia[i][j] == "":
        #             controllo = True
        # if controllo:
        #     return None
        # else:
        #     return "Pareggio"
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