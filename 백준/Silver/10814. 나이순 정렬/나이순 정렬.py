"""
기존 코드. 람다식을 통한 정렬 구현
입력으로 주어진 n을 제외하고, split()을 통해, 공백 단위로 데이터를 읽어온 후,
range를 2씩 뛰며, [나이, 이름]의 형태로 별도의 리스트에 저장하여 정렬을 수행한다.
이때, sort()를 람다식 없이 사용한다면, 자동으로 나이가 같으면, 이름의 사전순으로 정렬 기준이 맞춰지기 떄문에,
정렬 조건이 하나고, 오름차순이지만 람다식으로 별도 지정을 해주어야만 했다.
"""
import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()[1:]

member_list = [[int(data[index]), data[index + 1]] for index in range(0, len(data), 2)]
member_list.sort(key=lambda x: x[0])

print('\n'.join(f"{x[0]} {x[1]}" for x in member_list))
