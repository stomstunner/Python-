# decorator is naothig but a tool booth jo ki pahle method ke call hone pe khud ke ander se pass hone deta hai 



import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

# now we can use this timer fucntion as a decorator

@timer
def example_function(n):
    # start = time.time()
    time.sleep(n)
    # end = time.time()
    # print(end-start)

# call the example_fucntion

example_function(2)