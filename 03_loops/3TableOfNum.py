# here we write the code for user input number's table 1 to 10 but skip the 5th ittration

n = int(input("Enter a number : "))
for  i in range(1,11):
    if i == 5 :
        continue
    print(n,'X',i,'=',n*i)