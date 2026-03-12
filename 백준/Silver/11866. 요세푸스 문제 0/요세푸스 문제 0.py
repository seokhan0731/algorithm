"""
기존 코드. rotate()를 통한 원형큐 구현
해당 문제는 원형 큐를 통해 순환을 구현해야한다.
자바에서는 별도의 구현방법이 없기 때문에, 순환해야하는 만큼 offer 후, poll을 진행하여 구현했지만,
파이썬에서는 rotate(회전 수)를 사용하여, 돌리고 제거하는 방식으로 구현할 수 있었다.
m번째를 계속 제거해야하기 때문에, popleft()를 적용하기 위해 -m+1만큼 계속 앞으로 끌고온다.
m-1개의 요소를 뒤로 보내줘야하기 때문에, -(ㅡm-1)을 수행하여 -m+1만큼 앞으로 끌고온다.
"""
import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
# n, m = map(int, input().split())
# circular_queue = deque([str(i) for i in range(1, n + 1)])
# answer = []
# while circular_queue:
#     circular_queue.rotate(-m + 1)
#     answer.append(circular_queue.popleft())
#
# print('<' + ', '.join(answer) + '>')

"""
코드 2. 나머지 이용 풀이
두 번째 풀이는 순환해야하는 원형 큐의 특성을 나머지로 구현한다.
순환을 할때 %현재 길이를 통해, 진행되는 인덱스를 범위 안에서 구할 수 있는데, 이 특성을 활용하여,
(현재 idx+m-1)%현재 길이를 통해, 해당 순서에서 제거되야 하는 대상이 존재하는 인덱스를 직접 구하여 과정을 수행한다.
이때 m이 아닌 m-1이 들어가는 이유는, 첫 번째 제거되는 경우를 제외하고는, 그 전 과정에서 제거되는 과정이 
한 칸씩 당겨주는 역할을 하기 때문이며, 첫 번째 제거되는 경우는 인덱스가 1이 아닌 0부터 시작하기 때문이다. 
"""
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
circular_queue = [str(i) for i in range(1, n + 1)]
current_idx = 0
answer = []
while circular_queue:
    current_idx = (current_idx + m - 1) % len(circular_queue)
    answer.append(circular_queue.pop(current_idx))
print('<' + ', '.join(answer) + '>')
