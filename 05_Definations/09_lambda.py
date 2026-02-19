# here we learn about the lambda function , beacause if we want ki kam 1 hi line me koi chota sa funtion use kar le toh uske likhne ka lamnda function ek accha tarika hai

# def cube(x):
#     return x ** 3
# print(cube(5))

# ab uper wla ko ham ek hi line me kaisse likhe

cube = lambda x : x ** 3

print(cube(3))
# but we cannot do this
#  anothercube = cube(3)
# because the cube is varible that holds the whole defination of a lamnda x (lambda x : x ** 3 is  sabb ka vlaue ab cube hai )