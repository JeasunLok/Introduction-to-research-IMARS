# 找扩展名
string = "TiffToMat.py"
# 方法一
a = string.split(".")[-1]
print(a)
# 方法二
n = string.rfind(".")
a = string[n+1:]
print(a)