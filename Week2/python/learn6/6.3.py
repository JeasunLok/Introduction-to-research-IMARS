# 参数传递
def mul(a, b):
    return a**b
print(mul(2, 3))
print(mul(b=2, a=3))

print("===")

def func(a, b, *params):
    print(len(params))
    print(a)
    print(b)
    print(params)
    return a*b*params[0]*params[1]
print(func(1, 2, 3, 4))

print("===")

def func_(a, b, **params):
    print(len(params))
    print(a)
    print(b)
    print(params)
    return a*b*params["c"]
print(func_(1, 2, c=3, d=4, e=5))