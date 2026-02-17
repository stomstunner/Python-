# here we reverse of a string using a loop
input_str = input("Enter a word: ")
reversed_str = ""
for i in input_str:
    reversed_str = i + reversed_str
    print(reversed_str)
print("\n",reversed_str)


