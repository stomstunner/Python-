# here we want to write the code of sum of two number by using function

def sum_two_num(num1,num2):
    return num1 + num2

a = int(input("Enter first number: "))
b = int(input("Enter first number: "))

sum = sum_two_num(a,b)
print("The sum of",a,"and",b,"is:",sum)