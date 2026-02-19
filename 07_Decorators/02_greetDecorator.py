# Problem: Create a decorator to print the function name and the values of its arguments every time the function
# is called.

# lets make a decorator
# def debug(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper
# most basic decorator



def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        # now we make for kwargs
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        
        # now we print he value of args and kwargs
        print(f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper




# lets make a funtion jisme ham decorator lagaenge
@debug
def greet(name,greeting ="Hello"):
    return print(f"{greeting},{name}")

greet("ujjwal",greeting ="hi")

