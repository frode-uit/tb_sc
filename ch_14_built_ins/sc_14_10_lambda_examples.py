# file: sc_14_10_lambda_examples.py
# Examples of using lambda functions in Python

# Regular function
def square(x):
    print("Regular function called!")
    return x * x

# Equivalent with lambda (overrides the regular function)
square = lambda x: x * x
print("Calling square(5):")
print(square(5))  # 25 - only lambda runs
print(type(square))  # <class 'function'>


# Sort list of lists based on second element
data = [[1, 'banana'], [2, 'apple'], [3, 'cherry']]

# Sort on second element in sublist
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
# [[2, 'apple'], [1, 'banana'], [3, 'cherry']]

# Lambda remembers surrounding variables (closure example)
greeting = "Hello"
f = lambda name: f"{greeting}, {name}"
print(f("World"))  # Hello, World
