# 泰勒展开
e = 0
t1 = 1
t2 = 1
x = 1
n = 10
for i in range(1,n+1):
    t1 = t1 * x
    t2 = t2 * i
    e = e + t1/t2
print(e)

# 简单写法
e = 1
t = 1
x = 1
n = 10
for i in range(1,n+1):
    t*=x/i
    e+=t
print(e)