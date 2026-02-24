# File: sc_06_04_cels_to_fahr.py
# Demonstrerer en kodefil som inneholder en funksjon
# og som kan kjøres direkte eller importeres uten å kjøre koden under if __name__ == "__main__":

# Funksjon som konverterer Celsius til Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# kjøres når filen kjøres direkte
if __name__ == "__main__":
    celsius = float(input("Skriv inn temperatur i Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} grader Celsius er {fahrenheit} grader Fahrenheit.")   

