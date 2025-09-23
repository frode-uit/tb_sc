# File: sc_07_02_dict_demo.py
# Demonstrasjon av dictionary (ordbok) i Python

person = {
    "navn": "Frode",
    "alder": 42,
    "yrke": "Universitetslektor"
}

# Skriv ut hele ordboken
print("Person:", person)

# Hent ut enkeltverdier
print("Navn:", person["navn"])
print("Alder:", person["alder"])
print("Yrke:", person["yrke"])

# Legg til en ny nøkkel
person["hobby"] = "sykling"
print("Med hobby:", person)

# Endre en verdi
person["alder"] = 43
print("Oppdatert alder:", person["alder"])

# Slett en nøkkel
del person["yrke"]
print("Uten yrke:", person)

# Gå gjennom alle nøkler og verdier
for nøkkel, verdi in person.items():
    print(f"{nøkkel}: {verdi}")
