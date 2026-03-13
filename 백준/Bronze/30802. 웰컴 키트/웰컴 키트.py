"""
기존 코드. math.ceil()을 통한 올림
팬의 개수는 딱 맞아 떨어져야하고, 개별 구매가 필요하니 몫과 나머지 연산자를 통해 구현 가능하고,
옷의 경우는 개별 구매가 안 되고 모자르면 안 되기 때문에, 소수점으로 몫 결과가 나오는 경우, 올림 처리가 필수적이다.
이를 구현하기 위해 math.ceil()을 통해 구현할 수 있었다.

+) 수학적 공식을 통한 올림 구현
나눠지는 수 + t-1을 사용한다면, 올림을 구현할 수 있다. 나눠지는 수에서 기존의 몫이 나오고,
나머지 t-1항에서 기존 나눠지는 수의 나머지가 없다면, t-1+n(n<1)이기 때문에, 기존 몫을 유지시키고,
그 외의 경우 기존 몫+1이 가능하게끔 할 수 있다.
"""

import math
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
size_count = list(map(int, input().split()))
t, p = map(int, input().split())
total_t = 0
for data in size_count:
    total_t += math.ceil(data / t)
print(f"{total_t}\n{n // p} {n % p}")
