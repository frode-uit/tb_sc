# file: sc_14_06_reversed_examples.py
# reversed() - reversere iterables

print("=== Grunnleggende bruk ===")
numbers = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(numbers))
print("Reversert:", reversed_nums)
print("Original (uendret):", numbers)

print("\n=== reversed() er en iterator ===")
numbers = [1, 2, 3]
rev = reversed(numbers)
print("Type:", type(rev))
print("Som liste:", list(rev))

print("\n=== Bruk i for-løkke ===")
print("Nedtelling:", end=" ")
for num in reversed([1, 2, 3, 4, 5]):
    print(num, end=" ")
print()

print("\n=== Reversere strenger ===")
text = "Python"
reversed_text = ''.join(reversed(text))
print(f"'{text}' reversert: '{reversed_text}'")

print("\n=== reversed() vs slicing [::-1] ===")
numbers = [1, 2, 3, 4, 5]

# Med reversed() - iterator (lazy)
rev1 = reversed(numbers)
print("reversed():", type(rev1), "- lazy iterator")

# Med slicing - lager ny liste umiddelbart
rev2 = numbers[::-1]
print("[::-1]:", type(rev2), "- ny liste i minnet")
print("Resultat:", rev2)

print("\n=== Reversed range ===")
print("Nedtelling fra 10:", end=" ")
for i in reversed(range(1, 11)):
    print(i, end=" ")
print()
