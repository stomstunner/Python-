# here we write the code sum of given even numbers 

n = int(input("Enter a number : "))
sum_count = 0
for i in range(1,n+1):
    if i%2 == 0:
        sum_count+=i
print("The sum of even nummber till 0 to",n," is : ", sum_count)