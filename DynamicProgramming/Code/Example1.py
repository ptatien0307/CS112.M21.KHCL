def frog_1():
    stones = int(input())
    height_of_stone = [int(x) for x in input().split()]
    min_cost = [0] * stones

    min_cost[0] = 0
    min_cost[1] = abs(height_of_stone[1] - height_of_stone[0])

    for i in range(2, stones):
        temp_1 = min_cost[i-1] + abs(height_of_stone[i] - height_of_stone[i-1])
        temp_2 = min_cost[i-2] + abs(height_of_stone[i] - height_of_stone[i-2])
        min_cost[i] = min(temp_1, temp_2)
    
    print(min_cost[stones - 1])
