import sys
from collections import deque


def bfs_search(start_idx):
    schedule_queue.append(start_idx)
    while schedule_queue:
        start_node = schedule_queue.popleft()
        if start_node not in visited_list:
            visited_list.append(start_node)
            for adjacent_node in graph_list[start_node]:
                schedule_queue.append(adjacent_node)


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
node_count, edge_count = map(int, data[0].split())
graph_list = [[] for _ in range(node_count + 1)]

for line in data[1:]:
    node1, node2 = map(int, line.split())
    graph_list[node1].append(node2)
    graph_list[node2].append(node1)

visited_list = []
schedule_queue = deque()

component_count = 0

for i in range(1, node_count + 1):
    if i not in visited_list:
        bfs_search(i)
        component_count += 1
print(component_count)
