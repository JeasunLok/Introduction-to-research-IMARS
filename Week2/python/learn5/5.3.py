# 找到完数
n = eval(input("a number : "))
for a in range(2,n+1):
    s = 0
    L1 = []
    for i in range(1,a):
        if a%i ==0:
            s = s + i
            L1.append(i)
    if s==a:
        print("%d its factor are "%a,L1)