import sys

input = sys.stdin.readline
n, k = map(int, input().split())

max_value = 0
for i in range(1, k+1):
    temp = n * i
    temp = int(str(temp)[::-1])
    max_value = max(max_value, temp)

print(max_value)
