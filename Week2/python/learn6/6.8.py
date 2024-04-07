# 递归法求幂函数
def f(x, n):
    if n==0:
        return 1
    return f(x, n-1)*x

print(f(2, 5))