"""
자바 vs 파이썬 정렬
자바의 정렬은 듀얼 퀵소트와 팀소트로 나뉜다,
-1. 듀얼 퀵소트는 원시 자료형을 정렬하는데 사용되고
    Arrays.sort()로 unstable하여, 중복된 숫자끼리의 기존 선후 관계를 보장하지 못한다.
    다만, 최악의 경우(O(n^2))를 제외하고는 , 상당히 가볍고 빠르다.
-2. 팀소트는 객체 자료형을 정렬하는데 사용되고
    Collections.sort()로 stable하여, 중복된 숫자끼리의 기존 선후 관계를 보자한다.
    듀얼 퀵소트보다, 객체 생성 비용 등 전반적으로 무겁지만, 어떠한 경우든 성능적으로 편차가 크지 않다.

* 파이썬에서는 원시자료형이 존재하지 않기 때문에, 모든 정렬로 팀소트가 사용된다.
자바에서는 정렬 알고리즘으로 두 개의 정렬 방식을 알아놔야했지만,
파이썬에서는 원본 파괴 유무로 두 방식을 알아놓으면 된다,
arrays.sort() -> 원본에서 바로 정렬 수행(==java)
sorted(arrays) -> 원본은 유지한 채, 반환값으로 정렬된 리스트 반환

+) 리스트 컴프리헨션
기존 코드에서는 for 루프를 통해, append()를 통해, 숫자를 받았지만,
append() 메소드 호출 비용 중첩 등의 문제로 리스트를 반복 작업을 통해 생성할 때는 리스트 컴프레헨션 방식이 사용된다.
[표현식 for 항목 in 이터럽ㄹ 객체]의 형식이다.
해당 문제에서는 numbers = [int(input()) for _ in range(n)] 사용되었다.

+) 방대한 양의 데이터 통으로 읽어 처리
주로 방대한 양의 데이터를 처리할 때, 주로 사용되는 방식이다. 모든 입력이 공백으로 나누어져 있을 때 유리한데,
data = sys.stdin.read().split() => data는 모든 입력을 담은 리스트가 된다.
이후, 첫 번쨰 입력이 개수 등의 불필요한 데이터면 [1:]슬라이싱을 통해, 제거 후, 작업을 수행하는 방법도 있다.

+) join
구분자로 나누어준 후, 저장 시, 반드시 문자열로 파라미터가 들어와야 된다는 것을 명심할 것!
"""
import sys

# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# numbers = []
# n = int(input())
# for _ in range(n):
#     numbers.append(int(input()))
#
# numbers.sort()
# result = '\n'.join(map(str,numbers))
# print(result)

# -------------------------------------------------------

# 1. 리스트 컴프리헨션 사용
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# numbers.sort()
# result = '\n'.join(map(str, numbers))
# print(result)
#

# -------------------------------------------------------

# 2. 파일 통으로 읽기
# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
sorted_numbers = sorted(map(int, data[1:]))
print('\n'.join(map(str, sorted_numbers)))
