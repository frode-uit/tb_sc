# file: sc_14_07_min_max_sum_examples.py
# min(), max(), sum() - aggregering

print("=== min() og max() ===")
numbers = [3, 1, 4, 1, 5, 9, 2]

print(f"Minste tall: {min(numbers)}")
print(f"Største tall: {max(numbers)}")

# Fungerer også med strenger (leksikografisk)
words = ['banana', 'apple', 'cherry']
print(f"Første ord alfabetisk: {min(words)}")
print(f"Siste ord alfabetisk: {max(words)}")

print("\n=== Med key parameter ===")
words = ['banana', 'pie', 'Washington', 'book']

# Korteste ord
shortest = min(words, key=len)
print(f"Korteste ord: '{shortest}' (lengde {len(shortest)})")

# Lengste ord
longest = max(words, key=len)
print(f"Lengste ord: '{longest}' (lengde {len(longest)})")

print("\n=== Med komplekse objekter ===")
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Student med laveste karakter
worst = min(students, key=lambda s: s['grade'])
print(f"Laveste karakter: {worst['name']} ({worst['grade']})")

# Student med høyeste karakter
best = max(students, key=lambda s: s['grade'])
print(f"Høyeste karakter: {best['name']} ({best['grade']})")

print("\n=== sum() ===")
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum: {total}")

# Med start-verdi
total_plus_10 = sum(numbers, 10)
print(f"Sum + 10: {total_plus_10}")

print("\n=== Gjennomsnitt ===")
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Tall: {numbers}")
print(f"Gjennomsnitt: {average}")

print("\n=== Tom iterable ===")
# sum() returnerer 0 for tom liste
print(f"sum([]): {sum([])}")

# min() og max() krever minst ett element
try:
    min([])
except ValueError as e:
    print(f"min([]): ValueError - {e}")
