n = int(input())
a = [int(x) for x in input().split()]

zero, neg, pos = list(), list(), list()
res = 1

if len(a) == 1:
    print(a[0])
else:
    for i in a:
        if i == 0:
            zero.append(i)
        elif i < 0:
            neg.append(i)
            res *= i
        else:
            pos.append(i)
            res *= i
    if len(zero) == (n - 1) and len(neg) == 1:
        print(0)
    elif len(zero) == (n - 2) and len(neg) == 1 and len(pos) == 1:
        print(0)
    elif len(zero) == n:
        print(0)
    else:
        if res < 0:
            res //= max(neg)
            print(res)
        else:
            print(res)

