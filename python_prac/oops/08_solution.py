# SOLUTION 08

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    def carIntro(self):
        return f"Brand: {self.brand}, Model: {self.model}"
    
    @property
    def model(self):
        return self.__model

    
car1 = Car("Honda", "Civic")
# print(car1.model()) # Error

print(car1.model)