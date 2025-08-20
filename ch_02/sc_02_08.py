# File name: sc_02_08.py
# demonstrerer ymse måter å bruke print-funksjonen på

print("Hei", 42, 3.14, True)
# Utskrift: Hei 42 3.14 True

# standard separator er mellomrom, kan endres med sep-parameteren
print("Hei", 42, 3.14, True, sep=", ")
# Utskrift: Hei, 42, 3.14, True

# print gir normalt linjeskift etter utskrift, kan endres med end-parameteren
print("Hei", 42, 3.14, True, sep=", ", end=".")
print("neste linje")
# Utskrift: Hei, 42, 3.14, True.neste linje

# + kan brukes til å konkatinere strenger, pass på at alle elementer er strenger
print("Hei" + ", " + str(42) + ", " + str(3.14) + ", " + str(True))
# Utskrift: Hei, 42, 3.14, True

# du kan også utføre aritmetiske operasjoner i print-funksjonen
print("Summen av 2 og 3 er", 2 + 3)
# Utskrift: Summen av 2 og 3 er 5

print("ASCII verdien av 'a' er", ord('a'))
# Utskrift: ASCII verdien av 'a' er 97
