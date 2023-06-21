# banking_system.py

class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} made to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} made from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

# Usage example
account1 = BankAccount("1234567890", "John Doe", 1000)
account2 = BankAccount("0987654321", "Alice Smith", 500)

account1.deposit(500)
account1.withdraw(200)
account1.get_balance()

account2.deposit(1000)
account2.withdraw(800)
account2.get_balance()
