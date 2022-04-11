def frog_2():
    stones, steps = [int(x) for x in input().split()]
    height_of_stone = [int(x) for x in input().split()]
    min_cost = [999999999] * stones

    min_cost[0] = 0
    min_cost[1] = abs(height_of_stone[1] - height_of_stone[0])

    for i in range(2, stones):
        temp = 0
        for j in range(i - 1, -1, -1):
            if temp >= steps:
                break
            else:
                min_cost[i] = min(min_cost[i], min_cost[j] + abs(height_of_stone[i] - height_of_stone[j]))
                temp += 1

    return min_cost[stones - 1]
