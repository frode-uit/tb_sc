# File name: sc_02_06.py
# 1. Opprette strenger og bruke print-funksjonen
str1 = "Hei"
str2 = "verden"
print("1. Utskrift av strenger:")
print(str1)
print(str2)

# 2. Strengkonkatinering (sammenkobling av strenger)
str3 = str1 + " " + str2
print("\n2. Strengsammenslåing:")
print(str3)

# 3. Indeksering for å hente ut tegn
first_char = str1[0]
second_char = str2[1]
print("\n3. Indeksering for å hente ut tegn:")
print(f"Første tegn i '{str1}' er '{first_char}'")
print(f"Andre tegn i '{str2}' er '{second_char}'")

# 4. Multiplikasjon av strenger
str4 = str1 * 3
print("\n4. Multiplikasjon av strenger:")
print(str4)

# 5. Kombinasjon av flere operasjoner
str5 = (str1 + " ") * 2 + str2
print("\n5. Kombinasjon av flere operasjoner:")
print(str5)

# 6. Bruk av vanlige str-metoder
upper_str = str3.upper()
lower_str = str3.lower()
title_str = str3.title()
print("\n6. Bruk av vanlige str-metoder:")
print(f"Uppercase: {upper_str}")
print(f"Lowercase: {lower_str}")
print(f"Titlecase: {title_str}")