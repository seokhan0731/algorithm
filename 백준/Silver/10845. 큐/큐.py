import sys
from collections import deque


def control_queue(command, queue_val):
    if command.startswith("push"):
        queue_val.append(command.split()[-1])
    elif command == "pop":
        if queue_val:
            print(queue_val.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(queue_val))
    elif command == "empty":
        if queue_val:
            print(0)
        else:
            print(1)
    elif command == "front":
        if queue_val:
            print(queue_val[0])
        else:
            print(-1)
    else:
        if queue_val:
            print(queue_val[-1])
        else:
            print(-1)


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()[1:]
queue_val = deque([])
for line in data:
    control_queue(line, queue_val)
