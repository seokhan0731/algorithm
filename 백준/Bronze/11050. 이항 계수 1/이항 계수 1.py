"""
기존 코드. 파이썬 내장 라이브러리 이용(math.comb)
해당 문제는 이항 계수, 즉 조합을 구하는 문제이기 떄문에,
math.comb(n,k)꼴을 통해 구할 수 있다.

+) comb를 떠올리지 못하더라도
n!/k!의 공식을 math.factorial(n)/(math.factorial(k)*math.factorial(n-k))를 통해 구할 수 있다.
"""
import math
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
# print(math.comb(n, k))
print(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
