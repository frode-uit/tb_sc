# file: sc_13_02_inner_outer.py
# Closures - indre funksjoner som "husker" det ytre miljøet

# Eksempel 1: Grunnleggende closure
def outer(x: int):
    outer_var = x * 2

    def inner():
        # Closure: inner har tilgang til outer sine variabler
        # selv etter at outer har returnert
        inner_var = outer_var * 2
        print(f"x: {x}")           # Fra outer sin parameter
        print(f"outer_var: {outer_var}")  # Fra outer sin lokale variabel
        print(f"inner_var: {inner_var}")  # inner sin egen variabel
        print()

    return inner  # Returnerer inner adresse

# Hver closure "husker" sitt eget miljø
print("First closure (x=42):")
closure1 = outer(42)
closure1()  # Printer: 42, 84, 168

print("Second closure (x=10):")
closure2 = outer(10)
closure2()  # Printer: 10, 20, 40

# Begge closures eksisterer samtidig med sine egne verdier
print("Calling first closure again:")
closure1()  # Fortsatt: 42, 84, 168

print("\n" + "="*50 + "\n")

# Eksempel 2: Closure som wrapper en funksjon (grunnlag for decorators)
def simple_decorator(func):
    # Tar en funksjon og returnerer en ny funksjon som wrapper den.
    def wrapper():
        print("--- Før funksjonen kalles ---")
        func()  # Closure: wrapper husker func
        print("--- Etter funksjonen er kalt ---")
    return wrapper

def greet():
    print("Hei!")

# Manuell "decorering" - erstatter greet med wrapper-versjonen
print("Original greet:")
greet()

print("\nNå 'decorerer' vi greet:")
greet = simple_decorator(greet)  # greet er nå wrapper-funksjonen
greet()  # Kaller wrapper, som kaller den originale greet

# Dette er nøyaktig det som skjer når vi bruker @-syntaksen i neste fil!
