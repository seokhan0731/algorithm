from collections import deque

def solution(priorities, location):
    priorities_queue = deque()
    process_set = set()
    for idx, val in enumerate(priorities):
        process_set.add(idx)
        priorities_queue.append([idx, val])

    print(priorities_queue)

    answer = 0
    while location in process_set:
        current_process = priorities_queue.popleft()

        flag = 0
        for priority in priorities_queue:
            if priority[1] > current_process[1]:
                priorities_queue.append(current_process)
                flag = 1
                break

        if flag==1:
            continue

        answer += 1
        process_set.discard(current_process[0])

    return answer