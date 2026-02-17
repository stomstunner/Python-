m = int(input("Enter a number : "))
fact = 1
n=m
while n > 0:
    fact *= n
    n -= 1
    
print("The factorial of",m,'is:',fact)