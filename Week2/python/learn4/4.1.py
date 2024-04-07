# 求s=1/1!+1/3!+1/5!+...+1/n!
def jc(n):
    result=1
    for i in range(1,n+1):
        result = result * i
    return result
n = input("n:")
n = eval(n)
i = 1
s = 0
while i<=n:
    # print(jc(i))
    s = s + 1/jc(i)
    i = i + 2
print("s is %0.10f" % s)