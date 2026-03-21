import sys


def get_call_count(dp, max_size):
    if max_size >= 2:
        for i in range(2, max_size + 1):
            dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]


# sys.stdin = open("input.txt", "r")
data = list(map(int, sys.stdin.read().split()[1:]))
max_size = max(data)
dp = [[0, 0]] * (max_size + 1)
dp[0] = [1, 0]
if max_size >= 1:
    dp[1] = [0, 1]
    get_call_count(dp, max_size)
print('\n'.join(f"{dp[i][0]} {dp[i][1]}" for i in data))
