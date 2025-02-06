class Student:
    def __init__(self):
        self.name = input("Enetr name =")
        self.age = int(input("Enter age ="))
        self.roll_no = int(input("Enter roll no ="))
        self.gender = input("Enter your gender =")

    def info(self):
        print(f"roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")


s1 = Student()
print("----------")
s1.info()
