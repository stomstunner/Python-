# here we make a coffee shop order size program

order_size = str.capitalize(input("Enter order size(small, medium, large): "))

extra_short = str.capitalize(input("You want an extra short (True/False) : "))

if extra_short:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"
print("Order:", coffee)
