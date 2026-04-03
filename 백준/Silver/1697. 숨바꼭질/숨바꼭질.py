import math
import sys
from collections import deque

# def bfs_search():
#     """
#     코드 1. 딕셔너리를 통한 bfs 구현
#     그전까지의 bfs 문제들은, 노드가 명시되어 있어, 인접리스트로 그래프 형태를 구현하거나,
#     다차원 리스트로 시뮬레이션을 직접 돌릴 수 있었지만, 해당 문제는 인접하는 노드를,
#     채택할 수 있는 3가지 경우의 연산값들로 직접 정의해야했다. 선형 구조의 숫자들로 연산자들을 통해,
#     특정 목표에 대해 도달했어야한다, 시뮬레이션 문제랑 다르게 모든 값들이 정의되어 있는 상태가 아니였기 때문에,
#     연속된 구조의 리스트를 채택하기보단, 딕셔너리 구조를 채택하여 탐색한 노드들만 별도로 담아놓는 역할을 수행하게 하였다.
#     딕셔너리 구조를 통해, 방문한 노드(key), 방문 일자(value)로 해당 딕셔너리를 통해
#     방문 여부 판단 및 최소값 판단의 기반으로 사용할 수 있었다.
#     이또한 bfs이기 때문에, 탐색 노드 설정->인접 노드 방문 여부 판단->방문 일시 기록 및 다음 탐색 노드로 추가순으로 진행한다.
#
#     +) 튜플도 결국 이터러블 객체이기 때문에, for문을 통해 돌릴 수 있었다.
#     이전 문제까지는 +-연산자만 존재했기에 전역리스트로 dx=[1,-1]꼴로 추가하여 for문을 돌렸지만, *같은 종류의 연산이 필요하다하면
#     튜플로도 사용할 수 있다.
#
#     +) 해당 문제에서 bfs탐색을 채택해야 하는 이유는 다음과 같다.
#     그리디 알고리즘의 경우에서는, -1과 *2라는 선택지가 있기 때문에, 단순히 정방향으로 가는 선택지만 존재하는 것이 아니다.
#     즉, 어떠한 선택이 해당 선택지에서 최선이라고 볼 수 있는 기준이 존재하지 않기 때문에 기각된다.
#     dp의 경우에도 단순히 한 방향으로 가서 dp[n]와 dp[n-k]와의 점화식을 도출해야 하지만,
#     -1이라는 다른 방향으로 갈 수 있는 선택지가 존재하기에, 기각된다.
#
#     => 해당 문제에서 모든 이동 경우의 수의 가중치가 1이기 때문에, bfs 탐색을 통해 구현한다! (가중치가 각각이라면 다익스트라!)
#
#     :return: 최소 일수
#     """
#     while schedule_queue:
#         current_x = schedule_queue.popleft()
#         for new_x in (current_x + 1, current_x - 1, current_x * 2):
#             if new_x == target_x:
#                 return location_graph[current_x] + 1
#
#             if location_graph.get(new_x) is None and 0 <= new_x <= 100000:
#                 location_graph[new_x] = location_graph[current_x] + 1
#                 schedule_queue.append(new_x)
#     return None
#
#
# # sys.stdin = open("input.txt", "r")
# start_x, target_x = map(int, sys.stdin.read().split())
# if start_x == target_x:
#     print(0)
#     exit()
# location_graph = {start_x: 0}
# schedule_queue = deque([start_x])
# print(bfs_search())

# 코드 2. 리스트 자료구조 채택
MAX_SIZE = 100000


def bfs_search():
    """
    코드 2. 리스트 자료구조를 통한 bfs 구현
    문제에서의 입력의 개수는 제한이 되어있기 때문에, 딕셔너리보다, 리스트를 통해 탐색 속도를 높일 수 있다.
    토마토 문제와 같게, 결국 방문 여부를 판단할 값만 존재하면 되기 때문에, 별도의 visited 리스트를 만들기보단,
    math.inf로 배열값을 초기화 후, 초기 스타팅 포인트만 0으로 판단하여, 방문여부를 판단할 수 있었다.
    그 외는 기존 bfs와 같은 흐름으로 진행된다.

    :return: 도달할 수 있는 최소 시간
    """
    while schedule_queue:
        current_x = schedule_queue.popleft()
        for new_x in (current_x + 1, current_x - 1, current_x * 2):
            if new_x == target_x:
                return graph_list[current_x] + 1
            if 0 <= new_x <= MAX_SIZE and graph_list[new_x] == math.inf:
                graph_list[new_x] = graph_list[current_x] + 1
                schedule_queue.append(new_x)
    return None


# sys.stdin = open("input.txt", "r")
start_x, target_x = map(int, sys.stdin.read().split())
if start_x == target_x:
    print(0)
    exit()
graph_list = [math.inf] * (MAX_SIZE + 1)
graph_list[start_x] = 0
schedule_queue = deque([start_x])
print(bfs_search())
