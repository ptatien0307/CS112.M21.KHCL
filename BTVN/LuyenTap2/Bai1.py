import math
def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def findLocalMinDistance(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if distance(P[i], P[j]) < min_val:
                min_val = distance(P[i], P[j])
    return min_val


def findMin(arr, n):
    if n <= 3:
        return findLocalMinDistance(arr, n)
    mid = n // 2


    dl = findMin(arr[:mid], mid)
    dr = findMin(arr[mid:], n - mid)
    d = min(dl, dr)
    return d
def findStrip(arr_x, d, n):
    strip = list()
    mid = n // 2
    midPoint = arr_x[mid]
    for i in range(n):
        if abs(arr_x[i][0] - midPoint[0]) < d:
            strip.append(arr_x[i])
    sorted(strip, key=lambda x: x[1])
    return strip
def stripClosest(strip, size, d):

    min_val = d
 

    for i in range(size):
        j = i + 1
        while j < size and abs(strip[j][1] -
                            strip[i][1]) < min_val:
            min_val = distance(strip[i], strip[j])
            j += 1
 
    return min_val
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr_x = sorted(arr, key=lambda x: x[0])

d = findMin(arr_x, n)
strip = findStrip(arr_x, d, n)
print(stripClosest(strip, len(strip), d))