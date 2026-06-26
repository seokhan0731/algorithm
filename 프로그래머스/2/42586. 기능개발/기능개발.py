# def solution(progresses, speeds):
#     """
#     기존 코드. 다중 루프에서의 배포 여부 판단
#     각 idx별 기능이 완성되는 일자를 담는 days를 제작 후,
#     days의 각 idx별로 idx+1부터의 sublist를 돌며, 기능 완성이 기준 idx보다 빠른 기능들의 수를 카운트한다.
#     이때, 배포 여부를 담은 set을 통해, 이미 배포가 되었다면, 다음 루프로 넘어가게끔 구현했다.
#
#     +) 초기에는 기준 idx보다 더 빠르게 완수되는 경우에 모두 배포의 대상이 되는 줄로 오해하고,
#      배포 유무에 따라, 카운팅을 하도록 set을 사용하였다 ->중복 방지 및 유무 판단 효과적
#      하지만, 문제의 조건인, 모든 기능은 앞 idx의 기능 배포가 전제가 되어야하기에,
#      중간에 현 기준 idx보다 뒤늦게 구현이 되는 기능을 발견한 경우에는, 뒤쪽은 탐색할 필요가 없다.
#      즉, 배포 유무를 판단하는 set과 그 뒤를 탐색하는 로직도 굳이 존재할 이유가 없었다.
#
#     :param progresses: 현 기능 완성 상황
#     :param speeds: 하루당 증가되는 기능 완성도
#     :return: 배포에 따라, 몇 개의 기능을 배포할 수 있는지를 담은 리스트
#     """
#     answer = []
#     deployed = set()
#     days = calculate_complete_day(progresses, speeds)
#
#     for main_idx, main_value in enumerate(days):
#         if main_idx in deployed:
#             continue
#
#         count = 1
#         standard_day = main_value
#
#         for num in range(1, len(days[main_idx:])):
#             sub_idx = num + main_idx
#             if sub_idx in deployed:
#                 continue
#             if days[sub_idx] <= standard_day:
#                 count += 1
#                 deployed.add(sub_idx)
#             else:
#                 break
#
#         deployed.add(main_idx)
#         answer.append(count)
#     return answer
#
#

def solution(progresses, speeds):
    """
    코드 2. 단일 루프에서의 기준일수 갱신 및 카운팅
    앞의 기능의 배포가 선행되어야한다는 전제 조건만 만족하면 되기에,
    단일 루프로 해결 가능하다. 루프를 돌며,
    기준보다 완성 시점이 늦은 기능을 발견하는 순간, 해당 기능이 기준이 되며, 카운트를 초기화하도록 했다.

    :param progresses: 현 기능 완성 상황
    :param speeds: 하루당 증가되는 기능 완성도
    :return: 배포에 따라, 몇 개의 기능을 배포할 수 있는지를 담은 리스트
    """
    answer = []
    days = calculate_complete_day(progresses, speeds)
    standard_day = days[0]
    count = 1
    for idx in range(1, len(days)):
        if standard_day < days[idx]:
            answer.append(count)
            count = 1
            standard_day = days[idx]
        else:
            count += 1
    # 최종 카운트는 리스트에 추가 안 된 상태로 루프가 종료되기에
    answer.append(count)
    return answer


# + 두 개 이상의 이터러블 객체가 동일한 인덱스로 접근하는 경우에는 zip을 통해 간소화 가능!!
def calculate_complete_day(progresses, speeds):
    # days = [(100 - progresses[i] + (speeds[i] - 1)) // speeds[i] for i in range(0, len(progresses))]
    days = [(100 - p + (s - 1)) // s for p, s in zip(progresses, speeds)]
    return days