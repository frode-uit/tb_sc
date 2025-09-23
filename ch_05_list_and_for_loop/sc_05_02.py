# file: sc_05_02.py
# Viser ulike måter å initialisere en liste på

# Initialisere en tom liste
number_list = []
# initialisere en tom liste med constructor
number_list2 = list()

# Initialisere en liste med noen verdier
name_list = ["anna", "bjorn", "clara"]
# Initialisere en liste med noen verdier med constructor
name_list2 = list(["john", "paul", "liam"])


# Initialisere en liste med blandet innhold
mixed_list = [1, "tekst", 3.14, True]

# Legge til elementer i listen
number_list.append(1)
number_list.append(2)
number_list2.append(10)

# Endre elementer i en liste med indeksering
name_list[0] = "suzanne"      # Endrer første element
mixed_list[1] = "ny_tekst"    # Endrer andre element

# Skrive ut listene
print(number_list)  # [1, 2]
print(number_list2) # [10]
print(name_list2)   # ['john', 'paul', 'liam']
print(name_list)    # ['suzanne', 'bjorn', 'clara']
print(mixed_list)   # [1, 'ny_tekst', 3.14, True]

# initialisere fra en streng
tekst = "python"
bokstaver = list(tekst)
print(bokstaver)  # ['p', 'y', 't', 'h', 'o', 'n']
ord = list([tekst])
print(ord)  # ['python']
