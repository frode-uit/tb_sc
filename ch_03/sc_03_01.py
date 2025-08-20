# file: sc_03_01.py

a = 29  # binært: 11101
b = 15  # binært: 01111

print(f"a = {a} binært: {a:05b}")
print(f"b = {b} binært: {b:05b}")
print(f"b = {b} binært ved hjelp av bin() funksjonen: {bin(b)}")

print("Bitvise operasjoner med a = 29 og b = 15\n")

print(f"a & b  (AND): {a & b}  -> binært: {(a & b):05b}")
print(f"a | b  (OR):  {a | b}  -> binært: {(a | b):05b}")
print(f"a ^ b  (XOR): {a ^ b}  -> binært: {(a ^ b):05b}")
print(f"~a     (NOT): {~a}     -> binært: {(~a):05b} (negativt tall)")
print(f"a << 1 (SHIFT LEFT): {a << 1} -> binært: {(a << 1):05b}")
print(f"a >> 1 (SHIFT RIGHT): {a >> 1} -> binært: {(a >> 1):05b}")
