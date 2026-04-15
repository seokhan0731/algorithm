import sys


def is_possible(current_mid, how_many_need):
    """
    매개변수 탐색의 결정 함수.
    current_mid로 각 케이블들을 잘랐을 때, how_many_need 이상의 개수가 나와야 하기때문에,
    can_make>=how_many_need를 통해 참을 반환하도록 설계하였다.
    조건을 만족할 때 탐색 하한선을 높여 더 긴 절단 길이를 탐색하도록 유도하기에,
    최종적으로 how_many_need 이상일 때의 최대 절단 길이를 도출할 수 있었다.

    :param current_mid: 현재 자르고자하는 길이
    :param how_many_need: 총 필요한 케이블의 개수
    :return: 필요한 케이블의 개수 이상 획득 여부
    """
    can_make = 0
    for cable in cable_lengths:
        can_make += cable // current_mid
    if can_make >= how_many_need:
        return True
    return False


def parametric_search(how_many_need):
    """
    매개변수 탐색을 통한 구현
    해당 문제는 k개 이상의 자원을 얻을 수 있을때, 자를 수 있는 최대 길이를 구하는 문제이다.
    탐색을 수행하면서, 주어진 조건 내에서 최대/최소를 도출해야하기 때문에, 매개변수 탐색을 통해 구현했다.

    +) 초기에 current_left의 초기값을 0으로 배정했지만, 이 경우에는 current_right가 1인 경우에
    current_mid를 계산하는 과정에서 (0+1)//2=0이 나와 결정함수에서 cable//0이 도출되기에,
    각 케이블의 길이는 자연수 조건이 붙어있기에 current_left의 초기값을 1로 수정하였다.

    :param how_many_need: 총 필요한 케이블의 개수
    :return: 필요한 케이블의 개수 이상을 얻을 수 있는 최대 절단 길이
    """
    current_left = 1
    current_right = max(cable_lengths)

    max_length = 0
    while current_left <= current_right:
        current_mid = (current_left + current_right) // 2
        if is_possible(current_mid, how_many_need):
            max_length = current_mid
            current_left = current_mid + 1
        else:
            current_right = current_mid - 1
    return max_length


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
already_have, how_many_need = map(int, [data[0], data[1]])
cable_lengths = [int(cable) for cable in data[2:]]
print(parametric_search(how_many_need))
