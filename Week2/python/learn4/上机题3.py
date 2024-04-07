# 求一个数列的前n项和
n = 5
t1 = 2
tt1 = 3
t2 = 1
tt2 = 2
result = t1/t2
for i in range(n-2):
    temp1 = tt1
    tt1 = tt1 + t1
    t1 = temp1
    temp2 = tt2
    tt2 = tt2 + t2
    t2 = temp2 
    result = result + tt1/tt2
print(result)