items = ["apple", "banana","mango","apple","guava"]
unique_item = set()
for i in items:
    if i in unique_item:
        print("Duplicated ",i)
        break
    unique_item.add(i)