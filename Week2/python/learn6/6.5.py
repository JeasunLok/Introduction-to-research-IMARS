# 递归方法求阶乘
def jc(n):
    if n == 1:
        return 1
    return jc(n-1)*n