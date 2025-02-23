class Car:
    def __init__(self):
        self.color = input("Enter car color :")
        self.type = input("Enter car type :")
        self.mileage = input("Enter car mileage :")
        self.seat_cap = input("Enter seat capacity :")

    def base_info(self):
        print(f"color={self.color}")
        print(f"type={self.type}")
        print(f"mileage={self.mileage}")
        print(f"seat_cap={self.seat_cap}")


class audi(Car):
    def __init__(self):
        super().__init__()
        self.electric = input("Enter electric : ")
        self.city = input("Enter city : ")

    def audi_info(self):
        print(f"Electric:{self.electric}")
        print(f"city:{self.city}")

    def show_info(self):
        self.base_info()
        self.audi_info()


c1 = audi()
c1.show_info()
