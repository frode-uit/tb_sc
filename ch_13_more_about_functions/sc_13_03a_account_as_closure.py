# file: sc_13_03a_account_as_closure.py
# closure med flere funksjoner
def make_account(initial_balance: float = 0):
    """Lager et bankkonto-objekt med closure."""
    balance = initial_balance  # Privat variabel
    
    def deposit(amount: float):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount: float):
        nonlocal balance
        if amount > balance:
            print("Insufficient funds!")
            return balance
        balance -= amount
        return balance
    
    def get_balance():
        return balance
    
    # Returner funksjonene direkte som tuple
    return deposit, withdraw, get_balance

# Bruk account - pakk ut funksjonene
deposit, withdraw, get_balance = make_account(1000)
print("\n--- Bank Account Example ---")
print(f"Initial balance: {get_balance()}")
print(f"After deposit 500: {deposit(500)}")
print(f"After withdraw 200: {withdraw(200)}")
print(f"Final balance: {get_balance()}")

# Prøv å ta ut for mye
withdraw(2000)
