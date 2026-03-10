"""
기존 코드. 캐싱 테이블과 bisect() 사용
bisect_right-bisect_left를 이용하여, 갖고 있는 개수를 구하고, 해당 값을 딕셔너리에 저장한다.
캐싱 테이블이 존재하기 때문에, 구해야하는 target이 중복되어 입력되는 경우, 동일한 계산 과정을 더 수행하지 않고,
캐싱테이블에 찔러 바로 값을 뽑아낼 수 있다.
+) 딕셔너리
키값이 없는 상태에서, 조회를 시도하면 error가 나기 때문에, get() 메소드를 사용해야한다.(counter 딕셔너리 제외)
"""
import collections
import sys
from bisect import bisect_left
from bisect import bisect_right

# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
# _ = input()
# having_list = sorted(map(int, input().split()))
# _ = input()
# target_list = map(int, input().split())
#
# answer_list = []
# answer_dic = {}
# for target in target_list:
#     if target in answer_dic:
#         answer_list.append(answer_dic[target])
#     else:
#         answer_dic[target] = bisect_right(having_list, target) - bisect_left(having_list, target)
#         answer_list.append(answer_dic[target])
# print(' '.join(map(str, answer_list)))

"""
코드2. 카운터 이용
파이썬에서의 카운터는, 해시맵 기반으로 빈도수를 value값으로 저장하는 딕셔너리,
자바로 해당 문제를 hashmap을 사용해서 풀었을 때는, Integer의 객체를 사용해야하기 때문에, 원시자료형을 통해
이진탐색을 돌리는 것이 더 가벼웠다면, 파이썬에서는 원시 자료형이 별도로 존재하지 않기 때문에, 카운터를 통해 돌리는 것이
더 효율적!
+) 카운터가 딕셔너리여도, 만약 존재하지 않는 값이 키값으로 들어온다면, error를 뱉지 않고, 0을 반환한다!
(get()을 굳이 사용 안 해도 된다!)
"""
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
_ = input()
having_list = input().split()
_ = input()
target_list = input().split()

count_dict = collections.Counter(having_list)
answer = [str(count_dict[target]) for target in target_list]
print(' '.join(answer))
