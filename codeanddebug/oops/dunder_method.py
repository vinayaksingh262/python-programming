class Father:
    def __init__(self):
        self.fname = input("enter a father name :")
        self._balance = int(input("Enter a balance :"))
        self.__phonemodel = input("enter a phone model :")

    def __str__(self):
        return f"fathers name :{self.fname} \nfathers balance :{self._balance} \nfathers phone model :{self.__phonemodel}"


obj = Father()

print("--------")
print(obj)
