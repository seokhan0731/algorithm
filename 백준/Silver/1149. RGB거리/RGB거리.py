import sys


def get_minimum_cost(cost, n):
    r, g, b = cost[0], cost[1], cost[2]
    for i in range(2, n + 1):
        k = 3 * (i - 1)
        r, g, b = min(g, b) + cost[0 + k], min(r, b) + cost[1 + k], min(r, g) + cost[2 + k]
    return min(r, g, b)


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
n = int(data[0])
cost = list(map(int, data[1:]))
print(get_minimum_cost(cost, n))
