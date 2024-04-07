# 默认参数
def mul(x, y=2, z=3):
    return x*y*z
print(mul(1))
print(mul(1, 3))
print(mul(2, 4, 2))

def func(x, alist=[]):
    alist.append(x)
    return alist
print(func(1))
print(func(2))
print(func(3))

def func_none(x, alist = None):
    if alist == None:
        alist = []
    alist.append(x)
    return(alist)
print(func_none(1))
print(func_none(2))
print(func_none(3))