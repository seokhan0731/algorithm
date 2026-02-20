"""
코드 1. 스택 이용
해당 문제는 입력되는 문자열이 '('과 ')'로 한정 되어 있기 때문에, 스택을 사용하지 않고, 카운터 방식을 사용하여,
구현하는 것이 메모리 효율성 등의 측면에서 유리하지만, 여러 문자가 들어오는 상황에서는 사용할 수 X,
확장에 용이한 스택 자료구조를 통해 해당 코드를 파이썬으로 구현

결국 해당 문제에서 괄호끼리 올바른 짝을 이루기 위해서는, 두 가지 조건을 만족해야함.
1. '('가 들어오는 개수 만큼 ')'가 들어온다.
2. '('가 존재해야만 ')'가 들어올 수 있다.
    => '('인 경우, push ')'인 경우 pop 수행과 스택의 사이즈 검사

+) 파이썬 기본 문법
1. 자료 구조 관련
자바에서는 스택, 큐 상관없이 deque 사용해서 구현
파이썬에서는 스택 -> list
            큐 -> deque

2. 이터러블 객체 관련
파이썬은 이터러블 객체를 통해 루프를 자동화하여 돌릴 수 있는데, 문자열도 이터러블 객체 범주에 들어가기 떄문에
for i in range(len(str)) X -> for char in str 사용하는 것이 정석
    => 그냥 여러가지가 뭉쳐 있는 형태이면 웬만하면 이터러블 객체라고 생각해도 무방(list, str...)

3. list 문법
-1. stack.empty() -> not stack
자바에서는 별도의 메소드를 작성해야 했지만, 파이썬에서는 스택 이름을 조건으로 작성 시, 데이터 존재 -> True 반환
(not은 !과 동일한 효력)
-2. 맨 마지막 요소 제거
list를 스택용으로 사용하기 위해서는, del, pop이 존재하지만, pop을 사용하는 것이 국룰

4. 파이썬식 StringBuilder
자바에서는 sb.append -> 파이썬에서는 리스트에 append 후, join(각 리스트끼리 구분자로 나누어 한 번에 출력) 사용

5. 문자열 입출력
input -> 마지막 개행 문자까지 읽어옴 => rstrip() 사용하아ㅕ, 순수 문자열만 읽어오기
"""
import sys


def is_vps(parentheses):
    parentheses_stack = []
    for i in parentheses:
        if i == '(':
            parentheses_stack.append('(')
            continue
        if parentheses_stack:
            parentheses_stack.pop()
            continue
        return False
    return not parentheses_stack


sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
n = int(input())

result = []
for _ in range(n):
    parentheses = input().rstrip()
    result.append("YES" if is_vps(parentheses) else "NO")

print('\n'.join(result))
