# file: sc_08_use_Account2.py
from sc_08_Account2 import Account

account1 = Account(1, 1000, 50000, 7)

# Les attributter direkte
print("Kundenr:", account1._cust_id)
print("account1nr:", account1._account_no)
print("Saldo:", account1._balance)
print("Rente:", account1._interest)

# Endre attributter direkte
account1._balance = 500
account1._interest = 3.5
print("Ny saldo:", account1._balance)
print("Ny rente:", account1._interest)

# Gjør innskudd og uttak
account1.deposit(200)
account1.withdraw(100)

# Skriv ut transaksjoner
def print_transactions(account):
    print("Dato og tid           | Type     |   Beløp")
    print("-" * 42)
    for trans in account._transactions:
        print(trans)

print_transactions(account1)

# Skriv ut account1info
print(account1)
