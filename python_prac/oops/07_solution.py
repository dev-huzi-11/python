# SOLUTION 07

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "A car is a four-wheeled motor vehicle designed for transporting people, offering comfort, performance, and safety features."

    def carIntro(self):
        return f"Brand: {self.brand}, Model: {self.model}"
    
car1 = Car("Honda", "Civic")
print(car1.carIntro())
print(car1.general_description())
print(Car.general_description())