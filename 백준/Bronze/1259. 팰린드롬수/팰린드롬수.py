"""
기존 코드. 슬라이싱을 이용한 역순 조회
팰린드롬수라는 것은 결국 뒤집었을 때와 기존 상태가 같아야 하기 때문에,
조건문을 통해 기존==뒤집었을 때를 설정하여 해당 문제를 해결할 수 있었다.

+) reversed()
처음에는 reversed()를 통해 구현하고자 했으나, 예상 답변과 틀린 답이 도출되었다.
이를 확인하기 위해, print()를 사용하여 정체를 확인하니, 이터러블 객체로 찍혔다.
=> 해당 문제에서 reversed()를 통해 구현하고자 한다면, join을 통해, 
해당 객체를 문자열로 파싱해주는 별도의 추가 과정이 필요했다.
''.join(reversed())
"""
import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
answer = []
for number in data:
    if number == '0':
        break
    answer.append('yes' if number == number[::-1] else 'no')
print('\n'.join(answer))

