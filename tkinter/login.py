import tkinter as tk
from tkinter import messagebox

#finestra per il login
class FinestraLogin():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.geometry("400x300")

        self.label_username = tk.Label(root, text="Username: ")
        self.label_username.pack(pady=10)

        self.username = tk.Entry(root)
        self.username.pack(pady=5)

        self.label_password = tk.Label(root, text="Password: ")
        self.label_password.pack(pady=10)

        self.password = tk.Entry(root, show="\u2022")
        self.password.pack(pady=5)

        self.pulsanteLogin = tk.Button(root, text="LOGIN", command=self.verificaLogin)
        self.pulsanteLogin.pack(pady=10)

    def verificaLogin(self):
        #recuperare username e password
        usernameValue = self.username.get()
        passwordValue = self.password.get()

        #posso verificare se è un utente autorizzato
        utenti = {"test": "test", "mario": "1234", "ciccio": "ciccio"}
        controlloLogin = False
        for u, p in utenti.items():
            if u==usernameValue and p==passwordValue:
                #autorizzato
                controlloLogin = True
            
        if controlloLogin == True:
            messagebox.showinfo("Login", "Login effettuato con successo")
        else:
            messagebox.showerror("Login", "Username o password sbagliata")

#main
root = tk.Tk()
finestraLogin = FinestraLogin(root)

root.mainloop()