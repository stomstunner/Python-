# x = {"masala","lemon","ginger"}
# y= enumerate(x)
# y
# # enumerate object at 0x00000279BF6C6430>
# list(y)
# [(0, 'lemon'), (1, 'ginger'), (2, 'masala')]


# print(type(y))
# we can convert the list in a key value pair by just wriing in the enumerated


#now we can see how enumarate help use to numbering the list
# list se ham 2 tuple bana sakte hai
 
# list = [{'name':'ujjwal','time':'2min'}, {'name':'nirmal','time':'3min'}]       
# list
# [{'name': 'ujjwal', 'time': '2min'}, {'name': 'nirmal', 'time': '3min'}]
# enumerate(list,start=1)
# # enumerate object at 0x00000242E831F9C0>
# for i in enumerate(list,start=1):
#      print(i)

# (1, {'name': 'ujjwal', 'time': '2min'})
# (2, {'name': 'nirmal', 'time': '3min'})


#==============================
# for i in enumerate(list, start=1) :
#     print(i)

# (1, {'name': 'chai', 'time' : '2min' })
# (2, {'name' : 'code', 'time' : '3min'})
# for i, video in enumerate(list, start=1) :
#     print(f"{i}, {video['name']}")
    # here video ek dictniory hai jisko ager hame print karna hai toh hame video the uske ander variable ka naame likhna parte hai

# 1, chai
# 2, code