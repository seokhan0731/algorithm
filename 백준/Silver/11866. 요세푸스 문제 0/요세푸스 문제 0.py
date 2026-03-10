import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
circular_queue = deque([str(i) for i in range(1, n + 1)])
answer = []
while circular_queue:
    circular_queue.rotate(-m + 1)
    answer.append(circular_queue.popleft())

print('<' + ', '.join(answer) + '>')
