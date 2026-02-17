# num = int(input("Enter a number: "))
# is_Prime = True
# if num>1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             is_Prime = False
#             break
# print(is_Prime)

# this code is for prime numbers 
# prime number  1 or that number which is devisible by itself only


num = int(input("Enter a number : "))
is_prime = True
for i in range(2,num):
    if (num%i) == 0:
        is_prime = False
        break
if num == 1:
    print("Neither Prime Nor Composite")
elif is_prime == True:
    print(num,"is a prime numner")
else:
    print(num,"is not a prime number")

