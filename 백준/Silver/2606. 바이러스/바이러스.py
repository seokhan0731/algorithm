import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)


# def bfs_search():
#     """
#     코드 1. 너비우선 탐색
#     너비우선탐색이란 시작노드에서의 이웃 노드들을 순차적으로 탐색하는 방식이다.
#     이를 코드를 구현할 때는, 그래프를 제외한 두 가지 자료구조가 필요하다.
#     1. 방문 예정 대기열
#     2. 방문 여부 판단 리스트 or 집합...
#     결국 시작 노드의 이웃 노드의 이웃 노드..를 탐색하기 위해서는 지금 현재 노드의 이웃 노드를 갱신해줘야 하기 때문에
#     1.의 방문 예정 리스트가 필요하다.
#     또한 대개 그래프는 인접 리스트 구조로 표현되는데, 방문 여부를 별도로 판단하지 않는다면, 이웃한 노드들간에
#     무한하게 서로 방문하고 리스트에 넣는 일이 벌어지기 떄문에 2.의 방문 여부 판단 자료구조가 필요하다.
#
#     :return: 1을 제외한 1에서 시작하여 방문한 노드 수
#     """
#     total_count = 0
#     while schedule_queue:
#         current_node = schedule_queue.popleft()
#         for node in graph[current_node]:
#             if node not in visited:
#                 schedule_queue.append(node)
#                 visited.add(node)
#                 total_count += 1
#     return total_count

# def dfs_search(target_node):
#     """
#     코드 2. 스택을 이용한 DFS 구현
#     DFS는 결국 가장 최근의 탐색한 노드에서 꼬리를 물고 들어간다는 점에서,
#     꼬리를 물지 않고, 이웃들을 먼저 탐색하는 BFS와 구분된다.
#     이러한 탐색 알고리즘 탓에 BFS는 큐로 구현되고, DFS는 스택을 통해 구현된다.
#     스택은 LIFO구조로, 가장 최근에 탐색한 노드에서 인접한 이웃들은 확인하고, 이웃들을 다시
#     푸시하는 구조로 구현된다.
# 
#     +) 방문->방문 도장->이웃 탐색순
#     :param target_node: 탐색을 시작할 노드
#     :return: 탐색한 총 노드의 개수
#     """
#     total_count = 0
#     schedule_stack = [target_node]
#     while schedule_stack:
#         searching_node = schedule_stack.pop()
#         if searching_node not in visited:
#             visited.add(searching_node)
#             total_count += 1
# 
#           for node in graph[searching_node]:
#               if node not in visited:
#                   schedule_stack.append(node)
#     return total_count


def dfs_recursive(target_node):
    """
    코드 3. 재귀를 이용한 DFS 구현
    스택으로 구현한 DFS와 마찬가지로,
    방문->방문 도장->이웃 탐색순으로 진행된다.
    탐색하는 노드의 이웃이 여러개가 존재하더라도, 재귀 호출하는 순간 기존 for문이 돌지 않고,
    새로운 함수 스택을 할당받고 진행되기 때문에, 더 이상 갈 노드가 없을 정도로 먼저 내려간 뒤,
    백트래킹을 통해 나머지 탐색이 진행된다.

    :param target_node: 탐색 시작 노드
    :return: None(visited 원본 집합 수정)
    """
    visited.add(target_node)
    for node in graph[target_node]:
        if node not in visited:
            dfs_recursive(node)


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
n = int(data[0])
k = int(data[1])
graph = [[] for _ in range(n + 1)]

for line in data[2:]:
    node1, node2 = map(int, line.split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = set()

# 1. BFS
# schedule_queue = deque([1])
#
# print(bfs_search())


# 2-1. DFS(스택 이용)
# print(dfs_search(1))

# 2-2. DFS(재귀 이용)
dfs_recursive(1)
print(len(visited) - 1)
