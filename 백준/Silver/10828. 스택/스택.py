"""
해당 문제에서의 입력은 [입력1 \n 입력2]의 일정한 꼴을 갖기 때문에
n을 입력받아 for루프와 readline을 사용하여, 입력을 반복하기보단, 초기에는 read().split()을 통해
파일 전체를 읽어주었다.
명령 숫자꼴의 push를 제외한 나머지 명령들은 영문구만 존재하므로, 이에 따른 분기처리를 진행했다.
로직은 맞지만, 한 가지 아쉬운 부분이 존재한다면, push 다음 루프에 들어오는 숫자는 이미 push가 들어왔을 때,
append(data[i+1])을 통해 처리하였기 때문에, 의미가 없는 루프를 돌게 된다는 것이다.
이에 따라, .split이 아닌 splitlines()을 사용하여, 줄바꿈 단위로 입력을 받을 수 있다는 사실을 알았다.
splitlines()를 사용할 때는 주로 startswith()와 주로 같이 연계되어 사용된다는 사실을 알아두면 될 듯?
"""
import sys


# 1. 초기 풀이
# result = []
#
#
# def control_stack(data, stack):
#     length = len(data)
#     for i in range(length):
#         if data[i] == "push":
#             stack.append(data[i + 1])
#         elif data[i] == "pop":
#             result.append(stack.pop() if stack else -1)
#         elif data[i] == "size":
#             result.append(len(stack))
#         elif data[i] == "empty":
#             result.append(0 if stack else 1)
#         elif data[i] == "top":
#             result.append(stack[-1] if stack else -1)
#         else:
#             continue
#
#
# sys.stdin = open("input.txt", "r")
# data = sys.stdin.read().split()[1:]
# stack = []
# control_stack(data, stack)
# print('\n'.join(map(str, result)))


# 2. 최적화 풀이
def control_stack():
#    sys.stdin = open("input.txt", "r")
    data = sys.stdin.read().splitlines()[1:]
    stack = []
    result = []
    for command in data:
        if command.startswith("push"):
            stack.append(command.split()[1])
        elif command == "pop":
            result.append(stack.pop() if stack else -1)
        elif command == "size":
            result.append(len(stack))
        elif command == "empty":
            result.append(0 if stack else 1)
        elif command == "top":
            result.append(stack[-1] if stack else -1)
    return result


print('\n'.join(map(str, control_stack())))
