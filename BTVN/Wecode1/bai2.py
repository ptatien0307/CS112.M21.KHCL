def bai1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 8
    else:
        a = 3
        b = 8
        for i in range(3, n + 1):
            res = 2 * (a + b)
            a = b
            b = res
        return res % (10**9+7)

n = int(input())
print(bai1(n))