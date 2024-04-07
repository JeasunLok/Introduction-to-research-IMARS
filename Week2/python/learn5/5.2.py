# 镜像
b_list = input("请输入数据:")
a_list = []
for i in b_list.split(','):
    a_list.append(i)
print(b_list)
n = len(a_list)
for i in range(n//2):
    a_list[i],a_list[n-i-1] = a_list[n-i-1], a_list[i]
print(a_list)
a = list(map(int,a_list)) # map为映射函数
print(a)
b = [int(x) for x in a_list] # 迭代
print(b)

# 另一种方法
print(b_list[::-1])