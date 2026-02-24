# file: sc_17_04_email_example.py
import re

# En enkel regex for e-post.
# Merk: Regex for e-post kan bli veldig komplisert.
# Dette mønsteret dekker vanlige tilfeller, men ikke absolutt alle.
# \w er en metasekvens som betyr bokstav, tall eller underscore.

EPOST_MOENSTER = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
# Leses slik, fra venstre mot høyre:
# [\w.+-]+ -> lokaldel: ett eller flere ordtegn, ., + eller -.
# Tegnene ., + og - er bokstavelige inni tegnklassen.
# + etter ] betyr: én eller flere tegn fra tegnklassen foran.
# @         -> et bokstavelig @-tegn
# [\w-]+   -> domenenavn: ett eller flere ordtegn eller - (bokstavelig)
# \.        -> et bokstavelig punktum (escape fordi . er metategn)
# [\w.-]+  -> toppdomene/rest: ordtegn, punktum eller bindestrek 


def valider_epost(epost: str) -> bool:
    """Returnerer True hvis hele strengen er en e-postadresse."""
    # Vi bruker fullmatch for å kreve at hele inputen er e-post,
    # slik at vi unngår deltreff og ekstra tegn før/etter adressen.
    return bool(EPOST_MOENSTER.fullmatch(epost))


def finn_alle_eposter(tekst: str) -> list[str]:
    """Finner og returnerer alle e-postadresser i teksten."""
    return EPOST_MOENSTER.findall(tekst)


def main() -> None:
    """Kjører noen enkle eksempler."""
    eposter = [
        "test@example.com",      # Gyldig
        "invalid-email",         # Ugyldig
        "user.name@domain.co",   # Gyldig
        "ola+jobb@uit.no",       # Gyldig: + er lovlig i lokaldelen
        "user@domain",           # Ugyldig (mangler toppdomene)
        "user@domain.c",         # Gyldig, men uvanlig toppdomene
        "test@example.com!!!",   # Ugyldig (ekstra tegn til slutt)
    ]

    print("Validering av enkeltadresser:")
    for epost in eposter:
        status = "gyldig" if valider_epost(epost) else "ugyldig"
        print(f"- {epost!r} er {status}")

    tekst = (
        "Her er noen e-poster: test@example.com, user.name@domain.co, "
        "og en ugyldig: invalid-email."
    )

    print("\nAlle gyldige e-postadresser funnet med findall():")
    print(finn_alle_eposter(tekst))

    print("\nSamme søk med search() i en løkke:")
    start = 0
    while True:
        treff = EPOST_MOENSTER.search(tekst, start)
        if not treff:
            break
        print("- Fant:", treff.group())
        start = treff.end()


if __name__ == "__main__":
    main()