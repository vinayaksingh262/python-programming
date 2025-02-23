class Car:
    def __init__(self, color, type, mileage, seat_cap) -> None:

        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_cap = seat_cap

    def base_info(self):
        print(f"color={self.color}")
        print(f"type={self.type}")
        print(f"mileage={self.mileage}")
        print(f"seat_cap={self.seat_cap}")


class audi(Car):
    def __init__(self):
        print("audi init")


c1 = audi()
c1.color = "black"
c1.type = "petrol"
c1.mileage = 30
c1.seat_cap = 4
c1.base_info()
