import sys
from itertools import accumulate

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())
accumulate_list = [0] + list(accumulate(map(int, data[1].split())))

for line in data[2:]:
    start_num, finish_num = map(int, line.split())
    print(accumulate_list[finish_num] - accumulate_list[start_num - 1])
