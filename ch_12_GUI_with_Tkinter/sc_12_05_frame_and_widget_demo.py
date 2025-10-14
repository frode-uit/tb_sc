# file: sc_12_05_frame_and_widget_demo.py
import tkinter as tk
from tkinter import ttk

# Hovedvindu
root = tk.Tk()
root.title("Tkinter Demo - Strukturert GUI")

# === Frame: Personinfo ===
frm_personinfo = ttk.LabelFrame(root, text="Personinformasjon", padding=10)
frm_personinfo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Navn
lb_navn = ttk.Label(frm_personinfo, text="Navn:")
lb_navn.grid(row=0, column=0, sticky="w")
ent_navn = ttk.Entry(frm_personinfo, width=30)
ent_navn.grid(row=0, column=1, pady=5)

# Adresse
lb_adresse = ttk.Label(frm_personinfo, text="Adresse:")
lb_adresse.grid(row=1, column=0, sticky="w")
ent_adresse = ttk.Entry(frm_personinfo, width=30)
ent_adresse.grid(row=1, column=1, pady=5)

# === Frame: Valg ===
frm_valg = ttk.LabelFrame(root, text="Valg", padding=10)
frm_valg.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Radiobuttons
rb_valg = tk.StringVar(value="A")

lb_radio = ttk.Label(frm_valg, text="Velg en kategori:")
lb_radio.grid(row=0, column=0, sticky="w")

rb_a = ttk.Radiobutton(frm_valg, text="Fly + hotell", variable=rb_valg, value="A")
rb_a.grid(row=1, column=0, sticky="w")
rb_b = ttk.Radiobutton(frm_valg, text="Kun hotell", variable=rb_valg, value="B")
rb_b.grid(row=2, column=0, sticky="w")
rb_c = ttk.Radiobutton(frm_valg, text="Kun fly", variable=rb_valg, value="C")
rb_c.grid(row=3, column=0, sticky="w")
rb_d = ttk.Radiobutton(frm_valg, text="Ingen av delene", variable=rb_valg, value="C")
rb_d.grid(row=4, column=0, sticky="w")

# Checkbuttons
var_dag1 = tk.IntVar()
var_dag2 = tk.IntVar()
var_dag3= tk.IntVar()

lb_check = ttk.Label(frm_valg, text="Deltar dager:")
lb_check.grid(row=4, column=0, sticky="w")

cb_dag1 = ttk.Checkbutton(frm_valg, text="Dag 1", variable=var_dag1)
cb_dag1.grid(row=5, column=0, sticky="w")
cb_dag2 = ttk.Checkbutton(frm_valg, text="Dag 2", variable=var_dag2)
cb_dag2.grid(row=6, column=0, sticky="w")
cb_dag3 = ttk.Checkbutton(frm_valg, text="Dag 2", variable=var_dag3)
cb_dag3.grid(row=7, column=0, sticky="w")

# === Submit-knapp ===
def vis_data():
    print("Navn:", ent_navn.get())
    print("Adresse:", ent_adresse.get())
    print("Valgt kategori:", rb_valg.get())
    print("Deltar dag 1:", var_dag1.get())
    print("Deltar dag 2:", var_dag2.get())
    print("Deltar dag 3:", var_dag3.get())

bt_submit = ttk.Button(root, text="Send inn", command=vis_data)
bt_submit.grid(row=2, column=0, pady=10)

# Start GUI
root.mainloop()
