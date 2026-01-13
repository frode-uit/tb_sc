# file: sc_13_02b_closure_mechanics.py
# Hvordan Python implementerer closures - mekanismen bak kulissene

"""
CLOSURE-MEKANISMEN: Stack vs Heap

Problemet:
-----------
Når en funksjon returnerer, fjernes normalt dens stack frame (lokale variabler).
Men en closure må "huske" variabler fra det ytre scopet selv etter at 
den ytre funksjonen har returnert.

Python's løsning:
-----------------
Python flytter de "lukkede" variablene fra stack til heap ved å pakke dem inn
i spesielle 'cell'-objekter. Dette gjør at variablene overlever stack frame'en
de ble skapt i.
"""

print("=" * 70)
print("DEL 1: Grunnleggende closure-eksempel")
print("=" * 70)

def make_multiplier(factor):
    """
    Lager en funksjon som multipliserer med 'factor'.
    'factor' må overleve selv etter at make_multiplier returnerer.
    """
    def multiplier(x):
        # multiplier "lukker inn" factor fra det ytre scopet
        return x * factor
    
    return multiplier

# Opprett to forskjellige closures
times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(f"\ntimes_2(5) = {times_2(5)}")  # 10
print(f"times_3(5) = {times_3(5)}")    # 15

# make_multiplier har returnert, men 'factor' lever videre!
print("\nmake_multiplier's stack frame er borte,")
print("men 'factor' eksisterer fortsatt på heapen.")

print("\n" + "=" * 70)
print("DEL 2: Inspeksjon av closure-mekanismen")
print("=" * 70)

# Python lagrer lukkede variabler i __closure__ attributten
print(f"\ntimes_2.__closure__ = {times_2.__closure__}")
print(f"Type: {type(times_2.__closure__)}")

if times_2.__closure__:
    print(f"\nAntall lukkede variabler: {len(times_2.__closure__)}")
    
    for i, cell in enumerate(times_2.__closure__):
        print(f"  Cell {i}: {cell}")
        print(f"    Type: {type(cell)}")
        print(f"    Verdi: {cell.cell_contents}")

print("\n" + "=" * 70)
print("DEL 3: Sammenligning av to closures")
print("=" * 70)

print("\ntimes_2 lukker inn factor=2:")
print(f"  times_2.__closure__[0].cell_contents = {times_2.__closure__[0].cell_contents}")

print("\ntimes_3 lukker inn factor=3:")
print(f"  times_3.__closure__[0].cell_contents = {times_3.__closure__[0].cell_contents}")

print("\nHver closure har sitt eget cell-objekt på heapen!")

print("\n" + "=" * 70)
print("DEL 4: Flere lukkede variabler")
print("=" * 70)

def make_calculator(a, b):
    """Closure med flere lukkede variabler."""
    operation = "add"  # En tredje variabel
    
    def calculate():
        if operation == "add":
            return a + b
        return 0
    
    return calculate

calc = make_calculator(10, 5)
print(f"\ncalc() = {calc()}")

print(f"\nAntall lukkede variabler: {len(calc.__closure__)}")
for i, cell in enumerate(calc.__closure__):
    print(f"  Cell {i}: {cell.cell_contents}")

print("\n" + "=" * 70)
print("DEL 5: Closure med mutable state (nonlocal)")
print("=" * 70)

def make_counter(start=0):
    """
    Lager en teller som kan inkrementeres.
    Demonstrerer at cell-objektet på heap kan modifiseres.
    """
    count = start  # Lagres i cell-objekt på heap
    
    def increment():
        nonlocal count  # Må bruke nonlocal for å modifisere
        count += 1
        return count
    
    return increment

counter1 = make_counter(0)
counter2 = make_counter(100)

print("\nCounter 1:")
print(f"  {counter1()}")  # 1
print(f"  {counter1()}")  # 2
print(f"  {counter1()}")  # 3

print("\nCounter 2:")
print(f"  {counter2()}")  # 101
print(f"  {counter2()}")  # 102

# Inspiser cell-objektene
print("\nCounter 1's cell:")
print(f"  Nåværende verdi: {counter1.__closure__[0].cell_contents}")

print("\nCounter 2's cell:")
print(f"  Nåværende verdi: {counter2.__closure__[0].cell_contents}")

print("\n" + "=" * 70)
print("DEL 6: Funksjon uten closure (for sammenligning)")
print("=" * 70)

def regular_function(x):
    """Vanlig funksjon uten closure."""
    return x * 2

print(f"\nregular_function.__closure__ = {regular_function.__closure__}")
print("None betyr ingen lukkede variabler - ingen cells!")

print("\n" + "=" * 70)
print("OPPSUMMERING")
print("=" * 70)
print("""
Closure-mekanismen i Python:

1. Stack-problem: Lokale variabler forsvinner når funksjonen returnerer.

2. Heap-løsning: Python flytter lukkede variabler til heap ved å pakke
   dem inn i 'cell'-objekter.

3. __closure__: Hver closure har en __closure__ attributt som er en tuple
   av cell-objekter.

4. cell_contents: Hver cell har en cell_contents attributt som inneholder
   den faktiske verdien.

5. Levetid: Cell-objektene på heap overlever så lenge closuren eksisterer,
   uavhengig av stack frames.

6. Mutable state: Med 'nonlocal' kan closures modifisere verdier i cells,
   og gi funksjonene en form for "privat tilstand".

Dette er grunnen til at closures kan "huske" sitt miljø!
""")
