import sys


def get_minimum_way(dp):
    for i in range(3, 12):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]


# sys.stdin = open("input.txt", "r")
data = map(int, sys.stdin.read().split()[1:])
dp = [0] * 12
dp[0], dp[1], dp[2] = 1, 1, 2
get_minimum_way(dp)
answer = []
for i in data:
    answer.append(dp[i])
print('\n'.join(map(str, answer)))
