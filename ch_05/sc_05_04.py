# file: sc_05_04.py
import copy

list1 = [1, 2, 3]

# Bare referanse kopiering(ingen kopi)
list2 = list1
list2[0] = 10
print("Etter referanse-kopiering:")
print("list1:", list1)  # [10, 2, 3]
print("list2:", list2)  # [10, 2, 3]

# Shallow copy med slicing
list1 = [1, 2, 3]
list2 = list1[:]
list2[0] = 30
print("\nEtter shallow copy med slicing:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [30, 2, 3]

# Shallow copy med list comprehension
list1 = [1, 2, 3]
list2 = [x for x in list1]
list2[0] = 40
print("\nEtter shallow copy med comprehension:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [40, 2, 3]

# Shallow copy med +
list2 = [] + list1
list2[0] = 60
print("\nEtter shallow copy med +:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [60, 2, 3]

# Shallow copy med list klassen sin copy() metode
list1 = [1, 2, 3]
list2 = list1.copy()
list2[0] = 20
print("\nEtter shallow copy med copy():")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [20, 2, 3]


# Shallow copy med copy.copy()
list1 = [1, 2, 3]
list2 = copy.copy(list1)
list2[0] = 30
print("\nEtter shallow copy med copy.copy():")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [30, 2, 3]

# Deep copy
list1 = [1, 2, 3]
list2 = copy.deepcopy(list1)
list2[0] = 50
print("\nEtter deep copy:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [50, 2, 3]
