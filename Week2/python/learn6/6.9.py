# 字符串减法
def f(a, b):
    a = a.replace(b, "")
    return a

s = input("input: ").split("-")
print(s)
print(s[0][1:-1], s[1][1:-1])
print(f(s[0][1:-1], s[1][1:-1]))