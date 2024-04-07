# 匿名函数
def f(d):
    return d[1]

a = [("1", 88), ("2", 99), ("3", 85)]
print(sorted(a)) # 无法排序
print(sorted(a, key=lambda d:d[1])) # 同f
# print(sorted(a, key=f(a)))

# 模块 需要有__init__文件
from module6_6 import function
n = 1
m = 2
print(function(n, m))