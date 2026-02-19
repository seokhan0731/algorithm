"""
기존 코드. 자바에서 최종 리팩토링 코드와 일치하게 코드 구현
주어진 문제에서 있는 그대로, 최대값을 찾고, 각각의 요소를 보정하여 총합을 구한 후, 평균을 도출하는 것이 아닌,
최종 결과식을 선정리 후, 과정을 최소화하여, 하나의 식으로 병합.(최대값->최종값 도출 순으로 간략화)

+) [입출력 모듈] 파이썬 기본 문법( vs JAVA)
system.setIn(new FileInputStream("input.txt") -> sys.stdin=open("input.txt", "r")))
BufferedReader br, br.readline() -> sys.stdin.readline
    => input()할 때마다, 자동적으로 줄 넘겨줌.
StringTokenizer -> map. split() //input()은 문자열로만 받아오기 때문에, 정수형으로 쓰기 위해서는 map의
                                  첫 번째 인자로, 반환 함수 매핑해줘야 한다(변환기 느낌)!
StringBuilder -> list로 만든 후, append로 추가하여, join()사용하여, 한 번에 출력
"""
import sys


def get_new_average(arr: list[int]) -> float:
    total = sum(arr)
    max_val = max(arr)
    return total / (max_val * len(arr)) * 100


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
print(get_new_average(arr))
