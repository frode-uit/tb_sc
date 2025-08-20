# file: sc_o6_02.py
# Viser ulike teknikker for å definere og bruke funksjoner i Python

# Returnerer flere verdier
def calculate_sum_and_average(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average

sum1, avg1 = calculate_sum_and_average(3, 6, 9)
print("Sum:", sum1)
print("Gjennomsnitt:", avg1)

# Funksjon som kalles med keyword-argumenter
# Dette gjør det enklere å forstå hva hvert argument betyr
def create_greeting(name, greeting):
    return f"{greeting}, {name}!"

msg1 = create_greeting(name="Ola", greeting="Hei")
msg2 = create_greeting(greeting="Hallo", name="Kari")
print(msg1)
print(msg2)

# Funksjon med standardverdier
# Hvis argumentet ikke er spesifisert, brukes standardverdien
def greet(name, greeting="Hei"):
    print(f"{greeting}, {name}!")

greet("Anna")           # Bruker standardverdi
greet("Jon", "Hallo")   # Overstyrer standardverdi

# Vær obs på at standardverdier evalueres når funksjonen defineres, ikke når den kalles.
# Dette kan føre til uventede resultater hvis mutable objekter brukes som standardverdier
def legg_til(element, liste=[]):
    liste.append(element)
    return liste

print(legg_til(1))  # [1]
print(legg_til(2))  # [1, 2] 

# For å unngå dette, bruk None som standardverdi og initialiser listen inne i funksjonen
def legg_til(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

print(legg_til(1))  # [1]
print(legg_til(2))  # [2]

# Funksjon som tar et vilkårlig antall argumenter
# Dette er nyttig når antallet argumenter ikke er kjent på forhånd
def total_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))

# Funksjon som tar et vilkårlig antall keyword-argumenter
# Dette er nyttig for å håndtere fleksible data uten å måtte definere mange parametere
def print_user_info(**info):
    for key in info:
        print(key, ":", info[key])

print_user_info(name="Lise", age=30)
print_user_info(name="Per", hobby="ski", city="Oslo")
