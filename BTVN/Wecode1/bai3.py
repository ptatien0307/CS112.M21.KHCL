from sys import stdin
from sys import stdout

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, stdin.readline().split())
    dis = max(abs(x), abs(y))
    arr.append((dis, i + 1))

arr.sort(key=lambda arr: arr[0])

total_time = 0
flag = 0
for x in arr:
    if x[0] <= total_time:
        flag = 1
        break
    else:
        total_time += 1

if flag == 1:
    print(-1)
else:
    for x in arr:
        stdout.write(str(x[1]) + ' ')