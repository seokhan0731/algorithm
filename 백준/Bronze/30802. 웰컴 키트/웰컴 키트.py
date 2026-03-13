import math
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
size_count = list(map(int, input().split()))
t, p = map(int, input().split())
total_t = 0
for data in size_count:
    total_t += math.ceil(data / t)
print(f"{total_t}\n{n // p} {n % p}")
