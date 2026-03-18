import math
import sys


# sys.setrecursionlimit(10 ** 8)


# def get_minimum_way(n, dp):
#     """
#     코드 1. 바텀업 방식의 dp 구현
#     inf로 리스트를 초기화한 후, 3과 5를 채우기 위해 0만 초기값을 지정 후, dp 수행
#     n+1개의 원본 리스트를 수정하여, 각 케이스에 맞는 모든 dp값을 채워넣음.
#
#
#     :param n: 최종 완성하고자 하는 인덱스
#     :param dp: dp테이블
#     :return: None(원본 dp테이블을 직접 수정)
#     """
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 3] + 1
#         if i >= 5:
#             dp[i] = min(dp[i], dp[i - 5] + 1)


# def get_minimum_way(n, dp):
#     """
#     코드2. 탑다운 방식의 dp 구현
#     n-3값으로 일단 설정 후, 5 이상인 경우에만 n-3과 n-5를 비교하여 최소값을 설정한다.
#     3과 5의 조합으로 안 되는 숫자는 별도로 처리해야하기 때문에, inf라는 기준이 +1을 했을 때, 훼손되지 않을까싶었지만,
#     훼손 안되는 것을 확인했기에, inf일 때 최소값 설정 로직을 별도로 분기처리하지 않아도 됐다.
#
#     +) 파이썬에는 재귀를 호출할 때, 호출할 수 있는 횟수 제한이 디폴트로 존재하기 떄문에,
#     sys.setrecursionlimit(10 ** 8)를 별도로 설정해줘야. recursionerror가 나오지 않는다!
#     => 10^8만큼의 재귀까지 멈추지 말 것!
#
#     :param n: 찾고자 하는 목표 인덱스
#     :param dp: dp테이블
#     :return: dp테이블 속 해당 최소 비용
#     """
#     if n < 3:
#         return dp[n]
#     if not dp[n] == math.inf:
#         return dp[n]
#     dp[n] = get_minimum_way(n - 3, dp) + 1
#     if n >= 5:
#         dp[n] = min(dp[n], get_minimum_way(n - 5, dp) + 1)
#     return dp[n]

def get_minimum_way(n):
    """
    코드3. 그리디 알고리즘 사용
    결국 해당 문제의 최적해를 위해서는 5를 최대한 많이 사용해야 한다.
    그렇기에 5의 배수를 만드는 것을 목적으로 3을 빼주고, 5의 배수가 되자마자 //5를 수행하여 문제를 해결할 수 있다.

    :param n: 최소 비용을 찾고자 하는 목표값
    :return:  최소값 or 실패했을 떄의 -1
    """
    count = 0
    while n >= 0:
        if n % 5 == 0:
            count += n // 5
            return count
        n -= 3
        count += 1
    return -1


# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.read())
# dp = [math.inf] * (n + 1)
# dp[0] = 0
# 바텀업 방식
# dp[0] = 0
# get_minimum_way(n, dp)
# print(dp[n] if not dp[n] == math.inf else -1)

# 탑다운 방식
# answer = get_minimum_way(n, dp)
# print(answer if not answer == math.inf else -1)

# 그리디
print(get_minimum_way(n))
