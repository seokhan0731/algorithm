import sys
from bisect import bisect_left
from bisect import bisect_right

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
_ = input()
having_list = sorted(map(int, input().split()))
_ = input()
target_list = map(int, input().split())

answer_list = []
answer_dic = {}
for target in target_list:
    if target in answer_dic:
        answer_list.append(answer_dic[target])
    else:
        if bisect_left(having_list, target) >= len(having_list):
            answer_dic[target] = 0
            answer_list.append(0)
        else:
            answer_dic[target] = bisect_right(having_list, target) - bisect_left(having_list, target)
            answer_list.append(answer_dic[target])
print(' '.join(map(str, answer_list)))
