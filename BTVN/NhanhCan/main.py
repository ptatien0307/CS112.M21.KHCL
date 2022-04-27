
def subsetSum(arr, cur_sum, i, sum, count, n):
     
    if cur_sum == sum:
        count[0] += 1
        return

    elif cur_sum == sum or i == n:
        return
    else:
        subsetSum(arr, cur_sum + arr[i], i + 1, sum, count, n)

        subsetSum(arr, cur_sum, i + 1, sum, count, n)
apples = [int(x) for x in input().split()]

max_mass, n = [int(x) for x in input().split()]

count = [0]
subsetSum(arr, cur_sum, 0, sum, count, n)
print(count[0])

