# file name: sc_02_03.py
from datetime import datetime

current_year = datetime.now().year
first_name = input("Hva er ditt navn: ")
age = int(input("Hva er din alder: "))
body_weight = float(input("Hva er din vekt i kg: "))
body_height = float(input("Hva er din høyde i cm: "))
# Calculate BMI
bmi = body_weight / (body_height / 100) ** 2
birth_year = current_year - age

print("Hei,", first_name, "du ble født i", birth_year)
print("Din BMI er:", bmi)
print("Din BMI er:", round(bmi,2))
print(f"Din BMI er: {bmi:.2f}")