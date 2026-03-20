import sys

N, M = map(int, sys.stdin.readline().split())

d = {}
for i in range(N): d[i] = sys.stdin.readline().strip()

d2 = {v:k for k,v in d.items()}

for _ in range(M):
    f = sys.stdin.readline().strip()
    if f.isdigit(): print(d[int(f)-1])
    else: print(d2[f] + 1)
