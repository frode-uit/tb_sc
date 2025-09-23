# file: sc_08_use_Account3.py
from sc_08_Account3 import Account

account1 = Account("123", "456", 1000, 2.5)
account1.deposit(500)
account1.withdraw(200)
account1.add_monthly_interest()
account1.print_transactions()

# Bruk av properties
print(f"\nSaldo etter transaksjoner: {account1.balance:.2f}")
print(f"Rentesats: {account1.interest}%")

# Endre saldo og rente via properties
account1.balance = 2000
account1.interest = 3.0
print(f"\nNy saldo: {account1.balance:.2f}")