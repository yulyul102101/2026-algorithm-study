import sys

N = int(sys.stdin.readline())
Na = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Ma = list(map(int, sys.stdin.readline().split()))

for i in Ma:
    if(i in Na): print(1, end=" ")
    else: print(0, end=" ")