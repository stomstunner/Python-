# Star triangle space first
num = int(input("Enter the row number: "))
for i in range(num+1):
    for j in range(num+1):
        if i + j <= num:
            print(" ",end="")
        else:
            print("*",end="")
    print("")
    
# from while loop
i = 0
while i <= num:
    j = 0
    while j <= num:
        if i + j <= num:
            print(" ", end="")
        else:
            print("*", end="")
        j += 1
    print("")
    i += 1