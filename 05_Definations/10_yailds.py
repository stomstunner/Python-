# in this program we learn abour the yeilds 
# lets make a even generator with the help of range 
# range(start-inclusive,end-exclusive,jump-exclusive(>1))

# def even_generator(limit):
#     li =[]
#     for i in range(2,limit+1,2):
#         li.append(i)
#     return li

# print(even_generator(10))
# here we pass  the limit so woha tak ke sare number ko jo sirf even ho usse print kar dega but start hoga 2 se kyuki ham even generator bana rahe hai

# ===============================================

# lets understand yeild jo ki vlaue ko return karta hai but ittrable object ke state ko bhi store kar ke rakhta hai 


def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
    

for num in even_generator(10):
    print(num)

# isse ham baar baar even generator ko call kar toh rahe hai num jitni baar ittrate kar rha hai aur even genertor har baar start se run nahi ho rha hai baliki hamra current memory loaction ke vlaue ko return kar rha hai aur usko store bhi kar ke rkah rha hai aur next time call karne pe woh start se nahi chal rha hai balki current position se next pe jaa rha hai







