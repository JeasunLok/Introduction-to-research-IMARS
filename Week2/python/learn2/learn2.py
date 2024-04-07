# input时eval的作用
x = input("::")
print(type(x))
x = eval(input("::"))
print(type(x))

# print
x,a,b = 2.5,3,5
print(x,a,b,sep=", ",end="! ")
print(x,a,b,sep=", ",end="") # 原行输出2
print(x,a,b,sep=", ")
print(x,a,b,sep=", ",end="!")

print("%x"%11) # 十六进制
print("%0.2f"% 3.1415269) # 控制格式
print("%5dabcd%1.3f"%(12.3,12.3))