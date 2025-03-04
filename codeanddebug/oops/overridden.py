class Father:
    def show(self):
        self.show = print("this is father class")


class Child(Father):
    def show(self):
        Father.show = print("this is child class")


obj = Child()
obj.show()
