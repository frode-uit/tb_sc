import tkinter as tk

def vis_label_egenskaper():
    egenskaper = label.configure()
    tekstfelt.delete("1.0", tk.END)
    for navn, verdi in egenskaper.items():
        nåverdi = verdi[-1]  # Siste element er gjeldende verdi
        tekstfelt.insert(tk.END, f"{navn}: {nåverdi}\n")

root = tk.Tk()
root.title("Label-egenskaper med configure()")

label = tk.Label(root, text="Eksempeltekst", fg="blue", bg="white", font=("Arial", 12))
label.pack(pady=10)

knapp = tk.Button(root, text="Vis egenskaper", command=vis_label_egenskaper)
knapp.pack(pady=5)

tekstfelt = tk.Text(root, width=50, height=15)
tekstfelt.pack(padx=10, pady=10)

root.mainloop()