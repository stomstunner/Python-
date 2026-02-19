# in this code we see how to keep the track of how many car object created
# simple answer is that ki hamara class me object utni hi baar banta hai jitni baar hamra constructor chalta hai 

# here we write the code of polymorphish jisme ham 2 same naam ke methods banayenge jo ki hame return karege diffrent results

class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        # we have to mathod jisse ham class ke ander ke varibale ko use kar sakte hai ek toh ahi self and the other one is class name itself
        # self.total_car +=1
        Car.total_car +=1
    
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

# now to know hamra class kitni baar call hua hai ham just total_car kae value ko print karwa dete hai uske liye bhi hamra pass 2 methoda hai ek toh bass jo object hai usska naam likh ke total_car ko access kar sakte hai aur ther other one is Class name  dot thern total_car ka naam

# print(my_safari.total_car)
# print(Car.total_car)