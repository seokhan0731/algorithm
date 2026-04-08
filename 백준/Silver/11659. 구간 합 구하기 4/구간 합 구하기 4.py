import sys
from itertools import accumulate

"""
accumulate() 누적합을 통한 구현
누적합을 담은 리스트를 d라고 할 때,
d[j]-d[i]를 통해 j번째 누적합-(i-1)번째 누적합을 진행한다면, 
i~j까지의 합만이 남는 구조이기 때문에, 입력으로 들어온 데이터를 누적합 구조로 제작한 후,
해당 공식을 통해 풀이할 수 있었다,

+) 의미없는 초항 idx=0을 별도로 추가하지 않으면, start_num-1 부분에서 별도의 분기 처리를 해줘야하기 때문에,
누적합의 영향을 끼치지 못하는 0을 idx=0번에 추가하였다.
"""


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())
accumulate_list = [0] + list(accumulate(map(int, data[1].split())))

for line in data[2:]:
    start_num, finish_num = map(int, line.split())
    print(accumulate_list[finish_num] - accumulate_list[start_num - 1])
