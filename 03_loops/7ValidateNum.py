# here we have to write a program where we have to take input jab tak ki number 1 aur 10 ke bich ka na ho

while True:
    number = int(input("Enter a number between 1 an 10 : "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Try again!")