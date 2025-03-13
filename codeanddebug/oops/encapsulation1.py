from random import randint

# public


class Bank:
    def __init__(self):
        self.name = input("enter a name: ")
        self.account_no = randint(100000, 999999)
        self.age = int(input("Enter a age: "))
        self.balance = 0

    def display(self):
        print(f"your name : {self.name}")
        print(f"your account number : {self.account_no}")
        print(f"your age : {self.age}")
        print(f"your balance : {self.balance}")


obj = Bank()
obj.display()
obj.balance = 1
obj.display()
