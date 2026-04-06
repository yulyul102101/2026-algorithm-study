import sys
from itertools import groupby

input = sys.stdin.readline
n = int(input())
line = [int(input()) for _ in range(n)]

s = set(line)
max_value  = 0
for num in s:
    temp = [x for x in line if x != num]
    max_len = max(len(list(g)) for _, g in groupby(temp))
    max_value  = max(max_value, max_len)

print(max_value)
