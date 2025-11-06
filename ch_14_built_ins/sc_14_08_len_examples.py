# file: sc_14_08_len_examples.py
# len() - lengde av collections

print("=== Grunnleggende bruk ===")

# Lister
numbers = [1, 2, 3, 4, 5]
print(f"Liste: {numbers}")
print(f"Lengde: {len(numbers)}")

# Strenger
text = "Python"
print(f"\nStreng: '{text}'")
print(f"Lengde: {len(text)}")

# Tupler
coordinates = (10, 20, 30)
print(f"\nTupel: {coordinates}")
print(f"Lengde: {len(coordinates)}")

# Dictionaries (antall nøkkel-verdi par)
person = {'name': 'Alice', 'age': 25, 'city': 'Oslo'}
print(f"\nDictionary: {person}")
print(f"Antall nøkler: {len(person)}")

# Set
unique = {1, 2, 3, 2, 1}  # Duplikater fjernes
print(f"\nSet: {unique}")
print(f"Antall unike elementer: {len(unique)}")

print("\n=== Flerdimensjonale lister ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Matrise:")
for row in matrix:
    print(f"  {row}")
print(f"Antall rader: {len(matrix)}")
print(f"Antall kolonner i første rad: {len(matrix[0])}")

print("\n=== Bruk i løkker ===")
numbers = [10, 20, 30, 40]
print("Iterere med indeks:")
for i in range(len(numbers)):
    print(f"  Index {i}: {numbers[i]}")

print("\n=== Tom collection ===")
print(f"len([]): {len([])}")
print(f"len(''): {len('')}")
print(f"len({{}}): {len({})}")
