def sorted(a):
    b = a[:]
    lt = []
    for i in range(len(b)):
        v = min(b)
        lt.append(v)
        b.remove(v)
    return lt
l = [4, 8, 6, 5, 9]
print(l)
print(sorted(l))