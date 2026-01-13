# file: sc_08_08_Account4.py
from datetime import datetime

class Transaction:
    def __init__(self, amount, trans_type):
        self._amount = amount
        self._trans_type = trans_type  # "deposit", "withdraw", "interest"
        self._timestamp = datetime.now()

    def __str__(self):
        return f"{self._timestamp:%Y-%m-%d %H:%M:%S} | {self._trans_type.capitalize():8} | {self._amount:8.2f}"


class Account:
    @staticmethod
    def is_valid_account_no(account_no):
        """Returnerer True hvis kontonummeret er et heltall mellom 1000 og 9999."""
        return isinstance(account_no, int) and 1000 <= account_no <= 9999
    
    _next_account_no = 1000  # Klassevariabel: neste ledige kontonummer
    _account_count = 0       # Klassevariabel: antall kontoer opprettet
    _transaction_count = 0   # Klassevariabel: antall transaksjoner utført totalt

    @classmethod
    def set_next_account_no(cls, new_start):
        if new_start > cls._next_account_no and Account.is_valid_account_no(new_start):
            cls._next_account_no = new_start

    @classmethod
    def get_account_count(cls):
        return cls._account_count

    @classmethod
    def get_transaction_count(cls):
        return cls._transaction_count

    def __init__(self, cust_id, start_balance, interest):
        self._cust_id = cust_id
        self._account_no = Account._next_account_no
        Account._next_account_no += 1
        Account._account_count += 1
        self._balance = start_balance
        self._interest = interest
        self._transactions = []
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            print("Saldo kan ikke være negativ!")
        else:
            self._balance = new_balance

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, new_interest):
        if new_interest < 0:
            print("Rente kan ikke være negativ!")
        else:
            self._interest = new_interest
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(Transaction(amount, "deposit"))
            Account._transaction_count += 1
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(Transaction(amount, "withdraw"))
            Account._transaction_count += 1
        return self._balance

    def add_monthly_interest(self):
        monthly_interest = self.calculate_monthly_interest()
        self._balance += monthly_interest
        self._transactions.append(Transaction(monthly_interest, "interest"))
        Account._transaction_count += 1

    def calculate_monthly_interest(self):
        return self._balance * self._interest / 100 / 12

    def get_transactions(self):
        return self._transactions

    def __str__(self):
        return f'''
Customer id  = {self._cust_id}
Account no   = {self._account_no}
Balance      = {self._balance:.2f}
Interest     = {self._interest}%
'''

# Eksempel på bruk:
if __name__ == "__main__":
    # Sett nytt startpunkt for neste ledige kontonummer
    Account.set_next_account_no(2000)

    acc1 = Account("A123", 1000, 2.5)
    acc2 = Account("B456", 500, 1.8)
    acc1.deposit(200)
    acc2.withdraw(100)
    acc1.add_monthly_interest()

    print(acc1)
    print(acc2)
    print(f"Antall kontoer: {Account.get_account_count()}")    
    print(f"Antall transaksjoner: {Account.get_transaction_count()}")

    # Eksempel på bruk av staticmethod:
    test_no = 2345
    if Account.is_valid_account_no(test_no):
        print(f"{test_no} er et gyldig kontonummer.")
    else:
        print(f"{test_no} er IKKE et gyldig kontonummer.")
