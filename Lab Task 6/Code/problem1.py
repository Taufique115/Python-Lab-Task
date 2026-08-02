class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Withdraw amount must be positive")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account: {self.account_number} | Customer: {self.customer_name} | Balance: {self.balance}")


account1 = BankAccount("ACC-001", 5000, "2024-01-15", "Mostafa Jaman Taufique")
account1.check_balance()
account1.deposit(2000)
account1.withdraw(1000)
account1.check_balance()