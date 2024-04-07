# 牛顿迭代法求平方根
a = eval(input("input a : "))
x1 = a
x2 = x1
while 1:
    x1 = x2
    x2 = 0.5 * (x1+a/x2)
    if abs(x2-x1)<1e-6:
        break
print(x2)