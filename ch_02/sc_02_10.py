# file: sc_02_10.py
# Demonstrerer indeksering i strenger
tekst = "Hello, world!"
print(tekst[0])   # H
print(tekst[7])   # w
# print(tekst[13])  # IndexError: string index out of range
print(tekst[-1])  # !, siste tegn
print(tekst[-2])  # d, nest siste tegn
print(tekst[0:5]) # Hello (slice fra indeks 0 til 4)
print(tekst[7:])  # world! (slice fra indeks 7 til slutten)
print(tekst[::2])  # Hlo ol! (hvert andre tegn)
# det er ikke mulig å endre en streng direkte
# tekst[0] = 'h'  # Dette vil gi en TypeError
print(tekst[::-1]) # !dlrow ,olleH. reverser tekst