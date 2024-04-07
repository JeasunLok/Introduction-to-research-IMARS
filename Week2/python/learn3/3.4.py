# 判断任意一个数是不是水仙花数
x = input("a number : ")
if int(x)<100:
    raise KeyError("number is less than 100")
x = str(x)
x_list = []
for i in range(len(x)):
    x_list.append(int(x[i]))
x_sum = 0
for i in range(len(x_list)):
    x_sum = x_sum + x_list[i]**len(x)
if x_sum == int(x):
    print("%d is yes" % int(x))
else:
    print("%d is no" % int(x))

# 找出100-N的水仙花数
n = input("size : ")
n = eval(n)
n_list = []
for x in range(100, n + 1):
    x = str(x)
    x_list = []
    for i in range(len(x)):
        x_list.append(int(x[i]))
    x_sum = 0
    for i in range(len(x_list)):
        x_sum = x_sum + x_list[i]**len(x)
    if x_sum == int(x):
        n_list.append(int(x))
print("number : " , n_list)