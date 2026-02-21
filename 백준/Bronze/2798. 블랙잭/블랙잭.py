"""
기존 코드. 브루트포스 알고리즘 이용
3가지 카드를 뽑아, 주어진 m에 가장 근접하는 최대값을 만들어야 되기 때문에, 그리디 알고리즘 사용 불가
-> 모든 경우의 수를 구하며, 조건에 만족하는 최대값만을 별도로 저장하며, 갱신하주는 브루트포스 알고리즘 사용

+) 파이썬 문법 정리
1. 쓸데없는 값 무시하기
자바나 c계열에서는 n을 받아 루프를 돌며 n만큼 값을 채워줘야 하지만, 파이썬은 자료의 크기를 굳이 정할 필요 X
-> 해당 문제에서는 n 필요 X, '_" 사용하여 무시 가능 -> 의미 없는 루프 변수 _로 하는 것과 같은 맥락인듯?

2. combinations 이용
초기에는 주석처리된 것처럼 삼중루프를 이용하여, 풀이를 했지만, 이와 같은 역할을 하는 것이 combinations
->브루트포스 알고리즘에 최적화 되어있는듯(다중 루프와 시간복잡도는 동일(n^3))

3. range vs slice
슬라이싱을 하는 경우, -를 사용하여, 맨 뒤부터 요소에 접근할 수 있지만, range 의도대로 사용 불가
세 번째 파라미터로 감소를 넣어 range(10,-1,-1)이런식으로 하는 방법밖에 존재 X

4. 다중 루프
다중 루프 시, 바깥 루프의 변수를 사용하고자 하면, range를 사용하는 방법밖에 X
"""
import sys
from itertools import combinations


# def black_jack(cards, m):
#     length = len(cards)
#     max_val = 0
#     for i in range(0, length - 2):
#         for j in range(i + 1, length - 1):
#             for k in range(j + 1, length):
#                 total = cards[i] + cards[j] + cards[k]
#                 if total <= m and total > max_val:
#                     max_val = total
#     return max_val

def black_jack(cards, m):
    max_val = 0
    for i in combinations(cards, 3):
        total = sum(i)

        if total > max_val and total <= m:
            max_val = total
    return max_val


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

_, m = map(int, input().split())
cards = list(map(int, input().split()))

print(black_jack(cards, m))
