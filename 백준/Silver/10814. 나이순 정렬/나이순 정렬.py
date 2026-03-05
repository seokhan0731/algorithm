import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()[1:]
member_list = []

for index in range(0, len(data), 2):
    member_list.append([int(data[index]), data[index + 1]])

member_list.sort(key=lambda x: x[0])
print('\n'.join(f"{x[0]} {x[1]}" for x in member_list))
