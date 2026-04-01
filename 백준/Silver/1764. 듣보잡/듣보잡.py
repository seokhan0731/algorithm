import sys
from collections import Counter

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
member_counter = Counter(data[2:])
answer_list = sorted([name for name, frequency in member_counter.items() if frequency == 2])
print(len(answer_list))
print('\n'.join(answer_list))
