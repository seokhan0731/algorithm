import sys


def black_jack(cards, m):
    length = len(cards)
    max = 0
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                sum = cards[i] + cards[j] + cards[k]
                if sum <= m and sum > max:
                    max = sum
    return max


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

_, m = list(map(int, input().split()))
cards = list(map(int, input().split()))

print(black_jack(cards, m))
