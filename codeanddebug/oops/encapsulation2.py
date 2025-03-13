from random import randint

# private


class Bank:
    def __init__(self):
        self.name = input("enter a name: ")
        self.__account_no = randint(100000, 999999)
        self.age = int(input("Enter a age: "))
        self.__balance = 0

    def displaybalance(self):  # getter
        print(self.__balance)

    def setbalance(self, newAmount):  # setter
        self.__balance = newAmount

    def display(self):
        print(f"your name : {self.name}")
        print(f"your account number : {self.__account_no}")
        print(f"your age : {self.age}")
        print(f"your balance : {self.__balance}")


obj = Bank()
obj.display()
obj.setbalance(1000)
obj._Bank__balance = 1  # accessing the private members using name mangling
obj.display()
print("---------")
obj.displaybalance()
