# here we write the program where we pass 1 argument and the defination return 2 value 1 is area and the 2nd is circumference of circle
import math
def area_circum(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi *radius
    return area,circumference

input_num = int(input("Enter the radius of circle: "))

a,c=area_circum(input_num)
print("The area of circle is:",round(a,2),"and circumference is:",round(c,2))
