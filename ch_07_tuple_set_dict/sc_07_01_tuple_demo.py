# File: sc_07_01_tuple_demo.py
# Demonstrasjon av tupler i Python

# 1. Lage tupler på ulike måter
tu1 = (1, 2, 3)                 # Vanlig tuple med parenteser
tu2 = 4, 5, 6                   # Tuple uten parenteser
tu3 = tuple([7, 8, 9])          # Bruker tuple()-konstruktøren
tu4 = ()                        # Tom tuple
tu5 = (42,)                     # Én-verdi tuple (merk komma!)
tu6 = tuple(x for x in range(5)) # Tuple fra generatoruttrykk
tu7 = tuple([x * 2 for x in range(5)]) # Tuple fra list comprehension
tu8 = tuple(map(str, range(3))) # Tuple fra map-funksjon


print("tu1:", tu1)
print("tu2:", tu2)
print("tu3:", tu3)
print("tu4:", tu4)
print("tu5:", tu5)
print("tu6:", tu6)
print("tu7:", tu7)
print("tu8:", tu8)

# 2. Oppakking av tuple
a, b, c = tu1
print("Oppakket tu1:", a, b, c)

# 3. Bytte verdier med tuple-oppakking
x = 10
y = 20
x, y = y, x
print("Byttet x og y:", x, y)

# 4. Utvidet oppakking (Python 3+)
tu6 = (1, 2, 3, 4, 5)
første, *midt, siste = tu6
print("Første:", første)
print("Midten:", midt)
print("Siste:", siste)

# 5. Tupler er uforanderlige (immutable)
try:
    tu1[0] = 99
except TypeError as e:
    print("Tupler er uforanderlige:", e)

# 6. Tuple-pakking og oppakking i funksjoner
def min_maks(*verdier):
    return min(verdier), max(verdier)  # Returnerer en tuple

resultat = min_maks(3, 7, 2, 5)
print("min_maks-resultat:", resultat)
min_verdi, maks_verdi = resultat
print("Oppakket min og maks:", min_verdi, maks_verdi)
