# def solution(a, b):
#     """
#     기존 코드. 리스트 컴프리헨션을 사용
#     a와 b간(a<b 조건하에)에 존재하는 정수의 합을 누적해야하기때문에,
#     a와 b가 같은 경우와 a와 b가 다른 경우 총 두가지 경우의 수가 있다.
#     2번째 경우, a와 b의 대소 여부가 주어지지 않기 때문에, min(),max()를 사용해 선후 관계를 따진 후,
#     range()와 리스트 컴프레헨션을 통해, answer의 두 정수간 합이 누적되도록 구현했다.

#     :param a: 입력 1
#     :param b: 입력 2
#     :return: a와 b사이 존재하는 정수값의 합계
#     """

#     answer = 0
#     list_value = [i for i in range(min(a, b), max(a, b) + 1)]

#     for val in list_value:
#         answer += val
#     return answer

def solution(a, b):
    """
    코드 2. sum()사용
    코드 1은 리스트를 만들기 떄문에, 메모리를 잡아 먹지만, 사실 이 문제에서는 이전 상태값을 기억할 필요가 없기에,
    리스트를 굳이 생성할 이유가 없다.
    파이썬 내장 라이브러리의 sum()과 기존에 사용했던 range, min, max 로직을 사용한다면, 별도의 리스트 제작없이 문제의 요구사항에 맞춰
    구현 가능하다.
    
    :param a: 입력 1
    :param b: 입력 2
    :return: a와 b사이 존재하는 정수값의 합계
    """
    answer = 0
    answer = sum(range(min(a, b), max(a, b) + 1))

    return answer
