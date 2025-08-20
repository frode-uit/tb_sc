# file: sc_07_useAccount1.py
from sc_07_Account1 import Account

account1 = Account(1, 1000, 50000, 7)
account2 = Account(2, 1001, 10000, 5)
print(account1)
print(account2)
# account1.deposit(500)
Account.deposit(account1, 500)
print(f'New balance after depositing: {account1.get_balance()}')
account1.withdraw(1000)
print(f'New balance after withdrawal: {account1.get_balance()}')
account1.add_monthly_interest()
print(f'New balance after monthly interest: {account1._balance}')