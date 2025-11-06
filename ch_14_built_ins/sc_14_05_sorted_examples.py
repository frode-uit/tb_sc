# file: sc_14_05_sorted_examples.py
# sorted() - sortere iterables

print("=== Grunnleggende bruk ===")
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(numbers)
print("Sortert:", sorted_nums)
print("Original (uendret):", numbers)

print("\n=== Sortere i synkende rekkefølge ===")
numbers = [3, 1, 4, 1, 5]
desc = sorted(numbers, reverse=True)
print(desc)

print("\n=== Sortere strenger ===")
names = ['charlie', 'Alice', 'bob']

# Case-sensitive (standard)
print("Case-sensitive:", sorted(names))

# Case-insensitive med key
print("Case-insensitive:", sorted(names, key=str.lower))

print("\n=== Sortere med key parameter ===")
words = ['banana', 'pie', 'Washington', 'book']

# Sortere etter lengde
by_length = sorted(words, key=len)
print("Etter lengde:", by_length)

# Sortere etter siste bokstav
by_last = sorted(words, key=lambda w: w[-1])
print("Etter siste bokstav:", by_last)

print("\n=== Sortere komplekse objekter ===")
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sortere etter karakter
by_grade = sorted(students, key=lambda s: s['grade'])
print("Etter karakter:")
for student in by_grade:
    print(f"  {student['name']}: {student['grade']}")

# Sortere etter navn
by_name = sorted(students, key=lambda s: s['name'])
print("Etter navn:")
for student in by_name:
    print(f"  {student['name']}: {student['grade']}")

print("\n=== sorted() vs list.sort() ===")
numbers1 = [3, 1, 4, 1, 5]
numbers2 = [3, 1, 4, 1, 5]

# sorted() - returnerer ny liste
new_list = sorted(numbers1)
print("sorted() - original:", numbers1)
print("sorted() - ny liste:", new_list)

# list.sort() - endrer lista på stedet
numbers2.sort()
print("sort() - endret original:", numbers2)
