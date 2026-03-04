"""
기존 코드. deque를 통한 큐 구현
해당 문제는 제거->뒤로 옮기기->제순으로 이루어진다.
뒤로 옮기는 것을 삽입의 과정으로 이해한다면, 양방향에서 제거와 요소 추가가 이루어져야 한다는 것이다.
초기에는 이에 따라 list를 사용하여, pop()과 insert()를 사용하여, 구현했지만, 시간초과가 발생하였다.
그 이유를 분석했을 때, insert()는 해당 위치까지 하나하나 요소를 건너뛰며 이루어지기 떄문에, 큰 데이터에서는
막대한 시간비용이 소요되기 때문이었다.
이를 해결하기 위해, 양방향 삽입과 삭제가 가능한 deque자료구조를 도입하여 풀이하였다.

+) java vs python deque
조회: peak <-> 인덱스 접근
pop: poll <-> pop(left)
삽입: offer <-> append(left)

+) 리스트 컴프리헨션이 불필요한 경우
파이썬에서는 list나 deque나 새로 만들 때, 굳이 리스트로 포장을 하지 않아도 되는 경우가 존재하는데,
이는 들어는 것이 이터러블 객체일 경우이다. range도 이터러블 객체로 인식되기 때문에
초기 deque([i for i in range(1,n+1)])을 사용하는 대신 deque(range(1,n+1))을 해주면 된다.
"""
import sys
from collections import deque


def card_game(n):
    # card_deque = deque([i for i in range(1, n + 1)])
    card_deque = deque(range(1, n + 1))
    while len(card_deque) > 1:
        card_deque.popleft()
        card_deque.append(card_deque.popleft())
    print(card_deque[0])


# sys.stdin = open("input.txt", "r")
input = sys.stdin.read

n = int(input())
card_game(n)
