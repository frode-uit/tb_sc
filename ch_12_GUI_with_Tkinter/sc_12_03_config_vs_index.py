# file: sc_12_03_config_vs_index.py
import tkinter as tk

root = tk.Tk()
root.title("To måter å endre widgets")

# Label 1 – endres med config()
label_config = tk.Label(root, text="Label med config", fg="black")
label_config.pack(pady=5)

# Label 2 – endres med indeks
label_index = tk.Label(root, text="Label med indeks", fg="black")
label_index.pack(pady=5)

# Endre Label 1 med config()
label_config.config(text="Endret med config()", fg="blue")

# Endre Label 2 med option dictionary (indeks)
label_index["text"] = "Endret med indeks"
label_index["fg"] = "green"

root.mainloop()
