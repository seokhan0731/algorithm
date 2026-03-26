"""
코드 1. for문을 통한 누적합 구하기
해당 문제에서는 두 가지 과정을 진행해야 한다.
1. 전체 누적합 구조가 최소가 되게끔 구성
2. 누적합 구하기
1,2가 해당 과정인데, 결국 누적합을 최소로 만들기 위해서는 큰 수를 최대한 뒤쪽으로 배치하여,
큰 수가 나오는 빈도 수를 줄여야 했다.
이를 수행하기 위해 입력값을 sorted()를 통해 오름차순으로 정렬된 list로 구성했다.
또한 2를 구현하기 위해 배열 자체에서 누적합을 각 인덱스의 value값으로 덮어 씌우기 보다는,
val*(n-index)가 각 요소(val)의 총 개수라는 사실을 이용하여 for문을 통해 누적합을 구할 수 있었다.

+) enumerate()
enumerate()는 이터러블 객체를 파라미터로 받아, 인덱스와 요소값을 동시에 받아 사용할 수 있는 내장 함수

+) accumulate()
해당 함수는 누적합 구조로 리스트를 자동으로 만들어는 함수이다.
input이 1,2,3,4,5라면
accumulate()를 통해 [1,3,6,10,15]로 제작 가능하다.
"""
import sys
from itertools import accumulate

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
n = int(data[0])
time_per_person = sorted(map(int, data[1:]))

# enumerate 사용 X
# total = sum(time_per_person[i] * (n - i) for i in range(n))

# enumerate 사용
# total = sum(val * (n - i) for i, val in enumerate(time_per_person, start=0))
# print(total)

# ----------------------------------------------
# 누적합
prefix_sum = list(accumulate(time_per_person))
print(sum(prefix_sum))
