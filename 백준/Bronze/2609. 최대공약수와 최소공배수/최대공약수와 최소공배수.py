"""
기존 코드1. 내장 라이브러리 사용
자바와는 다르게 파이썬에는 자체적으로 최대공약수와 최소공배수를 반환하는 메소드가 자체적으로 내장 되어 있다.
math.gcd(), math.lcm()

+) map, 입/출력 관련
map도 이터러블 객체로서, 컨베이어 벨트 역할을 수행한다고 생각하면 된다. list와는 다르게 자체적으로 인덱스를 가지고 있지 않다.
초기에는 a, b 대신 list를 별도로 만들어 list(map())꼴로 감싸, 출력 부분에서 gcd(list[0],list[1])꼴로 사용하였지만,
입력의 개수가 소규모로 정해져있을 때는, list를 만들기보단 a,b처럼 별도의 변수를 몇 개 제작하여 코드를 수행하는 것이 성능적으로 더 유리하다.
-> 뒤쪽에서 특정 인덱스를 활용할 예정이라면 리스트로 list(map())꼴로 감싸 사용하는 것이 좋고, 그게 아니라면 list()꼴로 안 감싸도 된다.
또한 출력 부분에서는 map자체가 이터러블 객체이기 때문에, 굳이 list로 안 감싸고 join을 사옹해도 무방하다!
"""
import math
import sys

# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# a, b = map(int, input().split())
# print('\n'.join(map(str, [math.gcd(a, b), math.lcm(a, b)])))

"""
코드2. 유클리드 호제법 구현
유클리드 호제법이란 max,min꼴에서 max%min 수행 후, max%min=k라 할때, min%k를 수행 후, 이 과정을 반복하며,
k값이 0이 되기 전까지 진행하여 최대 공약수를 구하는 방법이다.
get_gcd()처럼 해당 과정을 while을 통해 반복함으로써, 최대공약수를 구할 수 있었다.
최소공배수는 gcd*나머지 인자들로 구할 수 있다.

+) 다중 할당
big_number, small_number = small_number, big_number % small_number에서 다중 할당이 수행되었는데,
이때는 우측 자체가 먼저 계산된 후, 좌측에 할당이 이루어진다!
c계열로 따지면 temp를 통해 swap해준 과정을 해당 코드로 수행하는 것과 동일하다.
"""


def get_gcd(big_number, small_number):
    while small_number > 0:
        big_number, small_number = small_number, big_number % small_number
    return big_number


def get_lcm(big_number, small_number, gcd):
    small_factor = small_number // gcd
    big_factor = big_number // gcd
    return big_factor * gcd * small_factor


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
a, b = map(int, input().split())
max_val, min_val = max(a, b), min(a, b)
gcd = get_gcd(max_val, min_val)
lcm = get_lcm(max_val, min_val, gcd)
print(gcd, lcm, sep='\n')
