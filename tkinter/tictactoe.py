import tkinter as tk

#classe Plancia
class Plancia():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")

        self.creaTavoloGioco()
        self.root.columnconfigure(0, weight=1)
    
    def creaTavoloGioco(self):
        for i in range(9):
            button = tk.Button(self.root, text="", width=10, height=10)
            button.grid(row=i//3, column=i%3, sticky="NSWE")

#main 
root = tk.Tk()

#crea la plancia di gioco
plancia = Plancia(root)

root.mainloop()