def solution(arr):
    # answer[-1]을 조건문으로 사용하기 위해, 초기값으로 arr[0] 사용
    answer = [arr[0]]
    for value in arr[1:]:
        # 연속된 것이 오지 않기 위해서는, 직전에 들어간 원소값만 알면 되기에, answer[-1]과 value 비교
        if answer[-1] != value:
            answer.append(value)

    return answer
