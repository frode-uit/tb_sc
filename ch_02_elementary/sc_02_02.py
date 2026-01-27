# file name: sc_02_02.py
from datetime import datetime

current_date = datetime.now()
current_year = current_date.year

first_name = input("Hva er ditt navn: ")
age = int(input("Hva er din alder: "))
birth_year = current_year - age

print("Hei,", first_name, "du ble født i", birth_year)