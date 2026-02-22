import sys

result = []


def control_stack(data, stack):
    length = len(data)
    global result
    for i in range(length):
        if data[i] == "push":
            stack.append(data[i + 1])
        elif data[i] == "pop":
            result.append(stack.pop() if stack else -1)
        elif data[i] == "size":
            result.append(len(stack))
        elif data[i] == "empty":
            result.append(0 if stack else 1)
        elif data[i] == "top":
            result.append(stack[-1] if stack else -1)


# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()[1:]
stack = []
control_stack(data, stack)
print('\n'.join(map(str, result)))
