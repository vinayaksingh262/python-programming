class Father:
    father_name = " "

    def displayFatherName(self):
        print(f"father name : {self.father_name}")


class Mother:
    mother_name = " "

    def displayMotherName(self):
        print(f"mother name : {self.mother_name}")


class Child(Father, Mother):
    child_name = " "

    def displayChildName(self):
        print(f"child name : {self.child_name}")

    def show_details(self):
        self.displayFatherName()
        self.displayMotherName()
        self.displayChildName()


c1 = Child()
c1.father_name = "sushil"
c1.mother_name = "kiran"
c1.child_name = "vinayak"
c1.show_details()
