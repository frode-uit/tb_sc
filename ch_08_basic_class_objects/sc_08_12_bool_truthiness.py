# file: sc_08_12_bool_truthiness.py
# __bool__() kontrollerer truthiness for OBJEKTER (ikke klassen)
# Den globale bool() funksjonen kaller __bool__() for et objekt

class Wallet:
    def __init__(self, money=0):
        self._money = money
    
    def __bool__(self):
        """Lommebok er 'True' hvis den har penger"""
        return self._money > 0

class Basket:
    def __init__(self):
        self._items = []
    
    def __bool__(self):
        """Kurv er 'True' hvis den har innhold"""
        return len(self._items) > 0
    
    def add(self, item):
        self._items.append(item)

# Test truthiness
wallet1 = Wallet(100)    # Har penger
wallet2 = Wallet(0)      # Tom

basket1 = Basket()       # Tom kurv
basket2 = Basket()       
basket2.add("eple")      # Kurv med innhold

print("=== TRUTHINESS TEST ===")
print(f"Wallet(100): {bool(wallet1)}")  # True
print(f"Wallet(0): {bool(wallet2)}")    # False
print(f"Empty basket: {bool(basket1)}")  # False  
print(f"Basket with apple: {bool(basket2)}")  # True

print("\n=== BRUK I IF-SETNINGER ===")
if wallet1: # i stedet for eksempelvis wallet.has_money()
    print("Du har penger!")
if not wallet2:
    print("Lommeboka er tom")
if basket2: # i stedet for eksempelvis basket.has_items()
    print("Kurven har innhold")

# Sammenligning med klasse uten __bool__()
class NoBoolean:
    def __init__(self, value):
        self._value = value

empty_obj = NoBoolean(0)
print(f"\nUten __bool__(): {bool(empty_obj)}")  # True (objekter er alltid truthy)