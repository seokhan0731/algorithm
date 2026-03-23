import math
import sys

sys.setrecursionlimit(10 ** 8)


# def get_max_score(score, dp, n):
#     """
#     코드 1. 바텀업 방식의 dp 구현
#     세 개의 연속된 계단을 밟지 못하기 때문에,
#     n-1, n-3을 거쳐 n을 가는 경우와 n-2를 거쳐 n을 가는 경우로 총 두 가지 방법이 존재한다,
#     이에 따라, n일 때의, 최대 점수값은 max(score[i - 1] + dp[i - 3], dp[i - 2]) + score[i]라는 식을 도출할 수 있다.
#     해당 조건의 점화식은 n=3일 때부터 유효하기 떄문에, 초기 조건은 n=1, 2일때 최대값으로 설정해주면 된다.
#     이때, 0번째 계단은 제약 조건에 해당하지 않기 때문에 n=2일때는 0,1,2번쨰의 계단의 총합이 된다.
#
#     +) 대개 입력값 조건 처리는 dp 테이블 등의 크기를 넉넉하게 잡는 더미 패딩을 통해, index error를 피하지만,
#     해당 문제에서 이 방식을 사용하기 위해서는 입력으로 주어지는 score 리스트까지 더미 패딩을 해야 한다.
#     이때는 원본 입력값을 오염시킬 수 있기 때문에 분기처리를 진행한다.
#
#     :param score: 각 계단의 점수를 저장하고 있는 리스트
#     :param dp: 각 단계에서의 점수 최대값을 담고 있는 리스트
#     :param n: 최종 목표로 하는 인덱스(마지막 계단)
#     :return: 최종 점수
#     """
#     for i in range(3, n + 1):
#         dp[i] = max(score[i - 1] + dp[i - 3], dp[i - 2]) + score[i]
#     return dp[n]
#
#
# sys.stdin = open("input.txt", "r")
# data = list(map(int, sys.stdin.read().split()))
# n = data[0]
# score = [0] + data[1:]
# if n == 1:
#     print(score[1])
#     exit()
# if n == 2:
#     print(score[1] + score[2])
#     exit()
#
# dp = [0] * (n + 1)
# dp[1] = score[1]
# dp[2] = score[1] + score[2]
#
# print(get_max_score(score, dp, n))

def get_max_score(target_idx, dp, score):
    """
    코드 2. 탑다운 방식의 dp 구현
    바텀업 방식의 점화식을 그대로 사용
    +) 탑다운 방식의 dp 구현은 4가지로 구성되는데, 종료 조건/메모이제이션/재귀 호출/반환이다.
    메모이제이션을 위해, 대개 inf로 값을 지정 후, inf가 아니라면, 이미 한 번 구한 값이기 때문에, 값을 계산하고
    가져다 쓰게 되는데, 이미 함수 호출 전, 종료 조건에 해당하는 인덱스 값들을 초기화 해놨기 때문에, 
    종료 조건을 별도로 명시하지 않고 메모이제이션 부분과 합칠 수 있었다.
    
    :param target_idx: 각 함수 호출에서 구하고자 하는 인덱스 
    :param dp: dp테이블
    :param score: 각 계단의 점수가 저장된 리스트
    :return: 인덱스에 해당하는 점수의 최대값
    """
    if dp[target_idx] != math.inf:
        return dp[target_idx]
    dp[target_idx] = max(get_max_score(target_idx - 3, dp, score) + score[target_idx - 1],
                         get_max_score(target_idx - 2, dp, score)) + score[target_idx]
    return dp[target_idx]


# sys.stdin = open("input.txt", "r")
data = list(map(int, sys.stdin.read().split()))
n = data[0]
score = [0] + data[1:]

if n == 1:
    print(score[1])
    exit()
if n == 2:
    print(score[1] + score[2])
    exit()

dp = [math.inf] * (n + 1)
dp[0], dp[1], dp[2] = 0, score[1], score[1] + score[2]
print(get_max_score(n, dp, score))
