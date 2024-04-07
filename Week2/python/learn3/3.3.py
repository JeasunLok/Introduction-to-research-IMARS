x = input("a number : ")
x = eval(x)
if x >= 0:
    x = x
    x_s = x**2
else:
    x = -x
    x_s = x**2
print(x, x_s)