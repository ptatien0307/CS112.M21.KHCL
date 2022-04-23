

# BOTTOM - UP
def climbStairs(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * (n + 1)
        
        # base case
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]
        
# TOP - DOWN
def climbStairs(n):
    lookup = [None] * 101
    return help_fn(n, lookup)
    
def help_fn(n, lookup)
    if n < 0:
        return 0
    if n == 0:
        return 1
    if lookup[n] is None:
        lookup[n] = help_fn(n-1, lookup) + help_fn(n-2, lookup)
    return lookup[n]
        
