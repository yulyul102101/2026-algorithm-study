import sys
from collections import Counter

n = int(sys.stdin.readline())
cards1 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
cards2 = map(int, sys.stdin.readline().split())

c1 = Counter(cards1)
c2 = Counter(cards2)

d1 = {k: c2[k] + c1[k] for k in c2}

print(' '.join('1' if v == 2 else '0' for v in d1.values()))