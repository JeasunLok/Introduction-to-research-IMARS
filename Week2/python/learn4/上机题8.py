# 打印三角
n = eval(input("input a number : "))
s = input("a symboy : ")
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i+1):
        print(s, end="")
    print()

for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i+1):
        print(str(i), end="")
    print()

# 简单做法
for i in range(n):
    print(" "*(n-i), s*(2*i+1))