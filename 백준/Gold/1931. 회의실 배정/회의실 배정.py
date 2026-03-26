import sys

START_IDX = 0
END_IDX = 1

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
n = int(data[0])
if n == 1:
    print(1)
    exit()
time_list = sorted((list(map(int, line.split())) for line in data[1:]), key=lambda x: (x[1], x[0]))

total_count = 1
last_time = time_list[0][END_IDX]
for time in time_list[1:]:
    if last_time <= time[START_IDX]:
        total_count += 1
        last_time = time[END_IDX]
print(total_count)
