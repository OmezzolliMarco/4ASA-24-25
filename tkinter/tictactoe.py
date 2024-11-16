import tkinter as tk

#classe Plancia
class Plancia():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")

        self.lista_pulsanti = []

        self.player = "X"

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
        self.lista_pulsanti[i].configure(text=self.player)
#main 
root = tk.Tk()

#crea la plancia di gioco
plancia = Plancia(root)

root.mainloop()