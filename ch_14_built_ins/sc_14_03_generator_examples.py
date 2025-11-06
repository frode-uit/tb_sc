def countdown(start):
    print("Starter nedtelling...")
    while start > 0:
        yield start # "Pauser" her og returnerer start
        start -= 1
    print("Ferdig!")

# Lager generator-objekt
gen = countdown(3)
print(type(gen)) # <class 'generator'>

# Henter verdier én om gangen
print(next(gen)) # Starter nedtelling... 3
print(next(gen)) # 2
print(next(gen)) # 1

# Med løkke..
for i in countdown(3):
    print(i)
