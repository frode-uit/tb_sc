# file: sc_13_03b_closure_as_wrapper.py
# Eksempel 2: Closure som wrapper en funksjon (grunnlag for decorators)
def simple_decorator(func):
    # Tar en funksjon,returnerer en ny funksjon som wrapper den.
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
