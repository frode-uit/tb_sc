# file: sc_05_05_slicing_demo.py
s = "Helloworld"

print(s[0:5])             # "Hello" – fra indeks 0 til 4
print(s[:])               # "Helloworld" – hele strengen
print(s[::])              # "Helloworld" – hele strengen
print(s[None:])           # "Helloworld" – None tolkes som
                          # standardverdi, dvs 0
print(s[0:len(s)])        # "Helloworld" – hele strengen
print(s[:None])           # "Helloworld" – None tolkes som
                          # standardverdi, dvs len(s)

print(s[0:5:2])           # "Hlo" – annethvert tegn fra
                          # indeks 0 til 4
print(s[::-1])            # "dlrowolleH" – reverserer hele
                          # strengen, standardverdier brukes
print(s[None:None:-1])    # "dlrowolleH" - reverserer hele
                          # strengen, standardverdier brukes
print(s[5:0:-1])          # "wolle" – baklengs fra indeks 5
                          # til 1
print(s[5::-1])           # "olleH" – baklengs fra indeks 5
                          # til starten

# slicing på en liste, samme regler som for strenger
list1 = ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(list1[::-1])  # ['d', 'l', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'H']
