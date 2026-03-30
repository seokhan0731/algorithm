import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# def dfs_recursive(origin_x, origin_y):
#     """
#     코드 1. 재귀 방식의 DFS구현
#     해당 문제에서 이동할 수 있는 경우의 수는 상/하/좌/우 총 4가지 경우밖에 없기 때문에,
#     해당 경우의 수로 이동했을 때, 유기농 배추가 존재하는 경우, 재귀 호출을 통해, 이를 반복하는 과정을 거치도록 수행하였다.
#
#     초기에는 그래프는 인접리스트 형식으로만 구현 가능한 줄 알고, 인접 리스트를 어떻게 구현해야할지 생각을 해봤지만,
#     2차원 좌표 값을 노드값으로 사용하기 때문에, 해당값을 인덱스로 사용하기에는 부적절한 것 같아, 위 풀이 방법을 채택하였다.
#     마찬가지로 탐색->방문 여부 확인->방문사실 저장->탐색순을 따른다.
#
#     +) 튜플
#     해당 풀이에서는 단순히 방문 여부를 저장하는 값이나, 노드값을 저장하는 그래프 모두 수정하지 않고,
#     단순히 조회만 하기 떄문에 튜플로 정의했다.
#
#     :param origin_x: 탐색 시작 노드의 x좌표값
#     :param origin_y: 탐색 시작 노드의 y좌표값
#     :return: None(호출 자체로 개별로 떨어진 노드가 존재한다는 사실이기 때문)
#     """
#     for i in range(len(dx)):
#         new_x, new_y = origin_x + dx[i], origin_y + dy[i]
#         if (new_x, new_y) in locations and (new_x, new_y) not in visited:
#             visited.add((new_x, new_y))
#             dfs_recursive(new_x, new_y)


# sys.stdin = open("input.txt", "r")
# data = sys.stdin.read().splitlines()
#
# n = int(data[0])
# k = 0
# for _ in range(n):
#     x1, y1, n1 = map(int, data[1 + k].split())
#     locations = set()
#     for line in data[2 + k:2 + k + n1]:
#         locations.add(tuple(map(int, line.split())))
#     visited = set()
#     count = 0
#     for location in locations:
#         x, y = location[0], location[1]
#         if location not in visited:
#             visited.add(location)
#             dfs_recursive(x, y)
#             count += 1
#     print(count)
#     k += (n1 + 1)


# def dfs_stack():
#     """
#     코드 2. 스택을 이용한 DFS 구현
#     탐색 노드 pop -> 방문하지 않은 인접한 노드 존재시, push순으로 동작
#     while stack: 조건을 사용하기 때문에, while 내부에서 pop을 진행해야 루프를 돌릴 수 있다
#     스택은 마지막에 들어온 놈이 pop되는 구조이기 때문에, DFS 구현에 이용
#
#     :return: None(그래프 탐색 여부만 별도로 카운팅)
#     """
#     while schedule_stack:
#         start_node = schedule_stack.pop()
#         start_x, start_y = start_node[0], start_node[1]
#         for i in range(len(dx)):
#             new_x, new_y = start_x + dx[i], start_y + dy[i]
#             if (new_x, new_y) in locations and (new_x, new_y) not in visited:
#                 visited.add((new_x, new_y))
#                 schedule_stack.append((new_x, new_y))
#
#
# sys.stdin = open("input.txt", "r")
# data = sys.stdin.read().splitlines()
#
# n = int(data[0])
# k = 0
# for _ in range(n):
#     x1, y1, n1 = map(int, data[1 + k].split())
#     locations = set()
#     for line in data[2 + k:2 + k + n1]:
#         locations.add(tuple(map(int, line.split())))
#     visited = set()
#     count = 0
#     for location in locations:
#         x, y = location[0], location[1]
#         if location not in visited:
#             visited.add(location)
#             schedule_stack = [(x, y)]
#             dfs_stack()
#             count += 1
#     print(count)
#     k += (n1 + 1)

def bfs_queue(start_node):
    """
    코드 3. BFS 구현
    BFS는 DFS와 다르게, 이웃부터 탐색하기 때문에, 큐를 사용한다.
    스택과 동일하게 pop을 진행한 노드를 탐색하기 때문에, popleft()를 통해, 이웃 노드를 탐색 후,
    이웃 노드가 인접한 노드가 존재한다면 append를 통해 반대쪽에 push하는 방식으로 수행된다.

    :param start_node: 초기 탐색 시작 노드
    :return: None(그래프 탐색 여부만 별도로 카운팅)
    """
    x, y = start_node
    schedule_queue = deque([(x, y)])
    while schedule_queue:
        origin_x, origin_y = schedule_queue.popleft()
        for i in range(len(dx)):
            new_x, new_y = origin_x + dx[i], origin_y + dy[i]
            if (new_x, new_y) in locations and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                schedule_queue.append((new_x, new_y))


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()

n = int(data[0])
k = 0
for _ in range(n):
    x1, y1, n1 = map(int, data[1 + k].split())
    locations = set()
    for line in data[2 + k:2 + k + n1]:
        locations.add(tuple(map(int, line.split())))
    visited = set()
    count = 0
    for location in locations:
        x, y = location[0], location[1]
        if location not in visited:
            visited.add(location)
            bfs_queue(location)
            count += 1
    print(count)
    k += (n1 + 1)
