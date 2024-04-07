# 判断素数
import math
x = input("number:")
x = eval(x)
flag = 1
for i in range(2,int(math.sqrt(x))+1):
    if x%i == 0:
        flag = 0
if flag == 1:
    print("%d yes" % x)
else:
    print("%d no" % x)

for i in range(2, x+1):
    for j in range(2,x+1):
        if i%j == 0:
            break
    if i==j:
     print(i, end=" ")