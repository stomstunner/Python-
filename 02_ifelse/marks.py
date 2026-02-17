# here we are writting the code for just a grade if else
score = int(input("Enter Your Score: "))
if score >=101:
    print("Enter a valid Score")
    exit()

if score >= 90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'
print("Your Grade is ",grade)