"""
그리디 알고리즘을 통한 풀이
최대한 많은 회의실을 사용하기 위한 최선의 선택은 선택 가능한 회의실 중,
가장 빠른 시점에 종료되는 회의실을 선택하면 된다.
입력은 무조건 하나 이상 존재하기 때문에, n!=1인 일반적인 경우에서는 무조건 idx=0인 회의를 선택해야 한다.
따라서 선형 탐색 전, count의 초기값을 1로 선형탐색을 할 리스트 시작점을 idx=1로 지정하여 코드를 구현했다.

+)정렬이 안 된 상태에서 탐색을 하고자하면 가장 빨리 끝나는 회의 찾고, 루프를 순회하는 등 불필요한 비용이 많아지기 때문에, 정렬을 선행했다.
또한 해당 문제에서는 시작 시각과 종료 시각이 같을 수도 있다는 점을 인지해야 하는데, 정렬 수행시, 종료 시점 정렬 후,
시작 시점 기준으로 2차 정렬을 수행하지 않으면, 입력 순서대로 가만히 존재하기 때문에 [2,2],[1,2]와 같은 케이스에서
1로 출력이 된다. 따라서 ***튜플***로 묶어 람다식을 설정해줘야 한다!  (초기에 햇갈려서 집합으로 람다식 설정해서 틀렸음!)

+) enumerate()
초기 코드는 가장 최근의 종료 시점값을 기억하지 않고, 인덱스만을 기억하기 위해 enumerate를 사용하여 구현하고,
enumerate의 start 파라미터를 리스트의 시작 시점으로 착각하여 start=1로 설정하였지만,
이때의 start는 오리지널 idx=0을 1로 치환하여 순회하는 것이지 오리지널 인덱스 1부터 순회하라는 것이 아니었음!
"""
import sys

START_IDX = 0
END_IDX = 1

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
n = int(data[0])
if n == 1:
    print(1)
    exit()
time_list = sorted((list(map(int, line.split())) for line in data[1:]), key=lambda x: (x[1], x[0]))

total_count = 1
last_time = time_list[0][END_IDX]
for time in time_list[1:]:
    if last_time <= time[START_IDX]:
        total_count += 1
        last_time = time[END_IDX]
print(total_count)
