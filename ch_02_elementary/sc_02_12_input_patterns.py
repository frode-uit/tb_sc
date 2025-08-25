# file : sc_02_12_input_patterns

# fjerne blanke, samt konvertere til små bokstaver
svar = input("Skriv ja eller nei: ").strip().lower()
print(f"Du skrev: {svar}")

# validering mot en liste av gyldige svar
valg = input("Velg [ja/nei] ").lower()
if valg not in ["ja", "nei"]:
    print("Ugyldig valg.")


# Gjenta valg til det er gyldig
svar = ""
while svar not in ['a', 'b', 'c']:
    svar = input("Velg alternativ [a/b/c]: ").lower()
print(f"Du valgte alternativ {svar}")

# Input med typekonvertering og feilhåndtering
while True:
    try:
        tall = int(input("Skriv inn et heltall: "))
        break
    except ValueError:
        print("Ugyldig input, prøv igjen.")

print(f"Du skrev inn tallet {tall}")

# input med standardverdi
def ask(melding, standard="ja"):
    svar = input(f"{melding} ({standard}): ").strip().lower()
    return svar if svar else standard

resultat = ask("Vil du fortsette?")
print(f"Du svarte: {resultat}")