# 买鸡问题
for i in range(21):
    for j in range(34):
        for k in range(101):
            if 5*i+3*j+k//3==100 and i+j+k==100:
                print(i,j,k)

print()

for i in range(21):
    for j in range(34):
        if 5*i+3*j+(100-i-j)//3==100:
            print(i,j,100-i-j)