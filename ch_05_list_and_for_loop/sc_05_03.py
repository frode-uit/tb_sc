# file: sc_05_03.py
numbers = [3, 7, 2, 8, 4]

for number in numbers:
    number = number * 2
    print(number, end=' ')
print()
print(numbers)

for index in range(len(numbers)):
    numbers[index] = numbers[index] * 2
print(numbers)

for index, value in enumerate(numbers):
    numbers[index] = value + 1
print(numbers)