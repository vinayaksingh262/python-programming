from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(100000000, 999999999)
        self.name = input("Enter your name:")
        self.phone = int(input("Enter your phone number:"))
        self.balance = 0

    def show_balance(self):
        print(f"current balance ={self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw ="))
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance = self.balance - amount

    def deposite(self) -> None:
        amount = int(input("Enter amount to depossite="))
        self.balance += amount


# b1 = Bank()
# b1.show_balance()
# b1.deposite()
# b1.show_balance()
# b1.withdraw()
# b1.show_balance()
# for multiple objects we have to create a lsit
banks = []
x = Bank()
banks.append(x)
y = Bank()
banks.append(y)
banks[0].show_balance()
banks[1].deposite()
banks[1].show_balance()
