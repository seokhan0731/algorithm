import sys


def is_bigger(mid_num, target_length):
    current_depth = mid_num
    length_he_get = 0
    for i in tree_depth:
        if i > current_depth:
            length_he_get += i - current_depth
    if length_he_get >= target_length:
        return True
    return False


def parametric_search(left_num, right_num, target_length):
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
