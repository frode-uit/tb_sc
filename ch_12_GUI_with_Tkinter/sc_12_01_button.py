# file: sc_12_01_button.py
import tkinter as tk

def on_button_click():
     print("Knappen ble trykket!")

root = tk.Tk()
root.title("Callback-eksempel")

bt_simple = tk.Button(root, text="Klikk meg!", command=on_button_click)
bt_simple.pack()

root.mainloop()