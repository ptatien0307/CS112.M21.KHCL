from sys import stdin

Count = 0
Temp = []
BestSolution = []


def BranchAndBound (nums, idx, MaxWeight, n):
    global Temp
    global Count
    global BestSolution
    if sum(Temp) > MaxWeight:
        return
    for i in range(idx, len(nums)):
        Temp.append(nums[i])
        if len(Temp) == n:
            if MaxWeight - sum(Temp) >= 0:
                Count += 1
                if sum(Temp) > sum(BestSolution):
                    BestSolution = Temp[:]
        else:
            BranchAndBound(nums, i + 1, MaxWeight, n)
        Temp.pop()


if __name__ == '__main__':
    nums = [int(i) for i in stdin.readline().split()]
    MaxWeight, n = [int(i) for i in stdin.readline().split()]
    BranchAndBound(nums, 0,  MaxWeight, n)
    print(Count)
    if Count != 0:
        print(sum(BestSolution))
        print(BestSolution)
