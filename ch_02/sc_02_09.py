# file: sc_02_09.py
# Bruk av ulike apostrof-typer i Python-strenger

# Eksempel 1: Direkte utskrift med print()
print('Dette er en "streng" med doble anførselstegn.')
print("Dette er en 'streng' med enkle anførselstegn.")

print("""Dette er en streng
som går over flere linjer
og bruker trippel doble anførselstegn.""")

# Eksempel 2: Bygge opp en streng før utskrift
tekst1 = 'Hei'
tekst2 = "på"
tekst3 = '''deg!'''
kombinert = tekst1 + " " + tekst2 + " " + tekst3
print(kombinert)

# Eksempel 3: Kombinasjon med f-string og ulike apostrof-typer
navn = "John"
hilsen = f'{navn} sier: "Hei på deg!"'
print(hilsen)

# Eller med trippel apostrof for flerlinje f-string
flerlinje = f"""Hei {navn},
dette er en melding
som bruker f-string og trippel apostrof."""
print(flerlinje)

# escape sekvens for doble anførselstegn i en streng
print("Dette er en \"streng\" med doble anførselstegn.")

# Demonstrasjon av raw streng
# Vanlig streng
sti1 = "C:\\Users\\Ola\\Documents"
print(sti1)  # C:\Users\Ola\Documents

# Råstreng
sti2 = r"C:\Users\Ola\Documents"
print(sti2)  # C:\Users\Ola\Documents

