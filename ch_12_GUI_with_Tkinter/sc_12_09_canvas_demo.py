# file: sc_12_09_canvas_demo.py
import tkinter as tk
from tkinter import ttk
import random

class CanvasDemo:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 500
        self.canvas_height = 350
        self.root.title("Canvas demo")
        self.root.resizable(False, False)
    
        # Størrelsesvalg
        self.size_var = tk.StringVar(value="Middels")
        size_frame = ttk.LabelFrame(root, text="Størrelse")
        size_frame.pack(padx=10, pady=5, fill="x")
        rb_liten = ttk.Radiobutton(size_frame, text="Liten", variable=self.size_var, value="Liten")
        rb_middels = ttk.Radiobutton(size_frame, text="Middels", variable=self.size_var, value="Middels")
        rb_stor = ttk.Radiobutton(size_frame, text="Stor", variable=self.size_var, value="Stor")
        rb_liten.pack(side="left", padx=5)
        rb_middels.pack(side="left", padx=5)
        rb_stor.pack(side="left", padx=5)

        # Knapperamme
        button_frame = ttk.Frame(root)
        button_frame.pack(padx=10, pady=5, fill="x")
        bt_rektangel = ttk.Button(button_frame, text="Rektangel", command=self.tegn_rektangel)
        bt_oval = ttk.Button(button_frame, text="Oval", command=self.tegn_oval)
        bt_trekant = ttk.Button(button_frame, text="Trekant", command=self.tegn_trekant)
        bt_rektangel.pack(side="left", padx=5)
        bt_oval.pack(side="left", padx=5)
        bt_trekant.pack(side="left", padx=5)

        # Canvas
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(padx=10, pady=10)

        # For markering og sletting
        self._select_rect = None
        self._start_x = None
        self._start_y = None

        self.canvas.bind("<Button-1>", self._on_canvas_click)
        self.canvas.bind("<B1-Motion>", self._on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_canvas_release)
    
    def _on_canvas_click(self, event):
        # Start alltid markeringsrektangel ved klikk
        self._start_x = event.x
        self._start_y = event.y
        self._select_rect = self.canvas.create_rectangle(event.x, event.y, event.x, event.y, outline="red", dash=(2,2))

    def _on_canvas_drag(self, event):
        # Oppdater markeringsrektangelet under drag
        if self._select_rect is not None:
            self.canvas.coords(self._select_rect, self._start_x, self._start_y, event.x, event.y)

    def _on_canvas_release(self, event):
        # Slett alle figurer innenfor markeringsrektangelet
        if self._select_rect is not None:
            x0, y0, x1, y1 = self.canvas.coords(self._select_rect)
            x_min, x_max = min(x0, x1), max(x0, x1)
            y_min, y_max = min(y0, y1), max(y0, y1)
            items = self.canvas.find_enclosed(x_min, y_min, x_max, y_max)
            for item in items:
                self.canvas.delete(item)
            self.canvas.delete(self._select_rect)
            self._select_rect = None
            self._start_x = None
            self._start_y = None

    def hent_storrelse(self):
        size = self.size_var.get()
        if size == "Liten":
            return 40, 40
        elif size == "Middels":
            return 80, 80
        else:
            return 120, 120

    def tegn_rektangel(self):
        w, h = self.hent_storrelse()
        x0 = random.randint(0, self.canvas_width - w)
        y0 = random.randint(0, self.canvas_height - h)
        x1, y1 = x0 + w, y0 + h
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="black")

    def tegn_oval(self):
        w, h = self.hent_storrelse()
        x0 = random.randint(0, self.canvas_width - w)
        y0 = random.randint(0, self.canvas_height - h)
        x1, y1 = x0 + w, y0 + h
        self.canvas.create_oval(x0, y0, x1, y1, fill="lightgreen", outline="black")

    def tegn_trekant(self):
        w, h = self.hent_storrelse()
        # Sørg for at hele trekanten er innenfor canvas
        x0 = random.randint(0, self.canvas_width - w)
        y0 = random.randint(h, self.canvas_height)  # y0 er bunnen av trekanten
        points = [x0, y0, x0 + w, y0, x0 + w/2, y0 - h]
        self.canvas.create_polygon(points, fill="lightcoral", outline="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasDemo(root)
    root.mainloop()
