


def check(n, m, path):
    cnt_unsafe = 0
    for i in range(n):
        for j in range(m):
            x, y = i, j
            for c in path:
                if c == 'L':
                    y -= 1
                elif c == 'R':
                    y += 1
                elif c == 'U':
                    x -= 1
                elif c == 'D':
                    x += 1

                if x not in range(n) or y not in range(m):
                    cnt_unsafe += 1
                    break

    if cnt_unsafe == n * m:
        return False
    else:
        return True

n, m = map(int, input().split())
path = input()
if check(n, m, path):
    print('Safe')
else: print('Unsafe')




