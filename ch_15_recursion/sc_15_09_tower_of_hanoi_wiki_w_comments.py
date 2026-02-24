# file : ch_15_09_tower_of_hanoi_wiki_w_comments.py
# Tower of Hanoi solution based on Wikipedia description

def hanoi(n, source, dest, help):
    # Base case: Når det bare er én skive igjen,
    # kan den flyttes direkte fra source til dest.
    # Dette er sluttpunktet (stoppbetingelsen) for EN
    # rekursjonsgren.
    # Merk: Base case kjøres mange ganger totalt,
    # én gang for hver gren i rekursjonstreet som ender
    # i n == 1.
    if n == 1:
        print(f"Move disk from {source} to {dest}")
        return

    # Linje 12–14: Steg 1 i den rekursive strukturen.
    # Før vi kan flytte den største skiven (disk n), må vi
    # "rydde toppen":
    # Flytt de n−1 mindre skivene fra source til help.
    # Merk at pinnenes roller BYTTES: help blir "dest"
    # i dette delproblemet, og dest blir "help".
    # Dette er helt nødvendig for å rotere oppgaven.
    hanoi(n - 1, source, help, dest)

    # Linje 18: Steg 2 i den rekursive strukturen.
    # Nå er alle mindre skiver flyttet unna, og den
    # største skiven er frigjort.
    # Derfor kan vi nå gjøre "det store trekket":
    # flytt disk n til dest.
    # print() MÅ stå akkurat her fordi dette trekket
    # må skje:
    # - etter at toppen er ryddet (linje 12–17)
    # - før vi kan bygge tårnet opp igjen (linje 25–29)
    print(f"Move disk from {source} to {dest}")

    # Linje 25–29: Steg 3 i rekursjonen.
    # Etter at den største skiven er flyttet, må de
    # n−1 mindre skivene flyttes fra help til dest slik
    # at de havner oppå den største.
    # Igjen bytter pinnene roller: help er nå "source",
    # dest er "dest", og source fungerer som midlertidig
    # pinne.
    # Dette steget speiler første rekursive kall
    # (linje 12–17), men nå "bygger vi opp tårnet igjen"
    # på dest.
    hanoi(n - 1, help, dest, source)

# Example call:
# Flytt 3 skiver fra A til C ved hjelp av B.
hanoi(3, "A", "C", "B")
