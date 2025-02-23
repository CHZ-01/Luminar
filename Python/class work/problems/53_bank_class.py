# Design a class named BankAccount in Python that models a simple bank account.

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient balance.")
        
    def get_balance(self):
        print("Balance:", self.balance)

account1 = BankAccount(12345678910,"Vaisakh",15687.47)
account1.deposit(5000.23)
account1.withdraw(2500.98)
account1.get_balance()