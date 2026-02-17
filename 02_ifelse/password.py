password = input("Enter Your password: ")
pass_len = len(password)
if pass_len < 6:
    strength = "Easy"
elif pass_len <= 10 :
    strength = "Medium"
else:
    strength = "Hard"
print("Your Password Strength is:",strength)