# 去重后排序（利用字典）
s = input("一串字符 : ")
a = list(s)
print(a)
b = list(set(a))
b.sort()
for x in b:
    print(x, end="")