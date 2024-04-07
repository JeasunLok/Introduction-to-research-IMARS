# 输入一串字符统计其中单词
words = input("input string : ").split()
d = {}
for w in words:
    d[w] = d.get(w, 0) + 1
print(d)