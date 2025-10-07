# file: sc_12_01_button.py
import tkinter as tk

def knapp_trykket():
     print("Knappen ble trykket!")

root = tk.Tk()
root.title("Callback-eksempel")

bt_simple = tk.Button(root, text="Klikk meg!", command=knapp_trykket)
bt_simple.pack()

root.mainloop()