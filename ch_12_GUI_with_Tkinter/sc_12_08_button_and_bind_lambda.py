# file: sc_12_08_button_and_bind_lambda.py
import tkinter as tk

def on_button_click(text, a_list, event):
    print(f"Event: {event}")
    print(f"Tekst: {text}, Liste: {a_list}")
    print(f"Widget som ble klikket: {event.widget}")
    print(f"Museklikk koordinater: x={event.x}, y={event.y}")
    a_list.append(a_list[-1] + 1)
    print("---")

root = tk.Tk()
root.title("Bind + Lambda Callback-eksempel")

some_list = [1]

# Bruk bind i stedet for command
bt_simple = tk.Button(root, text="Klikk Meg")
bt_simple.bind("<Button-1>", lambda event: on_button_click("Hei fra bind", some_list, event))
bt_simple.pack(pady=10)

root.mainloop()