# here we want ki ham multiple inhertance banye battery,engine ka 
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand + "!"
    # now we make a polymorphism mehtod
    def fuel_type(self):
        return "Petrol Or Desial"
    
    # now we make a static method jisse bass hamra class hi uss method ko use kar paye
    
    @staticmethod 
    def general_description():
        return "Car is a means of transport"
    
    # we use decorator named @property for non override
    @property
    def model(self):
        return self.__model

# now we make a child class
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    

# now we initilize two objects from the classess
# my_safari = Car("Tata","Safari")
# my_tesla = ElectricCar("Tesla","Super x","85kwh")

# now we call the methods of both classess
# print(my_safari.get_brand())
# print(my_safari.model)
# print(my_safari.fullname())
# print(my_safari.fuel_type())

# print("Tesla ha ha")
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.fullname())
# print(my_tesla.battery_size)
# print(my_tesla.fuel_type())

# print(my_safari.general_description())
# print(Car.general_description())

# override code
# my_safari.model ="City"
# print(my_safari.model)
# and we can use that attribute as a varibale not as a method but hamne usee mehtod hi banaya tha

class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

