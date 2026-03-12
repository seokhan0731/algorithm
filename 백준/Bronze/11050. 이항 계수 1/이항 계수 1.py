import math
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
print(math.comb(n, k))
