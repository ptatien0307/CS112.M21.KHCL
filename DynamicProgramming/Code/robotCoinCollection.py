
def RobotCoinCollection():
    n, m = [int(x) for x in input().split()]

    board = []
    for _ in range(n):
        a = list(map(int, input().split()))
        board.append(a)


    dp = [[0] * (m+1) for _ in range(n+1)]
    
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
           dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + board[i-1][j-1]
    



def RobotCoinCollection2():
    n, m = [int(x) for x in input().split()]

    board = []
    for _ in range(n):
        a = list(map(int, input().split()))
        board.append(a)

    dp = [[0] * (m) for _ in range(n)]
    dp[0][0] = board[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + board[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + board[i][0]
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + board[i][j]
    return dp[n-1][m-1]
print(RobotCoinCollection2())