import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
answer = []
for number in data:
    if number == '0':
        break
    answer.append('yes' if number == number[::-1] else 'no')
print('\n'.join(answer))
