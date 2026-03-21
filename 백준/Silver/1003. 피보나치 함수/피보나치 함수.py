import math
import sys


# def get_call_count(dp, max_size):
#     """
#     코드 1. 바텀업 방식의 dp 구현
#     피보나치 자체의 점화식은 dp[i]=dp[i-1]+dp[i-2]이기 떄문에, 0과 1의 호출 횟수 또한
#     i-1과 i-2의 0과 1의 호출 횟수를 더한 값을 따라갈 수 밖에 없다.
#     이에 따라 초기값을 idx=0,1일 떄 지정 후, 점화식을 돌려 수행할 수 있었다.
#
#     +) map -> 일회용 컨베이어벨트 역할로, 여러번 사용하고 싶으면 list로 감싸줘야한다.
#     +) 얕은 복사
#     처음에 코드를 작성할 때, dp[i][0]=dp[i-1][0]+dp[i-2][0]꼴로 작성을 했을 떄, 의도치 않은 결과값이 도출되었다
#     이에 따라, 현재 코드처럼 수정했을 떄, 의도했던 결과가 나왔다. 처음에 의도치 않은 결과가 나왔던 이유는
#     리스트의 초기 크기 할당 수행 시, dp = [[0, 0]] * (max_size + 2)로 작성되었기 때문이다. dp=[k]*n꼴로 작성시에는,
#     [k]의 메모리 주소를 가리키는 n개의 포인터?객체가 생성되기 때문에, dp[i][0]처럼 해당 인덱스에 접근하게 되면,
#     같은 메모리에 값을 덮어 씌우는 꼴이 되기 때문에 의도치 않은 결과가 나왔던 것이다. 물론 해당 코드에서는 dp[i]=~꼴로 새로운 공간을 만들어
#     의도치 않은 결과가 도출되는 것을 막을 수 있었다.
#     => 얕은 복사를 막기 위해 dp[[0,0] for _ in range()] 꼴로 작성하여, 새로운 공간 자체를 할당해줘야 한다.
#
#     +) dp=[0]*k
#     1차원 리스트에 dp를 풀 때는 이러한 고민을 겪지 않았던 이유는 0이라는 정수값으로 초기 공간을 할당했기 때문이다.
#     파이썬에서는 정수, 문자열, 튜플 등은 이뮤터블 객체로 같은 메모리를 가리키고 있음에도 해당 메모리에 값을 덮어씌우려고 할 때,
#     이뮤터블 객체이므로 자동적으로 다른 공간을 만들어 새로운 공간을 가리키도록 바뀌기 떄문이다. 반면 리스트는 뮤터블 객체로 위의 설명과 같은
#     얕은 복사 이슈가 생길 수 밖에 없었다.
#
#     :param dp: dp테이블
#     :param max_size: 바텀업 방식으로 도달하는 최종 인덱스
#     :return: none(원본 리스트를 직접 수정)
#     """
#     if max_size >= 2:
#         for i in range(2, max_size + 1):
#             dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]
#

def get_call_count(dp, target_idx):
    """
    코드 2. 탑다운 방식의 dp구현
    재귀의 종료조건을 idx=0,1로 설정한 후, 해당 인덱스의 값을 점화식 시작값으로 지정 후,
    재귀 호출을 진행한다.
    메모이제이션을 위해 종료 조건의 인덱스를 초기화 하기 전, 모든 값을 math.inf로 설정 후,
    math.inf가 아닌 경우 갖고 있는 값을 뱉도록 설계한다.
    입력 중 가장 큰 idx값을 구하면, 나머지 dp테이블은 재귀 중 채워지기 떄문에, max_size를 인덱스로
    재귀 호출 진행 후, 루프를 통해 dp테이블에서 값을 뽑아준다

    :param dp: dp테이블
    :param target_idx: 호출 횟수를 구하고자 하는 인덱스
    :return: 해당 인덱스에서의 0과 1의 호출 횟수(리스트)
    """
    if target_idx < 2:
        return dp[target_idx]
    if dp[target_idx][0] != math.inf:
        return dp[target_idx]
    list_1 = get_call_count(dp, target_idx - 1)
    list_2 = get_call_count(dp, target_idx - 2)
    dp[target_idx] = [list_1[0] + list_2[0], list_1[1] + list_2[1]]
    return dp[target_idx]


# sys.stdin = open("input.txt", "r")
data = list(map(int, sys.stdin.read().split()[1:]))
max_size = max(data)

# 바텀업
# dp = [[0, 0]] * (max_size + 2)
# dp[0], dp[1] = [1, 0], [0, 1]
# get_call_count(dp, max_size)
# print('\n'.join(f"{dp[i][0]} {dp[i][1]}" for i in data))

# 탑다운
dp = [[math.inf, math.inf] for _ in range(max_size + 2)]
dp[0], dp[1] = [1, 0], [0, 1]
_ = get_call_count(dp, max_size)
print('\n'.join(f"{dp[i][0]} {dp[i][1]}" for i in data))
