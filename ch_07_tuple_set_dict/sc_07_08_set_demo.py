# file: sc_07_08_set_demo.py
# Set operations demonstration

# Create sets
fruits1 = {'apple', 'banana', 'cherry'}
fruits2 = {'banana', 'orange', 'grape'}

# --- UNION ---
# CREATES NEW SET - all elements from both sets
result_set = fruits1 | fruits2
print(result_set)
# result_set = fruits1.union(fruits2)
# {'apple', 'banana', 'orange', 'cherry', 'grape'}

# --- INTERSECTION ---
# CREATES NEW SET - common elements
result_set = fruits1 & fruits2
print(result_set)
# result_set = fruits1.intersection(fruits2)
# {'banana'}

# --- DIFFERENCE ---
# CREATES NEW SET - elements in first but not second
result_set = fruits1 - fruits2
print(result_set)
# result_set = fruits1.difference(fruits2)
# {'apple', 'cherry'}

# --- SYMMETRIC DIFFERENCE ---
# CREATES NEW SET - elements in either but not both
result_set = fruits1 ^ fruits2
print(result_set)
# result_set = fruits1.symmetric_difference(fruits2)
# {'apple', 'cherry', 'orange', 'grape'}

# --- UNION UPDATE ---
# IN-PLACE UPDATE - add all elements from other set
set_a = {'apple', 'banana', 'cherry'}
set_b = {'banana', 'orange', 'grape'}
set_a |= set_b
print(set_a)
# set_a.update(set_b)
# {'apple', 'banana', 'cherry', 'orange', 'grape'}

# --- INTERSECTION UPDATE ---
# IN-PLACE UPDATE - keep only common elements
set_c = {'apple', 'banana', 'cherry'}
set_d = {'banana', 'orange', 'grape'}
set_c &= set_d
print(set_c)
# set_c.intersection_update(set_d)
# {'banana'}

# --- DIFFERENCE UPDATE ---
# IN-PLACE UPDATE - remove common elements
set_g = {'apple', 'banana', 'cherry'}
set_h = {'banana', 'orange', 'grape'}
set_g -= set_h
print(set_g)
# set_g.difference_update(set_h)
# {'apple', 'cherry'}

# --- SYMMETRIC DIFFERENCE UPDATE ---
# IN-PLACE UPDATE - elements in either but not both
set_e = {'apple', 'banana', 'cherry'}
set_f = {'banana', 'orange', 'grape'}
set_e ^= set_f
print(set_e)
# set_e.symmetric_difference_update(set_f)
# {'apple', 'cherry', 'orange', 'grape'}

# --- MEMBERSHIP ---
# Check membership
print('apple' in fruits1)  # True
print('orange' in fruits1)  # False

# --- SUBSET / SUPERSET ---
# Subset and superset (returns boolean)
small_set = {'banana'}
result = small_set <= fruits1
print(result)  # True
# result = small_set.issubset(fruits1)
result = fruits1 >= small_set
print(result)  # True
# result = fruits1.issuperset(small_set)