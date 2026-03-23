import sys


def get_max_score(score, dp):
    for n in range(3, len(score)):
        dp[n] = max(score[n - 1] + dp[n - 3], dp[n - 2]) + score[n]
    return dp[-1]


# sys.stdin = open("input.txt", "r")
score = list(map(int, sys.stdin.read().split()))
dp = [0] * (len(score))
dp[1] = score[1]
if len(score) > 2:
    dp[2] = score[1] + score[2]
print(get_max_score(score, dp))
