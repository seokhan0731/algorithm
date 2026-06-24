def solution(arr):
    answer = [arr[0]]
    for value in arr[1:]:
        if answer[-1] != value:
            answer.append(value)
    return answer