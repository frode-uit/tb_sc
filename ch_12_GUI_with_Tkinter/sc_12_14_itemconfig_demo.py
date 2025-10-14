# file: sc_12_14_itemconfig_demo.py
import tkinter as tk

def endre_farge():
    canvas.itemconfig(rektangel_id, fill="orange", outline="black")

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=150)
canvas.pack()

rektangel_id = canvas.create_rectangle(50, 50, 150, 100, fill="blue")
btn = tk.Button(root, text="Endre farge", command=endre_farge)
btn.pack()

root.mainloop()
