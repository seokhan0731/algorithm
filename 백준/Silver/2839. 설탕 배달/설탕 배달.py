import math
import sys


def get_minimum_way(n, dp):
    for i in range(3, n + 1):
        if i < 5:
            dp[i] = dp[i - 3] + 1
        else:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1


# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.read())
dp = [math.inf] * (n + 1)
dp[0] = 0
get_minimum_way(n, dp)
print(dp[n] if not dp[n] == math.inf else -1)
