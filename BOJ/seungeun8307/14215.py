import sys

T = list(map(int, sys.stdin.readline().split()))

if sum(T)-max(T) > max(T): print(sum(T))
else: print((sum(T)-max(T))*2-1)