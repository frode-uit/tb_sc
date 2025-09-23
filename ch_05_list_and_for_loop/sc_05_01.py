# file: sc_05_01.py
# les inn 10 heltall til en liste, summerer og sorter

heltall_liste = []
for i in range(10):
    tall = int(input(f"Skriv inn heltall nr {i + 1} av 10: "))
    heltall_liste.append(tall)

summen = sum(heltall_liste)
print("Summen av de innleste tallene er:", summen)
heltall_liste.sort()
print("Tallene, sortert:", heltall_liste)


