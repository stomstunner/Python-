# here in this program we see the usage of args 
# when we use args then we can pass multiple values in the defination and use it in a single defination 

def sum_all(*args):
    # args recive tuple from the arguments 
    # here args is an parameter that recive multiple arguments(* indeictes)
    return sum(args)
# this is an built in function for the addtion of multiple number
    
print(sum_all(1,2,3,4))
# def sum_all(*args):
#     a = 0
#     for i in args:
#         a +=i
#         print(i)
#     return a
    
# print(sum_all(1,2,3,4))