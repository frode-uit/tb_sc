# file sc_04_01.py
# Demonstrerer bruk av ternær operator i Python|
# flertallending i print-funksjonen
antall_epler = int(input("Hvor mange epler har du? "))
print(f"Du har {antall_epler} eple{'r' if antall_epler > 1 else ''}.")

# Versjon som skriver ut "ett" hvis ett eple, ikke 1
print(f"Du har {'ett' if antall_epler == 1 else antall_epler} eple{'r' if antall_epler > 1 else ''}.")

