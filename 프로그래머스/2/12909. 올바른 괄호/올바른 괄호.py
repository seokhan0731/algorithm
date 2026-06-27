# def solution(s):
#     """
#     기존 코드. 카운터 방식
#     여는 소괄호와 닫는 소괄호만이 존재하기에, 별도의 스택을 생성하는건 낭비라고 생각했기에,
#     count 변수를 통해, 참/거짓 여부 판단
#     올바른 괄호인 경우에는,
#     1. 반드시 여는 괄호와 닫는 괄호가 짝이 맞아야한다. -> 모든 문자를 검사했을 때, 사이즈가 0이여야함
#     2. 여는 괄호가 우선적으로 돌어와야한다 -> count가 0 미만이 되면 X
#
#     :param s: 소괄호들로 이루어진 문자열
#     :return: 올바른 괄호 여부
#     """
#     count = 0
#     for char in s:
#         if char == '(':
#             count += 1
#         else:
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0


def solution(s):
    """
    코드 2. 스택 구현
    기존 코드인 경우는, 단일 괄호 종류의 올바름 여부만 판단 가능 but 성능적으로는 더 우수
    스택 방식은, 여러 종류의 괄호가 들어와도, 기존에 들어온 값과 페어가 맞는 경우만 판단하는 로직만 추가하면됨

    :param s: 소괄호들로 이루어진 문자열
    :return: 올바른 괄호 여부
    """
    parentheses = []
    for char in s:
        if char == '(':
            parentheses.append(char)
        else:
            if not parentheses:
                return False
            parentheses.pop()
    return not parentheses
