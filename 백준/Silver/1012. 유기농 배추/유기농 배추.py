import sys
sys.setrecursionlimit(10**8)

def dfs_search(origin_x, origin_y):
    res.append([origin_x, origin_y])
    x_plus, x_minus = (origin_x + 1, origin_y), (origin_x - 1, origin_y)
    y_plus, y_minus = (origin_x, origin_y + 1), (origin_x, origin_y - 1)
    if x_plus in location1 and x_plus not in visited:
        visited.add(x_plus)
        dfs_search(x_plus[0], x_plus[1])
    if x_minus in location1 and x_minus not in visited:
        visited.add(x_minus)
        dfs_search(x_minus[0], x_minus[1])
    if y_plus in location1 and y_plus not in visited:
        visited.add(y_plus)
        dfs_search(y_plus[0], y_plus[1])
    if y_minus in location1 and y_minus not in visited:
        visited.add(y_minus)
        dfs_search(y_minus[0], y_minus[1])


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()

n = int(data[0])

k = 0
for _ in range(n):
    x1, y1, n1 = map(int, data[1 + k].split())
    location1 = set()
    for idx, line in enumerate(data[2 + k:2 + k + n1]):
        location1.add(tuple(map(int, line.split())))  # set에 리스트 형식 안 들어가는 것 같은데
    visited = set()
    count = 0
    for location in location1:
        x, y = location[0], location[1]
        if location not in visited:
            visited.add(location)
            res = []
            dfs_search(x, y)
            count += 1
    print(count)
    k += (n1 + 1)
