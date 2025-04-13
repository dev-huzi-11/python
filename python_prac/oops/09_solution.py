# SOLUTION 09
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

car1 = ElectricCar("Audi", "e-tron gt", "100kwh")

print(isinstance(car1, Car))
print(isinstance(car1, ElectricCar))