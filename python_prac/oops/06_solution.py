# SOLUTION 06

class Car:
    total_count = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_count += 1

    def carIntro(self):
        return f"Brand: {self.brand}, Model: {self.model}"
    
car1 = Car("Audi", "R8")
print(car1.carIntro())

car2 = Car("BMW", "i8")
print(car2.carIntro())

car3 = Car("Mercedez", "GLS 600")
print(car3.carIntro())

print(Car.total_count)