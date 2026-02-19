import sys

def get_new_average(arr):
    total = sum(arr)
    arr.sort()
    max = arr[-1]
    return total / (max * len(arr)) * 100

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
print(get_new_average(arr))
