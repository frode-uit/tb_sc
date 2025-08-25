# file name: sc_02_02.py
from datetime import datetime

current_year = datetime.now().year
first_name = input("Hva er ditt navn: ")
age = int(input("Hva er din alder: "))
birth_year = current_year - age

print("Hei,", first_name, "du ble født i", birth_year)