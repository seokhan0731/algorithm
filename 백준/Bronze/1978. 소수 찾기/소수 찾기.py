import sys

"""
코드 1. 약수의 대칭성 활용
소수는 1을 제외하고, 자기 자신외의 약수가 존재하지 않음.
모든 수(n)는 a*b로 짝을 이루고 있고, 이 중심에는 **0.5 X **0.5이기 때문에, 1부터 n까지 모든 루프를 돌 필요 x
또한 결국 개별 숫자에 대한 수식이 들어가기 때문에, 굳이 입력을 리스트로 받아 불필요한 메모리를 사용할 필요 x

+) 처음 파이썬으로 다시 이 문제를 풀 때, 제곱근이 아닌 자연수의 개념으로만 접근하여, number//2로 루프를 설정하였음.
    약수가 나온다면, 자연수의 개념뿐만 아니라, 제곱근의 개념도 반드시 연관되어 생각해줄 것!
    
+) 파이썬에서는 자료형 명시가 없기 때문에, number/2=float => 몫만 사용하고자 할 때, // 연산자 사용
   파이썬에는 sqrt대신 **연산자로 제곱 가능!
"""


def is_prime(number):
    for i in range(2, (int)(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
numbers = map(int, input().split())
count = 0

for number in numbers:
    if number == 1:
        continue
    if is_prime(number):
        count += 1

print(count)
