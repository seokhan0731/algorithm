import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs_search(start_nodes):
    """
    코드1. 큐를 통한 bfs 구현
    일반적인 그래프 탐색은 dfs와 bfs가 존재하지만, 이웃 노드를 먼저 탐색하지 않고,
    이웃의 이웃으로 넘어가는 dfs 특성상, 최소값 문제에 적절치 않음
    -> 이웃 노드부터 차근차근 탐색하는 bfs 사용

    1인 부분에서 첫 시작을 해야하며, 1인 부분이 여러 부분이 존재할 수 있기 때문에, 1인 지점을 기억하고,
    큐에 초기값으로 할당하여, 다중 시작점 구현
    일반적인 bfs에서는 visited를 통해, 방문 여부를 별도로 체크했지만,
    최소값을 위해, 전이된 시점의 일자를 기억해야 하기때문에 2차원 리스트에 요소 값을 일자 기록용과 방문 체크용으로 동시에 사용
    시작점 기억->popleft()를 통한 탐색 시작점 설정->방문 여부 확인->다음 탐색점 저장순 진행

    :param start_nodes: 다중 시작점 위치
    :return: None(토마토 리스트 원본 기록)
    """
    schedule_queue = deque(start_nodes)
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

# 다중 시작점 기억
idx_list1 = []
for i in range(n):
    for k in range(m):
        if tomato_map[i][k] == 1:
            idx_list1.append((i, k))
bfs_search(idx_list1)

# 최소 일수 탐색
total_max = 1
for line in tomato_map:
    if 0 in line:
        print(-1)
        exit()
    total_max = max(total_max, max(line))

print(total_max - 1)
