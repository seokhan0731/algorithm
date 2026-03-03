"""
코드 1. 이차원 리스틀 롵한 정렬 후 출력 수행
해당 문제의 입력의 형태는 첫 줄을 제외하고, a b의 꼴이기 때문에,
두 번째 줄부터 splitlines()[1:]을 통해 줄단위로 입력을 받은 뒤,
이차원 리스트에 입력을 받은 후, 정렬을 수행하였다.
다차원 리스트였기 때문에, 기존의 join(map(str,))을 통해서는 리스트의 []도 같이 출력되기 때문에,
f-string을 통해 출력 모듈을 맞추었다.

+) 정렬의 람다식 관련
다차원 리스트에서도 1차원과 마찬가지로 람다식을 적지 않는다면, 자동으로 여러 가지 요소의 정렬순을 자동으로 오름차순으로
정렬해준다. -> key=lambda x: (x[0], x[1]) 굳이 사용할 필요 X

+) 처음에는 입출력 모듈을 줄단위로 받았지만, 그냥 공백 단위로 모두 받은 후,
리스트 컴프리헨션을 통해서, 이차원 리스트를 생성하는 것이 더 좋았음
read().split()
matrics=[[data[i],data[i+1] for i in range(1, len(data),2)]
"""
import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().splitlines()[1:]

length = len(data)
matrics = []

for i in range(length):
    a, b = map(int, data[i].split())
    matrics.append([a, b])

# sorted_datas = sorted(matrics, key=lambda x: (x[0], x[1]))
sorted_datas = sorted(matrics)

print('\n'.join(f"{x[0]} {x[1]}" for x in sorted_datas))
