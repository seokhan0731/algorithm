import sys

# sys.stdin = open("input.txt", "r")
datas = sys.stdin.read().split()[1:]
sorted_datas = sorted(list(set(datas)), key=lambda x: (len(x), x))
print('\n'.join(sorted_datas))
