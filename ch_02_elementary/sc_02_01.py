# file name: sc_02_01.py
CURRENT_YEAR = 2025

# Spør brukeren om navn og alder
first_name = input("Hva er ditt navn: ")
age = int(input("Hva er din alder: "))

# Beregn fødselsåret
birth_year = CURRENT_YEAR - age

# Skriv ut hilsen og fødselsår
print("Hei", first_name,", du er ", age,\
      "år, og ble født i", birth_year)