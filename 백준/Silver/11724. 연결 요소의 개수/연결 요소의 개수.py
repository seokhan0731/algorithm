import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)


# def bfs_search(start_idx):
#     """
#     코드 1. bfs를 통한 연결 요소 개수 구하기
#     결국 출력해야 하는 값은 탐색 함수 호출 횟수로, 몇 번 호출해야 모든 정점을 탐색할 수 있냐는 문제로 귀결된다.
#     우선 인접 리스트꼴로 그래프를 구현한 후, 방문 여부를 담을 리스트와 함께 1번 노드부터 탐색을 수행한다.
#     탐색 후, 아직 방문 하지 않은 정점이 있다면, 해당 정점을 기준으로 탐색을 진행해가며, 함수 호출 횟수를 별도로 카운팅한다.
#
#     +) 방문 여부를 확인할 때, node in visited_list를 통해 구현했지만, 정점의 개수가 늘어나는만큼
#     in 연산자를 통한 리스트 순회 비용 등을 생각하면, 단순히 방문 여부만 체크하면 되기에,
#     Boolean형 리스트를 미리 정점 개수만큼 할당하여, 인덱스를 통해 접근하도록 하는 것이 더 효율적이였다!
#
#     :param start_idx: 탐색 시작 인덱스
#     :return: None(탐색 진행하며, visited_list에 정점 탐색 여부 기록함)
#     """
#     schedule_queue.append(start_idx)
#     visited_list[start_idx] = True
#     while schedule_queue:
#         start_node = schedule_queue.popleft()
#         for adjacent_node in graph_list[start_node]:
#             if not visited_list[adjacent_node]:
#                 visited_list[adjacent_node] = True
#                 schedule_queue.append(adjacent_node)


# def dfs_recursive(start_idx):
#     """
#     코드 2. 재귀 방식의 dfs 구현
#     인접한 노드 기준으로 재귀 호출을 통해, 더 이상 인접 노드가 없는 레벨까지 내려가기 때문에,
#     dfs 탐색으로 볼 수 있음
#
#     :param start_idx: 탐색 시작 인덱스
#     :return: None(탐색 진행하며, visited_list에 정점 탐색 여부 기록함)
#     """
#     visited_list[start_idx] = True
#     for adjacent_node in graph_list[start_idx]:
#         if not visited_list[adjacent_node]:
#             dfs_recursive(adjacent_node)

# def dfs_stack(start_idx):
#     """
#     코드 3. 스택을 통한 dfs 구현
#     만약 인접 노드의 방문 여부를 확인하자마자 방문 도장을 찍지 않고, pop()하는 시점에 도장을 찍는다면?
#     코드 자체는 의도대로 탐색을 수행하지만, 스택에 중복된 노드들이 여러 개가 존재 할 수가 있다.
#     첫 pop 이전 시점에는 뱡문 안 한줄 알고, 계속 append하기 떄문 (시점 주의!)
#
#     :param start_idx: 탐색 시작 인덱스
#     :return: None(탐색 진행하며, visited_list에 정점 탐색 여부 기록함)
#     """
#     visited_list[start_idx] = True
#     schedule_stack.append(start_idx)
#     while schedule_stack:
#         start_node = schedule_stack.pop()
#         for adjacent_node in graph_list[start_node]:
#             if not visited_list[adjacent_node]:
#                 visited_list[adjacent_node] = True
#                 schedule_stack.append(adjacent_node)


# sys.stdin = open("input.txt", "r")
# data = sys.stdin.read().splitlines()
# node_count, edge_count = map(int, data[0].split())
# graph_list = [[] for _ in range(node_count + 1)]
#
# for line in data[1:]:
#     node1, node2 = map(int, line.split())
#     graph_list[node1].append(node2)
#     graph_list[node2].append(node1)
#
# visited_list = [False] * (node_count + 1)

# 코드 1. bfs
# component_count = 0
# schedule_queue = deque()
# for i in range(1, node_count + 1):
#     if not visited_list[i]:
#         bfs_search(i)
#         component_count += 1
# print(component_count)


# 코드 2. dfs_recursive
# component_count = 0
# for i in range(1, node_count + 1):
#     if not visited_list[i]:
#         dfs_recursive(i)
#         component_count += 1
# print(component_count)

# 코드 3. dfs_stack
# schedule_stack = []
# component_count = 0
# for i in range(1, node_count + 1):
#     if not visited_list[i]:
#         dfs_stack(i)
#         component_count += 1
# print(component_count)


def find_parent(node):
    if parent_list[node] == node:
        return node
    parent_list[node] = find_parent(parent_list[node])
    return parent_list[node]


# 작은 노드의 부모 인덱스를 node1이랑 node 2중 누가 갖고 있는지를 알아야되네
def union(node1, node2):
    global count_val
    node1_parent = find_parent(node1)
    node2_parent = find_parent(node2)
    if node1_parent != node2_parent:
        count_val -= 1
        if node1_parent > node2_parent:
            parent_list[node1_parent] = node2_parent
        else:
            parent_list[node2_parent] = node1_parent


# 코드 4. 유니온 파인드
# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
node_count, edge_count = map(int, data[0].split())
parent_list = [i for i in range(node_count + 1)]
count_val = node_count
for line in data[1:]:
    node1, node2 = map(int, line.split())
    union(node1, node2)

print(count_val)
