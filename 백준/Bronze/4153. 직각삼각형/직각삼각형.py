"""
기존 코드. 정렬을 이용해, 큰 값을 찾은 후, 피타고라스 정리 사용
해당 문제에서 중요한건, 빗변의 길이가 되는 값을 찾은 후, 해당 숫자를 기억해야한다는 점이다.
이를 위해, 오름차순 정렬을 수행한 후, 마지막에 위치한 가장 큰값을 빗변으로 피타고라스 정리를 통해,
참/거짓 유무를 판단한다.

+) sys.stdin 입력 관련
sys.stdin도 결국 외부의 입력을 담당하는 하나의 이터러블 객체로, for 루프의 이터러블 객체로 사용 가능하다.
for line in sys.stdin이 해당 사용의 예시이다.

+) map + sorted 관련
map은 컨베이어 벨트 역할을 수행하며, sorted는 반드시 파라미터가 리스트가 아니여도 가능하다!
"""
import sys

# sys.stdin = open("input.txt", "r")
# data = list(map(int, sys.stdin.read().split()))
# answer = []
# for i in range(0, len(data), 3):
#     if data[i] == 0 and data[i + 1] == 0 and data[i + 2] == 0:
#         break
#     sorted_list = sorted([data[i], data[i + 1], data[i + 2]])
#     answer.append("right" if sorted_list[2] ** 2 ==
#                              sorted_list[0] ** 2 + sorted_list[1] ** 2 else "wrong")
# print('\n'.join(answer))


# sys.stdin = open("input.txt", "r")

answer = []
for line in sys.stdin:
    a, b, c = sorted(map(int, line.split()))
    if a == 0 and b == 0 and c == 0:
        break
    answer.append("right" if c ** 2 == a ** 2 + b ** 2 else "wrong")
print('\n'.join(answer))
