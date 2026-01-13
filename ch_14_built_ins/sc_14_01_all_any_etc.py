# File: sc_14_01_all_any_etc.py

print("all() examples")
numbers = [2, 4, 6]
print(all(x % 2 == 0 for x in numbers)) # True

numbers = [2, 4, 6, 7]
print(all(x % 2 == 0 for x in numbers)) # False

numbers = []
print(all(x % 2 == 0 for x in numbers)) # True!!

print("any() examples")
numbers = [1, 3, 4]
print(any(x % 2 == 0 for x in numbers))  # True

numbers = [1, 3, 4, 6]
print(any(x % 2 == 0 for x in numbers))  # True

numbers = []
print(any(x % 2 == 0 for x in numbers))  # False!!

print("map() examples, lambda")
numbers = [1, 2, 3]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9]

numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]

# Funksjonen tar 2 parametere (x og y)
# Stopper når korteste list når slutten
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # [11, 22, 33, 44]

print("map() examples, without lambda")

def square_it(x):
    return x**2

numbers = [1, 2, 3]
squares = list(map(square_it, numbers))
print(squares)  # [1, 4, 9]


print("filter() examples")
numbers = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]