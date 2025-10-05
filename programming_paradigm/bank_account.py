# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute to store balance
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount > self.__account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance}")
