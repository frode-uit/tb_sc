# file: sc_12_13_entry_list_demo.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def create_gui():
	root = tk.Tk()
	root.title("Listbox + Entry Demo")

	# Instruksjonstekst øverst
	lbl_intro = tk.Label(root, text="Legg til land i listen ved å skrive i feltet og trykke 'Legg til'.")
	lbl_intro.pack(padx=10, pady=(10, 0))

	# Frame for listbox + scrollbar
	frame = ttk.Frame(root)
	frame.pack(padx=10, pady=10, fill="both", expand=False)

	sb_scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL)
	lb_countries = tk.Listbox(frame, height=8, yscrollcommand=sb_scroll.set, selectmode=tk.SINGLE)
	sb_scroll.config(command=lb_countries.yview)
	sb_scroll.pack(side=tk.RIGHT, fill=tk.Y)
	lb_countries.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

	# Forhåndsutfylte land (delvis liste)
	initial_countries = [
		"Norge",
		"Sverige",
		"Danmark",
		"Finland",
		"Island",
		"Tyskland",
		"Frankrike",
	]
	for c in initial_countries:
		lb_countries.insert(tk.END, c)

	# Statusfelt som viser antall elementer
	status_var = tk.StringVar()

	def update_status():
		status_var.set(f"Antall land i listen: {lb_countries.size()}")

	update_status()

	lbl_status = ttk.Label(root, textvariable=status_var, anchor="w")
	lbl_status.pack(fill="x", padx=10)

	# Entry + knapp for å legge til nye land
	fr_entry = ttk.Frame(root)
	fr_entry.pack(padx=10, pady=(6, 10), fill="x")

	en_entry = ttk.Entry(fr_entry)
	en_entry.pack(side=tk.LEFT, fill="x", expand=True)

	def add_country(event=None):
		"""Legger til landet som står i entry hvis det er gyldig (ikke tomt, ikke duplikat)."""
		text = en_entry.get().strip()
		if not text:
			# Tom streng: gjør ingenting (eller vis en liten advarsel)
			messagebox.showinfo("Info", "Skriv inn et landnavn før du legger til.")
			return

		# Sjekk for duplikat (case-insensitiv)
		existing = [lb_countries.get(i) for i in range(lb_countries.size())]
		if any(text.lower() == e.lower() for e in existing):
			messagebox.showinfo("Info", f"'{text}' finnes allerede i listen.")
			en_entry.delete(0, tk.END)
			return

		lb_countries.insert(tk.END, text)
		en_entry.delete(0, tk.END)
		update_status()

	bt_add = ttk.Button(fr_entry, text="Legg til", command=add_country)
	bt_add.pack(side=tk.RIGHT, padx=(6, 0))

	# Valgfri: knapp for å fjerne valgte element
	def remove_selected():
		sel = lb_countries.curselection()
		if not sel:
			messagebox.showinfo("Info", "Velg et element i listen for å fjerne det.")
			return
		idx = sel[0]
		lb_countries.delete(idx)
		update_status()

	bt_remove = ttk.Button(root, text="Fjern valgt", command=remove_selected)
	bt_remove.pack(padx=10, pady=(0, 10), anchor="e")

	# Tastaturbindinger: Enter legger til, Del fjerner
	en_entry.bind("<Return>", add_country)
	root.bind("<Delete>", lambda e: remove_selected())

	return root


if __name__ == "__main__":
	app = create_gui()
	app.mainloop()

