import time
print("How are you")

name = "Ujjwal"

print(name)

# =========================================================

# iter tool

# >>> myList =[1,2,3,4,5,6]
# >>> I= iter(myList)
# >>> I
# <list_iterator object at 0x000001D552D1CC10>

# >>> I.__next__()
# 1
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4

# =========================================================
# iter in file is same as the name of the file stores in a variable

# >>>f = open('chai.py')
# >>> iter(f) is f
# True
# >>>iter(f) is f .__ iter_()
# True

# it means jab ham file ko ek vaible me store karte hai toh woh autometically ek ittrable object hai 

# but

# >>> myNewList = [1, 2, 3]
# >>> iter(myNewList) is myNewList
# False

#not for the list
# so if we give the refrence of the list in the other varible or object then it is not same as  the list itself it is just equal to the object not list
# =========================================================
# >>> D = {'a':1,'b':2}
# >>> for key,value  in D.items():
# ...     print(key,value)        
# ... 
# a 1
# b 2
# =========================================================

# range is also an ittrable

# range(5)
# range
# range (0, 5)
# >>> R = range(5)
# >>> R
# range(0, 5)
# >>> I = iter(R)
# >>> next(I)

# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last) :
# File "<stdin>", line 1, in <module>
# StopIteration
# >>>
# =========================================================
# =========================================================
# =========================================================

# we open folder in the integrated terminal then we write

# ls + enter = so we get the output of where we are in the file

# important 
# we have to open pyhton in the terminal
# =====================================================
# >>> f = open("script.py")
# >>> for line in f: 
# ...     print(line)

# ================

# but the answers comes with a line gap so we can write 
# >>> for line in f: 
# ...     print(line,end='')

# ================================================

#  f.__next__() 

# ==========================

# with while loop

# not check karta hai ki aage wala chiz me koi vlaue hai ki nahi 

# # >>> f = open("script.py")
# >>> while True:
# ...     line = f.readline()
# ...     if not line:    break
# ...     print(line,end="")
# ... 
# ==============================









# >>> f = open('script.py')
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# 'print("How are you")\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'name = "Ujjwal"\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print(name)\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '# we open folder in the integrated terminal then we write\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '# ls + enter = so we get the output of where we are in the file\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '# important \n'
# >>> f.readline()
# '# we have to open pyhton in the terminal\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# ''
# >>> f.readline()
# ''