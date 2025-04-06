# SOLUTION 05
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol, Diesel or CNG"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

car1 = ElectricCar("Audi", "e-tron gt", "100kwh")
print(car1.fuel_type())

car2 = Car("BMW", "i8")
print(car2.fuel_type())