# in this code we learn about the privatisation of a attributes ...ham uss attribute ko bahar outside of the class toh se nahi kar sakte hai but inside ka class use kar sakte hai

# in this program we discuss about the inheritance feature of the python
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def fullname(self):
#         return f"{self.brand} {self.model}"
    
    # we can make any attribute private by just appling double underscore in front of the varibale name jo ham use kar rahe hai class ke ander
    
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    # get method for better security now our attribute is more private 
    def get_brand(self):
        return self.__brand + "!"

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
# print(my_Electric_Car.brand)
print(my_Electric_Car.get_brand())
print(my_Electric_Car.battery_size)
print(my_Electric_Car.fullname())