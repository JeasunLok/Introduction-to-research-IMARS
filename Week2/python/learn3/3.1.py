# 判断闰年
x = input("year : ")
x = eval(x)
if x % 4 == 0 and x % 100!=0 or x % 400 ==0:
    print("%d yes" % x)
else:
    print("%d no" % x)