import sys

input = sys.stdin.readline
a, b, v = map(int, input().split())

res = (v-b-1)//(a-b)
r = (v-b-1)%(a-b)

if r <= a:
    res += 1
if a > v:
    res = 1
    
print(res)