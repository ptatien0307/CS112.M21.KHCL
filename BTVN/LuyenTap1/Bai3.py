





def Possible(col, row, target, table, prevChoice, colIdx, prevSum, tempList):
    global res
    global agree
    for rowIdx in range(row):
        if agree == 1:
            return

        if prevChoice <= table[rowIdx][colIdx]:
            currChoice = table[rowIdx][colIdx]

            temp = currChoice + prevSum
            if temp > target:
                continue
            else:
                currSum = currChoice + prevSum
                tempCurrList = list(tempList)
                tempCurrList.append(currChoice)

            if colIdx == col - 1:
                if currSum == target:
                    res = tempCurrList
                    agree = 1
                    return
                continue
            
            Possible(col, row, target, table, currChoice, colIdx + 1, currSum, tempCurrList)
S, K, N = [int(x) for x in input().split()]
table = [list(map(int, input().split())) for _ in range(N)]
res = []
agree = 0
Possible(K, N, S, table, 0, 0, 0, [])
if agree:
    print('YES')
    for i in res:
        print(i, end=' ')
else:
    print('NO')


