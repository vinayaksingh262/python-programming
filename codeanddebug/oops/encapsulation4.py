class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):  # we can directly access the private member using getter method
        return self.__age


student = Student("vinayak", 22)
print(student.get_age())
