import math
import sys


# def get_minimum_way(dp):
#     """
#     코드 1. 바텀업 방식의 dp
#     해당 문제의 입력의 크기는 11보다 작은 양수이기 때문에, 리스트의 사이즈를 11로 만든 후,
#     3부터 dp의 점화식을 돌려주면 된다.
#     결국 1,2,3을 더해 만드는 수는 dp[n]=dp[n-1]+1, dp[n-2]+2, dp[n-3]+3이고,
#     해당 방법의 수는 dp[n-1]+dp[n-2]+dp[n-3]으로 점화식을 도출할 수 있었다.
# 
#     :param dp: 점화식을 돌려 값을 저장할 dp 테이블
#     :return: none(원본 리스트 수정)
#     """
#     for i in range(3, 11):
#         dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]


# sys.stdin = open("input.txt", "r")
data = map(int, sys.stdin.read().split()[1:])


# 바텀업
# dp = [0] * 11
# dp[0], dp[1], dp[2] = 1, 1, 2
# # get_minimum_way(dp)
# answer = []
# for i in data:
#     answer.append(dp[i])
# print('\n'.join(map(str, answer)))

def get_minimum_way(target_index, dp):
    """
    코드 2. 탑다운 방식의 dp
    바텀업 방식의 점화식을 재사용하여 구현
    메모이제이션을 위해 리스트의 초기값은 inf로 설정 후, 재귀 종료 조건을 위한
    idx=0,1,2까지의 값만 초기화시켜 진행

    :param target_index: 탐색하고자 하는 정수값(인덱스와 동일)
    :param dp: 메모이제이션을 위한 dp테이블
    :return: 해당 정수에 도달하는 방법의 수
    """
    if target_index < 3:
        return dp[target_index]
    if not dp[target_index] == math.inf:
        return dp[target_index]
    dp[target_index] = (get_minimum_way(target_index - 1, dp)
                        + get_minimum_way(target_index - 2, dp)
                        + get_minimum_way(target_index - 3, dp))
    return dp[target_index]


dp = [math.inf] * 11
dp[0], dp[1], dp[2] = 1, 1, 2
print('\n'.join(str(get_minimum_way(i, dp)) for i in data))
