# here we find the first non repeated character in a string
input_str = input("Enter a word: ")
for i in input_str:
    if input_str.count(i) == 1: 
        # we apply count method on input_str because the python  solve string as list so it takes one by one character as a single values
        print("Char is ",i)
        break