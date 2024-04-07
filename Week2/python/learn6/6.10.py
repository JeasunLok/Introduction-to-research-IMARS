# 递归实现斐波那契数列
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)
n = 10
for i in range(1, n+1):
    print(fib(i), end=" ")