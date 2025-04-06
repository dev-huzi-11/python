# SOLUTION 02
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

car1 = Car("Ford", "Raptor")
print(car1.full_name())