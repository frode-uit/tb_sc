# file sc_13_01_function_as_parameter.py
# Define a list of lists
data = [[1, 'banana'], [2, 'apple'], [3, 'cherry']]

# Define a custom sorting function
def sort_by_second_element(item):
    return item[1]

# Use the sorted function with the custom sorting function
sorted_data = sorted(data, key=sort_by_second_element)

# Print the sorted list
print(sorted_data)
