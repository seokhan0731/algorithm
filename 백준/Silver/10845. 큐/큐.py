"""
기존 코드. deque를 통한 큐 구현
append(left), pop(left)와 인덱싱을 결합하여, 구현
+) 초기에는 append를 하지 않고, 각 command마다 print를 했지만,
append 후 한번에 출력하는 것이 I/O 관련 병목 현상이나 비용 등에서 유리하기 때문에, append() 후
한 번에 출력하는 방식으로 변경
"""
import sys
from collections import deque


def control_queue(command, queue_val, answer):
    if command.startswith("push"):
        queue_val.append(command.split()[-1])
    elif command == "pop":
        answer.append(queue_val.popleft() if queue_val else -1)
    elif command == "size":
        answer.append(len(queue_val))
    elif command == "empty":
        answer.append(0 if queue_val else 1)
    elif command == "front":
        answer.append(queue_val[0] if queue_val else -1)
    else:
        answer.append(queue_val[-1] if queue_val else -1)


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()[1:]
queue_val = deque([])
answer = []
for line in data:
    control_queue(line, queue_val, answer)
print('\n'.join(map(str, answer)))
