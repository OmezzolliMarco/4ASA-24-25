import tkinter as tk

root = tk.Tk()
root.title("Esempio place")
root.geometry("400x300")

button = tk.Button(root, text="Pulsante")
button.place(x=50, y=100, height=50, width=100)

root.mainloop()