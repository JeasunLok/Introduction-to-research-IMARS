def getMax(a, b, c):
    # if(a > b):
    #     n = a
    # else:
    #     n = b
    # if(c > n):
    #     n = c
    # return n
    n = a if a>b else b
    n = c if c>n else n
    return n

a, b, c = eval(input("3 numbers : "))
print(getMax(a, b, c)) 

# 地址传递
def f(a):
    a[0] = 100
list = [1, 2 ,3 ,4]
f(list)
print(list)

def swap(a ,b):
    a, b = b, a
    print(a, b)
x, y = 2, 3
swap(x, y)
print(x, y)

def swap1(alist):
    alist[0], alist[1] = alist[1], alist[0]
    print(alist[0], alist[1])
a = [1, 2]
swap1(a)
print(a[0], a[1])