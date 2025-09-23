# file: sc_03_03_to_decimal.py

# Konvertere fra binært til desimalt
# Utgangspunkt: en streng som representerer et bitmønster
# Teknikk: plukke ut siffer for siffer og multiplisere med grunntallet
# opphøyd i posisjonen til tallet

binary_string = "1010101101101"
result = 0

pos = len(binary_string) - 1 # Det vi skal opphøye sifferet i
for ch in binary_string:
    result = result + int(ch) * 2** pos
    pos -= 1

print(result) # 5485

# Konvertere fra hex til desimalt
# Utgangspunkt: en streng som representerer et hex tall
# Teknikk: plukke ut siffer for siffer og multiplisere med grunntallet
# opphøyd i posisjonen til tallet

hex_string = "156D"
result = 0

pos = len(hex_string) - 1 # Det vi skal opphøye sifferet i
for ch in hex_string:
    if (ch >= 'A' and ch <= 'F'):
        digit = (ord(ch) - ord('A') + 10)
    else:
        digit = int(ch)

    result = result + digit * 16 ** pos
    pos -= 1

print(result) # 5485

