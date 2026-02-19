# here we learn how we can open the file and write on that
# we have two methods
# first one

# file = open("YouTube.txt",'w')

# here we open a file youtube.txt in write mode if there is any youtube.txt file in the filder then it just open it in a write mode so we can write something on that
# otherwise there is no youtube.txt present in the folder then it just create a new one and we can write on it because we use the write mode in the open file code

# try:
#     file.write("Ujjwal is a good boy")
# finally:
#     file.close()
    
# =================================
# now we discuss the 2nd method that is mordern nowadays
with open("YouTube.txt",'w') as file: 
    file.write("Ujjwal is a bad boy")

