# file: sc_05_03.py
numbers = [3, 7, 2, 8, 4]

for number in numbers:
    number = number + 1
print(numbers)

for 3 not in numbers:
    number = number + 1
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

for index, value in enumerate(numbers):
    numbers[index] = value + 1
print(numbers)
