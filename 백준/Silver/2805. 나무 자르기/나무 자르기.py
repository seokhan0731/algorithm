import sys


def is_bigger(mid_num, target_length):
    """
    결정 함수로, 해당 문제에서는
    입력으로 주어진 나무를 탐색할 인덱스로 자른 값이 목표로 하는 값과 같고, 이게 최대값인지와 관련된다.
    parametric_search라는 본함수에서 얻을 수 있는 길이가 목표로 하는 길이보다 클 때, 자르는 높이를 키우기 떄문에,
    최종적으로는 목표로 하는 길이로 자를 수 있는 최대 컷팅 높이를 설정할 수 있었다.

    +) 초기에는 length_he_get>=target_length를 통해, 이렇게 되면 목표로 하는 높이보다 더 크게 나오는 쪽으로
    진행되지 않을까 싶었지만, 조건이 맞는다면,
    본함수에서는 이와 반대로 목표로 하는 높이보다 더 작게 나오는 쪽으로 진행을 하기떄문에, 크게 상관없다는 것을 깨달았다.

    :param mid_num: 자르는 높이
    :param target_length: 얻고자 하는 길이
    :return: 목표 길이 이상 확보 가능 여부
    """
    current_depth = mid_num
    length_he_get = 0
    for i in tree_depth:
        if i > current_depth:
            length_he_get += i - current_depth
    if length_he_get >= target_length:
        return True
    return False


def parametric_search(left_num, right_num, target_length):
    """
    매개변수 탐색(결정함수)
    매개변수 탐색은 주로 주어진 조건내에서 최대/최소을 탐색하는 알고리즘이다.
    기존의 이진탐색에 결정함수(is_bigger)가 추가되는 구조이다.
    기존의 이진탐색이 target값을 찾는다면, 매개변수 탐색은 조건을 만족하는 최대/최소값을 찾는다.
    이에 따라 매개변수 탐색도 이진탐색의 구조를 띄는데,
    해당 문제에서는 탐색할 인덱스 설정(current_mid)후 조건을 검사한다.
    주어진 조건은 입력으로 주어진 나무를 탐색할 인덱스로 자른 값이 목표로 하는 값과 같고, 이게 최대값인지와 관련된다.


    :param left_num: 자를 높이의 최소값
    :param right_num: 자를 높이의 최댓값(주어진 나무의 길이 중 최대 길이)
    :param target_length: 목표로 하는 길이
    :return: 목표로 하는 길이를 얻을 수 있는 최대 컷팅 높이
    """
    current_left = left_num
    current_right = right_num
    current_max = 0
    while current_left <= current_right:
        current_mid = (current_left + current_right) // 2
        if is_bigger(current_mid, target_length):
            current_max = current_mid
            current_left = current_mid + 1
        else:
            current_right = current_mid - 1
    return current_max


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
n, m = map(int, data[0].split())
tree_depth = sorted(map(int, data[1].split()))
max_depth = max(tree_depth)
print(parametric_search(0, max_depth, m))
