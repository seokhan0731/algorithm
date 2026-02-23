import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

_ = input()
a = set(map(int, input().split()))

_ = input()
b = list(map(int, input().split()))

answer = []
for target in b:
    answer.append(1 if target in a else 0)

print('\n'.join(map(str, answer)))
