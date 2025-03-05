from datetime import datetime


class Calender:
    def __init__(self):
        self.events = []

    def add_events(self, event_name):
        self.events.append(event_name)

    def display(self):
        print(f"events - {self.events}")

    @staticmethod
    def is_weekend(date):
        if date.weekday() > 4:
            print("it is a weekend")
        else:
            print("it is a weekday")


obj = Calender()
obj.add_events("movie")
obj.add_events("python")
obj.add_events("dinner")
obj.display()
currentdate = datetime.now()
Calender.is_weekend(currentdate)
