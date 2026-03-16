import sys
from collections import Counter

N = int(sys.stdin.readline())
Nl = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Ml = list(map(int, sys.stdin.readline().split()))

count = Counter(Nl)

for ms in Ml:
    print(count[ms],end=' ')