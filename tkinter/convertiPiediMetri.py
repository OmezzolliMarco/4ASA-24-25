import tkinter as tk

def converti():
    try:
        value = float(piedi.get())
        metri.set(0.3 * value)
    except:
        pass

root = tk.Tk()
root.title("Conversioni")
root.geometry("400x200")

frm = tk.Frame(root, bg="lightgreen")
frm.grid(row=0, column=0, sticky="NSEW", pady=5, padx=5)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#elementi
piedi = tk.StringVar() #non è un oggetto grafico
piedi_inserimento = tk.Entry(frm, width=7, textvariable=piedi)
piedi_inserimento.grid(row=0, column=1, sticky="NSEW")

label_piedi = tk.Label(frm, text="piedi")
label_piedi.grid(row=0, column=2, sticky="W")

#seconda riga
label_equivalente = tk.Label(frm, text="è equivalente a ")
label_equivalente.grid(row=1, column=0, sticky="E")

metri = tk.StringVar()
label_conversione = tk.Label(frm, textvariable=metri)
label_conversione.grid(row=1, column=1, sticky="NSEW")

label_metri = tk.Label(frm, text="metri")
label_metri.grid(row=1, column=2, sticky="W")

#terza riga
button = tk.Button(frm, text="Converti", command=converti)
button.grid(row=2, column=2, sticky="NSEW")

for child in frm.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()