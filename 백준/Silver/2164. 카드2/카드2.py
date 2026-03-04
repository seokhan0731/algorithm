import sys
from collections import deque


def card_game(n):
    card_deque = deque([i for i in range(1, n + 1)])
    while len(card_deque) > 1:
        card_deque.popleft()
        card_deque.append(card_deque.popleft())
        if len(card_deque) == 1:
            break
    print(card_deque[0])


# sys.stdin = open("input.txt", "r")
input = sys.stdin.read

n = int(input())
card_game(n)
