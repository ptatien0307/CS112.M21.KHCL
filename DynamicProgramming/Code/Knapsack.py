
# def knapsack_1():
#     n, bag_weight = [int(x) for x in input().split()]

#     item_value = [] 
#     item_weight = []

#     for _ in range(n):
#         wi, vi = list(map(int, input().split()))
#         item_weight.append(wi)
#         item_value.append(vi)
    
#     dp = [[-1] * (bag_weight + 1) for i in range(n + 1)]
    

    # for i in range(n + 1):
    #     for j in range(bag_weight + 1):
    #         dp[0][j] = 0
    #         dp[i][0] = 0

    # for i in range(1, n + 1):
    #     for j in range(1, bag_weight + 1):
    #         if item_weight[i-1] <= j:
    #             dp[i][j] = max(dp[i-1][j], dp[i-1][j-item_weight[i-1]] + item_value[i-1])
    #         else:
    #             dp[i][j] = dp[i-1][j]


    
    # for i in range(0, n + 1):
    #     for j in range(0, bag_weight + 1):
    #         if i == 0 or j == 0:
    #             dp[i][j] = 0
    #         else:
    #             if item_weight[i-1] <= j:
    #                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-item_weight[i-1]] + item_value[i-1])
    #             else:
    #                 dp[i][j] = dp[i-1][j]

    # print(dp[n][bag_weight])