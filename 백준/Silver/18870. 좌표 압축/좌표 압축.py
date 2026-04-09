import bisect
import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
n = int(data[0])
number_list = list(map(int, data[1].split()))
number_set = sorted(set(number_list))
answer_list = []
for i in number_list:
    answer_list.append(bisect.bisect_left(number_set, i))
print(' '.join(map(str, answer_list)))
