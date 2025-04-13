# SOLUTION 10

class Engine:
    def engine_info(self):
        return "This is engine"
    
class Battery:
    def battery_info(self):
        return "This is battery"
    
class ElectricCar(Engine, Battery):
    pass

car1 = ElectricCar()
print(car1.battery_info())
print(car1.engine_info())