def CrossRoad1(arr, m, n, x, y):
    sum = 0
    while 0 <= x < m and 0 <= y < n:
        sum += arr[x][y]
        x += 1
        y += 1
    return sum


def CrossRoad2(arr, m, n, x, y):
    sum = 0
    while 0 <= x < m and 0 <= y < n:
        sum += arr[x][y]
        x += 1
        y -= 1
    return sum


def CrossRoad3(arr, m, n, x, y):
    sum = 0
    while 0 <= x < m and 0 <= y < n:
        sum += arr[x][y]
        x -= 1
        y -= 1
    return sum


def CrossRoad4(arr, m, n, x, y):
    sum = 0
    while 0 <= x < m and 0 <= y < n:
        sum += arr[x][y]
        x -= 1
        y += 1
    return sum


def MaxSum(arr, m, n):
    max = 0
    for i in range(m):
        for j in range(n):
            temp = CrossRoad1(arr, m, n, i, j) + CrossRoad2(arr, m, n, i, j) + CrossRoad3(arr, m, n, i, j) + CrossRoad4(arr, m, n, i, j) - 3 * arr[i][j]
            if temp > max:
                max = temp
    return max


if __name__ == '__main__':
    m, n = map(int, input().split())
    arr = []
    for i in range(m):
        row = list(int(i) for i in input().split())
        arr.append(row)
    print(MaxSum(arr, m, n))