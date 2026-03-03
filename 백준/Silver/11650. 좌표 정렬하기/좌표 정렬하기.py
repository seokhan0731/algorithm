import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()[1:]

length = len(data)
matrics = []

for i in range(length):
    a, b = map(int, data[i].split())
    matrics.append([a, b])

sorted_datas = sorted(matrics, key=lambda x: (x[0], x[1]))
print('\n'.join(f"{x[0]} {x[1]}" for x in sorted_datas))
