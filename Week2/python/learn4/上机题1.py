# 求1-20的阶乘和
def fact(n):
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result

result = 0
for i in range(1,21):
    result = result + fact(i)
print(result)