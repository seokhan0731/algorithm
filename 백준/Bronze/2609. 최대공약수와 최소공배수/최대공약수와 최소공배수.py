import math
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

number_list = list(map(int, input().split()))
print('\n'.join(list(map(str, [math.gcd(number_list[0]
                                        , number_list[1]), math.lcm(number_list[0], number_list[1])]))))
