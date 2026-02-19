# here we write the code of polymorphish jisme ham 2 same naam ke methods banayenge jo ki hame return karege diffrent results

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!"
    # now we make a polymorphism mehtod
    def fuel_type(self):
        return "Petrol Or Desial"

# now we make a child class
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    

# now we initilize two objects from the classess
my_safari = Car("Tata","Safari")
my_tesla = ElectricCar("Tesla","Super x","85kwh")

# now we call the methods of both classess
print(my_safari.get_brand())
print(my_safari.model)
print(my_safari.fullname())
print(my_safari.fuel_type())

print("Tesla ha ha")
print(my_tesla.get_brand())
print(my_tesla.model)
print(my_tesla.fullname())
print(my_tesla.battery_size)
print(my_tesla.fuel_type())