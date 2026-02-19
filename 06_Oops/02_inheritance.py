# in this program we discuss about the inheritance feature of the python
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
                                    # we have to write the parent class in the bracket of the child class 
    def __init__(self,brand,model,battery_size): 
                                    # we have to first wite the constructor for child class jisme ham inheritanced attributes ko likhnge  + self
        super().__init__(brand,model) 
                                    #then we write the super() for conntecting to parent class aur fir uske constructor ka naam aur attributes
        self.battery_size = battery_size
                                    #then we write the main part 

my_Electric_Car = ElectricCar("Tesla","model x","85kWH")
print(my_Electric_Car.model)
print(my_Electric_Car.brand)
print(my_Electric_Car.battery_size)
print(my_Electric_Car.fullname())