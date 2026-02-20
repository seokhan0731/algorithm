import sys


def isVps(parentheses):
    parentheses_stack = []
    for i in range(len(parentheses)):
        if (parentheses[i] == '('):
            parentheses_stack.append('(')
            continue
        if (len(parentheses_stack) > 0):
            del parentheses_stack[-1]
            continue
        return False
    if (len(parentheses_stack) == 0):
        return True
    return False


# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
n = int(input())

result = []
for i in range(n):
    parentheses = input().rstrip()
    if (isVps(parentheses)):
        result.append("YES")
        continue
    result.append("NO")

print('\n'.join(result))
