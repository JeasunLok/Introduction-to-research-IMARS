# 求sin的泰勒展开
def fact(n):
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result

x = 3.14
t1 = x
t2 = 1
s = 1
result = 0
i = 1
while t1/t2>1e-6:
    result = result + s*t1/t2
    s = -s
    t1 = t1*x*x
    t2 = t2*(i+1)*(i+2)
    i = i + 2
print(result)
