# file: sc_00_01.py
# En person ønsker å komme inn på en klubb. For å få tilgang må følgende regler være oppfylt:
# Personen må være 18 år eller eldre.
# Personen må ha gyldig ID.
# Hvis personen er under 21 år, må de ikke være påvirket av alkohol.

alder = 19
har_id = True
er_pavirket = False

if alder >= 18 and har_id == True:
    if alder < 21 and er_pavirket == True:
        print("Tilgang nektet: Du er under 21 og påvirket.")
    else:
        print("Tilgang tillatt.")
else:
    print("Tilgang nektet: Du oppfyller ikke kravene.")

# alternativ koding
if alder >= 18 and har_id and (alder >= 21 or not er_pavirket):
    print("Tilgang tillatt.")
else:
    print("Tilgang nektet: Du oppfyller ikke kravene.")
