def solution(a, b):
    answer = 0
    if a == b:
        return a
    list_value = [i for i in range(min(a, b), max(a, b) + 1)]

    for val in list_value:
        answer += val
    return answer