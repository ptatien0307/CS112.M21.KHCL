

def frog_bottom_up(stones, height):
    dp = [0] * stones

    dp[0] = 0
    dp[1] = abs(height[1] - height[0])

    for i in range(2, stones):
        temp_1 = dp[i-1] + abs(height[i] - height[i-1])
        temp_2 = dp[i-2] + abs(height[i] - height[i-2])
        dp[i] = min(temp_1, temp_2)
    
    print(dp[stones - 1])

def frog_top_down(idx, height, lookup):
    if idx == 0:
        return 0
    if lookup[idx] != -1:
        return dp[idx]
    jumpTwo = 9999999999
    jumpOne = frog_top_down(idx-1, height, lookup) + abs(height[idx] - height[idx-1])
    if idx > 1:
        jumpTwo = frog_top_down(idx-2, height, lookup) + abs(height[idx] - height[idx-2])
    
    lookup[idx] = min(jumpOne, jumpTwo)

    return lookup[idx]
  
def main():
    n = int(input())
    height = [int(x) for x in input().split()]
    ## TOP - DOWN
    #lookup = [-1] * n
    #print(frog_top_down(n-1, height, lookup))
    
    ## BOTTOM - UP
    #print(frog_bottom_up(n, height))
main()
