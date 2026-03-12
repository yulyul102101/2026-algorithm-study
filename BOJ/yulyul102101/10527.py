import sys
from collections import Counter

n = int(sys.stdin.readline())
dom = [sys.stdin.readline().strip() for _ in range(n)]
kat = [sys.stdin.readline().strip() for _ in range(n)]

c1 = Counter(dom)
c2 = Counter(kat)

res = 0

for key in c1:
    res += min(c1[key], c2[key])

print(res)
