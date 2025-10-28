# file: sc_13_04_decorator.py
# Decorators - funksjoner som wrapper andre funksjoner
# (Dette bygger på closure-konseptet fra sc_13_03b_closure_as_wrapper.py)

# Steg 1: Enkel decorator med @-syntaks
def simple_decorator(func):
    """Wrapper en funksjon med ekstra funksjonalitet."""
    def wrapper():
        print("--- Før funksjonen kalles ---")
        func()  # Closure: wrapper husker func
        print("--- Etter funksjonen er kalt ---")
    return wrapper

# @simple_decorator betyr: greet = simple_decorator(greet)
@simple_decorator
def greet():
    print("Hei!")

greet()

print("\n" + "="*50 + "\n")

@simple_decorator
def say_goodbye():
    print("Ha det!")

say_goodbye()

print("\n" + "="*50 + "\n")

# Steg 2: Decorator som håndterer argumenter og returverdier
def smart_decorator(func):
    """Decorator som fungerer med argumenter og returverdier."""
    def wrapper(*args, **kwargs):
        print(f"Kaller {func.__name__} med args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returnerte: {result}")
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

@smart_decorator
def greet_person(name, greeting="Hei"):
    return f"{greeting}, {name}!"

result1 = add(5, 3)
print(f"Resultat: {result1}")

print()

result2 = greet_person("Anna", greeting="Hallo")
print(f"Resultat: {result2}")

print("\n" + "="*50 + "\n")

# Steg 3: Praktisk eksempel - logging decorator med state
def log_calls(func):
    """Logger alle kall til funksjonen."""
    call_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"[LOG] Kall #{call_count} til {func.__name__}")
        return func(*args, **kwargs)
    
    return wrapper

@log_calls
def calculate(x, y):
    return x * y + x

print(calculate(3, 4))
print(calculate(5, 2))
print(calculate(1, 1))
