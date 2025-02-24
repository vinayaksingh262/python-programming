class Father:
    def __init__(self):
        self.father_name = input("Enter father name :")
        self._bank_balance = int(input("Enter a bank balance :"))
        self.__phone_model = input("Enter phone model :")

    def display(self):
        print(f"fathers name : {self.father_name}")
        print(f"bank_balance : {self._bank_balance}")
        print(f"phone_model : {self.__phone_model}")


class Child(Father):
    def __init__(self):
        super().__init__()
        self.child_name = input("Enter child name :")

    def displayChildInfo(self):
        print(f"child name {self.child_name}")
        print(f"my father bank balance is {self._bank_balance} rupees...")


c1 = Child()
c1.displayChildInfo()
