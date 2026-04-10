import sys

"""
코드1. set을 이용한 중복 제거 및 딕셔너리를 통한 구현
해당 문제는 자신보다 작은 수가 몇 개가 있는지를 출력해야 한다.
중복되는 수는 자기 자신을 제외해야 하기 때문에, set을 통해 중복 제거를 수행했고,
정렬된 상태라면 자기 자신의 인덱스가 자신보다 작은 수의 개수가 되므로,
정렬 수행 후, 딕셔너리의 해당 결과값을 담아 구현했다.

+) 초기 접근
처음에는 딕셔너리를 사용하지 않았다. 그 이유는 딕셔너리 자체가 탐색을 할 때는 해시 알고리즘을 사용하기 때문에
빠르지만 중복되지 않은 입력값이 들어오는 최악의 경우에는 메모리적으로 너무 무거워질 것이라 생각했기 때문이다.
이에 따라, 초기에는 정렬까지는 똑같이 수행 후, number_set.index()를 index()의 구동방식을 모르고 작성했다가,
시간 초과가 났고, .index()의 구동원리를 보니, 순차적으로 탐색하기 때문임을 깨달았다.
그래서 이 해결법으로 bisect_left()를 도입하여 풀이를 했다.
하지만 그렇더라도, bisect_left()를 통해 매번 이진탐색을 하는 것보다는 메모리가 무겁더라도 빠르게 조회하는 것이
성능적으로는 매우 우수하다고 하여, 딕셔너리를 사용하는 로직으로 수정하였다. 
-> 고정된 데이터의 등수 찾기 && 널널한 메모리 => 딕셔너리 사용할 것

+) 출력 관련
해당 문제의 출력은 공백을 기준으로, 출력값을 나눠야하기 때문에,
for문을 통해 print를 하지 않고(i/o 계속 왔다갔다해야 하기 때문), join으로 묶어 한 번에 출력하는 방식을 택했다.
join외의 방법도 하나 존재한다는 사실을 알게 되었는데, *(언패킹)연산자를 사용한 print였다
*(제너레이터)를 사용한다면, 메모리에 출력 대상을 만들지 않고, print(요소1, 요소2...)을 출력하는 것과 같은 역할을 수행한다.
요소를 던질 때, print함수의 파라미터를 던지는 느낌이기에, 데이터의 수가 많이 큰 경우에는 join 사용하는 것이 더 유리하다.
"""

# sys.stdin = open("input.txt", "r")
# data = sys.stdin.read().splitlines()
# n = int(data[0])
# number_list = list(map(int, data[1].split()))
# number_set = sorted(set(number_list))
# number_dict = {val: idx for idx, val in enumerate(number_set)}
# print(' '.join(map(str, [number_dict[i] for i in number_list])))

# 코드2.
"""
코드 2. 인덱스 정렬을 통한 구현
인덱스 정렬이란, 자기 자신의 위치를 기억해줘야 되는 상태에서, 자신의 위치를 저장한 채로,
특정 기준에 맞추어 정렬하는 알고리즘이다. 이에 따라 [값,인덱스]의 꼴을 띄게 된다.
과정은 다음과 같다.
1. 다차원 리스트로 값과 인덱스 정보를 담아두기
2. 값 기준 정렬 사용
3. 중복을 체크하여, 순위 부여
이 과정을 수행하는데, 처음에는 별도의 answer_list를 만들지 않고,
값이 들어가는 위치에 rank값으로 덮어씌었지만, 이렇게 되면, 해당 리스트롤 또 정렬해야하기 때문에,
별도의 리스트를 초기에 크기를 주고 할당 후, 기존 인덱스순에 맞추어 rank값으로 채워 구현할 수 있었다.
"""
# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()
n = int(data[0])
number_list = list(map(int, data[1].split()))
number_with_idx = [[val, idx] for idx, val in enumerate(number_list)]
sorted_list = sorted(number_with_idx, key=lambda x: x[0])

rank_num = 0
answer_list = [0] * n
for i in range(n - 1):
    if sorted_list[i][0] != sorted_list[i + 1][0]:
        answer_list[sorted_list[i][1]] = rank_num
        rank_num += 1
        continue
    answer_list[sorted_list[i][1]] = rank_num
answer_list[sorted_list[-1][1]] = rank_num

print(' '.join(map(str, answer_list)))
