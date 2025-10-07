import tkinter as tk

root = tk.Tk()
root.title("Frame-eksempel")

frame_knapper = tk.Frame(root)
frame_knapper.pack(pady=10)

bt_ok = tk.Button(frame_knapper, text="OK")
bt_ok.pack(side="left", padx=5)

bt_cancel = tk.Button(frame_knapper, text="Avbryt")
bt_cancel.pack(side="left", padx=5)

root.mainloop()