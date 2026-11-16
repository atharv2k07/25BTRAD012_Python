class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print("Balance:", self.balance)

b = Bank(5000)

b.deposit(2000)
b.withdraw(1000)
b.display()