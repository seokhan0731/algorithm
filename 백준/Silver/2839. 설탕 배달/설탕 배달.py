import math
import sys

sys.setrecursionlimit(10 ** 8)


# def get_minimum_way(n, dp):
#     for i in range(3, n + 1):
#         if i < 5:
#             dp[i] = dp[i - 3] + 1
#         else:
#             dp[i] = min(dp[i - 3], dp[i - 5]) + 1

def get_minimum_way(n, dp):
    if n < 3:
        return dp[n]
    if not dp[n] == math.inf:
        return dp[n]
    dp[n] = get_minimum_way(n - 3, dp) + 1
    if n >= 5:
        dp[n] = min(dp[n], get_minimum_way(n - 5, dp) + 1)
    return dp[n]


# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.read())
dp = [math.inf] * (n + 1)
dp[0] = 0
# 바텀업 방식
# dp[0] = 0
# get_minimum_way(n, dp)
# print(dp[n] if not dp[n] == math.inf else -1)

# 탑다운 방식
answer = get_minimum_way(n, dp)
print(answer if not answer == math.inf else -1)
