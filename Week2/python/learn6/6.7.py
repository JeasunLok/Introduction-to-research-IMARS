def Bubsort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

b = input("number list:").split()
c = [eval(x) for x in b]
print(c)
print(Bubsort(c))