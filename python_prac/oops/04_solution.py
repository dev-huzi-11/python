# SOLUTION 04
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f"{self.__brand} is top brand."
    
car1 = Car("Audi", "R8")
# print(car1.__brand) 
print(car1.get_brand())