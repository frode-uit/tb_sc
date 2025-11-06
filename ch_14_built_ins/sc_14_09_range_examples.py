# file: sc_14_09_range_examples.py
# range() - generator for tallsekvenser

print("=== Grunnleggende syntaks ===")

# range(stop)
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("range(2, 7):", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step)
print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

print("\n=== Negativ step (nedtelling) ===")
print("range(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("range(20, 0, -5):", end=" ")
for i in range(20, 0, -5):
    print(i, end=" ")
print()

print("\n=== range() er en generator ===")
r = range(5)
print(f"Type: {type(r)}")
print(f"range objekt: {r}")
print(f"Som liste: {list(range(5))}")

print("\n=== Minneeffektivitet ===")
import sys

# range lagrer ikke tallene - tar minimal plass
r = range(1000000)
print(f"range(1000000) størrelse: {sys.getsizeof(r)} bytes")

# Liste lagrer alle tallene - tar mye plass
lst = list(range(1000))
print(f"list(range(1000)) størrelse: {sys.getsizeof(lst)} bytes")

print("\n=== Bruk med enumerate() ===")
for i, num in enumerate(range(10, 15)):
    print(f"Index {i}: verdi {num}")

print("\n=== Sjekk om tall er i range ===")
r = range(5, 15)
print(f"range: {r}")
print(f"10 in range(5, 15): {10 in r}")
print(f"20 in range(5, 15): {20 in r}")

print("\n=== Indeksering av range ===")
r = range(10, 50, 5)
print(f"range: {r}")
print(f"Første element: {r[0]}")
print(f"Siste element: {r[-1]}")
print(f"Element ved indeks 2: {r[2]}")
