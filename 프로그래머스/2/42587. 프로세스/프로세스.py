from collections import deque


# def solution(priorities, location):
#     answer = 0
#     priorities_queue = deque(priorities)
#     priorities_dic = Counter(priorities)
#     how_many_higher_priorities = []
#     for priority in priorities_queue:
#         count = 0
#         for k, v in priorities_dic.items():
#             if k > priority:
#                 count += v
#         how_many_higher_priorities.append(count)
#
#     if how_many_higher_priorities[idx] != 0:
#         priorities_queue.append(priorities_queue.popleft())
#     else:
#         answer += 1
#         priorities_queue.popleft()
#
#     return answer


# def solution(priorities, location):
#     """
#     기존 코드. 루프마다 우선순위가 높은 프로세스 존재 유무 확인
#     해당 문제에서의 핵심은 2가지이다.
#     1. 자기 자신보다 높은 우선순위가 존재하는지 how 확인?
#     2. location에 부합하는 인덱스를 어떻게 관리?
#
#     1.은 루프마다 any()를 통해 해결
#     2.은 큐의 요소들을 [idx, 우선순위]꼴로 저장하여, 기존 idx를 저장한 후, location과 대조
#
#     * 초기에는 매 루프마다 우선순위가 높은 것을 조회하는 것이 낭비라고 생각하여, 미리 자기 자신보다 높은 요소들의 개수를 구해놓은 후,
#     이를 이용하고자 하는 로직을 설계하였지만, 설계 도중, 높은 우선순위가 pop이 되었을 때, 갱신하는 로직에서 막힘
#     -> pop이 된 순간, 다시 루프를 순회하며 갱신해야 하는 문제 존재-> 루프 회피를 위해, 설계했지만, 결국 루프 필수
#     -> 우선순위가 동점인 경우 처리 필요
#     -> 이에 따라, 주어진 n 조건이 100이하이게에, 그냥 매 루프마다 조회하도록 구현
#
#     :param priorities: 우선순위값을 담은 리스트
#     :param location: 실행 순서를 구하고자 하는 프로세스의 idx
#     :return: location의 위치한 요소의 실행 순서
#     """
#     priorities_queue = deque([(i, p) for i, p in enumerate(priorities)])
#     answer = 0
#
#     while True:
#         current_process = priorities_queue.popleft()
#         if any(current_process[1] < priority[1] for priority in priorities_queue):
#             priorities_queue.append(current_process)
#         else:
#             answer += 1
#             if current_process[0] == location:
#                 break
#
#     return answer

def solution(priorities, location):
    """
    코드2. 현재 가장 높은 우선순위 활용
    기존 코드에서, 루프를 순회하며, 자기 자신보다 높은 우선순위가 있는지 조회하기보단, 우선순위를 별도로 정렬 수행.
    해당 정렬된 우선순위를 통해, 현 시점에 가장 높은 우선순위가 맞는지만 확인해주면 된다.
    비록 메모리는 더 먹고, 정렬 수행시 O(NlogN)이 들지만, 탐색 과정을 O(1)으로 처리 가능

    :param priorities: 우선순위값을 담은 리스트
    :param location: 실행 순서를 구하고자 하는 프로세스의 idx
    :return: location의 위치한 요소의 실행 순서
    """
    sorted_priorities = deque(sorted(priorities, reverse=True))
    priorities_queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0

    while True:
        current_process = priorities_queue.popleft()
        if current_process[1] == sorted_priorities[0]:
            answer += 1
            sorted_priorities.popleft()
            if current_process[0] == location:
                return answer
        else:
            priorities_queue.append(current_process)