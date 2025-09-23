# File: sc_06_05_use_cels_to_fahr.py
import sc_06_04_cels_to_fahr as converter
# bruker funksjonen fra sc_06_04_cels_to_fahr.py
celsius = float(input("Skriv inn temperatur i Celsius: "))
fahrenheit = converter.celsius_to_fahrenheit(celsius)
print(f"{celsius} grader Celsius er {fahrenheit} grader Fahrenheit.")
