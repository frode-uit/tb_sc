# Vanlig funksjon - returnerer alt på en gang
def get_numbers():
    return [1, 2, 3]

# Generator-funksjon - genererer verdier én om gangen
def generate_numbers():
    yield 1
    yield 2
    yield 3

# Bruk av vanlig funksjon
print("Vanlig funksjon:")
for num in get_numbers():
    print(num, end=" ")  # 1 2 3

# Bruk av generator
print("\n\nGenerator:")
for num in generate_numbers():
    print(num, end=" ")  # 1 2 3
