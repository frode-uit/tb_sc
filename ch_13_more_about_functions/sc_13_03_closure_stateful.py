# file: sc_13_03_closure_stateful.py
# Stateful closure - closure som holder på og endrer state

def make_counter(start: int = 0):
    """Lager en teller-funksjon som husker sin egen count."""
    count = start  # Denne variabelen blir "fanget" av closure
    
    def counter():
        nonlocal count  # Tillater oss å endre count fra outer scope
        count += 1
        return count
    
    return counter

# Lag to uavhengige tellere
counter1 = make_counter(0)
counter2 = make_counter(100)

print("Counter 1:")
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print("\nCounter 2:")
print(counter2())  # 101
print(counter2())  # 102

print("\nCounter 1 again:")
print(counter1())  # 4 (fortsetter å telle)


# Mer avansert eksempel: closure med flere funksjoner
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
