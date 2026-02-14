# Object types and datatypes
-Number : 1234, 3.14, 3+4j, 0b111, decimal(), fraction()

-String : 'spam', "string", "mom's", b'a\x01c', u'sp\xc4m'

-List : [1,2,3], [1,[2,'three'],4.5], list(range(10))

-Tuple : (1, 'spam',4,'U'), tuple('spam'), namedtuple

-Dictionary : {'food' : 'spam', 'taste' : 'yum'},dist(hours=10)

-Set : set('abc'), {'a','b','c'}

-File : open('eggs.txt'), open(r'C:\ham.bin','wb')

-Boolean : True, False

-None : None

-Functions, Modules, Classes

-Advance : Decorators, Generators, Iterators, MetaProgramming



-- math.floor() gives the closed value below the number

-- math.trunc() gives the number is near to the Zero 

- ocatal digit 
0o20 = 16

- hexadecimal digit
0xFF = 255

- binry digit
0b1000  = 8

funtion for all
ocatal = oct()
hexal = hex()
binary = bin()

- we can do one thing for finding the things for their base for conversion

int('',base)

- int('111',2) = 7
-int('20',8) = 16

-bitwise shift 
<< left ki aur arrow ja rha hai matlab woh bit ka value kitne se hame shift karna hai woh likhne

let x = 1
x << 2 iska matlab hai ki x ka value ko 2 bit se left me shift kar do

-import random
random.random()
== it just giva a randome number bitween 0 and  1 sone kindda decimal value so we want only real number then we can use the seperate integer related method 

- random.randint(1,100)
ham random number chaiye woh bhi integer but between the 1 to 100 


- decimal context manager
0.1  + 0.1  + 0.1  =
0.3000000000000004 

0.1 + 0.1  + 0.1  - 0.3 = 
5.551115123125783e-17
#problem

solution
from decimal import Decimal

then har chiz ko decimal aur qoute me likna parta hai

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') =
Decimal('0.3')

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') =
Decimal('0.0')

-Set 
- & is used for intersection 
-set can se understand by seeting the curly braket only number not in the key and value pair (key and value pair is used in dictonary) 

- we can find the union by just writing | in between two sets

-we can find that ki hamra koi bhi chiz ka type ky hai by using type()


-==   is    ==
is  = se hota ye hai ki hamra jo 2 chiz hai woh comare hota hai memeoray location ke basis pe


-string

-name = "Ujjwal Kumar Singh"
-print(name)
==Ujjwal Kumar Singh
-name[0]
=='U'
-slice_name = name[0:7] // we write the first character then the last + 1 number
-print(slice_name)
==Ujjwal


-slice

>>> name = "Ujjwal Kumar Singh"
>>> print(name)
Ujjwal Kumar Singh
>>> name[0]
'U'
>>> slice_name = name[0:7]
>>> print(slice_name)
Ujjwal
>>>
>>> num_list = "0123456789"
>>> num_list
'0123456789'
>>> num_list[:]
'0123456789'
>>> num_list[:5]
'01234'
>>> num_list[0:5]
'01234'
>>> num_list[:9]
'012345678'
>>> num_list[0:8:2]
'0246'
>>> num_list[0:8]
'01234567'
>>> num_list[0:8:4]
'04'
>>> num_list[0:9:4]
'048'
''
>>> num_list[-1:9]
''
>>> num_list[-1:-9]
''
>>> num_list[-9]
'1'

-strip
>>> name = "   ujjwal   "
>>> name
'   ujjwal   '
>>> print(name.strip())
ujjwal

<!-- here we are leaning how we can change the string in list -->
name = "ujjwal, nirmal, nirmal, ujjwal"
print(name.split())
 =  ['ujjwal,', 'nirmal,', 'nirmal,', 'ujjwal']
print(name.split(", "))
 =  ['ujjwal', 'nirmal', 'nirmal', 'ujjwal']


<!-- here we can see the funtion count and find -->
 print(name.find("ujjwal"))
==  0
 print(name.count("ujjwal"))
 == 2

 <!-- here we leanrn about varibale formting -->
chai_type = "Masala"       
quantity = 2
order = "I ordered {} cups of {} tea"
print(order.format(quantity, chai_type))
== I ordered 2 cups of Masala tea 

<!-- we can convert the list into string also with the help of join -->

name = ["ujjwal", "nirmal", "ujjwal", "nirmal"]
name
==  ['ujjwal', 'nirmal', 'ujjwal', 'nirmal']
print(" ".join(name))
== ujjwal nirmal ujjwal nirmal

<!-- invetted comma ke bich me hamjo bhi likhane wohi hi join ho jayega har ek list ke element ke baad  -->


<!--  we can find the length of the stirng  -->
name = "ujjwal kumar singh"
print(len(name))
18

<!-- we can print the character wise printing with the help of for loop -->
<!-- indentation is very important -->
for letter in name:
...     print(letter)
... 
u
j
j
w
a
l

k
u
m
a
r

s
i
n
g
h

<!-- if we are using the double inverted ya single invrted comma in a string itself the we can use backward \ slash for telling language ki isse as a comma hi treate karo as a text treat karo na ki as a sting  -->

massage = "He said that, \"Masala chai was awasome\" "
 massage
==  'He said that, "Masala chai was awasome" '


<!-- we  can use r"content" for any type of data in that trat as  string-->
 windows = r"c\user\app\vscode"
>>> print(windows)
c\user\app\vscode
>>> windows
'c\\user\\app\\vscode'
>>> windows = r"c\user\app\vscode\"


<!-- we can ask the python about out string ki koi bhi element hai ya nahi hai -->
>>> hello = "ujjwal kumar singh"
>>> hello
'ujjwal kumar singh'
>>> print("ujjwal" in hello)
True
>>> print("ujjwal kumar " in hello)
True
>>> print("ujjwal kum " in hello)  
False
>>> print("ujjwalkumar" in hello)
False
>>> print("ujjwalkumar singh" in hello)
False
>>> print("ujjwal kumarsingh" in hello) 
False
>>> print("ujjwal kumar singh" in hello)
True


<!-- we are learning about the list slii=cing  -->
>>> list[1:1]
[]
>>> list[1:1] = ["niraml1","nirmal2"]
>>> list
['ujjwal1', 'niraml1', 'nirmal2', 'ujjwal2', 'ujjwal3']
>>>

<!-- if we are tkaing about the for loop then the words are comming in the next line we can avoid that by just writting -->
>>> for n in name:
...     print(n,end =" ")      
...
==  ujjwal nirmal ujjwal1 ujjwal2

<!-- here we learn about the insert,remove,pop -->
>>> print(name.remove("ujjwal1"))          
None

>>> name
['ujjwal', 'nirmal', 'ujjwal2']

>>> name.insert(1,"prince")

>>> name
['ujjwal', 'prince', 'nirmal', 'ujjwal2']

print(name.pop())
prince

<!-- we can make  a copy of that list in the memory == another refrence for another list/varibale -->

list = ["ujjwal","nirmal","u1","u2"]
>>> list
['ujjwal', 'nirmal', 'u1', 'u2']
>>> list_copy = list.copy()
>>> list_copy
['ujjwal', 'nirmal', 'u1', 'u2']
>>> list_copy.pop()
'u2'
>>> list_copy
['ujjwal', 'nirmal', 'u1']
>>> list
['ujjwal', 'nirmal', 'u1', 'u2']


<!-- syntax for square root in a formate pranthitics -->
<!-- x **2  we call it comprehension  -->
sq_num = [ x**2 for x in range(10)]
sq_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


<!-- we can use the distanary to store a key and its value in the database/memory

we can access any data/vlaue by just giving the key of that vlaue -->

st = {"name" : "Ujjwal", "class" : "BCA","Roll" : 1324547}
>>> st
{'name': 'Ujjwal', 'class': 'BCA', 'Roll': 1324547}
>>> st["name"]
'Ujjwal'

print(st.get("name"))
Ujjwal

<!-- we can access the value in dist -->
for n in st:
...  print(n)
...
name
class
Roll

<!-- we can access the key and their vlaues also -->
for info in st:
...  print(info, st[info])
...
name Ujjwal
class BCA 4th
Roll 1324547

<!-- we can access the one items at a time with the help of the distnme.items() method 

isse ham ek baar me ek item ko utha rahe hai aur uspe kaam kar hai-->

for key,value in st.items():
...     print(key, value)
...
name Ujjwal
class BCA 4th
Roll 1324547

<!-- we can add a new key member and their  value in the dist -->
>>> st
{'name': 'Ujjwal', 'class': 'BCA 4th', 'Roll': 1324547}
>>> st["address"] = ["chaajan hari ray tola"]
>>> st
{'name': 'Ujjwal', 'class': 'BCA 4th', 'Roll': 1324547, 'address': ['chaajan hari ray tola']}
>>> st["address"] = "chhajan hari ray tola"  
>>> st
{'name': 'Ujjwal', 'class': 'BCA 4th', 'Roll': 1324547, 'address': 'chhajan hari ray tola'}

<!-- we can remove the element from the dist but while using pop mehthod we have to write the key of that vlaue we want to remove becaue here there is no indexing -->

>>> st
{'name': 'Ujjwal', 'class': 'BCA 4th', 'Roll': 1324547, 'address': 'chhajan hari ray tola'}
>>> st.pop("address")
'chhajan hari ray tola'
>>> st
{'name': 'Ujjwal', 'class': 'BCA 4th', 'Roll': 1324547}

<!--  we can remove the item that was lastly include in the dist with the help of popitem() -->

>>> st
{'name': 'Ujjwal', 'class': 'BCA 4th', 'Roll': 1324547}
>>> st.popitem()
('Roll', 1324547)
>>> st
{'name': 'Ujjwal', 'class': 'BCA 4th'}

<!-- we can delete the key and  its vlaue from memeory also -->
del st["class"]
st
{'name': 'Ujjwal'}


<!-- we can make a matrix like structure inside a dist itself but we have to give each inner dist its key and we can write the same key value pair in the inner dist -->

student = {
... "bca" : {"name" : "ujjwal" , "class" : "BCA" , "roll" : 1324547},
... "mca" : {"name" : "satyam" , "class" : "MCA" , "roll" : 1234567}
... }
student
 == {
    'bca': {'name': 'ujjwal', 'class': 'BCA', 'roll': 1324547}, 
    'mca': {'name': 'satyam', 'class': 'MCA', 'roll': 1234567}
  }
 <!-- here in the dist in dist we actully making  a  subset inside a superset -->

<!-- we can access the inner value of a dist -->
student["bca"]["class"] 
'BCA'

<!-- we can write the suare of digit or calculate / run loop inside a dist with some syntax xhange compared to list -->
<!-- here we give x as its key and another x as a value and change the vlaue of x and performing our operation on it -->
 sqrt = {x:x**2 for x in range(11) }
 sqrt
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

<!-- we can make join a key wala dict to a vlaue wla string  and we can join two dict by the help of for loop also-->

>>> sqrt = {x:x**2 for x in range(11) }
>>>
>>> sqrt
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

>>> keys = ["ujjwal","nirmal","prince"]

>>> value = "kumar"
>>> new_dict = dict.fromkeys(keys,value)
>>> new_dict
{'ujjwal': 'kumar', 'nirmal': 'kumar', 'prince': 'kumar'}



<!-- we use parenthathis () for difining tuple 
    currly bracket for set {}
    braket for list [] 
    curly braket for dictionary {}
 -->

name = ("ujjwal" ,"nirmal" , "prince" )
----------------------------------------
name
('ujjwal', 'nirmal', 'prince')
-------------------------------
>>> for i in name :
...     print(i)
... 
ujjwal
nirmal
prince
--------------------------
for i in name :
...     print(i,end=" ")
... 
ujjwal nirmal prince



<!-- we can do diffrent operation on the tuple like adding new elemment but we cant cahgne the original element -->

>>> name = ("ujjwal")
>>> name
'ujjwal'
<!-- when we have only one word in tuple then it acts as a sring and give the first letter -->
>>> name[0]
'u'
>>> name[0:3]
'ujj'
>>> name =("ujjwal","nirmal")
>>> name
('ujjwal', 'nirmal')
>>> name[0]
'ujjwal'
>>> name[0:2]
('ujjwal', 'nirmal')
<!-- we can find the lenght also -->
>>> len(name)
2

<!-- we can add 2 diffrent tuple , this method same for all other data type also -->
>>> surname =("kumar","singh")
>>> surname
('kumar', 'singh')
>>> main_name = name + surname

>>> main_name
('ujjwal', 'nirmal', 'kumar', 'singh')
>>>


<!--  we can assign variable to tuple at once but we should have same number of data in a tuple and in the same number of varibale-->

name
= ('ujjwal', 'nirmal')

(first,second) = name

first
= 'ujjwal'

second is the vaiable of 'nirmal'



<!-- we can take input from user by input() -->








PS C:\Users\niran\Desktop\Python> C:/Users/niran/anaconda3/Scripts/activate
PS C:\Users\niran\Desktop\Python> conda activate base
conda : The term 'conda' is not recognized as the
name of a cmdlet, function, script file, or
operable program. Check the spelling of the name,
or if a path was included, verify that the path
is correct and try again.
At line:1 char:1
+ conda activate base
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (co
   nda:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundExce
   ption

PS C:\Users\niran\Desktop\Python> python
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> mylist = [123,"ujjwal",45]
>>> mylist
[123, 'ujjwal', 45]
>>> len(mylist)
3
>>> len(mylist[1])
6
>>> mylist(-1
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    mylist(-1
    ~~~~~~^^^
    )
    ^
TypeError: 'list' object is not callable
>>> mylist(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    mylist(-1)
    ~~~~~~^^^^
TypeError: 'list' object is not callable
>>> mylist(-1)
Traceback (most recent call last):
    ~~~~~~^^^^
TypeError: 'list' object is not callable
>>> python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> ^Z

PS C:\Users\niran\Desktop\Python> python
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> mylist = [123,"ujjwal",345]
>>> mylist(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    mylist(-1)
    ~~~~~~^^^^
TypeError: 'list' object is not callable
>>> mylist[-1]
345
>>> <--lets create a distrinory-->
  File "<stdin>", line 1
    <--lets create a distrinory-->
    ^
SyntaxError: invalid syntax
>>> myD = {'one' : 'ujjwal' , 'two' : 'kumar' , 'three' : 'singh'}
>>> myD['three']
'singh'
>>> myD[three]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    myD[three]
        ^^^^^
NameError: name 'three' is not defined
>>> myD['two']
'kumar'
>>> p1 = [1,2,3]
>>> p2 = p1
>>> p1
[1, 2, 3]
>>> p2
[1, 2, 3]
>>> p1 = [2,3]
>>> p1
[2, 3]
>>> p2
[1, 2, 3]
>>> l1 = [1,2,3]
>>> l2 = l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0] = 33
>>> l1
[33, 2, 3]
>>> l2
[33, 2, 3]
>>> l2 =[1,2,3]
>>> a1 = [1,2,3]
>>> a2 = a1
>>> a1
[1, 2, 3]
>>> a2
[1, 2, 3]
>>> a2 = [1,2,3]
>>> a2
[1, 2, 3]
>>> a1
[1, 2, 3]
>>> a1[0] = 23
>>> a1
[23, 2, 3]
>>> a2
[1, 2, 3]
>>> h1 = [1,2,3]
>>> h2 = h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0] = 55
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]