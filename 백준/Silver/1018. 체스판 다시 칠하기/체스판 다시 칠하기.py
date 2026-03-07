"""
기존 코드. 브루트포스 알고리즘 이용
해당 문제는 8*8 사이즈를 흝으면서, 바꿔야하는 최소 개수를 구해줘야 한다.
직접 탐색해여 최소값을 갱신해줘야하기 때문에, 브루트포스 알고리즘으로 모든 경우를 탐색하여,
min()을 통해 최소값을 갱신한다.
또한 시작점이 B, W인지에 대한 두 가지 경우의 수는 한 가지 경우의 수로 탐색 후,
전체 사이즈 64-해당 케이스의 수로 대신하여 해결할 수 있다.
"""
import math
import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()[2:]

min_val = math.inf
for j in range(len(data) - 8 + 1):
    for i in range(len(data[0]) - 8 + 1):
        count = 0
        for r in range(8):
            for k in range(8):
                if (j + r + i + k) % 2 == 0:
                    if data[j + r][i + k] == 'W':
                        count += 1
                else:
                    if data[j + r][i + k] == 'B':
                        count += 1
        current_min = min(64 - count, count)
        min_val = min(current_min, min_val)
print(min_val)
