# sc_03_02_from_decimal.py

# Konverter desimalt tall til binært
# Utgangspunkt et tall (number) som er en ordinær int
# Teknikk: # Gjøres ved gjentagne % 2 og // 2 beregninger på number,
# bygg opp bit strengen tegn for tegn

number = 5485
result_str = ""

while number > 0:
    next_binary_digit = number % 2
    result_str = chr(next_binary_digit + ord('0')) + result_str
    number = number // 2
print(result_str) # 1010101101101

# Konverter desimalt tall til heksadesimalt
# Teknikk: Gjøres ved gjentagne % 16 og // 16 beregninger på number
# OBS vi må passe på å spesialbehandle hex_digit > 10, skal bli 'A' til 'F'
# Bygg opp hex strengen tegn for tegn

number = 5485
result_str = ""

while number > 0:
    next_hex_digit = number % 16
    if next_hex_digit < 10:
        result_str = chr(next_hex_digit + ord('0')) + result_str
    else:
        result_str = chr((next_hex_digit - 10) + ord('A')) + result_str
    number = number // 16
print(result_str) # 156D