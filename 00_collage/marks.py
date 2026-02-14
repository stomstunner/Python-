marks = int(input("Enter your marks: "))
# print(marks)
if marks >= 101:
    print("Enter a good marks")
    exit()

if marks>=90:
    grade = 'A'
  
elif  marks>=80:
    grade = 'B'
  
elif marks>=60:
    grade = 'C'
else :
    grade = 'F'

print("Your Grade is ",grade)