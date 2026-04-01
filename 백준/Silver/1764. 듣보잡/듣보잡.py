import sys
from collections import Counter

"""
코드 1. counter를 통한 구현
결국 듣지 못한 사람과 보지 못한 사람의 교집합이기 때문에,
입력값에서 멤버의 이름이 두 번 존재한다면, 해당 멤버를 출력해야 정렬 후, 출력하면 된다.
이에 따라 counter를 통해, 빈도 수==2인 경우 별도의 리스트에 기입 후, 정렬하여 구현했다.
"""
# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
# member_counter = Counter(data[2:])
# answer_list = sorted([name for name, frequency in member_counter.items() if frequency == 2])
# print(len(answer_list))
# print('\n'.join(answer_list))

"""
코드 2. set의 교집합 연산자를 통한 구현
교집합을 구하는 문제이기 때문에, 듣지 못한 사람 집합 & 보지 못한 사람 집합을 통해, 별도의 리스트로 할당 후, 정렬

+) 집합 연산자 정리(두 개 다 집합인 경우, 집합a와 리스트 b인경우)
교집합: &      a.intersection(b)
합집합: |      a.union(b)
차집합: a-b    a.difference(b)
대칭차집합: a^b      a.symmetric_difference(b)
"""
n, m = int(data[0]), int(data[1])
no_hear_set = set(data[2:n + 2])
no_see_set = set(data[n + 2:])
answer_list = sorted(no_see_set & no_hear_set)
print(len(answer_list))
print('\n'.join(answer_list))
