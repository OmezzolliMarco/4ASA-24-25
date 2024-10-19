import tkinter as tk

root = tk.Tk()
root.title("Esempio grid")
root.geometry("400x300")

label1 = tk.Label(root, text="Nord-Ovest", bg="lightgreen")
label2 = tk.Label(root, text="Sud", bg="lightblue")
label3 = tk.Label(root, text="Centro", bg="grey")

#realizziamo la griglia
label1.grid(row=0, column=0, sticky="NW")
label2.grid(row=1, column=0, sticky="S")
label3.grid(row=0, column=1, sticky="NSEW")

root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

#mainloop
root.mainloop()