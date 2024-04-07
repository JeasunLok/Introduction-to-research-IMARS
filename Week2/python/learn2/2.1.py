# 小写字母转盘
x = input("lower case : ")
x = ord(x)
orda = ord("a")
a = orda + (x + 1 - orda) % 26
b = orda + (x - 1 - orda) % 26
print("next : %c" % a)
print("last : %c" % b)