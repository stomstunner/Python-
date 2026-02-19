x = 99 #here x is an global variable


def f1():
    X = 88
    def f2():
        print(x)
    return f2
# ham f2 ka refrence return kar rahe hai aur jab ham () laga dete hai toh usko ham execute kar rahe hote hai ya usko call karte hai

myResult = f1()
myResult()
# yaha pe x sirfy line 6 se 8 tak hi nahi chal raha hai balki woh apne saat ke sare varible ke bhi memory refrence ko bhi le ke bag me daal ke aaya hai, clouser aur bagpack
# =========================================
# factory function
def ujjwalcoder(num):
    def actual(x):
        return x ** num
    return actual 
# toh jab hai ujjwalcoder ko jab ham call kanrege toh hamra actual funtion ka anser hi return hoga 
 
f = ujjwalcoder(2)
g = ujjwalcoder(3)

print(f(3))
print(g(3))
    

