import sys
from collections import deque


def bfs_search():
    """
    코드 1. 너비우선 탐색
    너비우선탐색이란 시작노드에서의 이웃 노드들을 순차적으로 탐색하는 방식이다.
    이를 코드를 구현할 때는, 그래프를 제외한 두 가지 자료구조가 필요하다.
    1. 방문 예정 대기열
    2. 방문 여부 판단 리스트 or 집합...
    결국 시작 노드의 이웃 노드의 이웃 노드..를 탐색하기 위해서는 지금 현재 노드의 이웃 노드를 갱신해줘야 하기 때문에
    1.의 방문 예정 리스트가 필요하다.
    또한 대개 그래프는 인접 리스트 구조로 표현되는데, 방문 여부를 별도로 판단하지 않는다면, 이웃한 노드들간에
    무한하게 서로 방문하고 리스트에 넣는 일이 벌어지기 떄문에 2.의 방문 여부 판단 자료구조가 필요하다.

    :return: 1을 제외한 1에서 시작하여 방문한 노드 수
    """
    total_count = 0
    while schedule_queue:
        current_node = schedule_queue.popleft()
        for node in graph[current_node]:
            if node not in visited:
                schedule_queue.append(node)
                visited.add(node)
                total_count += 1
    return total_count


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
visited.add(1)
schedule_queue = deque([1])

print(bfs_search())
