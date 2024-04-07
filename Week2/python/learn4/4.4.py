# 求最大公约数
m,n = eval(input("two number:"))
x=m
if m<n:
    min=m
else:
    min=n
for i in range(2,min+1):
    if m%i==0 and n%i==0:
        x=i
        # print(x)
print("result:",x)