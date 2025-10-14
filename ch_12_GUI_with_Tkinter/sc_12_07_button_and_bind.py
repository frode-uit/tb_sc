# file: sc_12_07_button_and_bind.py
import tkinter as tk

def on_button_click(event):
    print(f"Museklikk koordinater: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Bind-eksempel")

bt_simple = tk.Button(root, text="Klikk meg!")
bt_simple.pack()

# Bruker bind i stedet for command
bt_simple.bind("<Button-1>", on_button_click)

root.mainloop()
