from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(100000000, 999999999)
        self.name = input("Enter your name:")
        self.phone = int(input("Enter your phone number:"))
        self.balance = 0

    def show_info(self):
        print(f"account no : {self.account}")
        print(f"name  : {self.name}")
        print(f"balance  : {self.balance}\n")

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
# x = Bank()
# banks.append(x)
# y = Bank()
# banks.append(y)
# banks[0].show_balance()
# banks[1].deposite()
# banks[1].show_balance()
# banks[1].deposite()
# banks[1].show_balance()
while True:
    print("1.Create account")
    print("2.show all accounts detail")
    print("3.Deposite ammount ")
    print("4.withdraw ammount ")
    print("5.transfer ammount ")
    print("6.Exit")
    choice = int(input("Enter a choice ="))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
    elif choice == 2:
        if len(banks) == 0:
            print("not account have been created yet...")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("not account have been created yet...")
        else:
            acc_no = int(input("enter account number to deposite:"))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposite()
                    break
    elif choice == 4:
        if len(banks) == 0:
            print("no accounts have been created yet")
        else:
            acc_no = int(input("Enter account to withdraw money:"))
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break

    elif choice == 5:
        pass

    elif choice == 6:
        break
    else:
        print("invalid choice...")
