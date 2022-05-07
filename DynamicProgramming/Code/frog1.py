

def frog_bottom_up(stones, height_of_stone):
    dp = [0] * stones

    dp[0] = 0
    dp[1] = abs(height_of_stone[1] - height_of_stone[0])

    for i in range(2, stones):
        temp_1 = dp[i-1] + abs(height_of_stone[i] - height_of_stone[i-1])
        temp_2 = dp[i-2] + abs(height_of_stone[i] - height_of_stone[i-2])
        dp[i] = min(temp_1, temp_2)
    
    return dp[-1]




def frog_top_down(idx, height, dp):
    if idx == 0:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    jumpTwo = 9999999999
    jumpOne = frog_top_down(idx-1, height, dp) + abs(height[idx] - height[idx-1])
    if idx > 1:
        jumpTwo = frog_top_down(idx-2, height, dp) + abs(height[idx] - height[idx-2])
    
    dp[idx] = min(jumpOne, jumpTwo)

    return dp[idx]
def main():
    import time
    import random

    height = []
    for i in range(700):
        height.append(random.randint(1, 500))

    n = len(height)

    start = time.time()
    dp = [-1] * n
    print(frog_top_down(n-1, height, dp), end= ' ')
    
    end = time.time()
    print(end-start)
    start = time.time()
    dp = [-1] * n
    print(frog_bottom_up(n, height), end= ' ')

    end = time.time()
    print(end-start)
main()
