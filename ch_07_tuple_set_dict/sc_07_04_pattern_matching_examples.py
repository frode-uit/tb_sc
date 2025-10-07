# file: sc_07_04_pattern_matching_examples.py
import sys

def demo_pattern_matching():
    """Demonstrerer pattern matching med ulike input-typer"""
    
    print("Pattern matching demo")
    print("Eksempler på gyldige kommandoer:")
    print('- "quit" for å avslutte')
    print('- ["save", "filnavn.txt"] for å lagre til fil')
    print('- Skriv quit for å avslutte demoen')
    
    while True:
        print("\nSkriv en kommando (eller 'demo' for eksempler):")
        
        # Simuler ulike typer input
        user_choice = input("> ")
        
        if user_choice == "demo":
            # Demonstrer begge patterns
            demo_inputs = [
                "quit",
                ["save", "min_fil.txt"]
            ]
            
            for bruker_input in demo_inputs:
                print(f"\nTester input: {bruker_input}")
                process_command(bruker_input)
                
        elif user_choice == "quit":
            break
        else:
            # Parse input som string eller liste
            if user_choice.startswith('[') and user_choice.endswith(']'):
                # Enkel parsing av liste-format: ["save", "fil.txt"]
                try:
                    import ast
                    bruker_input = ast.literal_eval(user_choice)
                    process_command(bruker_input)
                except:
                    print("Ugyldig liste-format")
            else:
                process_command(user_choice)

def process_command(bruker_input):
    """Behandler kommandoer med pattern matching"""
    match bruker_input:
        case "quit":  # streng
            print("Avslutter programmet...")
            return "quit"
            
        case ["save", filename]:  # liste med eksakt 2 elementer
            print(f"Lagrer til fil: {filename}")
            # Her kunne vi faktisk lagre til fil
            with open(filename, 'w') as f:
                f.write("Dette er lagret innhold\n")
            print(f"Fil '{filename}' er lagret!")
            
        case _:  # default case
            print(f"Ukjent kommando: {bruker_input}")

if __name__ == "__main__":
    demo_pattern_matching()