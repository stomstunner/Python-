# in this program we learns about the key vlaue argument but for multiple key vlaue argument using **kwargs
# simple key vlaue args defination

# def print_all(name,lastname):
#     print("Name: ",name,"Roll: ",lastname)

# input_name = input("Enter Your Name: ")
# input_lastname = input("Enter Your lastname: ")
# print_all(name =input_name, lastname = input_lastname)

# lets use the **kwargs for multiple vlaues in the parmeter 

def print_all(**kwargs):
    for key, value in kwargs.items():
# here we have to use the kwargs items because we are using the 1 items at a time 
        print(f"{key}:{value}")

print_all(name = "ujjwal",roll = "1324547",cls = "BCA")
print("")
print_all(name = "nirmal",roll = "1324549",cls = "MCA")
print("")
print_all(name = "Ujjwal")
# here we are passing the arguments in the key and vlaue pair and giving to the **kwargs 
