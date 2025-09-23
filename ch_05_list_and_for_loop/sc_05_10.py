list1= []
print("Gi inn 3 tall, ett pr linje")
for i in range(3):
    tall = int(input(f"Tall {i+1}: "))
    list1.append(tall)
print("Tallene du ga inn er:", list1)

s = input("Gi inn tre tall på en linje, separert med mellomrom:")
list2 = s.split()

# lag kode som konverterer strenger i list2 til heltall
for i in range(len(list2)):
    list2[i] = int(list2[i])
print("Tallene du ga inn er:", list2)

# alternativt kan vi bruke list comprehension
list3 = [int(x) for x in s.split()]
print("Tallene du ga inn er:", list3)
