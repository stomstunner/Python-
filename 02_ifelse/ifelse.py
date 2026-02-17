# here we are writting the code for if elese statement taking input from the user then we use it in the code

age = int(input("Enter the age : "))
# print(age)

if age<13:
    print("Child")
elif age<20:
    print("Teen")
elif age<60:
    print("Adult")
else:
    print("Senior")