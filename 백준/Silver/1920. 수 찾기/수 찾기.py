"""
코드 1. 집합을 이용한 존재 유무 판단
b로 입력받은 값들이 a에 있는지 단순 확인만 하면 되기 때문에, 유무 판단에 효율적인 set으로 a를 제작하여,
b의 각요소가 a에 존재하는지 in 연산자를 사용하여 풀이

+) 해당 문제에서는 굳이 정렬 등의 작업이 필요하지 않기 때문에, 입력 단계에서 map을 통해 int로 안 바꾸는게 더 효율적
    for문까지 리스트 컴프리헨션으로 사용 가능하다는 사실 명심할 것!
"""
import sys
from bisect import bisect_left

# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# _ = input()
# a = set(input().split())
#
# _ = input()
# b = list(input().split())
#
# answer = ['1' if target in a else '0' for target in b]
# # for target in b:
# #     answer.append(1 if target in a else 0)
#
# print('\n'.join(answer))


"""
코드 2. 이진 탐색
코드1이 집합을 통해, 유무를 확인했더라면, 해당 코드는 이진 탐색을 통해 유무를 판단한다.
java에서의 binarySearch의 rtn은 탐색을 수행하는 값이 존재하지 않는다면, 만약 값이 존재한다면 어디에 존재해야 하는지에
대한 음수값이었다면, 파이썬의 이진 탐색 bisect_right(left)는 해당 값이 존재했을 때의 인덱스를 양수로 그냥 뱉어준다.
이때, 탐색을 수행하는 값이 피탐색 리스트에 비해 크다면, 마지막 인덱스+1(=len(arr))을 뱉기 때문에,
해당 코드에서의 로직 arr[idx]를 정상적으로 수행하기 위해서는 bisect_left<len(arr)로 크기 제약을 추가해야 한다.

+) bisect_left or right
bisect_이후에 붙는 왼/오른쪽은 만약 새로운 값이 들어온다면 기존 값의 왼쪽 경계의 idx를 뱉냐, 오른쪽 경계의 idx를 뱉냐에 따라 달라진다.

+) 바다코끼리 연산자(:=)
해당 연산자는 값을 변수에 할당하는 동시에 사용할 수 있게 하는 연산자이다.
해당 연산자가 없는 경우, 선언부와 사용부를 나누어야하지만, 이 연산자를 통해 값이 할당하는 동시에 사용할 수 있게 된다.
"""
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

_ = input()
arr = sorted(list(map(int, input().split())))

_ = input()

answer = ['1' if (idx := bisect_left(arr, value)) < len(arr) and arr[idx] == value else '0'
          for value in map(int, input().split())]

print('\n'.join(answer))
