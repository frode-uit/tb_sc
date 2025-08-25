# file: sc_05_05.py
s = "Helloworld"

print(s[0:5])             # "Hello" – fra indeks 0 til 4
print(s[:])               # "Helloworld" – hele strengen
print(s[::])              # "Helloworld" – hele strengen
print(s[None:])           # "Helloworld" – None tolkes som
                          # standardverdi
print(s[:None])           # "Helloworld"
print(s[0:len(s)])        # "Helloworld"
print(s[0:5:2])           # "Hlo" – annethvert tegn fra
                          # indeks 0 til 4
print(s[::-1])            # "dlrowolleH" – reverserer
                          # strengen
print(s[len(s)-1::-1])    # "dlrowolleH" – reverserer fra
                          # siste tegn
print(s[None:None:-1])    # "dlrowolleH"
print(s[5:0:-1])          # "wolle" – baklengs fra indeks 5
                          # til 1
print(s[5::-1])           # "olleH" – baklengs fra indeks 5
                          # til starten

list1 = ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(list1[::-1])  # ['d', 'l', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'H']
