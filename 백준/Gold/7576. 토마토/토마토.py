import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs_search(start_nodes):
    schedule_queue = deque([])
    for node in start_nodes:
        schedule_queue.append(node)
    while schedule_queue:
        origin_x, origin_y = schedule_queue.popleft()
        for i in range(len(dx)):
            new_x = origin_x + dx[i]
            new_y = origin_y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if tomato_map[new_x][new_y] == 0:
                    tomato_map[new_x][new_y] = tomato_map[origin_x][origin_y] + 1
                    schedule_queue.append((new_x, new_y))


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
m, n = map(int, data[0].split())
tomato_map = [list(map(int, line.split())) for line in data[1:]]
# 1인 부분의 인덱스 위치를 기억해줘야하는데, 어떻게 기억해줘야 할까
idx_list1 = []
for i in range(n):
    for k in range(m):
        if tomato_map[i][k] == 1:
            idx_list1.append((i, k))
bfs_search(idx_list1)

total_max = 1
for line in tomato_map:
    if 0 in line:
        print(-1)
        exit()
    total_max = max([total_max] + line)

print(total_max-1)
