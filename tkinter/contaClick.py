import tkinter as tk

def conteggio():
    global conta
    conta += 1
    label.config(text=f"Numero click: {conta}")

root = tk.Tk()
root.title("Conta click")
root.geometry("400x300")

conta = 0
label = tk.Label(root, text=f"Numero click: {conta}", font=("Monsterrat", 12))
label.pack(pady=20)

button = tk.Button(root, text="Cliccami!", command=conteggio)
button.pack(pady=10)

#mainloop
root.mainloop()
