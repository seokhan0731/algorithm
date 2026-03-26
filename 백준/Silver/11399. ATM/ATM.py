import sys

# sys.stdin = open("input.txt", "r")
data = sys.stdin.read().split()
n = int(data[0])
time_per_person = sorted(map(int, data[1:]))
sum = 0
for i in range(n):
    sum += (time_per_person[i] * (n - i))
print(sum)
