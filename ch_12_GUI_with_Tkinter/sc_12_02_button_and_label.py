# file: sc_12_02_button_and_label.py
import tkinter as tk

# Hovedvindu
root = tk.Tk()
root.title("Callback + Nullstill")

# Standardtekst for label
INSTRUKSJON = "Klikk knappen for å få en melding her."

# En Label hvor vi viser meldinger til brukeren.
lb_demo = tk.Label(root, text=INSTRUKSJON)
lb_demo.pack(padx=10, pady=10)

def show_message():
    lb_demo.config(text="Knappen ble trykket!")

def reset_message():
    lb_demo.config(text=INSTRUKSJON)


# Knapp for å vise meldingen
bt_show = tk.Button(root, text="Vis melding", command=show_message)
bt_show.pack(padx=5, pady=5)

# Knapp for å nullstille meldingen
bt_reset = tk.Button(root, text="Nullstill", command=reset_message)
bt_reset.pack(padx=5, pady=(0, 10))

root.mainloop()
