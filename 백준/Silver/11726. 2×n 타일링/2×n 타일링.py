import sys

DIVIDE_NUM = 10007


def get_number_of_way(dp, n):
    global DIVIDE_NUM
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % DIVIDE_NUM
    return dp[n]


# sys.stdin = open("input.txt", "r")
input = int(sys.stdin.read())
dp = [0] * (input + 1)
dp[0], dp[1] = 1, 1
print(get_number_of_way(dp, input))
