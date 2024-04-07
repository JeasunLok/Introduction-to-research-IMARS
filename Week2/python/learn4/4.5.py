# 求pi
d = 1e-6
pi = 0
s = 1
i = 1
while i<1e6:
    pi = pi + s/i
    s = -s
    i = i + 2
print("pi:%f" % (4*pi))