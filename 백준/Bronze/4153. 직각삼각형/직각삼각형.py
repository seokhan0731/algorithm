import sys

# sys.stdin = open("input.txt", "r")
data = list(map(int, sys.stdin.read().split()))
answer = []
for i in range(0, len(data), 3):
    if data[i] == 0 and data[i + 1] == 0 and data[i + 2] == 0:
        break
    sorted_list = sorted([data[i], data[i + 1], data[i + 2]])
    answer.append("right" if sorted_list[2] ** 2 ==
                             sorted_list[0] ** 2 + sorted_list[1] ** 2 else "wrong")
print('\n'.join(answer))
