# file: sc_17_03_regex_intro.py
# re-modulen gir kraftige verktøy for mønstergjenkjenning i tekst.
# Dette kalles regulære uttrykk (regex).
import re

# Python har allerede enkle måter å søke i tekst.
s = "fizzbuzz and the number 123 in a string"

# in-operator returnerer True hvis substring finnes i strengen.
if "123" in s:
    print("in: found 123")

# find() og rfind() returnerer posisjonen til første og siste forekomst,
# eller -1 hvis ikke funnet.
start_pos = s.find("123")
print("find():", start_pos)

last_pos = s.rfind("123")
print("rfind():", last_pos)

#### Start rene regex-eksempler ###
s = "fizz123buzz"

# re.search() returnerer match-objekt ved treff, ellers None.
# Regex "123" leses som: bokstavelig teksten 123.
match = re.search("123", s)

if match:
    print("Fant et treff:", match.group())
else:
    print("Ingen treff")

# Viser bruk av search() og findall().
# Merk bruk av raw string, dvs. en r foran pattern-strengen.
# Koden burde hatt en else-gren, men den er utelatt pga. plasshensyn.

# Matcher tre påfølgende sifre.
s = "fizz123buzz"
# [0-9] betyr ett siffer fra 0 til 9.
# [0-9][0-9][0-9] leses som: tre sifre etter hverandre.
match = re.search(r"[0-9][0-9][0-9]", s)
if match:
    # Utskrift: Fant et treff: 123
    print("Fant et treff:", match.group())

# Samme som ovenfor, men med metasekvensen \d.
# \d betyr ett siffer.
# \d\d\d leses som: tre sifre etter hverandre.
match = re.search(r"\d\d\d", s)  # Ville ikke fungert uten raw string.
if match:
    # Utskrift: Fant et treff: 123
    print("Fant et treff:", match.group())

# Matcher et hvilket som helst tegn mellom '1' og '3'.
s = "fizz1a3buzz"
# 1.3 leses som: '1', deretter ett vilkårlig tegn (.), deretter '3'.
match = re.search(r"1.3", s)
if match:
    # Utskrift: Fant et treff: 1a3
    print("Fant et treff:", match.group())

# Matcher et punktum.
# Siden . er en metakarakter, må vi escape med \.
s = "fizz.123buzz"
# \. leses som: et bokstavelig punktum.
match = re.search(r"\.", s)
if match:
    print("Fant et treff:", match.group())  # Utskrift: Fant et treff: .

# Demonstrerer bruk av anker.
# Matcher starten av strengen.
s = "fizz123buzz"
# ^fizz leses som: strengen må starte med "fizz".
match = re.search(r"^fizz", s)
if match:
    # Utskrift: Fant et treff: fizz
    print("Fant et treff:", match.group())

# Matcher slutten av strengen.
s = "fizz123buzz"
# buzz$ leses som: strengen må slutte med "buzz".
match = re.search(r"buzz$", s)
if match:
    # Utskrift: Fant et treff: buzz
    print("Fant et treff:", match.group())

# Bruk av findall() for å finne alle forekomster av tre sifre.
s = "abc123def456ghi789"
# \d\d\d leses som: tre sifre etter hverandre.
matches = re.findall(r"\d\d\d", s)
print(
    "Alle treff med findall:",
    matches,
)  # Utskrift: ['123', '456', '789']

# Bruk av findall() for å finne alle forekomster av enten 'f' eller 'b'.
s = "fizzbuzz"
# [fb] leses som: ett tegn som enten er 'f' eller 'b'.
matches = re.findall(r"[fb]", s)
print(
    "Alle treff med findall:",
    matches,
)  # Utskrift: ['f', 'b']

# Bruk av findall() for å finne alle forekomster av 1?3-mønster.
s = "fizz1a3buzz1b3"
# 1.3 leses som: '1', ett vilkårlig tegn, '3'.
matches = re.findall(r"1.3", s)
print(
    "Alle treff med findall:",
    matches,
)  # Utskrift: ['1a3', '1b3']

# fullmatch() kontra findall():
# - findall() finner alle deltreff i en større tekst.
# - fullmatch() krever at HELE strengen passer mønsteret.
s = "abc123def456"
# \d{3} leses som: nøyaktig tre sifre.
print("findall på større tekst:", re.findall(r"\d{3}", s))  # ['123', '456']

s = "123"
# Her må hele strengen være nøyaktig tre sifre for å gi True.
print("fullmatch på '123':", bool(re.fullmatch(r"\d{3}", s)))  # True

s = "abc123"
# Her feiler fullmatch fordi hele strengen ikke er bare tre sifre.
print("fullmatch på 'abc123':", bool(re.fullmatch(r"\d{3}", s)))  # False

# Eksempel på bruk av {n} for å matche nøyaktig n forekomster.
s = "aaaabbbbcccc"
# a{4} leses som: nøyaktig fire 'a' etter hverandre.
matches = re.findall(r"a{4}", s)
print("Alle treff med {n}:", matches)  # Utskrift: ['aaaa']

# Eksempel på bruk av {n,} for å matche minst n forekomster.
# b{2,} leses som: minst to 'b' etter hverandre.
matches = re.findall(r"b{2,}", s)
print("Alle treff med {n,}:", matches)  # Utskrift: ['bbbb']

# Eksempel på bruk av {n,m} for å matche mellom n og m forekomster.
# c{2,3} leses som: to eller tre 'c' etter hverandre.
matches = re.findall(r"c{2,3}", s)
print("Alle treff med {n,m}:", matches)  # Utskrift: ['ccc']