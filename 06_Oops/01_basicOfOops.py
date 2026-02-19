# here we learn about the basis of the oops 
# lets make the class
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
# __init__ is a constructor is a def which is firstly called

    def hello():
        print("Hello Ujjwal")
    # 
    def full_name(self):
        return f"{self.brand} {self.model}"

my_Car = Car("Toyota","Corolla")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name()) 
# fullname is a def thats why we use ()

my_New_Car = Car("Tata","Land Crusior")
print(my_New_Car.brand)
print(my_New_Car.model)

print(Car.__init__)   
print(Car.hello())



# Toyota
# Corolla
# Tata
# Land Crusior
# <function Car.__init__ at 0x000001BC89B47530>
# Hello Ujjwal
# None