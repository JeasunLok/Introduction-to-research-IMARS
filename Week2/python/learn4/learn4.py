# while 和 else 的搭配使用 没用的知识增加了
s = 0
i = 1
while i<=100:
    s += i
    i += 1
    if s > 4000:
        break
else:
    print("done!")
print(s)
