# File name: sc_02_07.py

# int
print(bool(0))        # False
print(bool(1))        # True
print(bool(-5))       # True

# float
print(bool(0.0))      # False
print(bool(3.14))     # True
print(bool(-2.7))     # True

# str
print(bool(""))       # False
print(bool("tekst"))  # True
print(bool(" "))      # True

# int
if (0):
    print("if(0) evaluerte til True")
else:
    print("if(0) evaluerte til False")

if (-5):
    print("if(-5) evaluerte til True")
else:
    print("if(-5) evaluerte til False")

# str 
if (''):
    print("if('') evaluerte til True")
else:
    print("if('') evaluerte til False")

if ('tekst'):
    print("if('tekst') evaluerte til True")
else:
    print("if('tekst') evaluerte til False")