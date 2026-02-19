def area(ht,bs):
    return (ht*bs)/2

input_height = int(input("Enter the height of triangle: "))
input_base = int(input("Enter the base of triangle: "))

a = area(input_height,input_base)
print("The area of triangle is:",a)