# file: sc_06_03.py

# parameter navn kan være hva som helst
# parameter navn har lokalt scope og har ingenting 
# med variabler utenfor funksjonen å gjøre

#def add_two_numbers(x, y):
#    return x + y

def add_two_numbers(a, b):
    return a + b

# bruk den
x = 1
y = 2
svar1 = add_two_numbers(x,y)
print(svar1) # 3
