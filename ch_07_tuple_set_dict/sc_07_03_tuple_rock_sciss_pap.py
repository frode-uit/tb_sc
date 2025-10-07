# file: sc_07_03_tuple_rock_sciss_pap.py
import random
def stein_saks_papir():
    """Implementerer stein-saks-papir med tuple unpacking og pattern matching"""
    
    print("Stein-saks-papir-spill")
    print("0: Stein, 1: Saks, 2: Papir")
    
    bruker = int(input("Velg 0 (stein), 1 (saks), 2 (papir): "))
    maskin = random.randint(0, 2)
    
    def valg_navn(kast):
        """Konverterer tall til navn med pattern matching"""
        match kast:
            case 0: return "Stein"
            case 1: return "Saks"
            case 2: return "Papir"
    
    # Vis valg
    print(f"Du valgte: {valg_navn(bruker)}")
    print(f"Maskinen valgte: {valg_navn(maskin)}")
    
    # Analyser resultat med tuple unpacking og pattern matching
    match (bruker, maskin):
        case (a, b) if a == b:  # Tuple unpacking i pattern
            print("Uavgjort!")
        case (0, 1) | (1, 2) | (2, 0):  # Stein slår saks, etc.
            print("Du vant!")
        case _:
            print("Du tapte!")

# Kjør spillet
stein_saks_papir()
