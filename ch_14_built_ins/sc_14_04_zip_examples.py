# file: sc_14_04_zip_examples.py
# zip() - kombinere flere iterables

print("=== Grunnleggende bruk ===")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} er {age} år")

print("\n=== Lage dictionary fra to lister ===")
keys = ['navn', 'alder', 'by']
values = ['Alice', 25, 'Oslo']

person = dict(zip(keys, values))
print(person)

print("\n=== Flere enn to iterables ===")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['Oslo', 'Bergen', 'Trondheim']

for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) bor i {city}")

print("\n=== Ulik lengde - stopper ved korteste ===")
short = [1, 2]
long = [10, 20, 30, 40]

result = list(zip(short, long))
print(result)  # [(1, 10), (2, 20)]

print("\n=== zip() er en iterator ===")
names = ['Alice', 'Bob']
ages = [25, 30]

zipped = zip(names, ages)
print(type(zipped))  # <class 'zip'>
print(list(zipped))  # [('Alice', 25), ('Bob', 30)]

print("\n=== Pakke ut (unzip) med zip(*...) ===")
pairs = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# "Unzip" - pakk ut til separate lister
names, ages = zip(*pairs)
print("Names:", names)
print("Ages:", ages)

print("\n=== Transponere matrise ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print("Original:")
for row in matrix:
    print(row)
print("\nTransponert:")
for row in transposed:
    print(row)
