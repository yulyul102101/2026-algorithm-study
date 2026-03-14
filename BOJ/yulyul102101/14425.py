import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
s1 = [sys.stdin.readline().strip() for _ in range(n)]
s2 = [sys.stdin.readline().strip() for _ in range(m)]

c1 = Counter(s2)

d1 = {s : c1[s] for s in s1}
print(sum(d1.values()))