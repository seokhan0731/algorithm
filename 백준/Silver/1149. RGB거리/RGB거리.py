import math
import sys

sys.setrecursionlimit(10 ** 8)


# def get_minimum_cost(cost, n):
#     """
#     코드 1. 바텀업 방식의 dp 구현
#     해당 문제는 주어진 규칙에 따라 n번째의 r,g,b일 떄의 각각의 최소 비용을 구해야 한다.
#     그 이유는 당장 규칙에 따라 최소값을 선택한다하더라도, 그 뒤쪽에 있는 색의 비용이 작다는 보장이 없기 떄문이다.
#     이 조건으로 인해, 그리디 알고리즘을 사용할 수 없으며, 브루트포스 알고리즘으로 모든 경우의 수를 탐색하기에는
#     비용이 보다 많이 필요하기 떄문에, 해당 문제는 n단계에서의 각각의 최소값을 저장하는 dp를 통해 구현한다.
#     dp에 점화식은 다음과 같다.
#     dp[n]=dp[n-1]+cost[r/g/b]
#     n단계에서의 값 3개만 필요하기 떄문에, 별도의 dp테이블을 바텀업 방식에서는 만들지 않고,
#     변수 3개로 롤링 기법을 사용하여 구현할 수 있었따.
# 
#     :param cost: 비용 저장 테이블
#     :param n: 최종 인덱스
#     :return: 최종 최소 비용
#     """
#     r, g, b = cost[0], cost[1], cost[2]
#     for i in range(2, n + 1):
#         k = 3 * (i - 1)
#         r, g, b = min(g, b) + cost[0 + k], min(r, b) + cost[1 + k], min(r, g) + cost[2 + k]
#     return min(r, g, b)
# 
# 
# # sys.stdin = open("input.txt", "r")
# data = sys.stdin.read().split()
# n = int(data[0])
# cost = list(map(int, data[1:]))
# print(get_minimum_cost(cost, n))


# 탑다운
def get_minimum_cost(target_idx, color_idx):
    """
    코드 2. 탑다운 방식의 dp 구현
    바텀업 방식과는 다르게, 탑다운 방식은 메모이제이션을 위해 dp테이블이 필요했다.
    여타 다른 dp 문제와 동일하게 종료 인덱스를 제외한 나머지 인덱스들은 inf로 정의하여,
    재귀의 종료 조건과 메모이제이션을 합쳐 구현할 수 있었다.
    재귀 부분을 정의할 때는, 각 단계에서의 색에 따라 다른 색을 선택해야 하기 때문에,
    color_index와 분기 처리를 통해, 각 단계에서의 규칙을 처리할 수 있었다.
    
    :param target_idx: 각 레벨의 인덱스
    :param color_idx:  각 레벨의 색깔 인덱스(r/g/b: 0/1/2)
    :return: 각 레벨에서의 최소 비용
    """
    if dp[target_idx][color_idx] != math.inf:
        return dp[target_idx][color_idx]
    if color_idx == 0:
        dp[target_idx][color_idx] = min(get_minimum_cost(target_idx - 1, 1)
                                        , get_minimum_cost(target_idx - 1, 2)) + cost_list[target_idx][0]
    if color_idx == 1:
        dp[target_idx][color_idx] = min(get_minimum_cost(target_idx - 1, 0)
                                        , get_minimum_cost(target_idx - 1, 2)) + cost_list[target_idx][1]
    if color_idx == 2:
        dp[target_idx][color_idx] = min(get_minimum_cost(target_idx - 1, 0)
                                        , get_minimum_cost(target_idx - 1, 1)) + cost_list[target_idx][2]
    return dp[target_idx][color_idx]


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
n = int(data[0])
cost_list = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    cost_list[i] = list(map(int, data[i].split()))
dp = [[math.inf, math.inf, math.inf] for _ in range(n + 1)]
dp[1][0], dp[1][1], dp[1][2] = cost_list[1][0], cost_list[1][1], cost_list[1][2]
print(min(get_minimum_cost(n, 0), get_minimum_cost(n, 1), get_minimum_cost(n, 2)))
