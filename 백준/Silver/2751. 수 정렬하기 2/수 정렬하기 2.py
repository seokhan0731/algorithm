import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

numbers = []
n = int(input())
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
result = '\n'.join(map(str,numbers))
print(result)
