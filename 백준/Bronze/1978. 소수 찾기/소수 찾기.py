import sys


def is_decimal(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False;
    return True;


# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
numbers = map(int, input().split())
count = 0

for number in numbers:
    if number == 1:
        continue
    if is_decimal(number):
        count += 1

print(count)
