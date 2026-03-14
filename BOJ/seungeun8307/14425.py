import sys

N, M = map(int, sys.stdin.readline().split())

S = []
for i in range(N):
    S.append(sys.stdin.readline())

count = 0
for i in range(M): 
    t = sys.stdin.readline()
    if t in S: count += 1

print(count)
