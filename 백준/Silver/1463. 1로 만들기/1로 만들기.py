import math
import sys


# def get_minimum_way(n, dp):
#     """
#     기존 코드. 바텀업 방식의 dp 구현
#     초기값을 함수 호출 전 [0,0,1,1]지정했기에 별도의 예외 처리 없이
#     idx=n까지 min값을 각 3가지 케이스와 비교하며 채워준다.
#
#     :param n: 1로 만들고자 하는 입력값 (최종 목표 인덱스)
#     :param dp: 이전값들을 저장할 dp테이블
#     :return: None(dp테이블을 직접 수정)
#     """
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + 1
#         if i % 3 == 0:
#             dp[i] = min(dp[i], dp[i // 3] + 1)
#         if i % 2 == 0:
#             dp[i] = min(dp[i], dp[i // 2] + 1)
#
#
#
# def get_minimum_way(target_index, dp):
#     """
#     코드2. 탑다운 방식의 dp 구현
#     함수 호출 전, 메모이제이션을 위해 math.inf로 초기화하였기에,
#     메모이제이션은 math.inf가 아닌 경우로 지정, 재귀 종료값은 2 또는 3이 될 때, 1을 반환하도록 지정
#     만약 이전에 계산하지 못했다면, 계산을 하기 위해 target_index-1을 파라미터로 재귀를 돌려줘야하는데,
#     구하고자 하는 target_index가 크면 클수록, target_index-1, //3, //2를 계속 호출해야하기 때문에,
#     효율성이 많이 떨어진다
#
#     :param target_index: 1로 만들고자 하는 최종 인덱스
#     :param dp: dp 테이블
#     :return: 계산이 완료된 1까지의 최소 비용값
#     """
#     if target_index == 0:
#         return 0
#     if target_index == 2 or target_index == 3:
#         return 1
#     if not dp[target_index] == math.inf:
#         return dp[target_index]
#     dp[target_index] = get_minimum_way(target_index - 1, dp) + 1
#     if target_index % 3 == 0:
#         dp[target_index] = min(dp[target_index], get_minimum_way(target_index // 3, dp) + 1)
#     if target_index % 2 == 0:
#         dp[target_index] = min(dp[target_index], get_minimum_way(target_index // 2, dp) + 1)
#     return dp[target_index]


def get_minimum_way(target_idx, dp_dic):
    """
    코드3. 탑다운 점프 방식의 dp 구현
    이전 탑다운 방식에서는 target_idx까지 모든 값들을 dp로 구해야하는 비효율적인 구조였지만,
    해당 코드는 모든 값을 구하지 않고, //3 or //2값들을 구하여, 입력값이 크더라도 계산 횟수를 줄일 수 있다.
    -1 연산 관련하여 따로 재귀 호출을 하지 않고 +1로 연산횟수를 계산한다면, 계산 방식은 3 또는 2로 나누는 2가지 방식만 존재하게 된다.
    3으로 나누어 떨어지지 않는 경우 -1 또는 -2 중 한 경우에는 해당되기 때문에, -1을 수행한 연산횟수를 추가하여,
    탑다운 점프 방식을 구현할 수 있었다.
    //2인 경우에도 //3과 같은 경우로 계산을 수행 후, min을 통해 최소 비용을 구할 수 있다.
    +) 모든 값을 dp테이블에 채우지 않기 때문에, 일반적인 dp테이블에서 사용되는 리스트가 아닌 필요한 값만 저장하는 딕셔너리를 이용한다!

    :param target_idx: 1로 만들고자 하는 최종 인덱스
    :param dp_dic: dp 테이블
    :return: 계산이 완료된 1까지의 최소 비용값
    """
    if target_idx in dp_dic:
        return dp_dic[target_idx]
    route3 = get_minimum_way(target_idx // 3, dp_dic) + target_idx % 3 + 1
    route2 = get_minimum_way(target_idx // 2, dp_dic) + target_idx % 2 + 1
    dp_dic[target_idx] = min(route3, route2)
    return dp_dic[target_idx]


# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.read())
dp_dic = {1: 0, 2: 1, 3: 1}
# dp = [math.inf] * (n + 1)
print(get_minimum_way(n, dp_dic))
