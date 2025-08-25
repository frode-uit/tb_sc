# file: sc_05_08.py
# viser at et slicing uttrykk kan stå på venstre side av en tilordning

list1 = [0, 1, 2, 3, 4, 5]
list1[1:4] = [10, 11, 12] # erstatter elementer
print(list1) # [0, 10, 11, 12, 5]

list1[2:4] = [] # fjerner elementer
print(list1) # [0, 10, 5]

list1[1:1] = [99, 100]  # Setter inn to elementer før indeks 1
print(list1) # [0, 99, 100, 10, 5]
