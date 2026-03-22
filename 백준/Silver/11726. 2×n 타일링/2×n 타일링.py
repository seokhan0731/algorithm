import math
import sys

sys.setrecursionlimit(10 ** 8)
DIVIDE_NUM = 10007


# def get_number_of_way(n):
#     """
#     코드 1. 바텀업 방식의 dp 구현
#     -1. 1*2를 사용한다면 2*n 중의 무조건 두개가 존재해야 행을 채울 수 있기 때문에
#     해당 경우는 dp[n]=dp[n-2]에 속한다.
#     -2. 2*1을 사용한다면 2*n 중의 하나만 존재해도 행을 채울 수 있기 때문에
#     해당 경우는 dp[n]=dp[n-1]에 속한다.
#     -1, -2를 종합하여 dp[n]=dp[n-1]+dp[n-2]라는 점화식을 도출할 수 있었다.
#
#     +) 나머지 법칙
#     자바로 처음 이 문제를 풀었을 떄도 마찬가지로, 해당 문제는 나머지 법칙을 사용해야 한다,
#     나머지 법칙이란 개별 나머지의 합의 나머지와 전체 합의 나머지는 일치한다는 법칙이며,
#     (n+k)%DIVIDE_NUM==((n%DIVIDE_NUM)+(K%DIVIDE_NUM))%DIVIDE_NUM으로 정의된다.
#
#     +) 공간 최적화
#     대개 dp 문제를 풀 때는 이전 상태를 기억하기 위해 dp테이블을 사용하는 경우가 대부분이지만,
#     해당 문제처럼 특정 k개의 상태만을 기억하면 되는 문제에 경우에는 모든 값에 따른 dp테이블을 동작시키는 것보다,
#     특정 k개의 변수를 스와핑을 통해 동작시키는 것이 공간 복잡도면에서 압도적으로 효율적이다!>
#
#     :param n: 찾고자 하는 최종 인덱스
#     :return: 최종 인덱스에 해당하는 방법 수
#     """
#     a, b = 1, 1
#     for _ in range(2, n + 1):
#         a, b = b, (a + b) % DIVIDE_NUM
#     return b


def get_number_of_way(dp, n):
    """
    코드 2, 탑다운 방식의 dp 구현
    점화식을 그대로 차용 후, 메모이제이션을 위해 dp테이블을 math.inf로 초기화 후,
    0과 1값만 점화식을 돌리기 위해 1, 1로 별도 할당

    :param dp: dp테이블
    :param n:  구하고자 하는 값의 인덱스
    :return: n에 해당하는 방법 수
    """
    if n < 2:
        return dp[n]
    if dp[n] != math.inf:
        return dp[n]
    dp[n] = (get_number_of_way(dp, n - 1) + get_number_of_way(dp, n - 2)) % DIVIDE_NUM
    return dp[n]


# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.read())

# 바텀업
# print(get_number_of_way(n))

# 탑다운
dp = [math.inf] * (n + 1)
dp[0], dp[1] = 1, 1
print(get_number_of_way(dp, n))
