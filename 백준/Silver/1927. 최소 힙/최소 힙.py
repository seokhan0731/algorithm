"""
1. 연산의 개수를 굳이 쓸 필요는 없고
2. 각 line을 for문을 통해 입력받음
3. 각 커멘드에 따른 행동을 함수로 구현
    0 -> 배열에 있는 가장 최소 값 출력 및 제거
    그 외 -> x를 넣어줌
    근데 만약에 비어있으면 이때도 0을 출력한다.
4. io를 그때마다 부를수는 없으니까 append를 통해 모아놓고 한꺼번에 출력하는 구조
"""
import heapq
import sys


def control_heapq(command):
    if command == '0':
        answers.append(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, int(command))


# sys.stdin = open("input.txt", "r")
commands = sys.stdin.read().splitlines()[1:]

answers = []
heap = []
for command in commands:
    control_heapq(command)
print('\n'.join(map(str, answers)))
