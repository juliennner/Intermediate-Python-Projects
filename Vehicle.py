# Defining the number of passengers and fare depending on the type of vehicle
class Vehicle:

    def __init__(self, name, mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Isuzu Bus", 10, 50)
print(School_bus.seating_capacity())

class Vehicle:

    def __init__(self, name, mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Van(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=20):
        return super().seating_capacity(capacity=20)

School_van = Van("School Nissan Van", 20, 20)
print(School_van.seating_capacity())


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 200

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 15 / 100
        return amount


School_bus = Bus("School Isuzu Bus", 10, 50)
print("Total Bus fare is:", School_bus.fare())

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 200

class Van(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
School_van = Van("School Nissan Van", 20, 20)
print("Total Van fare is:", School_van.fare())




