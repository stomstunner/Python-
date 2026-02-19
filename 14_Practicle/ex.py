# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     print("* " * i)

# Python program to print Full Pyramid pattern

# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("* " * i)
# # Name of Student: and  Roll No.: 
# print("Program executed by Ujjwal Kumar, Roll No.: 1324547")

# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     print("* " * i)

# # Name of Student: and  Roll No.: 
# print("Program executed by Ujjwal Kumar, Roll No.: 1324547")

n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# Name of Student: and  Roll No.: 
print("Program executed by Ujjwal Kumar, Roll No.: 1324547")
