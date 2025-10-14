# file: sc_12_10_canvas_bind.py
import tkinter as tk

def on_canvas_click(event):
    # Finn ID-en til objektet som ble truffet
    clicked_items = canvas.find_closest(event.x, event.y)
    if clicked_items:
        item_id = clicked_items[0]
        print(f"Du klikket på objekt med ID: {item_id}")
        # Endre farge på objektet som ble klikket
        canvas.itemconfig(item_id, fill="green")

root = tk.Tk()
root.title("Canvas med bind")
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Tegn noen figurer
rect_id = canvas.create_rectangle(50, 50, 150, 150, fill="red")
oval_id = canvas.create_oval(200, 50, 300, 150, fill="blue")

# Bind museklikk til canvas
canvas.bind("<Button-1>", on_canvas_click)

root.mainloop()