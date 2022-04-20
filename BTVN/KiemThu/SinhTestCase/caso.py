from sys import stdin


def ReadFile():
    n = []
    arr = []
    with open('Input.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line == '\n':
            continue
        temp = line.split()
        temp = list(map(int, temp))
        n.append(temp[0])
        arr.append(temp[1:])
    return n, arr

def CreateInputTestCase(n, arr):
    for i in range(len(n)):
        with open('Testcase\Input\Caso' + str(i) + '.in', 'w') as f:
            f.write(str(n[i]) + '\n')
            listToStr = ' '.join(map(str, arr[i]))
            f.write(listToStr)

def Check(n, arr):
    output = []
    for i in range(len(n)):
        res = 0
        x = 1
        arr_temp = sorted(arr[i])
        for j in range(n[i]-1):
            if arr_temp[j] == arr_temp[j+1]:
                x += 1
            else:
                res += (x * (x - 1) // 2)
                x = 1
        res += (x * (x - 1) // 2)
        x = 1
        output.append(res)
    return output


def CreateOutputTestCase(n, output):
    for i in range(len(n)):
        with open('Testcase\Output\Caso' + str(i) +'.out', 'w') as f:
            f.write(str(output[i]) + '\n')

n, arr = ReadFile()
CreateInputTestCase(n, arr)
output = Check(n, arr)
CreateOutputTestCase(n, output)


