# File: sc_05_09_slicing_object.py

# Demonstrasjon av slicing-objekter og hvordan None gir standardverdier

tekst = "Hei på deg"

# Lag slicing-objekter
slice1 = slice(2, None)      # Fra indeks 2 til slutten
slice2 = slice(None, 5)      # Fra start til indeks 5
slice3 = slice(None, None)   # Hele strengen
slice4 = slice(2, 8, 2)      # Fra 2 til 8, hopp 2

# Bruk slicing-objektene
print("tekst[2:None] =>", tekst[slice1])
print("tekst[:5] =>", tekst[slice2])
print("tekst[:] =>", tekst[slice3])
print("tekst[2:8:2] =>", tekst[slice4])

# Sjekk hva None gir som standardverdier
print("slice1.start:", slice1.start, "slice1.stop:", slice1.stop, "slice1.step:", slice1.step)
print("slice2.start:", slice2.start, "slice2.stop:", slice2.stop, "slice2.step:", slice2.step)
print("slice3.start:", slice3.start, "slice3.stop:", slice3.stop, "slice3.step:", slice3.step)
print("slice4.start:", slice4.start, "slice4.stop:", slice4.stop, "slice4.step:", slice4.step)

# Forklaring:
# Når start, stop eller step er None, bruker Python:
# - start=None: fra start
# - stop=None: til slutten
# - step=None: steg 1
