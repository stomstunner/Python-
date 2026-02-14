marks = int(input("Enter the marks of the student: "))
if marks >= 101:
    print("Enter a valid marks!")
    exit()

if marks >= 90:
    grade = 'First'
elif marks >= 60:
    grade = 'Second'
elif marks >= 40:
    grade = 'Third'
else:
    grade = 'Better Luck Next Time!'

print("You have achived", grade ,"grade.")

