import sys


def is_bigger(current_mid, how_many_need):
    can_make = 0
    for line in lines_length:
        if line >= current_mid:
            can_make += line // current_mid
    if can_make >= how_many_need:
        return True
    return False


def parametric_search(how_many_need):
    current_left = 1
    current_right = max(lines_length)

    max_length = 0
    while current_left <= current_right:
        current_mid = (current_left + current_right) // 2
        if is_bigger(current_mid, how_many_need):
            max_length = current_mid
            current_left = current_mid + 1
        else:
            current_right = current_mid - 1
    return max_length


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
already_have, how_many_need = map(int, [data[0], data[1]])
lines_length = [int(line) for line in data[2:]]
print(parametric_search(how_many_need))
