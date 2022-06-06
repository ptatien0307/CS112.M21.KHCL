
maxN = 20
maxSum = 50
minSum = 50
base = 50

dp = [[0] * (maxSum + minSum) for _ in range(maxN)]
v = [[0] * (maxSum + minSum) for _ in range(maxN)]

def countSubsetSum(arr, i, curr_sum, n) :
 

    if (i == n):
        if (curr_sum == 0):
            return 1;
        else:
            return 0;
 

    if (v[i][curr_sum + base]):
        return dp[i][curr_sum + base];
 
    v[i][curr_sum + base] = 1;
 
    dp[i][curr_sum + base] = countSubsetSum(arr, i + 1, curr_sum, n) + \
                             countSubsetSum(arr, i + 1, curr_sum - arr[i], n);
     
    return dp[i][curr_sum + base];



n = int(input())
arr = [int(x) for x in input().split()]
target = int(input())

res = countSubsetSum(arr, 0, target, n)

if res == 0:
    print('None')
else:
    print(res)
 
