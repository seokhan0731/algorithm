def solution(progresses, speeds):
    answer = []
    deployed = set()
    days = calculate_complete_day(progresses, speeds)

    for main_idx, main_value in enumerate(days):
        if main_idx in deployed:
            continue

        count = 1
        standard_day = main_value

        for num in range(1, len(days[main_idx:])):
            sub_idx = num + main_idx
            print(sub_idx)
            if sub_idx in deployed:
                continue
            if days[sub_idx] <= standard_day:
                count += 1
                deployed.add(sub_idx)
            else:
                break

        deployed.add(main_idx)
        answer.append(count)
    return answer


def calculate_complete_day(progresses, speeds):
    days = [(100 - progresses[i] + (speeds[i] - 1)) // speeds[i] for i in range(0, len(progresses))]
    return days