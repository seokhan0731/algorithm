import sys
from collections import deque

dx = [1, -1]


def bfs_search():
    while schedule_queue:
        current_x = schedule_queue.popleft()
        for i in range(2):
            new_x = current_x + dx[i]
            if new_x == target_x:
                return location_graph[current_x] + 1

            if location_graph.get(new_x) is None and 0 <= new_x <= 100000:
                location_graph[new_x] = location_graph[current_x] + 1
                schedule_queue.append(new_x)

        new_x = current_x * 2
        if new_x == target_x:
            return location_graph[current_x] + 1

        if location_graph.get(new_x) is None and 0 <= new_x <= 100000:
            location_graph[new_x] = location_graph[current_x] + 1
            schedule_queue.append(new_x)

    return None


# sys.stdin = open("input.txt", "r")
start_x, target_x = map(int, sys.stdin.read().split())
if start_x == target_x:
    print(0)
    exit()
location_graph = {start_x: 0}
schedule_queue = deque([start_x])
print(bfs_search())
