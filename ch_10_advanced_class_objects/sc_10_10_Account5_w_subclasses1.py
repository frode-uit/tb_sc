# file: sc_10_10_Account5_w_subclasses1.py


from datetime import datetime

from abc import ABC, abstractmethod
from datetime import datetime

class Transaction:
    def __init__(self, amount, trans_type):
        self._amount = amount
        self._trans_type = trans_type
        self._timestamp = datetime.now()
    def __str__(self):
        return f"{self._timestamp:%Y-%m-%d %H:%M:%S} | {self._trans_type.capitalize():8} | {self._amount:8.2f}"

class Account(ABC):
    def __init__(self, cust_id, start_balance, interest):
        self._cust_id = cust_id
        self._balance = start_balance
        self._interest = interest
        self._transactions = []

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(Transaction(amount, "deposit"))
        return self._balance

    def add_monthly_interest(self):
        monthly_interest = self.calculate_monthly_interest()
        self._balance += monthly_interest
        self._transactions.append(Transaction(monthly_interest, "interest"))

    def calculate_monthly_interest(self):
        return self._balance * self._interest / 100 / 12

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(Transaction(amount, "withdraw"))
        return self._balance

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"Customer id  = {self._cust_id}\nBalance      = {self._balance:.2f}\nInterest     = {self._interest}%\n"

class SavingsAccount(Account):
    def __init__(self, cust_id, start_balance, interest, savings_goal=0):
        super().__init__(cust_id, start_balance, interest)
        self._savings_goal = savings_goal

    def add_monthly_interest(self):
        # Savings accounts get double interest for demonstration
        monthly_interest = self.calculate_monthly_interest() * 2
        self._balance += monthly_interest
        self._transactions.append(Transaction(monthly_interest, "interest"))
       

    def account_type(self):
        return "SavingsAccount"

class StudentAccount(Account):
    def __init__(self, cust_id, start_balance, interest, student_id=None):
        super().__init__(cust_id, start_balance, interest)
        self._student_id = student_id

    def withdraw(self, amount):
        # Student accounts cannot withdraw more than 1000 at a time
        if amount > 1000:
            print("StudentAccount: Cannot withdraw more than 1000 at a time!")
            return self._balance
        return super.withdraw(amount)

    def account_type(self):
        return "StudentAccount"

class Bank:
    def __init__(self):
        self._accounts = []
        self._savings_count = 0
        self._student_count = 0

    def add_account(self, account):
        self._accounts.append(account)
        if isinstance(account, SavingsAccount):
            self._savings_count += 1
        elif isinstance(account, StudentAccount):
            self._student_count += 1
      

    def print_account_summary(self):
        print(f"Totalt: {len(self._accounts)} kontoer")
        print(f"  SavingsAccount: {self._savings_count}")
        print(f"  StudentAccount: {self._student_count}")
       
    def do_monthly_update(self):
        print("\nMånedlig oppdatering:")
        for acc in self._accounts:
            acc.add_monthly_interest()  # Polymorft kall
            print(f"{acc.account_type()} etter rente: {acc.balance:.2f}")

if __name__ == "__main__":
    bank = Bank()
    # acc1 = Account("A123", 5000, 2.0)  # Kan ikke lenger instansieres direkte
    acc2 = SavingsAccount("B456", 2000, 1.5, savings_goal=10000)
    acc3 = StudentAccount("C789", 1500, 1.2, student_id="STU123")
    bank.add_account(acc2)
    bank.add_account(acc3)

    bank.print_account_summary()

    # Demonstrer polymorfi og isinstance
    for acc in bank._accounts:
        print(f"\nType: {acc.account_type()}")
        acc.deposit(500)
        acc.add_monthly_interest()
        acc.withdraw(1200)
        print(acc)
        # Bruk av isinstance:
        if isinstance(acc, SavingsAccount):
            print(f"  Sparemål: {acc._savings_goal}")
        if isinstance(acc, StudentAccount):
            print(f"  Student-ID: {acc._student_id}")

    bank.do_monthly_update()
